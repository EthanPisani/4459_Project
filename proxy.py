import grpc
from concurrent import futures

import proxy_pb2
import proxy_pb2_grpc

class ProxyServer(proxy_pb2_grpc.ProxyServiceServicer):
    pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proxy_pb2_grpc.add_ProxyServiceServicer_to_server(ProxyServer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Proxy server started on port 50052.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()