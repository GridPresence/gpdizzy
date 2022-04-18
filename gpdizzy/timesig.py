
class TimeSig():

    def __init__(self) -> None:
        self._bpm = 60
        self._ppqn = 24
        self._calibrate()

    def _calibrate(self):
        if self._bpm > 0:
            self._quarter = 60.0 / self._bpm
            self._pulse = self._quarter / self._ppqn

    @property
    def bpm(self) -> int:
        return self._bpm

    @bpm.setter
    def bpm(self, value: int):
        if value > 0:
            self._bpm = value
            self._calibrate()
    
    @property
    def ppqn(self) -> int:
        return self._ppqn

    @ppqn.setter
    def ppqn(self, value: int):
        if value > 0:
            self._ppqn = value
            self._calibrate()

    @property
    def pulse(self) -> float:
        return self._pulse

    @property
    def quarter(self) -> float:
        return self._quarter

    @property
    def whole(self) -> float:
        return self._quarter * 4.0

    @property
    def half(self) -> float:
        return self._quarter * 2.0

    @property
    def eighth(self) -> float:
        return self._quarter / 2.0

    @property
    def sixteenth(self) -> float:
        return self._quarter / 4.0

    @property
    def quarter_triplet(self) -> float:
        return (self._quarter * 4.0) / 3.0

    @property
    def half_triplet(self) -> float:
        return ((self._quarter * 2.0) * 4.0) / 3.0

    @property
    def eighth_triplet(self) -> float:
        return ((self._quarter / 2.0) * 4.0) / 3.0

    @property
    def sixteenth_triplet(self) -> float:
        return ((self._quarter / 4.0) * 4.0) / 3.0

    @property
    def quarter_pulse(self) -> float:
        return self._ppqn

    @property
    def whole_pulse(self) -> float:
        return self._ppqn * 4

    @property
    def half_pulse(self) -> float:
        return self._ppqn * 2

    @property
    def eighth_pulse(self) -> float:
        return self._ppqn / 2

    @property
    def sixteenth_pulse(self) -> float:
        return self._ppqn / 4

    @property
    def quarter_triplet_pulse(self) -> float:
        return (self._ppqn * 4) / 3

    @property
    def half_triplet_pulse(self) -> float:
        return ((self._ppqn * 2) * 4) / 3

    @property
    def eighth_triplet_pulse(self) -> float:
        return ((self.ppqn / 2) * 4) / 3

    @property
    def sixteenth_triplet_pulse(self) -> float:
        return ((self._ppqn / 4) * 4) / 3
