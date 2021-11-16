import subprocess

username = 'root'
password = 'root'
database = 'classicmodels'

with open('file.sql','w') as output:
    c = subprocess.Popen(['mysqldump', '-u',username,'-p%s'%password,database],
                         stdout=output, shell=True)
    
 '''
 add to the start of dump file
 
 CREATE DATABASE /*!32312 IF NOT EXISTS*/`file` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `file`;
'''
