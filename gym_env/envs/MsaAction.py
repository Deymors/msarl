class MsaAction:
    def __init__(self, seq_num: int, gap_position: int, adding: bool):
        self.seq_num = seq_num
        self.gap_position = gap_position
        self.adding = adding
