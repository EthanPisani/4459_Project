import grpc
import chat_pb2
import chat_pb2_grpc
import proxy_pb2_grpc
import threading

class ChatClient:
    def __init__(self, name):
        self.name = name
        self.channel = grpc.insecure_channel('localhost:50052') # TODO don't hardcode proxy address
        self.stub = proxy_pb2_grpc.ProxyServiceStub(self.channel)

    def join_chat(self):
        response = self.stub.Join(chat_pb2.JoinRequest(name=self.name))
        print(response.welcome_message)

    def send_message(self):
        while True:
            msg = input(f"{self.name}: ")
            if msg.lower() == 'exit':
                print("Exiting chat...")
                break
            self.stub.SendMessage(chat_pb2.Message(sender=self.name, content=msg))

    def receive_messages(self):
        for message in self.stub.ReceiveMessages(chat_pb2.Empty()):
            print(f"{message.sender}: {message.content}")

    def run(self):
        self.join_chat()
        threading.Thread(target=self.receive_messages, daemon=True).start()
        self.send_message()

if __name__ == '__main__':
    name = input("Enter your name: ")
    client = ChatClient(name)
    client.run()
