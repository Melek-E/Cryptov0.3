import hashlib

import requests

from time import time

from datetime import datetime

from find import find_new_chains, validate_blockchain
from confignode import NODE_URL, PEER_NODES
from flask import Flask, redirect, url_for, render_template, request, Blueprint

MINER_NODE_URL = "http://localhost:5000"






def consensus(blockchain):
    # Get the blocks from other nodes
    other_chains = find_new_chains()
    # If our chain isn't longest, then we store the longest chain
    BLOCKCHAIN = blockchain
    longest_chain = BLOCKCHAIN
    for chain in other_chains:
        if len(longest_chain) < len(chain):
            longest_chain = chain
    # If the longest chain wasn't ours, then we set our chain to the longest
    if longest_chain == BLOCKCHAIN:
        # Keep searching for proof
        return False
    else:
        # Give up searching proof, update chain and start over again
        BLOCKCHAIN = longest_chain
        return BLOCKCHAIN

class Blockchain:
    def __init__(self):

        self.chain= [] #constructing the first block and creating our chain
        self.genesis()
        #print(self.chain)
        self.comptransact= [] #all completed transactions
        self.newtransact= []  #all new transactions
        self.nodes= [] #our system of computers
        self.reward=50 #reward for mining a block


    def create(self, Transac, index):


        #timestamp
        time=datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        print('Creating a new block at', time)
        #creating block using Transac: transaction class
        newblock= Block(Transac, time , index)
        #verification de l'index pour voir si c'est le bloc genesis
        if index>0:
            newblock.previous=self.chain[index-1].hash
        self.chain.append(newblock)

        return newblock

    #fonction genesis pour la creation du premier bloc
    def genesis(self):
        genesis= self.create(Transaction('me','me',50) , 0)
        genesis.previous=None
        return genesis

    #Ajouter une nouvelle transaction, verfication pas complete!!!! faut lier ca aux autres nodes
    def addTransaction(self, newtrans):
        if not newtrans.sender and not newtrans.receiver and not newtrans.amount:
            print("Erreur transaction 1")
            return False
        if newtrans.sender == newtrans.receiver :
            return False

        self.newtransact.append(newtrans)
    #pas complete
    def find_new_chains(self):
        other_chains=[]
        for node_url in PEER_NODES:
            pass




    #proof of work avec verfication
    def proof_of_work(self, last_proof, blockchain):
        # Creates a variable that we will use to find our next proof of work
        incrementer = last_proof + 1
        # Keep incrementing the incrementer until it's equal to a number divisible by 7919
        # and the proof of work of the previous block in the chain
        start_time = time()
        while not (incrementer % 1313 == 0 and incrementer % last_proof == 0):
            incrementer += 1
            # Check if any node found the solution every 60 seconds
            if int((time() - start_time) % 60) == 0:
                # If any other node got the proof, stop searching
                new_blockchain = consensus(blockchain)
                if new_blockchain:
                    # (False: another node got proof first, new blockchain)
                    return False, new_blockchain
        # Once that number is found, we can return it as a proof of our work
        return incrementer, blockchain

    #mining
    def mine(self, blockchain):
        lenPT = len(self.newtransact);
        if lenPT <= 1:
            print("Not enough transactions to mine! (Must be > 1)")
            return False
        else:
            # Find the proof of work for the current block being minedvalidate_blockchain
            last_block=self.chain[-1]
            last_proof=last_block.proof_nonce
            self.proof_of_work(last_proof, blockchain)







    #affichage
    def __str__(self):
        for block in self.chain:
            print(block.__str__())


class Block:
    def __init__(self, transactions, time, index):
        self.previous=0 #the hash of the previous block, our link
        self.transactions=transactions
        self.index = index
        self.timestamp=time
        self.proof_nonce=1 #A nonce is an abbreviation for "number only used once"
        self.hash=self.hasheet() #fonction hashing

    def hasheet(self):
        stringhash="{}{}{}".format(self.previous, self.index, self.proof_nonce)
        return hashlib.sha256(stringhash.encode('utf-8')).hexdigest() #sha256() to create a SHA-256 hash object
                                                      #hexdigest for the output (digest)



    #affichage block
    def __str__(self):
        temp="Prev: {}\nTransactions: {}\nIndex: {}\nPoN: {}\nHash: {}\n".format(self.previous, self.transactions, self.index, self.proof_nonce, self.hash)
        return temp


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender=sender
        self.receiver=receiver
        self.amount=amount



    def __str__(self):
        temp={'sender': "{}".format(self.sender), 'receiver': "{}".format(self.receiver), 'quantity':self.amount}
        return str(temp)



#creating test blocks
transactions=[]
'''X=Block("6e27587e8a27d6fe376d4fd9b4edc96c8890346579e5cbf558252b24a8257823", {'sender': '0', 'recipient': 'Quincy Larson', 'quantity': 1}, time() )
X=Block(transactions, {'sender': '0', 'receiver': 'Quincy Larson', 'quantity': 1}, time() )'''

trans=Transaction('me','me',444)
trans2=Transaction('me','you',123)
Y=Blockchain()
Y.create(trans, 1)
Y.create(trans2, 2)

#print(Y.__str__())

temp=Transaction('test','noot',5)
Y.addTransaction(temp)
Y.addTransaction(temp)


Y.mine(Y)

#print('tes')

#validate_blockchain(Y)

print(str(trans))
#print(Y.__str__())
#print(Y.genesis().transactions)

#print(X.__str__())
