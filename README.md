# Affinit_Assement-2
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
