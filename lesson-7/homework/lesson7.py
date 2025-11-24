# ============================================================
# MAP and FILTER explanations with examples
# ============================================================

print("=== MAP explained ===")
print("""
map(function, iterable) — применяет функцию к каждому элементу списка.

Example:
numbers = [1, 2, 3]
doubled = list(map(lambda x: x*2, numbers))
# Result: [2, 4, 6]
""")

print("=== FILTER explained ===")
print("""
filter(function, iterable) — оставляет только те элементы,
для которых функция возвращает True.

Example:
numbers = [1, 2, 3, 4]
even = list(filter(lambda x: x % 2 == 0, numbers))
# Result: [2, 4]
""")


# ============================================================
# 1. is_prime(n) — tub son aniqlash funksiyasi
# ============================================================

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):   # √n gacha tekshirish
        if n % i == 0:
            return False
    return True


# ============================================================
# 2. digit_sum(k) — raqamlar yig'indisi
# ============================================================

def digit_sum(k):
    return sum(map(int, str(k)))   # lambda ham bo'lishi mumkin: lambda x: int(x)


# ============================================================
# 3. powers_of_two(N) — N dan oshmaydigan 2**k darajalarini chiqarish
# ============================================================

def powers_of_two(N):
    p = 1
    result = []
    while p <= N:
        result.append(p)
        p *= 2
    return result


# ============================================================
# TEST INPUTS
# ============================================================

print("\n--- Test: is_prime ---")
n = int(input("n = "))
print("Natija:", is_prime(n))

print("\n--- Test: digit_sum ---")
k = int(input("k = "))
print("Natija:", digit_sum(k))

print("\n--- Test: powers_of_two ---")
N = int(input("N = "))
print("Natija:", *powers_of_two(N))
