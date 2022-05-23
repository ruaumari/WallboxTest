import pytest
from FirstFile import firstCompliantFile

def test_TC_BadCase_BigExe():
    exceptionCatch= False
    try:
         firstCompliantFile("./2/TestFiles/BadCase_BigExe")
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

def test_TC_BadCase_NoExeFile():
    exceptionCatch= False
    try:
         firstCompliantFile("./2/TestFiles/BadCase_NoExeFile")
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

def test_TC_BadCase_AdminIsNotFileOwner():
    exceptionCatch= False
    try:
         firstCompliantFile("./2/TestFiles/BadCase_NoAdminOwner")
    except Exception:
         exceptionCatch = True
    assert exceptionCatch

def test_TC_GoodCase():
    file = firstCompliantFile("./2/TestFiles/GoodCase")
    assert file.find("3_Exec_GoodCase.exe")