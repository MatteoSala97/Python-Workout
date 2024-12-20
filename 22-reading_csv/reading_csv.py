import csv

def pwd_to_csv(pwd_filename, csv_filename):
    with open(pwd_filename, 'r') as input, open(csv_filename, 'w') as output: 
        input_file = csv.reader(input, delimiter=':')
        output_file = csv.writer(output, delimiter='\t')
        
        for record in input_file:
            if len(record) > 1:
                output_file.writerow((record[0], record[2]))
                
# paths
p1 = r'C:\Users\matteo.sala\Documents\Python Workout\22-reading_csv\linux.txt'
p2 = r'C:\Users\matteo.sala\Documents\Python Workout\22-reading_csv\pwd.csv'

pwd_to_csv(p1,p2)
print('Parsing completed.')