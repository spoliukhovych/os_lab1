import threading
import time


class CalculationManager:
    def __init__(self):
        self.result_cache = {}
        self.failure_reason = None
        self.cancelled = False
        self.max_failures = 3  # Порогова кількість некритичних збоїв
        self.timeout_limit = 5  # Ліміт часу на обчислення

    def calculate_f(self, x):
        # Мемоізація
        if x in self.result_cache:
            return self.result_cache[x]

        # Реалізація обчислення f
        time.sleep(2)  # Демонстраційна затримка
        result = x * 2  # Приклад

        # Зберігання результату в кеші
        self.result_cache[x] = result
        return result

    def calculate_g(self, x):
        # Мемоізація
        if x in self.result_cache:
            return self.result_cache[x]

        # Реалізація обчислення g
        time.sleep(3)  # Демонстраційна затримка
        result = x + 5  # Приклад

        # Зберігання результату в кеші
        self.result_cache[x] = result
        return result

    def binary_operation(self, f_result, g_result):
        # Реалізація бінарної операції
        return f_result * g_result  # Приклад

    def calculate_expression(self, x):
        try:
            # Паралельні обчислення f та g
            f_result = self.calculate_f(x)
            g_result = self.calculate_g(x)

            # Обчислення бінарної операції
            result = self.binary_operation(f_result, g_result)
            print(f"Result: {result}")

        except Exception as e:
            self.failure_reason = str(e)

    def run_calculation(self, x):
        # Запуск обчислення та обробка результату
        start_time = time.time()

        try:
            calculation_thread = threading.Thread(target=self.calculate_expression, args=(x,))
            calculation_thread.start()

            while calculation_thread.is_alive():
                elapsed_time = time.time() - start_time
                if elapsed_time > self.timeout_limit:
                    self.cancelled = True
                    calculation_thread.join()
                    self.failure_reason = "Calculation timed out"
        except Exception as e:
            self.failure_reason = str(e)

        # Вивід результату
        if self.failure_reason is not None:
            print(f"Calculation failed. Reason: {self.failure_reason}")
        elif self.cancelled:
            print("Calculation cancelled due to timeout")


if __name__ == "__main__":
    manager = CalculationManager()
    x_value = int(input("Enter a value for x: "))
    manager.run_calculation(x_value)