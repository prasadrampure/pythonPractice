import time
import threading

def Sum(No1,No2):
    return No1+ No2

def main():
    starttime = time.perf_counter()
    t1 = threading.Thread(target=Sum)
    t1.start()
    endtime - time.perf_counter()

    print(f"Time required is ; {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()