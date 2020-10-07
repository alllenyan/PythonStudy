import csv

rows = ['ID_ORIGIN','ID','COMM_MEDIUM','IA_TYPE','TIMESTAMP','NAME_TEXT','ZZ1_ZIMPORT_BATCH_NO_MIA','ZZ1_ZCHO7_MIA','ZZ1_ZMODEL_MIA','ZZ1_ZSERIES_MIA','ZZ1_ZCAR_VIN_MIA']
rows1 = ['MOBILE','+8612217394198','WEB','ZIMPORT','202000812164000','import test','2020081101','2','MG 3','名爵三越野','20200811']

# csv文件在写入的时候, 默认每次写入时会有一个空行作为分割, 使用newline = ''
# 会把空行去掉
with open('test1.csv', 'w', newline='')as csv_file:
    # 获取一个csv对象进行内容写入
    writer = csv.writer(csv_file)
    for row in rows:
        # writerow 写入一行数据
        writer.writerow(row)
    # 写入多行

