import csv

def read_dictionary(reader, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dict = {}

    with open(file="products.csv", mode="rt") as product_file:

         reader = csv.reader(product_file)

         next(reader)

         for row in reader:
            if len(row) != 0:
                key = row[key_column_index]
                products_dict[key] = row

    # Return the dictionary.
    return products_dict


def main():
    # Read the contents of the products.csv file
    products_dict = read_dictionary("products.csv", 0)

    # Print the stores products list.
    print(products_dict)
    
    with open("request.csv", newline="") as request_file:
        
        reader = csv.reader(request_file)

        next(reader)

# Call main to start this program.
if __name__ == "__main__":
    main()




