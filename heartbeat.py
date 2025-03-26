import grpc
import asyncio
from concurrent import futures
from heartbeat_pb2 import HeartbeatResponse, SwitchResponse, SwitchRequest
import heartbeat_pb2_grpc

class HeartbeatServicer(heartbeat_pb2_grpc.HeartbeatServicer):
    def __init__(self):
        self.primary_server = "primary"
        self.backup_server = "backup"
        self.proxy = None
        self.heartbeat_status = {"primary": True, "backup": True}

    async def SendHeartbeat(self, request, context):
        self.heartbeat_status[request.server_id] = True
        return HeartbeatResponse(received=True)

    async def SwitchServer(self, request, context):
        self.primary_server = request.new_primary
        return SwitchResponse(success=True)

    async def monitor_heartbeats(self):
        while True:
            await asyncio.sleep(5)
            if not self.heartbeat_status.get(self.primary_server, False):
                print(f"Primary {self.primary_server} failed. Switching to {self.backup_server}.")
                self.heartbeat_status[self.primary_server] = False
                self.primary_server, self.backup_server = self.backup_server, self.primary_server
                if self.proxy:
                    await self.proxy.SwitchServer(SwitchRequest(new_primary=self.primary_server))
            self.heartbeat_status = {key: False for key in self.heartbeat_status}

async def serve():
    server = grpc.aio.server()
    servicer = HeartbeatServicer()
    heartbeat_pb2_grpc.add_HeartbeatServicer_to_server(servicer, server)
    server.add_insecure_port("[::]:50053")
    await server.start()
    asyncio.create_task(servicer.monitor_heartbeats())
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())