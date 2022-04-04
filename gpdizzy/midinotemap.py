class MidiNoteMap() : 
    '''
    '''
    MIDI = {
        "A0" : 21, "A#0" : 22, "Bb0" : 22, "B0" : 23,
        "C1" : 24, "C#1" : 25, "Db1" : 25, "D1" : 26, "D#1" : 27, "Eb1" : 27, "E1" : 28, "F1" : 29,
        "F#1" : 30, "Gb1" : 30, "G1" : 31, "G#1" : 32, "Ab1" : 32, "A1" : 33, "A#1" : 34, "Bb1" : 34, "B1" : 35,     
        "C2" : 36, "C#2" : 37, "Db2" : 37, "D2" : 38, "D#2" : 39, "Eb2" : 39, "E2" : 40, "F2" : 41,
        "F#2" : 42, "Gb2" : 42, "G2" : 43, "G#2" : 44, "Ab2" : 44, "A2" : 45, "A#2" : 46, "Bb2" : 46, "B2" : 47,
        "C3" : 48, "C#3" : 49, "Db3" : 49, "D3" : 50, "D#3" : 51, "Eb3" : 51, "E3" : 52, "F3" : 53,
        "F#3" : 54, "Gb3" : 54, "G3" : 55, "G#3" : 56, "Ab3" : 56, "A3" : 57, "A#3" : 58, "Bb3" : 58, "B3" : 59,
        "C4" : 60, "C#4" : 61, "Db4" : 61, "D4" : 62, "D#4" : 63, "Eb4" : 63, "E4" : 64, "F4" : 65,
        "F#4" : 66, "Gb4" : 66, "G4" : 67, "G#4" : 68, "Ab4" : 68, "A4" : 69, "A#4" : 70, "Bb4" : 70, "B4" : 71,        
        "C5" : 72, "C#5" : 73, "Db5" : 73, "D5" : 74, "D#5" : 75, "Eb5" : 75, "E5" : 76, "F5" : 77,
        "F#5" : 78, "Gb5" : 78, "G5" : 79, "G#5" : 80, "Ab5" : 80, "A5" : 81, "A#5" : 82, "Bb5" : 82, "B5" : 83,
        "C6" : 84, "C#6" : 85, "Db6" : 85, "D6" : 86, "D#6" : 87, "Eb6" : 87, "E6" : 88, "F6" : 89,
        "F#6" : 90, "Gb6" : 90, "G6" : 91, "G#6" : 92, "Ab6" : 92, "A6" : 93, "A#6" : 94, "Bb6" : 94, "B6" : 95,
        "C7" : 96, "C#7" : 97, "Db7" : 97, "D7" : 98, "D#7" : 99, "Eb7" : 99, "E7" : 100, "F7" : 101,
        "F#7" : 102, "Gb7" : 102, "G7" : 103, "G#7" : 104, "Ab7" : 104, "A7" : 105, "A#7" : 106, "Bb7" : 106, "B7" : 107,
        "C8" : 108, "C#8" : 109, "Db8" : 109, "D8" : 110, "D#8" : 111, "Eb8" : 111, "E8" : 112, "F8" : 113,
        "F#8" : 114, "Gb8" : 114, "G8" : 115, "G#8" : 116, "Ab8" : 116, "A8" : 117, "A#8" : 118, "Bb8" : 118, "B8" : 119,        
        "C9" : 120, "C#9" : 121, "Db9" : 121, "D9" : 122, "D#9" : 123, "Eb9" : 123, "E9" : 124, "F9" : 125,
        "F#9" : 126, "Gb9" : 126, "G9" : 127,
        "ConcertA" : 69, "MiddleC" : 60
    }

    NOTES = [
        "A", "A#", "Bb", "B",        
        "C", "C#", "Db", "D",
        "D#", "Eb", "E", "F",
        "F#", "Gb", "G"
    ]

    OCTAVES = [
        0, 1, 2,3, 4,
        5, 6, 7, 8, 9
    ]

    def __init__(self) -> None : 
        pass

    def __getattribute__(self, __name: str) -> int:
        retval = None
        if __name in self.MIDI:
            retval = self.MIDI[__name]
        else:
            raise ValueError("Invalid note value")
        return retval

    def map(self, __note: str, __octave: int) -> int:
        retval = None
        if __note in self.NOTES:
            if __octave in self.OCTAVES:
                nidx = f'{__note}{str(__octave)}'
                retval = self.MIDI[nidx]
            else:
                raise ValueError("Unmapped note/octave combination")
        else:
            raise ValueError("Unmapped note/octave combination")
        return retval
