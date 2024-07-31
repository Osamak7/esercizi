from multiprocessing import Process
import time

def bubble_sort_v2():
    from random import randint

    x =[randint(0 , 10000) for _ in range(50000)]
    ho_fatto_swap : bool = True
    
    for i in range(len(x)):
        for j in range(len(x) -i -1):
            if x[j] > x[j+1]:
                ho_fatto_swap =False
                temp: int = x[j]
                x[j] = x[j +1]
                x[j+1] = temp
        if ho_fatto_swap:
            break


def sleep():
    print(f"Sono nella funzione ")
    tic: float = time.time()

    time.sleep(1)

    toc :float= time.time()
    time_elapsed_padre : float =toc -tic 

    print(f"{time_elapsed_padre=}")
    print(f"sto uscendo dalla funzione")

if __name__== "__main__":
    tic: float = time.time()

    t1 = Process(target=bubble_sort_v2)
    t2 = Process(target=bubble_sort_v2)
    t3 = Process(target=bubble_sort_v2)
    t4 = Process(target=bubble_sort_v2)
    t5 = Process(target=bubble_sort_v2)
    t6 = Process(target=bubble_sort_v2)
    t7 = Process(target=bubble_sort_v2)
    t8 = Process(target=bubble_sort_v2)
    t9 = Process(target=bubble_sort_v2)
    t10 = Process(target=bubble_sort_v2)
    t11= Process(target=bubble_sort_v2)
    t12= Process(target=bubble_sort_v2)
    t13= Process(target=bubble_sort_v2)
    t14= Process(target=bubble_sort_v2)
    t15= Process(target=bubble_sort_v2)
    t16= Process(target=bubble_sort_v2)
    t17= Process(target=bubble_sort_v2)
    t18= Process(target=bubble_sort_v2)
    t19= Process(target=bubble_sort_v2)
    t20= Process(target=bubble_sort_v2)
   
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()


    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()

    toc :float= time.time()
    time_elapsed : float =toc -tic 

    print(f"{time_elapsed=}")