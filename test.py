
def s_s(m, a):
    exit = 1
    text = ""
    while (exit != '0'):

        first = a
        second = m
        while first != 0 and second != 0:
            if first > second:
                first %= second
            else:
                second %= first
        nod = first + second
        text+=f'НОД введенных чисел равен {nod} \n'
        print('НОД введенных чисел равен',nod)

        if (nod == 1):
            s = 0           
            flag = 0        
            if (a == 0):    
                answ = 0    
                flag = 1   

            else:
                x = a       
                y = m       
                s = 1
                if (a<0):                   
                    x = -a                 
                    s = (-1)**((m-1)//2)   

                while (flag == 0):
                    t = 0   
                    c = x % y               
                    x = c                   
                    if (x == 0):
                        answ = 1            
                        flag = 1            
                    else:
                        while (x%2 == 0):   
                            x = x//2        
                            t = t+1
                        if (t%2==1):       
                            s = s*(-1)**((y**2-1)//8)   
                                                        
                        if (x>1):
                            s = s * ((-1) **(((x - 1) // 2)*((y - 1) // 2)))
                            c = x
                            x = y
                            y = c
                        else:           
                            flag = 1    
                answ = s

            text += f"({a}/{m}) = {answ}\n"
            print('(',a,'/',m,') = ',answ) 

        if (nod == 1):
            deg = int((m-1)//2 )    
            numdeg = [1]            
            adeg = [a]              
            res = 1                 
                                    

            i = 1
            while ((numdeg[i-1])*2<deg):        
                numdeg.append(numdeg[i-1]*2)                  
                adeg.append((adeg[i - 1] * adeg[i - 1]) % m)   
                i = i + 1

            i = i - 1
            while (deg>0):                      
                if (deg >= numdeg[i]):
                    deg = deg - numdeg[i]
                    res = (res * adeg[i]) % m
                i = i - 1

            if (res > int((m-1)//2)):          
                res = res - m
            text += f"<p>{a}<sup>({m}-1)/2</sup> &equiv; {res}(mod {m})</p>\n"
            print(a,'^((',m,'-1)/2) = ',res,' mod ',m)
            if (res == answ):
                text+=f"Число {m} является псевдопростым по основанию {a} (по критерию Эйлера)."
                print('Число ', m,' является псевдопростым по основанию ',a,' (по критерию Эйлера).')
            else:
                text+=f"Число {m} является составным."
                print('Число ', m, ' является составным.')

        return text
    
x = s_s(69,4)
print(x)