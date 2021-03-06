"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def print_list(my_list):
    """Print each item in the input list

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9

    """
    # Iterate through the input list and print each item.
    for item in my_list:
        print item


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    odd_nums = []  # Create an empty list that will be used to store all odd numbers.

    for num in number_list:
        if num % 2 != 0:  # num % 2 == 0 is true for all even numbers. If num % 2 is not 0 then the number must be odd.
            odd_nums.append(num)  # Append all numbers to the list that meet the condition on line 36.

    return odd_nums  # Return the list.


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    even_nums = []  # Create an empty list that will be used to store all even numbers.

    for num in number_list:
        if num % 2 == 0:  # If the num divided by 2 has a remainder of 0, then it must be an even number.
            even_nums.append(num)  # Append all even numbers to the list.

    return even_nums  # Return the list.


def every_other_item(my_list):
    """Return a list that contains every other item in my_list starting
       with the first item.

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["you", "friend", "are", "very", "good", " ", "at", " ", "coding"])
       ['you', 'are', 'good', 'at', 'coding']

    """
    every_other_item_list = my_list[::2]  # From the beginning of the list to the end, give back every other number then bind resulting list to an identifier.

    return every_other_item_list


def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """
    #  Iterate through list and print the index of the element and the respective element.
    for item in my_list:
        print my_list.index(item), item


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    long_words_list = []  # Create an empty list to store words that have more than 4 characters.

    for word in word_list:
        if len(word) > 4:  # If the length of the word is more than 4 characters, then append the word to the list.
            long_words_list.append(word)

    return long_words_list  # Return the list


def n_long_words(word_list, n):
    """Return all words in input list that are longer than n characters.

    >>> n_long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"], 3)
    ['hello', 'spam', 'spam', 'bacon', 'bacon']

    >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
    ['apples', 'bananas']
    """
    n_long_words_list = []  # Create an empty list that will store words longer than n characters.

    for word in word_list:  # If length of word in input list is longer than the n argument, then append word to the list.
        if len(word) > n:
            n_long_words_list.append(word)

    return n_long_words_list


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """
    number_list.sort()  # Sort elements in input list in-place using the sort method.
    if number_list == []:  # If input list is an empty list, return None.
        return None
    else:
        smallest_integer = number_list[0]  # Bind identifier to the first element in the list, which will be the smallest integer in input list.
        return smallest_integer


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """
    number_list.sort()  # Sort elements in input list in-place using the sort method.
    if number_list == []:  # If input list is an empty list, return None.
        return None
    else:
        largest_integer = number_list[-1]  # Bind identifier to the last element of input list, which will be the largest integer in input list.
        return largest_integer


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    halves_list = []  # Create an empty list that will store halved integers from input list.

    for num in number_list:
        halved_num = float(num)/2  # Bind identifier to expression to get halved float value of integer from input list.
        halves_list.append(halved_num)  # Append halved integer to list.

    return halves_list


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    len_list = []  # Create an empty list that will store the length of the words from input list.

    for word in word_list:
        len_list.append(len(word))  # Append the length of word to list.

    return len_list


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    total = 0  # Initialize total count.

    for num in number_list:
        total += num  # Increment total by num from input list.

    return total


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    product = 1  # Bind identifier to 1.

    for num in number_list:
            product *= num  # Multiply product by num from input list.

    return product


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    join_words = ""  # Bind identifier to empty string.

    for word in word_list:
        join_words += word  # Concatenate string to join_words.

    return join_words


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    sum_total = 0  # Bind identifier to 0.

    for num in number_list:
        sum_total += num  # Get the sum of all numbers from input list
        avrg = float(sum_total)/len(number_list)  # Divide the float sum of the numbers by length of the list to get average.

    return avrg


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """
    new_word = ""  # Bind identifier to empty string.

    for word in list_of_words:
        if len(list_of_words) == 1:  # If the length of the input list is 1, then print word as a string.
            new_word = word
        else:
            if word == list_of_words[-1]:  # If the word is the last element in list, then add word to new_word.
                new_word += word
            else:
                new_word += word + ", "  # Add each word to new_word followed by a comma and a space.

    return new_word


