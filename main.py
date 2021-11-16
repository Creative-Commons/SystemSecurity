import subprocess

username = 'root'
password = 'root'
database = 'classicmodels'

with open('file.sql','w') as output:
    c = subprocess.Popen(['mysqldump', '-u',username,'-p%s'%password,database],
                         stdout=output, shell=True)

# from subprocess import Popen, PIPE

# filename = 'C:\\Users\\Admin\\Desktop\\securityp8-msccs1\\file.sql'
# process = Popen(['mysql', database, '-u', username, '-p', password],
#                 stdout=PIPE, stdin=PIPE)
# output = process.communicate(str.encode('source ' + filename))[0]
# # output = process.run('mysql'))[0]

# print(output)

# import os
# import datetime
# from zipfile import ZipFile


# BACKUP_DIR_NAME = "mysql_backups"
# FILE_PREFIX = "my_db_backup_"
# FILE_SUFFIX_DATE_FORMAT = "%Y%m%d%H%M%S"
# USERNAME = "root"
# DBNAME = USERNAME+"$mysqlsampledatabase.sql"


# # get today's date and time
# timestamp = datetime.datetime.now().strftime(FILE_SUFFIX_DATE_FORMAT)
# backup_filename = BACKUP_DIR_NAME+"/"+FILE_PREFIX+timestamp+".sql"

# os.system("mysqldump -u "+ password + ' ' + DBNAME+"'  > " + backup_filename)
