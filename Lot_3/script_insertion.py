import happybase
import csv
from datetime import datetime

# Configure the connection to HBase
hbase_table = 'my_test_5'  # Name of your HBase table
connection = happybase.Connection('node175910-env-1839015-etudiant18.sh1.hidora.com', 11560)
connection.open()

# Create HBase table with column families
column_families = {
    'cf': dict()  # Assuming you want all columns under one column family 'cf'
}
connection.create_table(hbase_table, column_families)

# Get a reference to the newly created table
table = connection.table(hbase_table)

# Path to your CSV file
csv_file_path = 'dataw_fro04.csv'


# Function to import data into HBase based on the criteria
# Function to import data into HBase based on the criteria
def import_data_to_hbase(csv_file_path, hbase_table):
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # Ignore the first line (header)
        index = 0  # Initialize index for generating row keys

        for row in csv_reader:
            index += 1  # Increment index for each row

            # Extract columns from the CSV based on your structure
            codcli, genrecli, nomcli, prenomcli, cpcli, ville, codecde, date_str, timbrecli, timbrecde, Nbcolis, cheqcli, barchive, bstock, codobj, qte, Colis, libobj, Tailleobj, Poidsobj, points, indispobj, libcondit, prixcond, puobj = row

            # Replace null values with '0'
            row = ['' if value == 'NULL' else value for value in row]

            # Filter the data according to the criteria of your project
            try:
                # Convert the date to datetime object
                date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

                # Insert the data into HBase without specifying row key (HBase will generate it)
                table.put(str(index).encode(), {  # Use index as row key
                    b'cf:codecli': codcli.encode(),
                    b'cf:genrecli': genrecli.encode(),
                    b'cf:nomcli': nomcli.encode(),
                    b'cf:prenomcli': prenomcli.encode(),
                    b'cf:cpcli': cpcli.encode(),
                    b'cf:ville': ville.encode(),
                    b'cf:codecde': codecde.encode(),
                    b'cf:date': date_str.encode(),
                    b'cf:timbrecli': timbrecli.encode(),
                    b'cf:timbrecde': timbrecde.encode(),
                    b'cf:Nbcolis': Nbcolis.encode(),
                    b'cf:cheqcli': cheqcli.encode(),
                    b'cf:barchive': barchive.encode(),
                    b'cf:bstock': bstock.encode(),
                    b'cf:codobj': codobj.encode(),
                    b'cf:qte': qte.encode(),
                    b'cf:Colis': Colis.encode(),
                    b'cf:libobj': libobj.encode(),
                    b'cf:Tailleobj': Tailleobj.encode(),
                    b'cf:Poidsobj': Poidsobj.encode(),
                    b'cf:points': points.encode(),
                    b'cf:indispobj': indispobj.encode(),
                    b'cf:libcondit': libcondit.encode(),
                    b'cf:prixcond': prixcond.encode(),
                    b'cf:puobj': puobj.encode()
                })
            except ValueError:
                pass  # Skip to the next iteration if there's an error in date conversion


# Call the import function
import_data_to_hbase(csv_file_path, hbase_table)

# Close the connection to HBase
connection.close()
print("done")
