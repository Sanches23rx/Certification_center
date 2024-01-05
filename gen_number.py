import psutil
#за отправную точку берется время использования процессора пользователем

def gen(left=1, right=2**512):
    a = str(psutil.cpu_times())
    a, b, c, d, e = psutil.cpu_times()
    a = int((a % 1)*100000)
    if not hasattr(gen, 'N'):
        gen.N = a
    gen.N = (5 ** 17 * gen.N) % (2 ** 40)
    out = int(str(gen.N * 1.0 / (2 ** 40))[2:]) % right
    if out > left:
        return out
    else:
        return gen(left, right)

def is_prime1(number):
    k = 0
    for i in range(2, int(number ** 0.5) + 2):
        if number % i == 0:
            k = k + 1
            break
    if k <= 0:
        return True
    else:
        return False

def is_prime2(number):
    for _ in range(20):
        n = gen(right=number - 1)
        if pow(n, number - 1, number) != 1:
            return False
        return True

def gen_prime(left=1, right=2 ** 512): #2**64
    while True:
        rand_num = gen() % right
        if rand_num > left:
            if is_prime1(rand_num) and is_prime2(rand_num):
                return rand_num
            else:
                continue
        else:
            gen_prime(left, right)