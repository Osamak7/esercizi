import time

class Tempo_di_esecuzione:
    @staticmethod
    def tempo_imp(func):

        def wrap(*arg):
            start= time.time()
            time.sleep(1)
            print(f"tempo impiegato = {start - time.time()}")
        
        return wrap
    
@Tempo_di_esecuzione.tempo_imp
def ciclo(num_volte:int):
    a:int= 0
    for i in range(num_volte):
        print(a)
        a+=1
ciclo(1000000)