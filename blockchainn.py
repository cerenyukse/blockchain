import datetime
from bc import Block
b1 = Block.create_genesis_block()
print(b1.hash) #ilk blok
block_chain=[Block.create_genesis_block()]

print("Genesis block created!")
print("Hash:%s" %block_chain[-1].hash)
num_blocks_to_add =10
for i in range(1,num_blocks_to_add +1): #bir sonraki block oluşturma
    block_chain.append(Block(block_chain[-1].hash,"DATA!",
                             datetime.datetime.now())) #ilk blok çıkar
    print ("Block #%d has been created" %i)
    print ("Block #%d hash: %s" % (i, block_chain[i].hash))
