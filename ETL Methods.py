import petl as etl, psycopg2 as pg, sys
from sqlalchemy import *
import  pandas as pd

#DB Connection

dbCn={'NR2':"dbname = postgres2 user = postgres  host=127.0.0.1",
'NR3': "dbname = postgres3 user = postgres  host=127.0.0.1"}

#connectiosn and cursors
sourceConn = pg.connect(dbCn['NR2'])
target = pg.connect(dbCn['NR3'])

sourceCursor = sourceConn.cursor()
targetCursor = target.cursor()

sourceCursor.execute("""select * from installs_by_country_2""")

sourceTables = sourceCursor.fetchall()

for t in sourceTables:
    targetCursor.execute("drop table if exists %s" % (t[0]))
    sourceDs =  etl.fromdb(sourceConn, "select * from %s" % (t[0]))
    etl.todb(sourceDs, target, t[0], create = True, sample=1000)

d = pd.DataFrame([sourceTables])
