def swap_chars(input_string, i, j):
    sub_result = list(input_string)
    aux = sub_result[i]
    sub_result[i] = sub_result[j]
    sub_result[j] = aux

    return "".join(sub_result)


def generate_permutations(input_string, i, solutions):
    if i == len(input_string):  # GOAL
        solutions.add(input_string)
    else:
        for j in range(i, len(input_string)):   # CHOICES
            input_string = swap_chars(input_string, i, j)
            generate_permutations(input_string, i + 1, solutions)


if __name__ == "__main__":
    results = set()
    generate_permutations("abc", 0, results)
    print(results)
