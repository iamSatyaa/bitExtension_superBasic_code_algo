def simple_4to8bit_adder(a,b):
    frag1=a[0:4]
    frag2=a[4:8]
    x=bin(int(frag2,2)+int(b,2))
    if len(x)==7:
        powerbit=x[2]
        modified_frag1=bin(int(frag1,2)+int('1',2))
        frag1=str(modified_frag1)
        frag2=str(x)
        result=frag1+frag2[3:11]
        print(result)
    elif len(x)==6:
        result=str(frag1)+str(x)[2:11]
        print(result)
