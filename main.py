import random

def multi_tabl():
    wright_choys = 0
    dont_write_choys = 0
    for i in range(30):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        print(x, "*", y)
        res = x * y
        try:
            answer = int(input("Ответ: "))
        except Exception:
            print("Вы не ввели число")
        else:
            if res != answer:
                print("Не правильно, попробуй еще раз!")
                answer = int(input("Ответ: "))
                dont_write_choys +=1
            else:
                print("Правильно!")
                wright_choys +=1
    print(f"Правильных ответов -{wright_choys}\nНе правильных ответов - {dont_write_choys}")
multi_tabl()




