# import subprocess
#
# host = "localhost",
# user = "jayashree",
# password = "J@yashreevj30",
# database = "assembly",
# backup_file = "backup.sql"
#
#
# cmd = f"mysqldump -h{host} -u{user} -p{password} {database} > {backup_file}"
# subprocess.run(cmd, shell= True)


# ----------------------------------------------------------------------Final_code------------------------------------------------------------------------


import os
import datetime
import pymysql

host = "localhost"
user = "yagnesh"
password = "yagnesh"
database = "assembly"
backup_file = "back_previous_month.sql"

now = datetime.datetime.now()
first_day_current_month = datetime.datetime(now.year, now.month, 1)
first_day_previous_month = first_day_current_month - datetime.timedelta(days=1)
first_day_previous_month = datetime.datetime(first_day_previous_month.year, first_day_previous_month.month, 1)
first_day_two_months_ago = first_day_previous_month - datetime.timedelta(days=1)
first_day_two_months_ago = datetime.datetime(first_day_two_months_ago.year, first_day_two_months_ago.month, 1)

backup_cmd = f"mysqldump -h {host} -u {user} -p {database} --where='created_at >= \"{first_day_previous_month.strftime('%Y-%m-%d')}\" AND created_at < \"{first_day_current_month.strftime('%Y-%m-%d')}\"' production_monitering > {backup_file}"
os.system(backup_cmd)

connection = pymysql.connect(host=host, user=user, password=password, database=database)
cursor = connection.cursor()

delete_query = f"DELETE FROM production_monitering WHERE created_at >= '{first_day_two_months_ago.strftime('%Y-%m-%d')}' AND created_at < '{first_day_current_month.strftime('%Y-%m-%d')}'"
cursor.execute(delete_query)
connection.commit()

cursor.close()
connection.close()
