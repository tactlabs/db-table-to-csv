#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on April 03, 2018

Course work: 

@author: 

Source:
    http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
    http://www.sqlitetutorial.net/sqlite-python/insert/
    
    https://docs.python.org/3/library/sqlite3.html
    https://stackoverflow.com/questions/7831371/is-there-a-way-to-get-a-list-of-column-names-in-sqlite
    https://stackoverflow.com/questions/228912/sqlite-parameter-substitution-problem
    
    Create table
        http://www.sqlitetutorial.net/sqlite-python/create-tables/
    
    Date format readable:
        https://stackoverflow.com/questions/2158347/how-do-i-turn-a-python-datetime-into-a-string-with-readable-format-date
        
    Geo Location
        http://en.mygeoposition.com/    
        
    Exception Handling:
        https://docs.python.org/2/tutorial/errors.html
        
    Datetime now in local:
        https://stackoverflow.com/questions/381371/sqlite-current-timestamp-is-in-gmt-not-the-timezone-of-the-machine
        
    Delete Sqlite
        http://www.sqlitetutorial.net/sqlite-python/delete/
        
    Sql and Python:
        http://www.sqlitetutorial.net/sqlite-python/delete/
        
    Sqlite and Python:
        https://docs.python.org/2/library/sqlite3.html
    

'''

# Import necessary modules

import sqlite3
from xlsxwriter.workbook import Workbook
def main():

    workbook = Workbook('E:/tact_excel_data/indeed_job.csv')
    worksheet = workbook.add_worksheet()
    
    conn=sqlite3.connect("E:/tact_db/tact_public.db")
    c=conn.cursor()
    #c.execute("select * from LINKEDIN_DEVELOPER_INFORMATION")
    c.execute("select * from  INDEED_JOB_COLLECTOR")
    mysel=c.execute("select * from INDEED_JOB_COLLECTOR")
    for i, row in enumerate(mysel):
        print (row)
        worksheet.write(i, 0, row[0])
        worksheet.write(i, 1, row[1])
        worksheet.write(i, 2, row[2])
        
        worksheet.write(i, 3, row[3])
        '''
        worksheet.write(i, 4, row[4])
        worksheet.write(i, 5, row[5])
        worksheet.write(i, 6, row[6])
        worksheet.write(i, 7, row[7])
        worksheet.write(i, 8, row[8])
        worksheet.write(i, 9, row[9])
        worksheet.write(i, 10, row[10])
        worksheet.write(i, 11, row[11])
        worksheet.write(i, 12, row[12])
        worksheet.write(i, 13, row[13])
        '''
    workbook.close()

 
if __name__ == '__main__':
    main()
