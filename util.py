# This Python file uses the following encoding: windows-1251

from typing import Tuple, List
from random import randint, choice
from math import gcd, sqrt


def read_text(FILENAME):
    f = open(FILENAME, 'r', encoding='utf8')
    ot = f.read()
    f.close()
    return ot

def read_text_list(filename):
    text = []
    with open(filename, 'r') as f:
        text.append(f.readline())
    return text

def get_random_message(size: int) -> str:
    # ��������� ��������� ������
    m = []
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size):
        m.append(choice(alpha))
    res = ""
    res = res.join(m)
    return res
    
def get_prime_numbers_in_range(start: int, finish: int) -> List[int]:
    # ������� ��� ������� ����� �� �������� ����������
    primes = [] # ������ ������� ����� �� ���������
    # ������ � ������� True - ����� �������, False - ����� ���������
    is_prime = [True] * (finish + 1)
    # 0 � 1 �� �������
    is_prime[0] = is_prime[1] = False
    # ������ ���������� i - �����, is_prime_i - ������� ��� ���
    for i, is_prime_i in enumerate(is_prime):
        if is_prime_i:
            # ��������� ������� ����� � ������, ���� ��� � ���������
            if i >= start:
                primes.append(i)
            # ��� ����� �� i * i �� finish � ����� i ������ i
            for j in range(i * i, finish + 1, i):
                is_prime[j] = False
    return primes

def get_prime_number_in_range(start: int, finish: int) -> int:
    # ������� ������� ����o �� ���������� [start, finish]
    res = get_prime_numbers_in_range(start, finish)
    return res[randint(2, len(res) - 1)]

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    # ������������ �������� �������
    a0 = a
    b0 = b
    t0 = 0
    t = 1
    s0 = 1
    s = 0
    q = a0 // b0
    r = a0 - q * b0
    while r > 0:
        temp = t0 - q * t
        t0 = t
        t = temp
        temp = s0 - q * s
        s0 = s
        s = temp
        a0 = b0
        b0 = r
        q = a0 // b0
        r = a0 - q * b0
    r = b0
    return r, s, t

def binary_pow(a: int, b: int, p: int) -> int:
    # �������� ��������� ���������� � �������
    # ���� ������� ����� 0, �� ��������� ����� 1
    if b == 0:
        return 1
    # ������������� d � �������� �������
    # ������� bin() ���������� ������ ���� '0b1010'
    # ������� ������������� � �������� ������� ���������� �� 2 �������
    d = bin(b)[2:]
    r = len(d) - 1
    # �������� ������ a_i
    a_ = [0] * (r + 1)
    # ������� a_0 = a
    a_[0] = a
    # ��������� a_i ��� i = 1,...,r, r = len(d) - 1
    for i in range(1, r + 1):
        # ��������� a_i
        a_[i] = (a_[i - 1] ** 2) * (a ** int(d[i]))
        # ����� ������� �� ������
        a_[i] %= p
    # ���������� a_r �� ������ ��� ������� ����� d = 1
    return a_[r] % p

def modular_inv(number: int, mod: int) -> int:
    # ������� �������� ����� �� ������ ��� �����
    # ������� ��� ������ � ����� � ������������ ����������� ����
    # ��������� ����������� �������� �������.
    t, x, y = extended_gcd(number, mod)
    # ���� ��� �� ����� 1, �� ��������� ����� ���
    if t != 1:
        raise ValueError('----')
    # ��� ������������� ����� ����� ��������� ������
    return (x % mod + mod) % mod

def get_coprime_in_range(
        start: int, finish: int, number: int) -> int:
    # ������� ����� �� ���������� [start, finish] ������� ������� � number
    for i in range(start, finish):
        if gcd(number, i) == 1:
            return i
    return i

def is_prime(n: int) -> bool:
    # ���������, �������� �� ����� �������.
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_values(a: int, b: int, p: int) -> bool:
    # ��������� �������� ���������� ���������
    #
    return gcd(a, p) == 1 and gcd(b, p) == 1 and p != 2 and is_prime(p)

def get_values(number_of_runs: int) -> List[Tuple[int, int, int]]:
    # ������� ���������� �������� ��� �������� ������� ����������.
    # �������� ����������� ��� ������������ �������� �������.
    values = []
    for _ in range(number_of_runs):
        a, b, p = 0, 0, 0
        # ���� ����� �� ������������� �������� ������
        # ���������� ����� ��������
        while not check_values(a, b, p):
            a, b, p = randint(1, 900), randint(1, 900), randint(1, 900)
        values.append((a, b, p))
    return values

def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac

def get_uneven(x,y):
    num = randint(x,y)
    if num%2==1: return num
    else: 
        num+=1
        return num
    
def get_miller(x):
    num = x - 1
    facs = primfacs(num)
    temp = set(facs)
    got = { i:facs.count(i) for i in temp}
    print(got)
    mini = 10001
    for i in got:
        print(i)
        if int(i)**got[i] < mini : mini = int(i)
    print(mini)

def fast_pow(base, degree, module):
    degree = bin(degree)[2:]
    r = 1

    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module
    return r


def test_Rabin_Miller(n, k):
    text = ""
    if n == 2 or n == 3:
        return [True, text,[d,r]]
    if n < 2 or n % 2 == 0:
        return [False,text,[d,r]]

    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    text+=f"<p>d = {d}, r = {r}</p>\n"
    print('d = {0}'.format(d))
    print('s = {0}'.format(r))
    print('---'*20)

    for i in range(k):
        a = randint(2, int(n/2))
        x = pow(a, d, n)
        text+=f"<p>a = {a}, x = {x}</p>"
        print('a = {0}'.format(a))
        print('x = {0}'.format(x))

        if x == 1 or x == n - 1:
            continue

        for j in range(1, r):
            x = fast_pow(x, 2, n)
            #if x != 0:print('x = {0}'.format(x))
            if x == 1:return [False, text,[d,r]]
            if x == n - 1:return [True,text,[d,r]]
        return [False,text,[d,r]]
    return [True,text,[d,r]]

def s_s(m, a):
    exit = 1
    text = ""
    nod, jac, ans = 1,1,1
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
            
            ans = res
            jac = answ
            otvet = ""
            text += f"<p>{a}<sup>({m}-1)/2</sup> &equiv; {res}(mod {m})</p>\n"
            print(a,'^((',m,'-1)/2) = ',res,' mod ',m)
            if (res == answ):
                text+=f"Число {m} является псевдопростым по основанию {a} (по критерию Эйлера)."
                otvet = "псевдопростым."
                print('Число ', m,' является псевдопростым по основанию ',a,' (по критерию Эйлера).')
            else:
                text+=f"Число {m} является составным."
                otvet = "составным."
                print('Число ', m, ' является составным.')

        return [nod, jac, ans, otvet]
    
