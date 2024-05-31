import csv

data=open('example.csv',encoding='utf-8')

csv_data=csv.reader(data)

data_lines=list(csv_data)

print(data_lines[0][3])

for i in data_lines[:5]:
    print(i)
    
all_emails=[]
for i in data_lines[1:100]:
    all_emails.append(i[3])
    
print (all_emails,end=" ")

file_to_output=open('to_save_file.csv',mode='w',newline='')
csv_writer=csv.writer(file_to_output,delimiter=',')

csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])

file_to_output.close()

f=open('to_save_file.csv',mode='a',newline='')
csv_writer=csv.writer(f)

csv_writer.writerow(['1','2','3'])
file_to_output.close()
