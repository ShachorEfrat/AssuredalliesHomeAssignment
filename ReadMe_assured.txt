Code Explanation:

A server has been defined by the FastAPI library.
The statistics are collected using global variables.
enumerate, itertools - slice is used to insert the memory only the relevant words / only to count the word. Not the whole file.


# # # # # # #         USE THE SERVICES      # # # # # # #

To run and use the services - follow the instructions 

1. 
To get the words with specific prefix:
open cmd
change the text <prefix_you_want> to the prefix you want to display
 and run:

curl http://127.0.0.1:8000/dictionary?prefix=<prefix_you_want>

2. 
To display the dictionary servie statistics
run on cmd:

curl http://127.0.0.1:8000/statistics

3. 
To update the dictionary with some file
change <words_to_insert.txt> to your file
and run:
curl --form "words_file_name=@<words_to_insert.txt>" http://127.0.0.1:8000/update_dictionary
