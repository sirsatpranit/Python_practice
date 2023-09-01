import time
list1 = list(range(10))
list2 = list(range(100))
list3 = list(range(1000))

for list in [list1, list2, list3]:
    start_time = time.time()
    time.sleep(5)
    print(len(list))
    end_time = time.time()
    print(f"required time = {end_time-start_time}")