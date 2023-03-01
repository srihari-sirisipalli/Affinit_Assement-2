# Affinit_Assement-2

## Question-1


## The following questions test your aptitude for interacting with databases. The questions are based off the following public SQL DB: https://docs.rfam.org/en/latest/database.html 

- How many types of tigers can be found in the taxonomy table of the dataset? What is the "ncbi_id" of the Sumatran Tiger? (hint: use the biological name of the tiger)
- Find all the columns that can be used to connect the tables in the given database.
- Which type of rice has the longest DNA sequence? (hint: use the rfamseq and the taxonomy tables)
- We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page. (hint: we need the family accession ID, family name and the maximum length in the results)

## Code
### Rfam Database Python Code
This is a Python code that interacts with the Rfam database to retrieve information about biological data. The Rfam database is a collection of RNA families that provide information about RNA molecules' structure, function, and evolution.

### The code creates a RfamDatabase class that has the following methods:

- count_of_different_types_of_species(species): this method counts the number of different types of species in the Rfam database that match the input species string.
- ncbi_id(species): this method returns the NCBI ID for the input species string.
- type_of_species_with_longest_dna_sequence(species): this method returns the type of species with the longest DNA sequence for the input species string.
- get_common_columns(): this method retrieves the common columns between all tables in the Rfam database and returns a list of tuples, each containing two table names and a list of common column names.
- get_paginated_families(page_num=9, page_size=15): this method retrieves a paginated list of RNA families' names and their longest DNA sequence lengths where only families that have DNA sequence lengths greater than 1,000,000 are included. The method returns a list of tuples containing the family's RFAM ID, description, and length.

The RfamDatabase class has an initializer method that takes four parameters: host, user, port, and database. These parameters are used to create a connection to the Rfam database using the mysql.connector module.

To use the code, simply create an instance of the RfamDatabase class and call the desired method with the necessary parameters. The code retrieves information from the Rfam database and returns it as a Python object (e.g., string, list, tuple).


## Question-2

### This question is to test your aptitude for writing small shell scripts on Unix. You are given this URL https://www.amfiindia.com/spages/NAVAll.txt. Write a shell script that extracts the Scheme Name and Asset Value fields only and saves them in a csv file.

This is a shell script written in Bash that fetches the content of a webpage and extracts two fields, "Scheme Name" and "Net Asset Value", from the content. The extracted data is then saved in a CSV file named "output.csv".

### Here is a step-by-step explanation of how the script works:

- The script starts by using the "wget" command to download the content of the webpage located at the specified URL. The "-qO-" option tells wget to output the content to stdout instead of saving it to a file.
- The script then uses the "echo" command to pass the content of the webpage to the "head" and "awk" commands. The "head" command selects only the first line of the content, while the "awk" command searches for the positions of the "Scheme Name" and "Net Asset Value" fields in the line.
- The positions of the two fields are stored in variables named "SCHEME_POS" and "ASSET_POS".
- The script then uses the "echo" command again to pass the content of the webpage to another "awk" command. This time, the command is told to print only the "Scheme Name" and "Net Asset Value" fields, based on their positions. The command also filters out any lines with fewer than the required number of fields.
- The output of the "awk" command is then saved to a CSV file named "output.csv".
- Finally, the script prints a message to the console indicating that the output has been saved to the CSV file.
