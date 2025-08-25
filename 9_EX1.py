# Import libraries
import hashlib
import binascii
import datetime
import collections
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

# -----------------------------
# Client
# -----------------------------
class Client:
    def __init__(self):
        random = Crypto.Random.new().read
        self.pri_key = RSA.generate(1024, random)
        self.pub_key = self.pri_key.publickey()
        self.signer = PKCS1_v1_5.new(self.pri_key)

    def identity(self):
        return binascii.hexlify(self.pub_key.exportKey(format='DER')).decode('ascii')

# -----------------------------
# Transaction
# -----------------------------
class Transaction:
    def __init__(self, sender, receiver, value):
        self.sender = sender
        self.receiver = receiver
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity()
        return collections.OrderedDict({
            'sender': identity,
            'receiver': self.receiver,
            'value': self.value,
            'time': self.time
        })

    def sign_transaction(self, signer):
        pri_key = signer.pri_key
        signer = PKCS1_v1_5.new(pri_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

    def display_transaction(self):
        dict = self.to_dict()
        print("sender:", dict['sender'])
        print('-----')
        print("receiver:", dict['receiver'])
        print('-----')
        print("value:", dict['value'])
        print('-----')
        print("time:", dict['time'])
        print('-----')
        print()

# -----------------------------
# Block
# -----------------------------
class Block:
    def __init__(self, previous_block_hash, verified_transactions):
        self.verified_transactions = verified_transactions
        self.previous_block_hash = previous_block_hash
        self.Nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.previous_block_hash).encode('utf-8') + str(self.Nonce).encode('utf-8'))
        return sha.hexdigest()

    def mine(self, difficulty):
        while self.hash[0:difficulty] != "0" * difficulty:
            self.Nonce += 1
            self.hash = self.calculate_hash()

# -----------------------------
# Blockchain display
# -----------------------------
def dump_blockchain(block_list):
    print("Number of blocks in the chain:", str(len(block_list)))
    for i, block in enumerate(block_list):
        print("block #", str(i))
        for tran in block.verified_transactions:
            tran.display_transaction()
# -----------------------------
# Main
# -----------------------------
transactions = []
blockchain = []
transaction_index = 0
clients = []

# สร้าง Client อย่างน้อย 4 คน
for i in range(4):
    clients.append(Client())
    # print("Client", i+1, ":", clients[i].identity())
print('---------------------')

# สร้าง Genesis Block
genesis_block = Block(None, [])
genesis_block.previous_block_hash = None
genesis_block.Nonce = None

# สร้าง Transaction แรก: Genesis ให้ Client[0]
transactions.append(Transaction("Genesis", clients[0].identity(), 50.0))
genesis_block.verified_transactions.append(transactions[transaction_index])
transaction_index += 1

# Digest = hash ของ Genesis block
last_hblock = genesis_block.hash

# ใส่ Genesis block ลงใน blockchain
blockchain.append(genesis_block)

# แสดง blockchain
# dump_blockchain(blockchain)

# Transaction ที่ 2: Client[0] → Client[1]
transactions.append(Transaction(clients[0], clients[1].identity(), 100))
transactions[transaction_index].sign_transaction(clients[0])
transaction_index += 1

# สร้าง Block ใหม่
new_block = Block(last_hblock, [])

# ใส่ transaction นี้ลงใน block
new_block.verified_transactions.append(transactions[1])

# mine block นี้ด้วย difficulty = 4
new_block.mine(4)
last_hblock = new_block.hash

# ใส่ block ใหม่ลงใน blockchain
blockchain.append(new_block)

# -----------------------------
# Transaction ที่ 3: Client[1] → Client[0]
transactions.append(Transaction(clients[1], clients[0].identity(), 2.5))
transactions[transaction_index].sign_transaction(clients[1])
transaction_index += 1

# Transaction ที่ 4: Client[0] → Client[1]
transactions.append(Transaction(clients[0], clients[1].identity(), 1.0))
transactions[transaction_index].sign_transaction(clients[0])
transaction_index += 1

# สร้าง Block ใหม่อีกหนึ่ง
new_block2 = Block(last_hblock, [])
new_block3 = Block(last_hblock, [])

# ใส่ transaction ที่ 3 และ 4
new_block2.verified_transactions.append(transactions[2])
new_block3.verified_transactions.append(transactions[3])

# mine block นี้ด้วย difficulty = 4
new_block2.mine(4)
last_hblock = new_block2.hash

new_block3.mine(5)
last_hblock = new_block3.hash

# ใส่ block ใหม่ลงใน blockchain
blockchain.append(new_block2)
blockchain.append(new_block3)


# -----------------------------
# แสดง blockchain ทั้งหมด
dump_blockchain(blockchain)

# output:
# ---------------------
# Number of blocks in the chain: 4
# block # 0
# sender: Genesis
# -----
# receiver: 30819f300d06092a864886f70d010101050003818d0030818902818100d5e551bcf9bb55cb8bcadb19b3a30fe0d7a751f6b2e3bd8b59a9fbb540e81ba5f44b7cf0a434acbda5eb082bf1b0b5e41d52d55c66752d35cb86baeab504a4344280037e85333262390b72164f0ac1cadc05cebfd69779f6ec15f8e20018659990dbc957a99195c978ddcafcb96e1a96b7aac6df5b05e8c0315d363e79e911a90203010001
# -----
# value: 50.0
# -----
# time: 2025-08-25 15:05:47.621694
# -----

