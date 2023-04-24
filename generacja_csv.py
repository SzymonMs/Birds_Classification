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

    # for n in range(101,193):
    #     writer.writerow(["bird"+str(n)+".tiff","kaczka"])
    # for n in range(193,293):
    #     writer.writerow(["bird"+str(n)+".tiff","kawka"])
    # for n in range(293,393):
    #     writer.writerow(["bird"+str(n)+".tiff","labedz"])
    # for n in range(393,493):
    #     writer.writerow(["bird"+str(n)+".tiff","mewa"])
    # for n in range(493,593):
    #     writer.writerow(["bird"+str(n)+".tiff","sroka"])
    # for n in range(593,689):
    #     writer.writerow(["bird"+str(n)+".tiff","wrobel"])
    # for n in range(689,777):
    #     writer.writerow(["bird"+str(n)+".tiff","bocian"])

    # for n in range(777,877):
    #     writer.writerow(["bird"+str(n)+".tiff","golab"])
    # for n in range(877,969):
    #     writer.writerow(["bird"+str(n)+".tiff","kaczka"])
    # for n in range(969,1069):
    #     writer.writerow(["bird"+str(n)+".tiff","kawka"])
    # for n in range(1069,1169):
    #     writer.writerow(["bird"+str(n)+".tiff","labedz"])
    # for n in range(1169,1269):
    #     writer.writerow(["bird"+str(n)+".tiff","mewa"])
    # for n in range(1269,1369):
    #     writer.writerow(["bird"+str(n)+".tiff","sroka"])
    # for n in range(1369,1465):
    #     writer.writerow(["bird"+str(n)+".tiff","wrobel"])
    # for n in range(1465,1553):
    #     writer.writerow(["bird"+str(n)+".tiff","bocian"])
    # for n in range(1,49):
    #     writer.writerow(["bird"+str(n)+".tif","bocian"])
    # for n in range(49,99):
    #     writer.writerow(["bird"+str(n)+".tif","golab"])
    # for n in range(99,145):
    #     writer.writerow(["bird"+str(n)+".tif","kaczka"])
    # for n in range(145,195):
    #     writer.writerow(["bird"+str(n)+".tif","kawka"])
    # for n in range(225,275):
    #     writer.writerow(["bird"+str(n)+".tif","mewa"])
    # for n in range(275,325):
    #     writer.writerow(["bird"+str(n)+".tif","sroka"])
    # for n in range(325,373):
    #     writer.writerow(["bird"+str(n)+".tif","wrobel"])
    # for n in range(373,423):
    #     writer.writerow(["bird"+str(n)+".tif","labedz"])
    # for n in range(423,473):
    #     writer.writerow(["bird"+str(n)+".tif","golab"])
    # for n in range(473,519):
    #     writer.writerow(["bird"+str(n)+".tif","kaczka"])
    # for n in range(519,569):
    #     writer.writerow(["bird"+str(n)+".tif","kawka"])
    # for n in range(569,620):
    #     writer.writerow(["bird"+str(n)+".tif","labedz"])
    # for n in range(620,670):
    #     writer.writerow(["bird"+str(n)+".tif","mewa"])
    # for n in range(670,720):
    #     writer.writerow(["bird"+str(n)+".tif","sroka"])
    # for n in range(720,768):
    #     writer.writerow(["bird"+str(n)+".tif","wrobel"])
    # for n in range(768,812):
    #     writer.writerow(["bird"+str(n)+".tif","bocian"])