def foods_in_common(foods1, foods2):
    """Using ANY Python data structure presented in the last week, given 2 lists of foods,
    return a set of items that are in common between the two. (Don't include any duplicates
    in the output collection.)

    For example:

    >>> foods_in_common(["cheese", "bagel", "cake"], ["hummus", "beets", "bagel", "lentils"])
    set(['bagel'])

    If there are no foods in common, return an empty set.

    >>> foods_in_common(["lamb", "chili", "cheese"], ["cake", "ice cream"])
    set([])

    """
    in_common_foods_set = set(foods1) & set(foods2)  # Convert both arguments to sets and find the intersection of both sets.

    return in_common_foods_set


def reverse_list(my_list):
    """Return the inputted list, reversed.

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

    Do not use the python methed reverse()/reversed().

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    """
    # From the first element to the last element of input list, return the list in reverse order.
    reversed_list = my_list[::-1]
    return reversed_list


def reverse_list_in_place(my_list):
    """Return the inputted list reversed--WITHOUT creating a new list.
       This will involve moving the items in my_list to different positions
       in the same list.

       Do not use the python method reverse()/reversed()

        >>> reverse_list_in_place([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list_in_place(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    """
    i = 0  # Initialize identifier to 0.
    for item in my_list:
        last_item = my_list.pop()  # Pop last element of input list and bind to an identifier.
        my_list.insert(i, last_item)  # Insert popped item to index i.
        i += 1  # Increment value and bind to i for each iteration.

    return my_list


def duplicates(my_list):
    """Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    >>> duplicates(["apple", "apple", "banana", "cherry", "banana", "apple"])
    ['apple', 'banana']

    >>> duplicates([1, 2, 2, 4, 4, 4, 7])
    [2, 4]

    """
    unique_list = []  # Create an empty list to store only unique items.
    duplicate_set = set()  # Create an empty set to store duplicate items found in input list.

    for item in my_list:
        if item in unique_list:  # If item in unique_list, add item to duplicate_set.
            duplicate_set.add(item)
        else:
            unique_list.append(item)  # Append any items not found in unique_list to unique_list.

    return list(duplicate_set)  # Convert set to list and return list of all duplicate items.


def find_letter_indices(list_of_words, letter):
    """Given a list of words and a letter, return a list of integers that correspond
    to the index of the first occurance of the letter in that word.

    Do not use the .index() list method.

    >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
    [0, 1, 2]

    If the letter doesn't occur in one of the words, use None for that word in
    the output list. For example:

    >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
    [0, 1, 2, None]

    """
    index = -1  # The index value of the first element in a list is 0, therefore identifier is set to -1.
    index_list = []  # Create an empty list to store integers corresponding to the first occurance of the letter.

    for word in list_of_words:
        if letter in word:  # If letter found in a word in input list, then increment index and append to list.
            index += 1
            index_list.append(index)
        else:
            index_list.append(None)  # Otherwise, append None if letter not found in word.

    return index_list


def largest_n_items(input_list, n):
    """Given a list of integers along with an integer n, return a
    list of the largest n numbers in the input list in ascending order.

    You can assume that n will be less than the length of the list.

    For example:

    >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
    [59, 700, 6006]

    """
    largest_n_items_list = []  # Create an empty list to store largest n integers.

    input_list.sort()  # Sort input list by ascending order.

    for num in input_list:
        if len(largest_n_items_list) == n:
            break
        else:
            largest_n_items_list.append(input_list.pop())  # Pop last item in input list and append to largest_n_items_list.
            largest_n_items_list.sort()  # Sort list.

    return largest_n_items_list


##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.
if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
