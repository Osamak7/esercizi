import time

with open("es2.py" , mode="r")as prova:
    start=time.time()
    contenuto = prova.read()
    time.sleep(1)
    temp_att= time.time()
    print(f"tempo impiegato {start - temp_att}")



    
  