'''
1.6.1 exercise in the book
'''
#Get the number of cycles for a number
def get_cycles(num: int) -> int:
    count = 1 #The count starts at 1 to include the front endpoint.
    while num != 1:
        if num % 2 == 0:
            num /= 2
            count += 1
        else:
            num = 3*num + 1
            count += 1
    return count

def main() -> None:
    user_input = input()
    input_data = user_input.split(" ")
    num_range = range(int(input_data[0]), int(input_data[1]))
    max_cycles = 0 #This will be updated as bigger numbers are encountered
    for num in num_range:
        cycles = get_cycles(num)
        if cycles > max_cycles:
            max_cycles = cycles
    print (f"{input_data[0]} {input_data[1]} {max_cycles}")

main()