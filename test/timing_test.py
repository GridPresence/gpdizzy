from pytest import approx
from gpdizzy.timesig  import TimeSig

std_ppqn = 24
std_pulse = 1.0 / std_ppqn
hi_ppqn = 96
hi_pulse = 1.0 / hi_ppqn

def test_01():
    thing = TimeSig()
    assert thing.bpm == 60
    assert thing.ppqn == std_ppqn
    assert thing.pulse == approx(std_pulse)
    assert thing.quarter == approx(thing.pulse * thing.ppqn)
    assert thing.quarter_pulse == thing.ppqn
    assert thing.half == approx(2.0)
    assert thing.eighth == approx(0.5)
    assert thing.sixteenth_pulse == 6

def test_02():
    thing = TimeSig()
    thing.bpm = 120
    assert thing.ppqn == std_ppqn
    assert thing.pulse == approx(std_pulse / 2.0)
    assert thing.quarter == approx(thing.pulse * thing.ppqn)
    assert thing.quarter_pulse == thing.ppqn
    assert thing.half == approx(1.0)
    assert thing.eighth == approx(0.25)
    assert thing.sixteenth_pulse == 6
    assert thing.sixteenth_triplet_pulse == 8

def test_03():
    thing = TimeSig()
    thing.ppqn = hi_ppqn
    assert thing.bpm == 60
    assert thing.ppqn == hi_ppqn
    assert thing.pulse == approx(hi_pulse)
    assert thing.quarter == approx(thing.pulse * thing.ppqn)
    assert thing.quarter_pulse == thing.ppqn
    assert thing.half == approx(2.0)
    assert thing.eighth == approx(0.5)
    assert thing.sixteenth_pulse == 24

def test_04():
    thing = TimeSig()
    thing.bpm = 120
    thing.ppqn = hi_ppqn
    assert thing.ppqn == hi_ppqn
    assert thing.pulse == approx(hi_pulse / 2.0)
    assert thing.quarter == approx(thing.pulse * thing.ppqn)
    assert thing.quarter_pulse == thing.ppqn
    assert thing.half == approx(1.0)
    assert thing.eighth == approx(0.25)
    assert thing.sixteenth_pulse == 24
    assert thing.sixteenth_triplet_pulse == 32
