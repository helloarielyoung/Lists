"""List Assessment - for E. Ariel Young, Ada Cohort June 2017

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """
    #create my final list to hold the output
    odd_list =[]

    #iterate through the list and append the odd ones to my list
    for number in numbers:
        if number % 2 == 0:
            continue
        else:
            odd_list.append(number)

    return odd_list


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

        >>> print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])
        0 Toyota
        1 Jeep
        2 Toyota
        3 Volvo

    """
    #iterte through the list and print the index and the item
    for i in range(len(items)):
        print i, items[i]


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale", "zebra cakes"],
        ...     ["hummus", "cheese", "beets", "kale", "lentils", "bagel", "cake" ]
        ... )
        ['bagel', 'cake', 'cheese', 'kale']

    The returned list should not have any duplicates::
        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "cheese"],
        ...     ["hummus", "cheese", "beets", "kale", "bagel", "cake"]
        ... )
        ['bagel', 'cake', 'cheese']

    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """

    #convert both lists to sets so I can use set math
    foods1_as_set = set(foods1)
    foods2_as_set = set(foods2)

    #create a set to hold the result
    items_in_common_set = set()

    #identify the items in common using set math
    items_in_common_set = (foods1_as_set & foods2_as_set)

    # # #create list to hold the output
    items_in_common_list = []

    # #turn result set into a list for output;
    items_in_common_list = list(items_in_common_set)

    # #alphabetize the list
    items_in_common_list.sort()

    #return the list sorted alphabetically
    return items_in_common_list


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["pickle", "pickle", "juice", "pickle", "juice", "pop"])
       ['pickle', 'juice', 'juice']

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """

    #create a blank list for my final output
    every_other_list = []

    #iterate through the list by index and take the even ones
    for i in range(len(items)):
        if i % 2 == 0:
            every_other_list.append(items[i])

    return every_other_list


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """

    #create list to hold my final output
    largest_integers = []

    #quit and return empty list if n = 0
    if int(n) == 0:
        return largest_integers

    #sort the incoming list to put in order of smallest to largest
    items.sort()

    #print items
    #take a slice of the list from the right appending 'n' largest
    #to my list
    largest_integers = items[:-int(n)-1:-1]

    #sort the list
    largest_integers.sort()

    return largest_integers


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")
