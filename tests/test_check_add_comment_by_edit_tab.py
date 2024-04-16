import lackey
from re_tests_plugin import *
import firebird.driver as fdb

def init_alter(icon, reload=False):
    lackey.click("tree_plus.png")
    if reload:
        lackey.rightClick(icon)
        lackey.click("tree_reload_menu.png")
    lackey.click(plus_find(icon))

def click_tab_comment(object, object_name=None, table=False):
    if table:
        lackey.click("tab_properties.png")
        lackey.click("text_comment.png")
    else:
        lackey.click("tab_comment.png")
    mouse = lackey.Mouse()
    lackey.click(mouse.getPos().offset(30, 100))
    lackey.type("test comment")
    lackey.click("icon_commit.png")
    with fdb.connect('employee') as con:
        cur = con.cursor()
        if object == "RDB$GENERATORS":
            cur.execute(f"select RDB$DESCRIPTION from {object} where RDB$DESCRIPTION is not NULL and RDB$GENERATOR_NAME = '{object_name}'")
        elif object == "SEC$USERS":
            cur.execute(f'select SEC$DESCRIPTION from {object} where SEC$DESCRIPTION is not NULL')
        else:
            cur.execute(f'select RDB$DESCRIPTION from {object} where RDB$DESCRIPTION is not NULL')
        result = cur.fetchall()
        cur.close()
    lackey.click(mouse.getPos().offset(30, 100))
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.click("icon_commit.png")
    lackey.rightClick("icon_abstract_object_blue.png")
    lackey.click("bt_tab_close_all.png")
    return result[0][0]


def test_alter_domain(open_connection):
    init_alter("icon_domains.png")
    lackey.doubleClick("tree_domain_name_ADDRESSLINE.png")
    result = click_tab_comment("RDB$FIELDS")
    assert result == 'test comment'

def test_alter_table(open_connection):
    init_alter("icon_tables.png")
    lackey.doubleClick("tree_table_name_EMPLOYEE.png")
    result = click_tab_comment("RDB$RELATIONS", table=True)
    assert result == 'test comment'

def test_alter_gtt(lock_employee, open_connection):
    with fdb.connect('employee') as con:
        con.execute_immediate('CREATE GLOBAL TEMPORARY TABLE NEW_GTT (TESTS BIGINT) ON COMMIT DELETE ROWS')
        con.commit()
    init_alter("icon_gtt.png", reload=True)
    lackey.doubleClick("tree_gtt_name_NGTT.png")
    result = click_tab_comment("RDB$RELATIONS", table=True)
    assert result == 'test comment'

def test_alter_view(open_connection):
    init_alter("icon_views.png")
    lackey.doubleClick("tree_view_name_PHONE_LIST.png")
    result = click_tab_comment("RDB$RELATIONS")
    assert result == 'test comment'

def test_alter_procedure(open_connection):
    init_alter("icon_procedures.png")
    lackey.doubleClick("proc_ALL_LANGS.png")
    result = click_tab_comment("RDB$PROCEDURES")
    assert result == 'test comment'

def test_alter_function(lock_employee, open_connection):
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
    init_alter("icon_functions.png", reload=True)
    lackey.doubleClick("func_NEW_FUNC.png")
    result = click_tab_comment("RDB$FUNCTIONS")
    assert result == 'test comment'

def test_alter_package(lock_employee, open_connection):
    script1 = """
CREATE OR ALTER PACKAGE NEW_PACK
AS
BEGIN
END
"""
    with fdb.connect('employee') as con:
        con.execute_immediate(script1)
        con.commit()
    init_alter("icon_packages.png", reload=True)
    lackey.doubleClick("pack_NEW_PACK.png")
    result = click_tab_comment("RDB$PACKAGES")
    assert result == 'test comment'

def test_alter_trigger_for_table(open_connection):
    init_alter("icon_triggers_for_table.png")
    lackey.doubleClick("trigger_POST_NEW_ORDER.png")
    result = click_tab_comment("RDB$TRIGGERS")
    assert result == 'test comment'

def test_alter_trigger_for_ddl(lock_employee, open_connection):
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
    init_alter("icon_triggers_for_ddl.png", reload=True)
    lackey.doubleClick("trigger_for_DDL_NEW_TRIGGER.png")
    result = click_tab_comment("RDB$TRIGGERS")
    assert result == 'test comment'

def test_alter_trigger_for_db(lock_employee, open_connection):
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
    init_alter("icon_triggers_for_db.png", reload=True)
    lackey.doubleClick("trigger_for_DB_NEW_TRIGGER.png")
    result = click_tab_comment("RDB$TRIGGERS")
    assert result == 'test comment'

def test_alter_sequence(open_connection):
    init_alter("icon_sequences.png")
    lackey.doubleClick("sequence_EMP_NO_GEN.png")
    result = click_tab_comment("RDB$GENERATORS", object_name="EMP_NO_GEN")
    assert result == 'test comment'

def test_alter_exception(open_connection):
    init_alter("icon_exceptions.png")
    lackey.doubleClick("exception_CUSTOMER_CHECK.png")
    result = click_tab_comment("RDB$EXCEPTIONS")
    assert result == 'test comment'

def test_alter_udf(lock_employee, open_connection):
    script = """
DECLARE EXTERNAL FUNCTION NEW_UDF
RETURNS
BIGINT
ENTRY_POINT '123' MODULE_NAME '123'
"""
    with fdb.connect('employee') as con:
        con.execute_immediate(script)
        con.commit()
    init_alter("icon_UDFs.png", reload=True)
    lackey.doubleClick("udf_NEW_UDF.png")
    result = click_tab_comment("RDB$FUNCTIONS")
    assert result == 'test comment'

def test_alter_user(open_connection):
    init_alter("icon_users.png")
    lackey.doubleClick("user_SYSDBA.png")
    result = click_tab_comment("SEC$USERS")
    assert result == 'test comment'

def test_alter_role(lock_employee, open_connection):
    with fdb.connect('employee') as con:
        con.execute_immediate("CREATE ROLE NEW_ROLE")
        con.commit()
    init_alter("icon_roles.png", reload=True)
    lackey.doubleClick("role_NEW_ROLE.png")
    result = click_tab_comment("RDB$ROLES")
    assert result == 'test comment'