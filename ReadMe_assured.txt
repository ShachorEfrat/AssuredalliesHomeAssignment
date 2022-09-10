open cmd
change the text <prefix_you_want> to the prefix you want to display
 and run:

curl http://127.0.0.1:8000/dictionary?prefix=<prefix_you_want>

run on cmd:

curl http://127.0.0.1:8000/statistics

to get the statistics.

For update the dictionary, run:
change <words_to_insert.txt> to your file

curl --form "words_file_name=@<words_to_insert.txt>" http://127.0.0.1:8000/update_dictionary