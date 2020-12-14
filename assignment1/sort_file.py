import pandas as dataframe
import logging

# initialization
data = None
in_file = None
out_file = None
# configuring log file
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='sort_file.log',
                    filemode='a')

# function to sort dataframe data
def sort(data_to_sort, index_value):
    data_after_sort = data_to_sort.sort_values(index_value)
    return data_after_sort

# opening input_data.txt file to read contents and sort it add the sorted contents in output_data.txt
try:
    with open("input_data.txt", 'r') as in_file:
        logging.info("Successfully opened input_data.txt")
        data = dataframe.read_csv("input_data.txt", delimiter="\n", header=None)
        print(data)
    sorted_data = sort(data, 0)
    lower_case_sorted = sorted_data[0].str.lower()
    logging.info("File content sorted and converted to lower case")
    try:
        with open("output_data.txt", 'w') as out_file:
            logging.info("Successfully opened output_data.txt")
            out_file.write(
                lower_case_sorted.to_string(header=False, index=False)
                )
            logging.info("Contents written to output_data file successfully")
    except OSError:
        print("could not open", out_file)
        logging.exception("Could not open", out_file)
except OSError:
    print("Could not open", in_file)
    logging.exception("Could not open", in_file)
finally:
    out_file.close()
    logging.info("Closed output_data.txt successfully")
    in_file.close()
    logging.info("Closed output_data.txt successfully")
