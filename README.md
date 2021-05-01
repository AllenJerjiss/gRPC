# project 3 for CSE531 @ASU:  Client-Centric Consistency

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

The problem to solve in this project is built on top of the first gRPC project; A distributed banking system that allows multiple customers to withdraw or deposit money from the multiple branches of a bank.  Here we implement a couple of examples of client-centric consistencies in order to make sure the transactions are recorder in the correct order across the different replicas for any interactions for a given "client", which in this case is the customer.  With the enforcement of the client-centric consistency checks, we are able to remove the limitation where in the first project a customer was only allowed to interact with one specific bank branch.

Goal:

In order to achieve the objective stated in the problem statement, the goal of this project is to implement the "Monotonic Writes" and "Read your Writes" policies in order to enforce client-centric consistency for the bank's customers.

"Monotonic Writes" ensure that when a specific process performs a write operation in a specific order, that it is replicated across all other processes in the same exact order. 

"Read your Writes" is another way to ensure consistency across the replicas, and it mandates that when a transactions is performed by the customer process, that any subsequent transaction is able to work from the latest updated version as the starting point. 


Implementation Process:

The first thing to tackle is to remove the constraint that a given customer can only interact with a specific branch, instead here a customer can access any branch.  We do this by removing the tight coupling done in Customer.py which bound a customer to a specific Id. 

The next step is to update the branch.proto to account for not only sending the message, but the writesets as well in both sending and receiving operations.

We also need to do work in order to make sure that we are not only sending the writeset to the Branch, rather we also maintain the local writeset of operations as we will use that information in order to implement the two different consistency models.

For "Monotonic Writes" we keep track of the writesets of a given customer interaction by pushing each action into a queue as they come in.  When we call the process to synchronize the data across the different branches, we will make sure to process the queue in the FIFO fashion, thereby on each branch, thereby abiding by the Monotonic write principal. 

For "Read Your Writes" consistency, we rely on Lamport's logical clock and maintain a dictionary which maps a customer's ID and the last updated timetamp whenever a Customer does an update.  We then build this check into the query operation, which is performed at the start of a deposit or withdrawal operation as well.  If we find the dictionary to have an entry for any given replica with a larger logical time than our processes, we first adjust the current balance to match across the rest of the replicas and then attempt either the deposit or withdrawal operations.


