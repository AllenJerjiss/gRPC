# gRPC project for CSE531 @ASU

Prerequsites:

1.  Python 3.9.2
2.  gRPC Python Libraries
       * grpcio
       * grpcio-tools
3.  virtualenv Python library

Setup:

$ git clone https://github.com/AllenJerjiss/gRPC.git
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt



Problem statement:

The problem to solve in this project is to build a distributed banking system that allows multiple customers to withdraw or deposit money from the multiple branches of a bank, for a simplified version of what the real life scenario would be..  Our goal is simplified versus a realistic scenario as we do not account for concurrent updates to the same account and we limit each customer to access money from their home branch only.  Albeit this simplification, the bank ledger needs to be replicated across all branches as one would expect in a real life scenario. 

Goal:

In order to achieve the objective stated in the problem statement, the goal of this project is to implement the communication between the customer and the bank’s branches using gRPC by implementing the interfaces for querying, depositing, and withdrawing money between the customer and branch interactions.  In addition, we use the same technology to implement the syncing of the ledger between the branches by implementing interfaces for propagating deposits and withdrawals amongst the banks’ branches. 

Progress:

