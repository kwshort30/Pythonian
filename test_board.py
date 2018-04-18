
from board import pick_who_goes_first

def test_smoke():
	assert True==True

def test_pick_who_goes_first():
	assert pick_who_goes_first() in [ "X", "O" ] 
