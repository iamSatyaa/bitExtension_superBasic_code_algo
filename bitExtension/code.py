import bitExtender as bE
bnum=input("Enter binary : ")
num=input("Add binary : ")
if len(bnum)>4:
    print("Simple calculation can't be performed, because binary is in virtual 4 bit register")
    print("Simulation of Bit can make it possible")
    bE.simple_4to8bit_adder(bnum,num)
else:
    print(bin(int(bnum,2)+int(num,2)))
