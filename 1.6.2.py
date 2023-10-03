'''
(Programming challenges 1.6.2)
The input will consist of an arbitrary number of fields. The first line of each field contains two integers n and m (0 < n, m ≤ 100) 
which stand for the number of lines and columns of the field, respectively. 

Each of the next n lines contains exactly m characters, representing the field.
Safe squares are denoted by “.” and mine squares by “*,” both without the quotes. The first field line where n = m = 0 represents 
the end of input and should not be processed.

'''


def get_neighbor_counts(field_dicts: dict) -> dict:
    neighbor_fields = {} #This will hold the modified fields with the hint values
    field_count = 1
    #We will modify the list in place, and then add it to the neighbor_fields dict.
    #Loop through the dictionary
    for key in field_dicts:
        current_field = field_dicts[key]
        rows = len(current_field)
        columns = len(current_field[0])
        for col in range(columns):
            for row in range(rows):
                if current_field[row][col] == '.': #We're only checking the non-mined dots.
                    #Top Left corner
                    if row == 0 and col == 0:
                        #Check below, to the right, and diagonally down right.
                        neighbors = (current_field[row+1][col],
                                     current_field[row+1][col+1],
                                     current_field[row][col+1],)
                        mine_neighbor_count = neighbors.count('*')
                        current_field[row][col] = str(mine_neighbor_count)

                    #Bottom left corner
                    elif row == rows-1 and col == 0:
                        #Check above, to the right, and up right diagonal.
                        neighbors = (current_field[row-1][col],
                                     current_field[row-1][col+1],
                                     current_field[row][col+1],)
                        mine_neighbor_count = neighbors.count('*')
                        current_field[row][col] = str(mine_neighbor_count)

                    #Bottom right corner
                    elif row == rows-1 and col == columns-1:
                        #Check above, to the left, and up left diagonal
                        neighbors = (current_field[row][col-1],
                                     current_field[row-1][col-1],
                                     current_field[row-1][col],)
                        mine_neighbor_count = neighbors.count('*')
                        current_field[row][col] = str(mine_neighbor_count)

                    #Top right corner
                    elif row == 0 and col == columns-1:
                        #Check below, to the left, and down left diagonal
                        neighbors = (current_field[row][col-1],
                                     current_field[row+1][col],
                                     current_field[row+1][col-1],)
                        mine_neighbor_count = neighbors.count('*')
                        current_field[row][col] = str(mine_neighbor_count)
                    
                    #Left edge
                    elif col == 0:
                        #Check above, below, to the right, up right, and down right.
                        neighbors = (current_field[row+1][col],
                                     current_field[row-1][col],
                                     current_field[row][col+1],
                                     current_field[row-1][col+1],
                                     current_field[row+1][col+1],)
                        mine_neighbor_count = neighbors.count('*')
                        current_field[row][col] = str(mine_neighbor_count)
                    
                    #Right edge
                    elif col == columns-1:
                        #Check above, below, to the left, up left, down left.
                        neighbors = (current_field[row+1][col],
                                     current_field[row-1][col],
                                     current_field[row][col-1],
                                     current_field[row-1][col-1],
                                     current_field[row+1][col-1],)
                        mine_neighbor_count = neighbors.count('*')
                        current_field[row][col] = str(mine_neighbor_count)
                    
                    #Top edge
                    elif row == 0:
                        #Check to the right, to the left, below, down left, down right.
                        neighbors = (current_field[row][col+1],
                                     current_field[row][col-1],
                                     current_field[row+1][col-1],
                                     current_field[row+1][col],
                                     current_field[row+1][col+1],)
                        mine_neighbor_count = neighbors.count('*')
                        current_field[row][col] = str(mine_neighbor_count)
                    
                    #Bottom edge
                    elif row == rows-1:
                        #Check to the right, to the left, up, up right, up left.
                        neighbors = (current_field[row][col+1],
                                     current_field[row][col-1],
                                     current_field[row-1][col-1],
                                     current_field[row-1][col],
                                     current_field[row-1][col+1],)
                        mine_neighbor_count = neighbors.count('*')
                        current_field[row][col] = str(mine_neighbor_count)
                    
                    #All other cases, which will be in the middle of the board
                    else:
                        #Check to the right, left, up, down, up left, up right, down left, down right
                        neighbors = (current_field[row][col+1],
                                     current_field[row][col-1],
                                     current_field[row-1][col],
                                     current_field[row-1][col-1],
                                     current_field[row-1][col+1],
                                     current_field[row+1][col],
                                     current_field[row+1][col-1],
                                     current_field[row+1][col+1],)
                        mine_neighbor_count = neighbors.count('*')
                        current_field[row][col] = str(mine_neighbor_count)
        neighbor_fields[f"Field #{field_count}"] = current_field
        field_count += 1
    return neighbor_fields    
    
def get_fields() -> dict:
    fields = {} #Dictionary will store all rows
    field_count = 1
    while True:
        top_input = '' #The top input resets after the specified number of rows is entered.
        top_input = input()
        if top_input == "0 0":
            break
        rows = []
        #Create a 2d list to represent each field
        for i in range(int(top_input[0])):
            row = input()
            row_characters = [x for x in row]
            rows.append(row_characters)
        #Add each field to a dictionary
        fields[f"Field {field_count}"] = rows
        field_count += 1
    return fields

def main() -> None:
    input_fields = get_fields()
    modified_field = get_neighbor_counts(input_fields)
    #print out the resulting fields
    for key in modified_field:
        field_list = modified_field[key]
        print(f"{key}") #Field #x
        #Join the elements of the list while printing
        for elem in field_list:
            print(''.join(elem))
        print()

main()



