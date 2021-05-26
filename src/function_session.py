
# functions

def print_greeting(name):
    print(f"Hi ..{name}")


def get_greeting(name):
    return f"the custom name is {name}"


def get_multiply(*num_list):
    print(f"this returns the product of all numbers in list")
    print(type(num_list))
    total = 1
    for num in num_list:
        total *= num
    return total

def get_fact(num):
    print("Printing the factorial of the given number - ")
    print(num)
    if(num<0):
        print("Factorial could not be calculated due to bad number")
    elif(num==0):
        print("Factorial of 0 is 1")
    else:
        counter = 1
        product = 1
        while(counter<=num):
            product = product * counter
            counter += 1
        print("The factorial of ", num , " is ", product)
            



def word_count(sent):
    print(f"received sentence is : {sent}\n")
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
    print(f"received sentence is: {sent}\n")
    char_freq_dict = {}
    for char in sent:
        if char in char_freq_dict:
            char_freq_dict[char] += 1
        else:
            char_freq_dict[char] = 1
            
    print("unsorted dict of chars is ", char_freq_dict)
    
    #remove the item ' '
    char_freq_dict.pop(' ')
    
    #sorted returns a list with tuples of char and count
    char_freq_sorted_list = sorted(char_freq_dict.items(),
                                   key=lambda item: item[1],
                                   reverse=True)
    

    print("\nsorted dict with out \' \'", char_freq_sorted_list)

    print("\nThe most repeated character apart from \' \' is",
          char_freq_sorted_list[0])


# Main program
#multiple calls
print_greeting("New name")
print(get_greeting("test message"))
print(get_multiply(1, 2, 3, 4))
word_count("Hello this is not a Hello but this is Hi")
char_frequency("Hello this is not a Hello but this is Hi ieieieieieieieieieieieieieieieieieieieieieieieieie")

get_fact(6)
