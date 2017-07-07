# mdb to mongo

### steps:
1. Find Борей.mdb in the internet
2. install to Ubuntu tools for work with mdb
3. With pandas_access read names of tables
4. Save tables with os.system("mdb-export {0} {1} > {1}.csv".format(DB_NAME, table))
5. Merge tables and insert it to mongo
6. Make filters and save results

### About structure
Structure of collection in mongo is equal to sum of
merged tables from mdb