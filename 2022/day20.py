from mycode import readfromfile
intel = readfromfile('input20')

file = []
for i,line in enumerate(intel):
    if line=='':
        break
    if int(line)==0:
        zeroth = (i,0)
    file.append((i,int(line)))

L = len(file)-1
decrypted = file.copy()
for i in range(len(file)):
    byte = file[i]

    index = decrypted.index(byte)
    decrypted.pop(index)

    new_index = (index+byte[1])%L
    if new_index==0 and byte[1]<0:
        decrypted.insert(L+1,byte)
    else:    
        decrypted.insert(new_index,byte)


#print(decrypted)

start = decrypted.index(zeroth)
total = 0
for i in range(1,4):
    #print(decrypted[(start+i*1000)%(L+1)][1])
    total += decrypted[(start+i*1000)%(L+1)][1]
print(total)
