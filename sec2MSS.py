
def sec2MSS(seconds):
    return '{}:{:02d}'.format(*divmod(int(seconds), 60))

def test_sec2MSS_0():
    assert sec2MSS(0)=="0:00"

def test_sec2MSS_0_5():
    assert sec2MSS(0.5)=="0:00"

def test_sec2MSS_0_1():
    assert sec2MSS(0.1)=="0:00"

def test_sec2MSS_0_9():
    assert sec2MSS(0.9)=="0:00"

def test_sec2MSS_1_01():
    assert sec2MSS(1.01)=="0:01"

def test_sec2MSS_1_99():
    assert sec2MSS(1.99)=="0:01"

def test_sec2MSS_1():
    assert sec2MSS(1)=="0:01"

def test_sec2MSS_59():
    assert sec2MSS(59)=="0:59"

def test_sec2MSS_60():
    assert sec2MSS(60)=="1:00"

def test_sec2MSS_61():
    assert sec2MSS(61)=="1:01"

def test_sec2MSS_122():
    assert sec2MSS(122)=="2:02"
    
