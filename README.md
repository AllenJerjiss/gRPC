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

The problem to solve in this to build on top of the first gRPC project; A distributed banking system that allows multiple customers to withdraw or deposit money from the multiple branches of a bank.  The first version of this project did not take into account the problem of the lack of a global clock, which can lead to consistency problems when the multiple branches are synchronizing the customer interactions, as preserving the order of events in a distributed system are critical and, in this case, can lead to discrepancies between the different local data replicas at each branch.  For instance, if customer A deposits 100 dollars and then withdraws 50 versus if they first withdrew the money and then deposited it, since depending on their balance, the latter example might lead to an insufficient funds scenario while the former example does not.  In this project we implement Lamport's logical clock algorithm upon the first project to solve the problem herein.


Goal:

As noted in the problem statement, the overall goal of this project is to implement Lamport's logical clock algorithm to solve the inherent problem due to the lack of a global clock. In order to do this, we need to implement sub-interfaces in the Customer and Branch code to account for keeping track of the local time as well as the Lamport's time.  We do this by incrementing the local counter before we send the data.  When we receive the data, we take the max of the local counter of the receiver and compare it with that of the Lamport's time and increment it. 

Implementation Process:

The first task was to update the Bank.proto to reflect the new Lamport's logical clock in order to be able to send the value between the Branch and Customer processes.  

I went ahead and then implemented a local counter in both of the processes to keep track of a counter representative of the local time for each process, starting at time 0.    

I then went on to update the counter when sending a message, which in my implementation happens from Customer.py by making sure the Lamport's counter increments the local counter by one every time it sends a message.  Vice versa, I went on to update the counter in Branch.py, but this time instead of simply incrementing the local counter and setting as the Lamport time, I compare the reciever and sender's values, and set the Lamport's counter to increment based on that value.
