import mysql.connector

my = mysql.connector.connect(
    host = 'us-cdbr-east-05.cleardb.net',
    user= 'b8739bb261d15f',
    passwd = '6cb5c1b7'
)

my_cor = my.cursor()
my_cor.execute('SHOW TABLES FROM heroku_31fcfa56ddd3838')
for db in my_cor:
    print(db)