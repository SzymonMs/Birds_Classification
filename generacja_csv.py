import csv  

header = ['File','Status']

with open('golebie_labels.csv', 'w', encoding='UTF8',newline = '') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    for n in range(1,193):
        if n <10:
            writer.writerow(["bird_H00"+str(n)+".tiff","wrobel"])
        elif n<100:
            writer.writerow(["bird_H0"+str(n)+".tiff","wrobel"])
        else:
            writer.writerow(["bird_H"+str(n)+".tiff","wrobel"])
