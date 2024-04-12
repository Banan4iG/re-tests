import lackey
from re_tests_plugin import *

def init_create(icon):
    lackey.click("tree_plus.png")
    lackey.rightClick(icon)
    lackey.click("tree_create_menu.png")

def init_column_create():
    lackey.SettingsMaster.MinSimilarity = 0.96
    lackey.click(lackey.exists("table_column_Name.png").getTarget().below(20))
    lackey.SettingsMaster.MinSimilarity = 0.97
    lackey.type("test")
    lackey.click(lackey.exists("table_column_Datatype.png").getTarget().below(20))
    lackey.click("datatype_BIGINT.png")

def init_procedure(param=None):
    script = "BEGIN\nEND"
    lackey.App.setClipboard(script)
    lackey.click(lackey.exists("tab_procedure_body_focus.png").getTarget().below(50))
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    lackey.type("v", lackey.Key.CTRL)
    if param:
        lackey.click(param)

def click_tab_column():
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
    lackey.click("bt_cancel.png")
    lackey.click("bt_YES.png")
    assert result1 == 2
    assert result2 != None
    assert result3 != None
    assert result4 != None

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
    lackey.click("bt_cancel.png")
    lackey.click("bt_YES.png")
    assert result1 >= 2
    assert result2 != None
    assert result3 != None
    assert result4 != None

def test_create_domain(open_connection):
    init_create("icon_domains.png")
    click_tab_comment()  

def test_create_table(open_connection):
    init_create("icon_tables.png")
    init_column_create()
    click_tab_comment()

def test_create_table_columns(open_connection):
    init_create("icon_tables.png")
    init_column_create()
    click_tab_column()

def test_create_gtt(open_connection):
    init_create("icon_tables.png")
    init_column_create()
    click_tab_comment()

def test_create_gtt_columns(open_connection):
    init_create("icon_tables.png")
    init_column_create()
    click_tab_column()

def test_create_view(open_connection):
    init_create("icon_views.png")
    lackey.SettingsMaster.MinSimilarity = 0.93
    lackey.click(lackey.exists("tab_DDL.png").getTarget().below(50))
    lackey.SettingsMaster.MinSimilarity = 0.97
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.BACKSPACE)
    script = "SELECT emp_no FROM employee"
    lackey.App.setClipboard(script)
    lackey.type("v", lackey.Key.CTRL)
    time.sleep(3)
    click_tab_comment()

def test_create_procedure(open_connection):
    init_create("icon_procedures.png")
    init_procedure()
    click_tab_comment()

def test_create_procedure_input_p(open_connection):
    init_create("icon_procedures.png")
    init_procedure("tab_input_parameters.png")
    init_column_create()
    click_tab_column()

def test_create_procedure_output_p(open_connection):
    init_create("icon_procedures.png")
    init_procedure("tab_output_parameters.png")
    init_column_create()
    click_tab_column()

def test_create_function(open_connection):
    init_create("icon_functions.png")
    click_tab_comment()

def test_create_function_arg(open_connection):
    init_create("icon_functions.png")
    lackey.click("tab_arguments.png")
    init_column_create()
    click_tab_column()

def test_create_package(open_connection):
    init_create("icon_packages.png")
    click_tab_comment()

def test_create_trigger_for_table(open_connection):
    init_create("icon_triggers_for_table.png")
    lackey.click("chb_INSERT.png")
    click_tab_comment()

def test_create_trigger_for_ddl(open_connection):
    init_create("icon_triggers_for_DDL.png")
    lackey.click("chb_ANY_DDL_STATEMENT.png")
    click_tab_comment()

def test_create_trigger_for_db(open_connection):
    init_create("icon_triggers_for_db.png")
    click_tab_comment()

def test_create_sequence(open_connection):
    init_create("icon_sequences.png")
    click_tab_comment()

def test_create_exception(open_connection):
    init_create("icon_exceptions.png")
    click_tab_comment()

def test_create_udf(open_connection):
    init_create("icon_UDFs.png")
    click_tab_comment()

def test_create_user(open_connection):
    init_create("icon_users.png")
    lackey.click("text_input_password.png")
    lackey.type("test")
    click_tab_comment()

def test_create_role(open_connection):
    init_create("icon_roles.png")
    click_tab_comment()

def test_create_index(open_connection):
    init_create("icon_indices.png")
    lackey.click("bt_dbl_triangle_right.png")
    click_tab_comment()