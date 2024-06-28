import time
import threading


threads:list = []

def thread_function(name):
    print(f"name: {name} ,time :{time.time()}")
    time.sleep(2)
    print(f"name: {name}, time :{time.time()}")

for i in range(3):
    x = threading.Thread(target=thread_function, args=(i,)) #tra parentesi e con la virgola perche senno non lo riconosce come tupla 
    threads.append(x)
    x.start()

for t in threads:
    t.join()
    
# print(f"Prima di thread")
# x.start()
# print(f"thread partito")
# x.join()
# print(f"thread finito?????")
