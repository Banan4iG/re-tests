import lackey
from re_tests_plugin import *
import firebird.driver as fdb

def init_alter(icon, name, reload=False):
    lackey.click("tree_plus.png")
    if reload:
        lackey.rightClick(icon)
        lackey.click("tree_reload_menu.png")
    lackey.click(plus_find(icon))
    lackey.rightClick(name)
    lackey.click("tree_edit_menu.png")

def click_tab_comment(MinSimilarity=0.97):
    if MinSimilarity != 0.97:
        lackey.SettingsMaster.MinSimilarity = MinSimilarity
        lackey.click("tab_comment.png")
        lackey.SettingsMaster.MinSimilarity = 0.97
    else:
        lackey.click("tab_comment.png")
    mouse = lackey.Mouse()
    lackey.click(mouse.getPos().below(100))
    lackey.type("test comment")
    lackey.click("bt_OK.png")
    result1 = len(list(lackey.findAll("text_success.png")))
    result2 = lackey.exists("text_test_comment.png")
    lackey.click("bt_rollback.png")
    lackey.click("bt_cancel.png")
    lackey.click("bt_YES.png")
    return result1, result2

def test_alter_domain(open_connection):
    init_alter("icon_domains.png", "tree_domain_name_ADDRESSLINE.png")
    result1, result2 = click_tab_comment()
    assert result1 == 2
    assert result2 != None

def test_alter_view(open_connection):
    init_alter("icon_views.png", "tree_view_name_PHONE_LIST.png")
    result1, result2 = click_tab_comment(MinSimilarity=0.93)
    assert result1 == 2
    assert result2 != None

def test_alter_procedure(open_connection):
    init_alter("icon_procedures.png", "proc_ALL_LANGS.png")
    result1, result2 = click_tab_comment()
    assert result1 == 2
    assert result2 != None

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
    result1, result2 = click_tab_comment()
    with fdb.connect('employee') as con:
        con.execute_immediate('DROP FUNCTION NEW_FUNC')
        con.commit()
    assert result1 == 2
    assert result2 != None

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
    result1, result2 = click_tab_comment()
    with fdb.connect('employee') as con:
        con.execute_immediate('DROP PACKAGE NEW_PACK')
        con.commit()
    assert result1 == 3
    assert result2 != None

def test_alter_trigger_for_table(open_connection):
    init_alter("icon_triggers_for_table.png", "trigger_POST_NEW_ORDER.png")
    result1, result2 = click_tab_comment()
    assert result1 == 2
    assert result2 != None

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
    result1, result2 = click_tab_comment()
    with fdb.connect('employee') as con:
        con.execute_immediate("DROP TRIGGER NEW_TRIGGER")
        con.commit()
    assert result1 == 2
    assert result2 != None

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
    result1, result2 = click_tab_comment()
    with fdb.connect('employee') as con:
        con.execute_immediate("DROP TRIGGER NEW_TRIGGER")
        con.commit()
    assert result1 == 2
    assert result2 != None

def test_alter_sequence(open_connection):
    init_alter("icon_sequences.png", "sequence_EMP_NO_GEN.png")
    result1, result2 = click_tab_comment(MinSimilarity=0.93)
    assert result1 == 2
    assert result2 != None

def test_alter_exception(open_connection):
    init_alter("icon_exceptions.png", "exception_CUSTOMER_CHECK.png")
    result1, result2 = click_tab_comment()
    assert result1 == 2
    assert result2 != None

def test_alter_udf(open_connection):
    pass
#     script = """
# DECLARE EXTERNAL FUNCTION NEW_UDF
# RETURNS
# BIGINT
# ENTRY_POINT ''
# MODULE_NAME ''
# """
#     with fdb.connect('employee') as con:
#         con.execute_immediate(script)
#         con.commit()
#     init_alter("icon_UDFs.png", "")
#     result1, result2 = click_tab_comment()
#     with fdb.connect('employee') as con:
#         con.execute_immediate("DROP FUNCTION NEW_UDF")
#         con.commit()
#     assert result1 == 2
#     assert result2 != None

def test_alter_user(open_connection):
    init_alter("icon_users.png", "user_SYSDBA.png")
    result1, result2 = click_tab_comment()
    assert result1 == 1
    assert result2 != None

def test_alter_index(open_connection):
    icon_conn_open = lackey.exists("icon_conn_open.png")
    init_alter("icon_indices.png", "index_BUDGETX.png")
    result1, result2 = click_tab_comment()
    mouse = lackey.Mouse()
    mouse.move(icon_conn_open.getTarget())
    lackey.wheel(lackey.Mouse.WHEEL_UP, 10)
    assert result1 == 1
    assert result2 != None