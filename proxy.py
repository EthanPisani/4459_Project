import grpc
from concurrent import futures

import proxy_pb2
import proxy_pb2_grpc
import heartbeat_pb2_grpc
import chat_pb2_grpc

class ProxyServer(proxy_pb2_grpc.ProxyServiceServicer):
    def __init__(self):
        self.heartbeat_channel = grpc.insecure_channel('localhost:50053') #TODO don't hardcore heartbeat service address
        self.heartbeat_stub = heartbeat_pb2_grpc.HeartbeatStub(self.heartbeat_channel)

        self.current_server = 'primary'

        self.server_channel = grpc.insecure_channel('localhost:50051')
        self.server_stub = chat_pb2_grpc.ChatServiceStub(self.server_channel)
        
    def Join(self, request, context):
        return self.server_stub.Join(name=request.name)

    def SendMessage(self, request, context):
        return self.server_stub.SendMessage(sender=request.sender, content=request.content)
    
    def ReceiveMessages(self, request, context):
        return self.server_stub.ReceiveMessages()

    def SwitchServer(self, request, context):
        self.current_server = request.new_primary
        
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proxy_pb2_grpc.add_ProxyServiceServicer_to_server(ProxyServer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Proxy server started on port 50052.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()