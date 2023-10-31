import lackey
from re_tests_plugin import *


def test_1(open_connection):
    lackey.click("tab_query_editor.png")
    lackey.click("tab_query_editor_text.png")
    script = """select * from select * from select * from select * from select * from select * from select * from select * from select * from select * from select * from select * from select * from select * from select * from select * from select * from select * from 
select 
1345
5
4
6
create table

"""
    lackey.App.setClipboard(script)
    lackey.type("v", lackey.Key.CTRL)
    chb = lackey.exists("chb_wrap_lines.png")
    lackey.click(chb)
    result = lackey.exists("line_numbers.png")
    lackey.click(chb.getTarget().below(20))
    lackey.type("a", lackey.Key.CTRL)
    lackey.type(lackey.Key.DELETE)
    assert result != None

