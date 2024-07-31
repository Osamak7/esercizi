import time
    

def funzione(id: int):
    import time
    import random
    
    sleep_time: int = random.randint(1, 10)
    print(f"{id=} time {time.time()}")
    time.sleep(sleep_time)
    print(f"{id=} time {time.time()}")
    
if __name__ == "__main__":
    
    import threading
    from concurrent.futures import ThreadPoolExecutor
    
    with ThreadPoolExecutor(max_workers=10) as executor: # max_worker numero massimo di tread eseguibili 
        executor.map(funzione, range(100))

    
   
   
    
    # lista_thread: list[threading.Thread] = []
    
    # for id in range(3):
        
    #     x: threading.Thread = threading.Thread(target=funzione, args=(id,))
    #     lista_thread.append(x)
    #     print(f"Prima di runnare il thread {time.time()}")
    #     x.start()
    #     print(f"Ho runnato il thread {time.time()}")
    
    # for t in lista_thread:
        
    #     t.join()
    #     print(f"Terminato!")
    