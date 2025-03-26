import grpc
from concurrent import futures
import time
import proxy_pb2
import proxy_pb2_grpc
import heartbeat_pb2
import heartbeat_pb2_grpc
import chat_pb2
import chat_pb2_grpc

class ProxyServer(proxy_pb2_grpc.ProxyServiceServicer):
    def __init__(self):
        self.heartbeat_channel = grpc.insecure_channel('localhost:50053') #TODO don't hardcore heartbeat service address
        self.heartbeat_stub = heartbeat_pb2_grpc.HeartbeatStub(self.heartbeat_channel)

        self.current_server = 'primary'
        self.server_port = 50051

        self.server_channel = grpc.insecure_channel(f'localhost:{self.server_port}')
        self.server_stub = chat_pb2_grpc.ChatServiceStub(self.server_channel)
        
    def Join(self, request, context):
        tries = 0
        while True:
            if tries == 5:
                context.abort(code=grpc.StatusCode.UNAVAILABLE, details='Primary went down and could not reconnect.')
            try:
                return self.server_stub.Join(chat_pb2.JoinRequest(name=request.name))
            except grpc.RpcError as e:
                tries = tries + 1
                time.sleep(5)

    def SendMessage(self, request, context):
        tries = 0
        while True:
            if tries == 5:
                context.abort(code=grpc.StatusCode.UNAVAILABLE, details='Primary went down and could not reconnect.')
            try:
                return self.server_stub.SendMessage(chat_pb2.Message(sender=request.sender, content=request.content))
            except grpc.RpcError as e:
                tries = tries + 1
                time.sleep(5)

    def ReceiveMessages(self, request, context):
        tries = 0
        while True:    
            if tries == 5:
                context.abort(code=grpc.StatusCode.UNAVAILABLE, details='Primary went down and could not reconnect.')
            try:
                stream = self.server_stub.ReceiveMessages(chat_pb2.Empty())
                tries = 0
                for message in stream:
                    yield message
            except:
                print(f'Error occurred while reading messages (try={tries}). Retrying...')
                tries = tries + 1
                time.sleep(5)

    def SwitchServer(self, request, context):
        print(f'Switching to {request.new_primary}:{request.server_port}')

        self.current_server = request.new_primary
        self.server_port = request.server_port
        
        self.server_channel.close()
        
        self.server_channel = grpc.insecure_channel(f'localhost:{self.server_port}')
        self.server_stub = chat_pb2_grpc.ChatServiceStub(self.server_channel)

        return heartbeat_pb2.SwitchResponse(success=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proxy_pb2_grpc.add_ProxyServiceServicer_to_server(ProxyServer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Proxy server started on port 50052.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()