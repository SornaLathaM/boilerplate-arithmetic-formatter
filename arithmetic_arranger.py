def arithmetic_arranger(sum,calc=False):
    soln=''
    line1=line2=line3=line4=''
    if len(sum)>5:
        soln='Error: Too many problems.'
        return soln
    else:
        for s in sum:
            n1,op,n2=s.split()
            if n1.isdigit() and n2.isdigit():
                if len(n1)>4 or len(n2)>4:
                    return 'Error: Numbers cannot be more than four digits.'
            else:
                return "Error: Numbers must only contain digits."
            if op!='+' and op!='-':
                return "Error: Operator must be '+' or '-'."
            sp=max(len(n1),len(n2))
            line1+=n1.rjust(sp+2)+'\t'
            line2+=op+' '+n2.rjust(sp)+'\t'
            line3+='_'*(sp+2)+'\t'
            if op=='+':
                ans=int(n1)+int(n2)
                line4+=str(ans).rjust(sp+2)+'\t'
            elif op=='-':
                 ans=int(n1)-int(n2)
                 line4+=str(ans).rjust(sp+2)+'\t'
        if calc==True:
            soln=line1.rstrip()+'\n'+line2.rstrip()+'\n'+line3.rstrip()+'\n'+line4.rstrip()
            return soln
        else:
            soln=line1.rstrip()+'\n'+line2.rstrip()+'\n'+line3.rstrip()
            return soln
        
