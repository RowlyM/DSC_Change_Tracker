"""
Author :Rowly Mudzhiba


"""
# importing libraries
import pyodbc
from mysql.connector import Error
import pandas as pd

import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=iceproduction.scd.sasol.com;'
                      'Database=aegis;'
                      'uid=ice_db_prod;'
                      'pwd=ice_db_prod;')

cursor = conn.cursor()

query = "SELECT top(10)[EventID],"\
        '[EventDataID],'\
        '[OME],'\
        '[BusinessUnit],'\
        '[Plant],'\
        '[Area],'\
        '[SourceServer],'\
        '[SourceAsset],'\
        '[EventType],'\
        '[TimeStamp],'\
        '[TagName],'\
        '[Parameter],'\
        '[Action],'\
        '[Description],'\
        '[Priority],'\
        '[OldValue],'\
        '[NewValue]'\
        "FROM pull_event_log WHERE Timestamp > '2021-03-01 17:57:00.00' AND Timestamp < '2021-03-21 17:57:00.00' AND Eventtype = 'Change' "


# data = cursor.execute("SELECT top(10) * FROM pull_event_log WHERE [Area] = 'U244 - Waterworks' " )
#
# for item in data:
#     print(item)

df = pd.read_sql_query(query, conn)
print(df)

# Todo count number of changes per unit per 10 mins
# Todo classify change type ( mode changes, setpoint changes and on which type of process variable
