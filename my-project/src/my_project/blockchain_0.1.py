class BLockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []


    def new_block(self):
        # Generate new block and add it to the chain
        pass

    @staticmethod
    def hash(block):
        # Hashes a block
        pass
    
    def last_block(self):
        # Gets the latest block in the chain
        pass

    def new_transaction(self, sender, recipient, amount):
        # Adds a new transaction to the list of pending transactions
        self.pending_transactions.append({
            "recipient": recipient,
            "sender": sender,
            "amount": amount                   
    })