import grpc
import bank_pb2_grpc as pb2_grpc
import bank_pb2 as pb2
import json


class Customer(object):
    
    def __init__(self, id, events=None):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # pointer for the stub
        self.stub = None
        self.host = 'localhost'
        self.portOffset = 58888
        self.serverPort = self.portOffset + self.id

        # instantiate the channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.serverPort))

        # bind the client and the server
        self.stub = pb2_grpc.BankMicroServiceStub(self.channel)

    def transaction(self, message,localCounter):
        message = pb2.Message(message=message)
        lamportCounter = pb2.Message(lamportCounter=localCounter)
        print("send %s" %lamportCounter)
        return self.stub.MsgDelivery(message)

if __name__ == '__main__':
    localCounter = 0
    output = {}
    interfaces = []
    with open("./input.json", 'r') as file:
        interactions = json.load(file)
        for interaction in interactions:
            if str(interaction["type"]) == "branch":
                #noop as this is a branch sync interaction that should be handled by the server side Branch code
                pass
            else:
                for event in interaction["events"]:
                    id = int(interaction["id"])
                    client = Customer(id)
                    #increment the local counter with each send request
                    localCounter +=1
                    result = client.transaction(message=str(event),localCounter=localCounter)
                    interface = event['interface']
                    print(f'id: {id}, interface: {interface}, balance: {result}')
