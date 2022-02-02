'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''

def e_fibonacci(n):
 
    f3 = 0
    f1 = 1
    f2 = 1
    
    if (n in [f1,f3]):
        return True
 
    else:
      
        while f3 < n:
            
            f3 = f1 + f2
            f2 = f1
            f1 = f3
            
        if f3 == n:
            return True
        else:
            return False

def main():
    while True:
        numero = input('Digite um numero para saber se e ou não da sequencia de fibonacci ou digite sair para finalizar: ')
        try:
            if numero == 'sair':
                break
            
            elif e_fibonacci(int(numero)):
                print(f'O numero {numero} e pertecente a sequencia de fibonacci\n')
                
            else:
                
                print(f'O numero {numero} não e pertecente a sequencia de fibonacci\n')
        except:
            print('comando invalido\n')
               

if __name__ == '__main__':
        main()