# block # 1
# sender: 30819f300d06092a864886f70d010101050003818d0030818902818100d5e551bcf9bb55cb8bcadb19b3a30fe0d7a751f6b2e3bd8b59a9fbb540e81ba5f44b7cf0a434acbda5eb082bf1b0b5e41d52d55c66752d35cb86baeab504a4344280037e85333262390b72164f0ac1cadc05cebfd69779f6ec15f8e20018659990dbc957a99195c978ddcafcb96e1a96b7aac6df5b05e8c0315d363e79e911a90203010001
# -----
# receiver: 30819f300d06092a864886f70d010101050003818d0030818902818100a54085095c8dfd12a2f4e44ac0c39611ce54bd4d5875440fc18d90a041ba535badf4336b3d6bf769e428e34ba2bcb2freceiver: 30819f300d06092a864886f70d010101050003818d0030818902818100a54085095c8dfd12a2f4e44ac0c39611ce54bd4d5875440fc18d90a041ba535badf4336b3d6bf769e428e34ba2bcb2ff8753cc0ee60f4d041a0388b646d387ffda4c9e625ebec5ae4da1b861158fdda790681d0951bf4ab5ac179401e7ac9c9ef765dc58f6a05c09c144eee6c446f6098cc40093414ac91891b43bd3edcc39390203010001
# f8753cc0ee60f4d041a0388b646d387ffda4c9e625ebec5ae4da1b861158fdda790681d0951bf4ab5ac179401e7ac9c9ef765dc58f6a05c09c144eee6c446f6098cc40093414ac91891b43bd3edcc39390203010001
# -----
# value: 100
# -----
# -----
# value: 100
# -----
# time: 2025-08-25 15:05:47.621694
# -----

# time: 2025-08-25 15:05:47.621694
# -----

# block # 2
# sender: 30819f300d06092a864886f70d010101050003818d0030818902818100a54085095c8dfd12a2f4e44ac0c39611ce54bd4d5875440fc18d90a041ba535badf4336b3d6bf769e428e34ba2bcb2ff8753cc0ee60f4d041a0388b646d387ffda4c9e625ebec5ae4da1b861158fdda790681d0951bf4ab5ac179401e7ac9c9ef765dc58f6a05c09c144eee6c446f6098cc40093414ac91891b43bd3edcc39390203010001
# block # 2
# sender: 30819f300d06092a864886f70d010101050003818d0030818902818100a54085095c8dfd12a2f4e44ac0c39611ce54bd4d5875440fc18d90a041ba535badf4336b3d6bf769e428e34ba2bcb2ff8753cc0ee60f4d041a0388b646d387ffda4c9e625ebec5ae4da1b861158fdda790681d0951bf4ab5ac179401e7ac9c9ef765dc58f6a05c09c144eee6c446f6098cc40093414ac91891b43bd3edcc39390203010001
# -----
# receiver: 30819f300d06092a864886f70d010101050003818d0030818902818100d5e551bcf9bb55cb8bcadb19b3a30fe0d7a751f6b2e3bd8b59a9fbb540e81ba5f44b7cf0a434acbda5eb082bf1b0b5e41d52d55c66752d35cb86baeab504a4344280037e85333262390b72164f0ac1cadc05cebfd69779f6ec15f8e20018659990dbc957a99195c978ddcafcb96e1a96b7aac6df5b05e8c0315d363e79e911a902-----
# receiver: 30819f300d06092a864886f70d010101050003818d0030818902818100d5e551bcf9bb55cb8bcadb19b3a30fe0d7a751f6b2e3bd8b59a9fbb540e81ba5f44b7cf0a434acbda5eb082bf1b0b5e41d52d55c66752d35cb86baeab504a4344280037e85333262390b72164f0ac1cadc05cebfd69779f6ec15f8e20018659990dbc957a99195c978ddcafcb96e1a96b7aac6df5b05e8c0315d363e79e911a90203010001
# -----
# 03010001
# -----
# value: 2.5
# -----
# value: 2.5
# -----
# time: 2025-08-25 15:05:47.654637
# -----
# time: 2025-08-25 15:05:47.654637
# -----

# block # 3
# sender: 30819f300d06092a864886f70d010101050003818d0030818902818100d5e551bcf9bb55cb8bcadb19b3a30fe0d7a751f6b2e3bd8b59a9fbb540e81ba5f44b7cf0a434acbda5eb082bf1b0b5e41d52d55c66752d35cb86baeab504a4344280037e85333262390b72164f0ac1cadc05cebfd69779f6ec15f8e20018659990dbc957a99195c978ddcafcb96e1a96b7aac6df5b05e8c0315d363e79e911a90203010001
# -----
# receiver: 30819f300d06092a864886f70d010101050003818d0030818902818100a54085095c8dfd12a2f4e44ac0c39611ce54bd4d5875440fc18d90a041ba535badf4336b3d6bf769e428e34ba2bcb2ff8753cc0ee60f4d041a0388b646d387ffda4c9e625ebec5ae4da1b861158fdda790681d0951bf4ab5ac179401e7ac9c9ef765dc58f6a05c09c144eee6c446f6098cc40093414ac91891b43bd3edcc39390203010001
# -----
# value: 1.0
# -----
# time: 2025-08-25 15:05:47.655637
# -----
