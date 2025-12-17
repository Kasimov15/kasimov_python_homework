# ==================================================
# HOMEWORK
# ==================================================

import threading
from collections import Counter
import math


# ==================================================
# EXERCISE 1
# ==================================================

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def check_primes(start, end, result):
    local_primes = []
    for num in range(start, end):
        if is_prime(num):
            local_primes.append(num)
    result.extend(local_primes)


def threaded_prime_checker(start, end, thread_count):
    threads = []
    primes = []
    step = (end - start) // thread_count

    for i in range(thread_count):
        s = start + i * step
        e = end if i == thread_count - 1 else s + step
        t = threading.Thread(target=check_primes, args=(s, e, primes))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return sorted(primes)


# ==================================================
# EXERCISE 2
# ==================================================

def count_words(lines, result):
    local_counter = Counter()
    for line in lines:
        words = line.lower().split()
        local_counter.update(words)
    result.append(local_counter)


def threaded_word_count(file_path, thread_count):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    threads = []
    results = []
    chunk_size = len(lines) // thread_count

    for i in range(thread_count):
        start = i * chunk_size
        end = len(lines) if i == thread_count - 1 else start + chunk_size
        t = threading.Thread(
            target=count_words,
            args=(lines[start:end], results)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_count = Counter()
    for counter in results:
        total_count.update(counter)

    return total_count


# ==================================================
# MAIN PROGRAM (TESTING BOTH EXERCISES)
# ==================================================

if __name__ == "__main__":

    print("=== EXERCISE 1: THREADED PRIME CHECKER ===")
    primes = threaded_prime_checker(start=1, end=100, thread_count=4)
    print("Prime numbers found:")
    print(primes)

    print("\n=== EXERCISE 2: THREADED FILE WORD COUNT ===")

    # Create a sample file for testing
    sample_text = """Python is great
    Python is fast
    Threading in Python is useful
    Python threading helps performance"""

    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write(sample_text)

    word_counts = threaded_word_count("sample.txt", thread_count=3)

    print("Word occurrences:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
