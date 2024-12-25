def algorithm(limit):
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return [i for i in range(limit + 1) if is_prime[i]]

def get_user_input():
    while True:
        try:
            user_input = input("Введите до какого числа будем искать (целое положительное число): ")
            limit = int(user_input)

            if limit < 1:
                print("Ошибка: Пожалуйста, введите положительное целое число больше 0.")
                continue

            return limit

        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное целое число.")

def main():
    limit = get_user_input()
    primes = algorithm(limit)
    print(f"Простые числа до {limit}: {primes}")
    exit_prog = input("Нажмите Enter для выхода из программы")

if __name__ == "__main__":
    main()