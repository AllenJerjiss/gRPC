# project 2 for CSE531 @ASU:  Logical Clocks

Prerequsites:

1.  Python 3.9.2
2.  gRPC Python Libraries
       * grpcio
       * grpcio-tools
3.  virtualenv Python library

Setup:

1.  git clone https://github.com/AllenJerjiss/gRPC.git
2.  pushd gRPC
3.  pip install -r requirements.txt
4.  Open 2 shells and run the following commands:
      a.  virtualenv venv
      b.  source venv/bin/activate
5.  In the first shell run "python -m Branch"
6.  In the 2nd shell run "python -m Customer"

Problem statement:

The problem to solve in this project is to build a distributed banking system that allows multiple customers to withdraw or deposit money from the multiple branches of a bank, for a simplified version of what the real life scenario would be..  Our goal is simplified versus a realistic scenario as we do not account for concurrent updates to the same account and we limit each customer to access money from their home branch only.  Albeit this simplification, the bank ledger needs to be replicated across all branches as one would expect in a real life scenario. 

Goal:

In order to achieve the objective stated in the problem statement, the goal of this project is to implement the communication between the customer and the bank’s branches using gRPC by implementing the interfaces for querying, depositing, and withdrawing money between the customer and branch interactions.  In addition, we use the same technology to implement the syncing of the ledger between the branches by implementing interfaces for propagating deposits and withdrawals amongst the banks’ branches. 

Progress:

So far my progress has included:
1.  Creating the proto buffer using the uniary mode and compling it to provide an interface for the communication
2.  Spinning up processes dynamically based on the number of branches for a given bank
3.  Processing a message from the Customer and sending it to the correct port corresponding to the branch ID.
4.  Determening the type of interaction and the boilerplate for processing all 3 types of supported operations;  query, depsit, withdraw.


TODO:
1.  Persist the result of operations and calcualte depsoit and withdraw amounts based on it.
2.  Data syncronization between branches
3.  formatting of the oputput to project specifications

