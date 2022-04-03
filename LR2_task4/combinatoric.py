import numpy as np

class Combinatoric:
    """Класс для работы с основными формулми комбинаторики"""
    def __init__(self):
        pass

     
    def combinations_without_repeats(n, m):
        """Вычислить число сочетаний без повторений
        
        Ключевые аргументы:
        n -- (int) Число, из которого делается выборка
        m -- (int) Число, по которому делается выборка

        Возвращаемое значение:
        (int) Количество комбинаций
        """
        arr = [m, n-m]     # определить основания факториалов в знаменателе
        maximum = max(arr) # определить максимум из оснований факториалов знаменателя
        minimum = min(arr) # определить минимум из оснований факториалов знаменателя

        # Определить число сочетаний. В числителе n!, сокращенный на факториал максимума, в знаменателе факториал минимума 
        result = np.prod(np.arange(maximum + 1, n + 1, 1, dtype=np.object)) // np.math.factorial(minimum)     
        return result


    def combinations_with_repeats(n, m):
        """Вычислить число сочетаний с повторениями
        
         Ключевые аргументы:
        n -- (int) Число, из которого делается выборка
        m -- (int) Число, по которому делается выборка

        Возвращаемое значение:
        (int) Количество комбинаций
        """
        n = n + m - 1                                            # переопределить n для перехода к формуле сочетаний
        result = Combinatoric.combinations_without_repeats(n, m) # определить число сочетаний для нового значения n
        return result


    def accommodation_with_repeats(n, m):
        """Вычислить число размещений с повторениями

          Ключевые аргументы:
        n -- (int) Число, из которого делается выборка
        m -- (int) Число, по которому делается выборка

        Возвращаемое значение:
        (int) Количество комбинаций
        """
        return n**m

    def accomodation_without_repeats(n, m):
        '''Вычислить число размещений без повторений'''
        denominator = n - m
        result = np.prod(np.arange(denominator + 1, n + 1, 1, dtype=np.object))
        return result

    def permutation_without_repeats(n):
        '''Вычислить число перестановок без повторений'''
        return np.math.factorial(n)  # n!

    def permutation_with_repeats(n, array_of_types):
        '''Вычислить число перестановок с повторениями'''
        maximum = max(array_of_types) # определить максимум из оснований факториалов знаменателя
        array_of_types.remove(maximum) #Скоратить на наибольшее основание из знаменателя, исключив его из массива

        # Посчитать значение знаменателя как n_1! * n_2! * n_3! *...* n_m!
        denominator = 1
        for value in array_of_types:
            denominator *= np.math.factorial(value) 

        # Определить число сочетаний. В числителе n!, сокращенный на факториал максимума, в знаменателе произведение факориалов  
        result = np.prod(np.arange(maximum + 1, n + 1, 1, dtype=np.object)) // denominator
        return result
