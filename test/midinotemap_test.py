from gpdizzy.midinotemap import MidiNoteMap

def test_01():
    thing = MidiNoteMap()

    assert thing.map("ConcertA", 0) == 69
    assert thing.map("MiddleC", 0) == 60
    assert thing.map("F", 3) == 53

def test_02():
    thing = MidiNoteMap()
    assert thing.map("A#", 4) == thing.map("Bb", 4)
    assert thing.map("F#", 2) == thing.map("Gb", 2)
    assert thing.map("D#", 1) == thing.map("Eb", 1)
    assert thing.map("C#", 3) == thing.map("Db", 3)
    

