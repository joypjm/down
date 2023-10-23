def divide(num_1, num_2):
    if num_2 == 0:
        print("Error. La división entre 0 es indefinida.")
        return None
    result = num_1 / num_2
    print(f'{num_1} / {num_2} is equal to {result}')
    return result
