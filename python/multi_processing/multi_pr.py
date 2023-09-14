import time
import multiprocessing

def count1(N):
    count = 0
    for i in range(N):
        count += 1
    print("done with count1")

def count2(N):
    count = 0
    for i in range(0, N, 2):
        count +=1
    print("done with count2!")

#single processing example
#N = 5 * 9**8
#start_time = time.time()

#count1(N)
#count2(N)

#end_time = time.time()

#print("total time taken in single is: ", end_time - start_time)

#multiprocessing using the same example

if __name__ == "__main__":
    N = 5 * 9**8
    
    start_time = time.time()

    pr1 = multiprocessing.Process(target=count1, args=(N,))
    pr2 = multiprocessing.Process(target=count2, args=(N,))

    pr1.start()
    pr2.start()

    pr1.join()
    pr2.join()

    end_time = time.time()

    print("total time taken in multi is: ", end_time - start_time)

