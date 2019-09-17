import csv
import time

arg = input('ENTER for minimal: ')

start = time.time()
new_list = []
with open('playerDB.csv', newline='', encoding='ISO-8859-1') as database:
    print('Reading from playerDB.csv')
    file_iterator = csv.reader(database)
    for row in file_iterator:
        if not arg:
            if row[7] == 'GK' or row[7] == 'CAM' or row[0] == 'id':
                if row[7] == 'GK':
                    position = 0
                elif row[7] == 'CAM':
                    position = 1
                else:
                    position = row[7]
                new_row = [row[62], row[10], row[11], row[23], position]
                new_list.append(new_row)
        else:
            new_row = [row[62], row[10], row[11], row[23], row[7]]
            new_list.append(new_row)

with open('playerDataSet.csv', 'w', newline='') as datase:
    print('Writing to platerDataSet.csv')
    writer = csv.writer(datase, quoting=csv.QUOTE_ALL)
    for element in new_list:
        writer.writerow(element)
    
end = time.time()
print('Finished in: ', end-start, ' seconds')
