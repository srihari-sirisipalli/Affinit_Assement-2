import mysql.connector

class RfamDatabase:
    def __init__(self,host,user,port,database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            port=port,
            database=database,
        )
        self.mycursor = self.mydb.cursor(buffered=True)
        self.db_dict = {}
        self.tables = []
    def count_of_different_types_of_species(self,species):
        # Construct the SQL query to find the longest DNA sequence for a given species name
        sql_query="SELECT COUNT(*) FROM taxonomy WHERE species LIKE "+"'%"+species+"%' ;"
        # Execute the SQL query
        self.mycursor.execute(sql_query)
        # Get the result of the SQL query
        result = self.mycursor.fetchone()
        return result[0]
    def ncbi_id(self,species):
        # Construct the SQL query to find the ncbi_id for a given species name
        sql_query="SELECT ncbi_id FROM taxonomy WHERE species LIKE "+"'%"+species+"%' ;"
        # Execute the SQL query
        self.mycursor.execute(sql_query)
        # Get the result of the SQL query
        result = self.mycursor.fetchone()
        return result[0]
    def type_of_species_with_longest_dna_sequence(self,species):
        # Construct the SQL query to find the types in species with longest DNA sequence
        sql_query="SELECT t.species AS species_name, r.length AS length FROM rfamseq r JOIN taxonomy t ON r.ncbi_id = t.ncbi_id WHERE t.species LIKE '%"+species+"%' ORDER BY r.length DESC LIMIT 1;"
        # Execute the SQL query
        self.mycursor.execute(sql_query)
        # Get the result of the SQL query
        result = self.mycursor.fetchone()
        return result[0]
    def get_tables(self):
        # Construct the SQL query to list all tables in the Rfam database
        sql = "show tables;"
        # Execute the SQL query
        self.mycursor.execute(sql)
        # Add each table name to the dictionary as a key, with an empty list as its value
        for x in self.mycursor:
            self.db_dict[x[0]] = []

    def get_table_columns(self):
        # Construct the SQL query to describe the columns in each table
        sql = "DESCRIBE "
        # Loop through each table in the dictionary
        for table in list(self.db_dict.keys()):
            # Add the table name to the SQL query
            sql1 = sql + table
            # Execute the SQL query
            self.mycursor.execute(sql1)
            # Add the column names to the dictionary as the value of the corresponding table key
            self.db_dict[table] = [row[0] for row in self.mycursor.fetchall()]
        # Add each table name to the list of table names
        self.tables = list(self.db_dict.keys())
    # Define a helper function to find the common columns between two lists
    def common_member(self,a, b):
        a_set = set(a)
        b_set = set(b)

        if (a_set & b_set):
            return (a_set & b_set)
        else:
            return None
    def get_common_columns(self):
        # Loop through each pair of tables in the dictionary
        self.get_tables()
        self.get_table_columns()
        common_columns=[]
        for i in range(len(self.tables)-1):
            for j in range(i+1, len(self.tables)):
               temp=self.common_member(self.db_dict[self.tables[i]], self.db_dict[self.tables[j]])
               if temp!=None :
                   common_columns.append([self.tables[i], self.tables[j],list(temp)])
        return common_columns
    def get_paginated_families(self, page_num=9, page_size=15):
        offset = (page_num-1) * page_size
        # Construct a query to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page. 
        sql = "SELECT f.rfam_id, f.description, MAX(rf.length) as length FROM family f JOIN full_region r ON f.rfam_acc = r.rfam_acc JOIN rfamseq rf ON rf.rfamseq_acc=r.rfamseq_acc WHERE length > 1000000 GROUP BY f.rfam_acc, f.description HAVING length > 1000000 ORDER BY length DESC LIMIT " + str(page_size) + " OFFSET " + str(offset) + ";"
        self.mycursor.execute(sql)
        results = self.mycursor.fetchall()
        return results
    

# Create a connection to the Rfam database
db = RfamDatabase(
    host="mysql-rfam-public.ebi.ac.uk",
    user="rfamro",
    port="4497",
    database="Rfam"
)

# Print the count of different types of species for "panthera tigris"
species="panthera tigris"
print(f"Count of different type of species of {species} in taxonomy table : {db.count_of_different_types_of_species(species)}")

print("-------------------------------------------------------------------------------------------------------------------")
# Retrieve the NCBI ID for "Sumatran Tiger"
species="Sumatran Tiger"
print(f"NCBI ID of {species} : {db.ncbi_id(species)}")
print("-------------------------------------------------------------------------------------------------------------------")
# Retrieve the common columns for all families in the Rfam database
common_columns=db.get_common_columns()
print("Common columns between all pairs of tables(print first 10 rows):")
for ele in common_columns[0:10]:
    print(ele[0]+':'+ele[1],*ele[2])
print("-------------------------------------------------------------------------------------------------------------------")
# Retrieve the type of species with the longest DNA sequence for "Oryza sativa"
species="Oryza sativa"
print(f"Types of species with longents DNA in {species} : {db.type_of_species_with_longest_dna_sequence(species)}")
print("-------------------------------------------------------------------------------------------------------------------")
# Retrieve a paginated list of families in the Rfam database
page_num=9;
page_size=15
paginated_data=db.get_paginated_families(page_num=page_num,page_size=page_size)
print("Paginated Data query that will return the page.no-{page_num} when there are {page_size} results per page")
for ele in paginated_data:
    print(*ele)
print("-------------------------------------------------------------------------------------------------------------------")