import requests, json

from confignode import NODE_URL, PEER_NODES




def validate_blockchain(blockchain):
    chainn=blockchain.chain
    print('len', len(chainn))
    for i in range(0, len(chainn)-1):
        b1 = chainn[i]
        b2 = chainn[i+1]
        #print('i is ', i)
        #print('two', b2.hash)
        #print('one', b2.hasheet())
        STRINGWORKSDOESNT= '''if b2.hash != b2.hasheet():

            print("error hash")
            #print('huh', b1)
            print()
            #print(b2)
            return False'''

        if b2.previous !=  b1.hash:
            print("error hash precedent")
            return False
    print('gucci')
    return True

def find_new_chains():
    # Get the blockchains of every other node
    other_chains = []
    for node_url in PEER_NODES:
        # Get their chains using a GET request
        block = requests.get(url = node_url + "/blocks").content
        # Convert the JSON object to a Python dictionary
        block = json.loads(block)
        # Verify other node block is correct
        validated = validate_blockchain(block)
        if validated:
            # Add it to our list
            other_chains.append(block)
    return other_chains

''' print(b2.previous)
            print(b2.index)
            print(b2.proof_nonce)

            print(b2.hash)
            print(b2.hasheet())'''


