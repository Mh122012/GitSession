import pyodbc
conn=pyodbc.connect('Host=localhost;'            
                    'Driver={ODBC Driver 17 for SQL Server};'
                    'Server=DESKTOP-425FDN3;'
                    'Trusted_Connection=yes;'
                    'Port= 1433'
                    'Database=test04'
                    )
cur=conn.cursor()
#cur.execute("create table Companies(Name Varchar(20),Age int,Sal int)")
cur.execute("insert into Companies values ('Rakesh',25,56000)")
cur.commit()
