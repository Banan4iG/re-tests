import lackey
from re_tests_plugin import *

def init_create(icon):
    lackey.click("tree_plus.png")
    lackey.rightClick(icon)
    lackey.click("tree_create_menu.png")

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
    assert result1 >= 2
    assert result2 != None

def test_create_domain(open_connection):
    init_create("icon_domains.png")
    click_tab_comment()  

def test_create_table(open_connection):
    init_create("icon_tables.png")
    lackey.SettingsMaster.MinSimilarity = 0.96
    lackey.click(lackey.exists("table_colum_Name.png").getTarget().below(20))
    lackey.SettingsMaster.MinSimilarity = 0.97
    lackey.type("test")
    lackey.click(lackey.exists("table_colum_Datatype.png").getTarget().below(20))
    lackey.click("datatype_BIGINT.png")
    click_tab_comment()

def test_create_gtt(open_connection):
    init_create("icon_gtt.png")
    lackey.SettingsMaster.MinSimilarity = 0.96
    lackey.click(lackey.exists("table_colum_Name.png").getTarget().below(20))
    lackey.SettingsMaster.MinSimilarity = 0.97
    lackey.type("test")
    lackey.click(lackey.exists("table_colum_Datatype.png").getTarget().below(20))
    lackey.click("datatype_BIGINT.png")
    click_tab_comment()

def test_create_view(open_connection):
    init_create("icon_views.png")
    lackey.SettingsMaster.MinSimilarity = 0.96
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
    lackey.click("tab_output_parameters.png")
    lackey.click(lackey.exists("table_colum_Name.png").getTarget().below(20))
    lackey.type("test")
    lackey.click(lackey.exists("table_colum_Datatype.png").getTarget().below(20))
    lackey.click("datatype_BIGINT.png")
    click_tab_comment()

def test_create_function(open_connection):
    init_create("icon_functions.png")
    click_tab_comment()

def test_create_package(open_connection):
    init_create("icon_packages.png")
    click_tab_comment(MinSimilarity=0.93)

def test_create_trigger_for_table(open_connection):
    init_create("icon_triggers_for_table.png")
    lackey.click("chb_INSERT.png")
    click_tab_comment(MinSimilarity=0.93)

def test_create_trigger_for_ddl(open_connection):
    init_create("icon_triggers_for_DDL.png")
    lackey.click("chb_ANY_DDL_STATEMENT.png")
    click_tab_comment(MinSimilarity=0.93)

def test_create_trigger_for_db(open_connection):
    init_create("icon_triggers_for_db.png")
    click_tab_comment(MinSimilarity=0.93)

def test_create_sequence(open_connection):
    init_create("icon_sequences.png")
    click_tab_comment(MinSimilarity=0.93)

def test_create_exception(open_connection):
    init_create("icon_exceptions.png")
    click_tab_comment(MinSimilarity=0.93)

def test_create_udf(open_connection):
    init_create("icon_UDFs.png")
    click_tab_comment(MinSimilarity=0.93)

def test_create_user(open_connection):
    init_create("icon_users.png")
    lackey.click("text_input_password.png")
    lackey.type("test")
    click_tab_comment()

def test_create_role(open_connection):
    init_create("icon_roles.png")
    click_tab_comment(MinSimilarity=0.93)

def test_create_index(open_connection):
    init_create("icon_indices.png")
    lackey.click("bt_dbl_triangle_right.png")
    click_tab_comment(MinSimilarity=0.93)