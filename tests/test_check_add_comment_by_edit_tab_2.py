import lackey
from re_tests_plugin import *
import firebird.driver as fdb

def init_alter(icon, name, reload=False):
    lackey.click("tree_plus.png")
    if reload:
        lackey.rightClick(icon)
        lackey.click("tree_reload_menu.png")
    lackey.click(plus_find(icon))
    lackey.doubleClick(name)

def click_tab_comment():
    lackey.click("tab_comment.png")
    mouse = lackey.Mouse()
    lackey.click(mouse.getPos().offset(30, 100))
    lackey.type("test comment")
    lackey.click("bt_OK.png")
    result1 = len(list(lackey.findAll("text_success.png")))
    result2 = lackey.exists("text_test_comment.png")
    result3 = lackey.exists("operation_ADD_COMMENT.png")
    result4 = lackey.exists("text_comment_added.png")
    lackey.click("bt_rollback.png")
    lackey.rightClick("icon_abstract_object_blue.png")
    lackey.click("bt_tab_close_all.png")
    return result1, result2, result3, result4

def click_tab_column(param):
    tab = lackey.exists(param)
    lackey.click(tab)
    mouse = lackey.Mouse()
    mouse.move(tab.getTarget().below(20))
    count = 0
    while lackey.exists("table_column_Comment.png") == None:
        lackey.wheel(lackey.Mouse.WHEEL_DOWN, 1)
        if (count == 10):
            break
        count += 1   
    
    lackey.click(lackey.exists("table_column_Comment.png").getTarget().below(20))
    lackey.type("test comment")
    lackey.type("{ENTER}")
    lackey.click("bt_OK.png")
    result1 = len(list(lackey.findAll("text_success.png")))
    result2 = lackey.exists("text_test_comment.png")
    result3 = lackey.exists("operation_ADD_COMMENT.png")
    result4 = lackey.exists("text_comment_added.png")
    lackey.click("bt_rollback.png")
    lackey.rightClick("icon_abstract_object_blue.png")
    lackey.click("bt_tab_close_all.png")
    return result1, result2, result3, result4

