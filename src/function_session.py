
# functions

def print_greeting(name):
    print(f"Hi ..{name}")


def get_greeting(name):
    return f"the custom name is {name}"


def get_multiply(*num_list):
    print(f"this returns the factorial")
    print(type(num_list))
    total = 1
    for num in num_list:
        total *= num
    return total


def get_even_list(num_list):
    print(type(num_list))
    print(f"received list is {num_list}")
    return num_list[::2]


def word_count(sent):
    print(f"received sentence is : {sent}")
    words = sent.split(" ")
    wc_dict = {}
    for word in words:
        print(word)
        if word in wc_dict:
            wc_dict[word] = wc_dict[word] + 1
        else:
            wc_dict[word] = 1
    for key, value in wc_dict.items():
        print(key, value)


def char_frequency(sent):
    print(f"received sentence is: {sent}")
    char_freq = {}
    for char in sent:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    char_freq_sorted_list = sorted(char_freq.items(),
                                   key=lambda item: item[1],
                                   reverse=True)

    for i in range(len(char_freq_sorted_list)-1):
        my_tuple = char_freq_sorted_list[i]
        print(my_tuple)
        if my_tuple[0] == ' ':
            char_freq_sorted_list.pop(i)
            break
    print(char_freq_sorted_list)

    print("The most repeated character apart from \' \' is",
          char_freq_sorted_list[0])


# Main program
print_greeting("New name")
print(get_greeting("test message"))
print(get_multiply(1, 2, 3, 4))
# print even through func
print(get_even_list(list(range(50))))
word_count("Hello this is not a Hello but this is Hi")
char_frequency("Hello this is not a Hello but this is Hi")
