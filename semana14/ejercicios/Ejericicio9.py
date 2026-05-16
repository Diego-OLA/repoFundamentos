numbers = [1,2,3,4,5,6,7,8 ,9,10]

def contarNumerosPares(nums):
    suma = 0
    for num in nums:
        if num % 2 == 0:
            suma = num + suma

    print("La suma de los números pares es: ", suma)

contarNumerosPares(numbers)