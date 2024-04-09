import firebird.driver as fdb

def create_objects(rdb5: bool):
    with fdb.connect("employee") as con:
        #add objects
        con.execute_immediate("CREATE GLOBAL TEMPORARY TABLE NEW_GLOBAL_TEMPORARY_1 (TEST INTEGER) ON COMMIT DELETE ROWS;")
        con.execute_immediate("""
CREATE OR ALTER FUNCTION NEW_FUNC
RETURNS VARCHAR(5)
AS
begin
  RETURN 'five';
end
""")
        con.execute_immediate("CREATE PACKAGE NEW_PACK AS BEGIN END;")
        con.execute_immediate("RECREATE PACKAGE BODY NEW_PACK AS BEGIN END;")
        con.execute_immediate("""
CREATE OR ALTER TRIGGER NEW_DDL_TRIGGER
ACTIVE BEFORE ANY DDL STATEMENT  POSITION 0
AS
BEGIN
END
""")
        con.execute_immediate("""
CREATE OR ALTER TRIGGER NEW_DB_TRIGGER
ACTIVE ON CONNECT POSITION 0
AS
BEGIN
END
""")
        con.execute_immediate("""
DECLARE EXTERNAL FUNCTION NEW_UDF
RETURNS
BIGINT
ENTRY_POINT '123' MODULE_NAME '123'
""")
        con.execute_immediate("CREATE ROLE TEST_ROLE;")       
        con.execute_immediate("create collation iso8859_1_unicode for iso8859_1")

        #add comments
        con.execute_immediate("COMMENT ON DOMAIN EMPNO IS 'comment'")
        con.execute_immediate("COMMENT ON TABLE EMPLOYEE IS 'comment'")
        con.execute_immediate("COMMENT ON TABLE NEW_GLOBAL_TEMPORARY_1 IS 'comment'")
        con.execute_immediate("COMMENT ON VIEW PHONE_LIST IS 'comment'")
        con.execute_immediate("COMMENT ON PROCEDURE ADD_EMP_PROJ IS 'comment'")
        con.execute_immediate("COMMENT ON FUNCTION NEW_FUNC IS 'comment'")
        con.execute_immediate("COMMENT ON PACKAGE NEW_PACK IS 'comment'")
        con.execute_immediate("COMMENT ON TRIGGER POST_NEW_ORDER IS 'comment'")
        con.execute_immediate("COMMENT ON TRIGGER NEW_DDL_TRIGGER IS 'comment'")
        con.execute_immediate("COMMENT ON TRIGGER NEW_DB_TRIGGER IS 'comment'")
        con.execute_immediate("COMMENT ON SEQUENCE CUST_NO_GEN IS 'comment';")
        con.execute_immediate("COMMENT ON EXCEPTION CUSTOMER_CHECK IS 'comment'")
        con.execute_immediate("COMMENT ON EXTERNAL FUNCTION NEW_UDF IS 'comment'")
        con.execute_immediate("COMMENT ON ROLE TEST_ROLE IS 'comment'")
        con.execute_immediate("COMMENT ON INDEX CHANGEX IS 'comment'")
        
        if rdb5:
            con.execute_immediate("CREATE TABLESPACE NEW_TABLESPACE_1 FILE 'file.ts';")
            con.execute_immediate("""                                 
CREATE JOB NEW_JOB
'13 17 * * *'
INACTIVE
START DATE NULL
END DATE NULL
AS
begin
end
""")
        con.commit()

def delete_objects(rdb5: bool):
    with fdb.connect("employee") as con:

        #remove objects
        con.execute_immediate("DROP TABLE NEW_GLOBAL_TEMPORARY_1")
        con.execute_immediate("DROP FUNCTION NEW_FUNC")
        con.execute_immediate("DROP PACKAGE NEW_PACK")
        con.execute_immediate("DROP TRIGGER NEW_DDL_TRIGGER")
        con.execute_immediate("DROP TRIGGER NEW_DB_TRIGGER")
        con.execute_immediate("DROP EXTERNAL FUNCTION NEW_UDF")
        con.execute_immediate("DROP ROLE TEST_ROLE")
        con.execute_immediate("DROP COLLATION iso8859_1_unicode")

        #remove comment
        con.execute_immediate("COMMENT ON DOMAIN EMPNO IS ''")
        con.execute_immediate("COMMENT ON TABLE EMPLOYEE IS ''")
        con.execute_immediate("COMMENT ON VIEW PHONE_LIST IS ''")
        con.execute_immediate("COMMENT ON PROCEDURE ADD_EMP_PROJ IS ''")
        con.execute_immediate("COMMENT ON TRIGGER POST_NEW_ORDER IS ''")
        con.execute_immediate("COMMENT ON SEQUENCE CUST_NO_GEN IS ''")
        con.execute_immediate("COMMENT ON EXCEPTION CUSTOMER_CHECK IS ''")
        con.execute_immediate("COMMENT ON INDEX CHANGEX IS ''")

        if rdb5:
            con.execute_immediate("DROP TABLESPACE NEW_TABLESPACE_1;")
            con.execute_immediate("DROP JOB NEW_JOB;")
        con.commit()

#sql script
"""
DROP TABLE NEW_GLOBAL_TEMPORARY_1;
DROP FUNCTION NEW_FUNC;
DROP PACKAGE NEW_PACK;
DROP TRIGGER NEW_DDL_TRIGGER;
DROP TRIGGER NEW_DB_TRIGGER;
DROP EXTERNAL FUNCTION NEW_UDF;
DROP ROLE TEST_ROLE;
DROP COLLATION iso8859_1_unicode;
DROP TABLESPACE NEW_TABLESPACE_1;
DROP JOB NEW_JOB;
COMMENT ON DOMAIN EMPNO IS '';
COMMENT ON TABLE EMPLOYEE IS '';
COMMENT ON VIEW PHONE_LIST IS '';
COMMENT ON PROCEDURE ADD_EMP_PROJ IS '';
COMMENT ON TRIGGER POST_NEW_ORDER IS '';
COMMENT ON SEQUENCE CUST_NO_GEN IS '';
COMMENT ON EXCEPTION CUSTOMER_CHECK IS '';
COMMENT ON INDEX CHANGEX IS '';
"""