def test_alter_domain(open_connection):
    init_alter("icon_domains.png", "tree_domain_name_ADDRESSLINE.png")
    result1, result2, result3, result4 = click_tab_comment()
    assert result1 == 2
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_alter_procedure(open_connection):
    init_alter("icon_procedures.png", "proc_ALL_LANGS.png")
    result1, result2, result3, result4 = click_tab_comment()
    assert result1 == 2
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_alter_procedure_input_p(open_connection):
    init_alter("icon_procedures.png", "proc_DELETE_EMPLOYEE.png")
    result1, result2, result3, result4 = click_tab_column("tab_input_parameters.png")
    assert result1 == 2
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_alter_procedure_output_p(open_connection):
    init_alter("icon_procedures.png", "proc_ALL_LANGS.png")
    result1, result2, result3, result4 = click_tab_column("tab_output_parameters.png")
    assert result1 == 2
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_alter_function(open_connection):
    script = """
CREATE OR ALTER FUNCTION NEW_FUNC
RETURNS VARCHAR(5)
AS
begin
  RETURN 'five';
end
"""
    with fdb.connect('employee') as con:
        con.execute_immediate(script)
        con.commit()
    init_alter("icon_functions.png", "func_NEW_FUNC.png", reload=True)
    result1, result2, result3, result4 = click_tab_comment()
    with fdb.connect('employee') as con:
        con.execute_immediate('DROP FUNCTION NEW_FUNC')
        con.commit()
    assert result1 == 2
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_alter_function_arg(open_connection):
    script = """
CREATE OR ALTER FUNCTION NEW_FUNC ("test" BIGINT)
RETURNS VARCHAR(5)
AS
begin
  RETURN 'five';
end
"""
    with fdb.connect('employee') as con:
        con.execute_immediate(script)
        con.commit()
    init_alter("icon_functions.png", "func_NEW_FUNC.png", reload=True)
    result1, result2, result3, result4 = click_tab_column("tab_arguments.png")
    with fdb.connect('employee') as con:
        con.execute_immediate('DROP FUNCTION NEW_FUNC')
        con.commit()
    assert result1 == 2
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_alter_package(open_connection):
    script1 = """
CREATE OR ALTER PACKAGE NEW_PACK
AS
BEGIN
END
"""
    script2 = """
RECREATE PACKAGE BODY NEW_PACK
AS
BEGIN
END
"""
    with fdb.connect('employee') as con:
        con.execute_immediate(script1)
        con.execute_immediate(script2)
        con.commit()
    init_alter("icon_packages.png", "pack_NEW_PACK.png", reload=True)
    result1, result2, result3, result4 = click_tab_comment()
    with fdb.connect('employee') as con:
        con.execute_immediate('DROP PACKAGE NEW_PACK')
        con.commit()
    assert result1 == 3
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_alter_trigger_for_table(open_connection):
    init_alter("icon_triggers_for_table.png", "trigger_POST_NEW_ORDER.png")
    result1, result2, result3, result4 = click_tab_comment()
    assert result1 == 2
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_alter_trigger_for_ddl(open_connection):
    script = """
CREATE OR ALTER TRIGGER NEW_TRIGGER
ACTIVE BEFORE ANY DDL STATEMENT POSITION 0
AS
BEGIN
END
"""
    with fdb.connect('employee') as con:
        con.execute_immediate(script)
        con.commit()
    init_alter("icon_triggers_for_ddl.png", "trigger_for_DDL_NEW_TRIGGER.png", reload=True)
    result1, result2, result3, result4 = click_tab_comment()
    with fdb.connect('employee') as con:
        con.execute_immediate("DROP TRIGGER NEW_TRIGGER")
        con.commit()
    assert result1 == 2
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_alter_trigger_for_db(open_connection):
    script = """
CREATE OR ALTER TRIGGER NEW_TRIGGER
ACTIVE ON CONNECT POSITION 0
AS
BEGIN
END
"""
    with fdb.connect('employee') as con:
        con.execute_immediate(script)
        con.commit()
    init_alter("icon_triggers_for_db.png", "trigger_for_DB_NEW_TRIGGER.png", reload=True)
    result1, result2, result3, result4 = click_tab_comment()
    with fdb.connect('employee') as con:
        con.execute_immediate("DROP TRIGGER NEW_TRIGGER")
        con.commit()
    assert result1 == 2
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_alter_sequence(open_connection):
    init_alter("icon_sequences.png", "sequence_EMP_NO_GEN.png")
    result1, result2, result3, result4 = click_tab_comment()
    assert result1 == 2
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_alter_exception(open_connection):
    init_alter("icon_exceptions.png", "exception_CUSTOMER_CHECK.png")
    result1, result2, result3, result4 = click_tab_comment()
    assert result1 == 2
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_alter_udf(open_connection):
    script = """
DECLARE EXTERNAL FUNCTION NEW_UDF
RETURNS
BIGINT
ENTRY_POINT '123' MODULE_NAME '123'
"""
    with fdb.connect('employee') as con:
        con.execute_immediate(script)
        con.commit()
    init_alter("icon_UDFs.png", "udf_NEW_UDF.png", reload=True)
    result1, result2, result3, result4 = click_tab_comment()
    with fdb.connect('employee') as con:
        con.execute_immediate("DROP FUNCTION NEW_UDF")
        con.commit()
    assert result1 == 3
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_alter_user(open_connection):
    init_alter("icon_users.png", "user_SYSDBA.png")
    result1, result2, result3, result4 = click_tab_comment()
    assert result1 == 1
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_alter_role(open_connection):
    with fdb.connect('employee') as con:
        con.execute_immediate("CREATE ROLE NEW_ROLE")
        con.commit()
    init_alter("icon_roles.png","role_NEW_ROLE.png", reload=True)
    result1, result2, result3, result4 = click_tab_comment()
    with fdb.connect('employee') as con:
        con.execute_immediate("DROP ROLE NEW_ROLE")
        con.commit()
    assert result1 == 1
    assert result2 != None
    assert result3 != None
    assert result4 != None