import time
from threading import Thread
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i} \n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
print(f"Время выполнения функций: {end_time - start_time} секунд")

start_time2 = time.time()
thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_forth = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_forth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_forth.join()

end_time2 = time.time()
print(f"Время выполнения функций: {end_time2 - start_time2} секунд")

#write_words(10, 'example5.txt')
#write_words(30, 'example6.txt')
#write_words(200, 'example7.txt')
#write_words(100, 'example8.txt')