from normal.searchfilein_dir import Searchfiles
def test_files():
    ob=Searchfiles()
    data=ob.search("../normal","demo1.py")
    assert data==['../normal\\demo1.py']