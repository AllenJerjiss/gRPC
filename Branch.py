import grpc
import bank_pb2_grpc as pb2_grpc
import bank_pb2 as pb2
import json
import re
from concurrent import futures
import threading
from multiprocessing import Process
import time


portOffset = 58888 

class BranchService(pb2_grpc.BankMicroServiceServicer):

    def __init__(self, id, balance):
        # unique ID of the Branch
        self.id = id
        #self.processid = processid
        # replica of the Branch's balance
        self.balance = balance
        # the list of process IDs of the branches, this list will update by find_process_ids function
        self.branches = []
        # the list of Client stubs to communicate with the branches
        self.stubList = list()
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        self.Request = []


    def MsgDelivery(self, request, context):
        #ensure that one message is processed at the same time by obtaining a lock
        lock = threading.Lock()
        with lock:
            message = request.message
            money = re.search('\'money\': (.+?)}', message)
            if 'query' in message:
                if money:
                    #for a query, we don't change the balance
                    balance = money.group(1)
            elif 'deposit' in message:
                if money:
                    #todo:  create class dict to store balance and update based on action
                    balance = str(400 + int(money.group(1)))
            elif 'withdraw' in message:
                if money:
                    #todo:  create class dict to store balance and update based on action
                    balance = str(400 - int(money.group(1)))

        result = {'message': balance, 'received': True}
        time.sleep(1)
        return pb2.MessageResponse(**result)


def bankServer(branch_id,balance):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    branch = BranchService(branch_id, balance)
    pb2_grpc.add_BankMicroServiceServicer_to_server(branch, server)
    server.add_insecure_port('localhost:'+ str(portOffset + branch_id))
    server.start()
    print("Branch %s is listening on port %s" % (branch_id,portOffset + branch_id))
    server.wait_for_termination()


if __name__ == '__main__':
    balance = []
    processes = []
    with open("./input.json", 'r') as file:
        interactions = json.load(file)
    for interaction in interactions:
        #branch sync interaction should be handled by the server side Branch code
        if interaction["type"] == "branch":
            balance.append({"id":interaction["id"], "balance":interaction["balance"]})
    for interaction in interactions:
        processes = []
        #start the banck to bank sync process
        if interaction["type"] == "branch":
            p = Process(target=bankServer, args=(interaction["id"],balance))
            processes.append(p)
            p.start()
    for proc in processes:
        proc.join()
