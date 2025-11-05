def check_with_one_removal(lst):
    """
    Checks if removing one element from the report can make it safe.
    Returns True if removing one element makes the report safe, False otherwise.
    """
    # If the report is already safe without removal
    if is_sorted_and_differences_valid(lst):
        return True

    # Try removing each element one by one and check if the new list is safe
    for i in range(len(lst)):
        # Create a new list without the element at index i
        new_lst = lst[:i] + lst[i + 1:]
        if is_sorted_and_differences_valid(new_lst):
            return True

    # If no valid list was found, return False
    return False


def count_safe_reports(report):
    return is_sorted_and_differences_valid(report) or check_with_one_removal(report)


def is_sorted_and_differences_valid(lst):
    is_ascending = True
    is_descending = True
    for i in range(1, len(lst)):
        diff = abs(lst[i] - lst[i - 1])
        if not 1 <= diff <= 3:
            return False  # Difference is not valid
        if lst[i] < lst[i - 1]:
            is_ascending = False
        if lst[i] > lst[i - 1]:
            is_descending = False

    return is_ascending or is_descending  # Check if list is either ascending or descending


# Initialize the valid line count
s = [0, 0]

# Open the file safely using a context manager
with open("demo2.txt") as file:
    for line in file:
        # Split the line into integers
        t = list(map(int, line.split()))

        # Check if the list is sorted and differences are valid
        if is_sorted_and_differences_valid(t):
            s[0] += 1
        if count_safe_reports(t):
            print(t)
            s[1] += 1

# Print the result
print(s)
