import numpy as np

from gym_env.envs.MsaAction import MsaAction


class MsaState:
    gap_penalty = -2
    mismatch_penalty = -1
    match_reward = 1

    def __init__(self, sequence_chars):
        self.num_sequences = len(sequence_chars)
        self.sequences = []
        self.sequences_gaps = []
        self.sequences_lens = []
        for sequence_of_chars in sequence_chars:
            sequence = np.array([])
            for char in sequence_of_chars:
                hot_encode = 4
                if char == 'A':
                    hot_encode = 1
                elif char == 'G':
                    hot_encode = 2
                elif char == 'C':
                    hot_encode = 3
                elif char == 'T':
                    hot_encode = 4
                np.append(sequence, hot_encode)
            self.sequences.append(sequence)
            sequence_gaps = np.zeros(shape=(len(sequence)))
            self.sequences_gaps.append(sequence_gaps)
            self.sequences_lens.append(len(sequence))

    def is_valid_action(self, action: MsaAction):
        if (not action.adding) and self.sequences[action.seq_num][action.gap_position] == 0:
            return False
        return True

    def apply_action(self, action: MsaAction):
        if self.is_valid_action(action):
            if action.adding:
                self.sequences[action.seq_num][action.gap_position] += 1
                self.sequences_lens[action.seq_num] += 1
            else:
                self.sequences[action.seq_num][action.gap_position] -= 1
                self.sequences_lens[action.seq_num] -= 1

    def calculate_score(self):
        score = 0
        indexes = np.zeros(self.num_sequences)
        gaps = np.zeros(self.num_sequences)
        nts = np.zeros(self.num_sequences)
        while True:
            score, sequence_ended = self.__get_step_score(gaps, indexes, nts, score)
            if sequence_ended:
                break
        return score

    def __get_step_score(self, gaps, indexes, nts, score):
        step_score = 0
        sequence_ended = True
        self.__get_curr_nts(gaps, indexes, nts)
        step_score = self.__calc_step_score(nts, step_score)
        score += step_score
        return score, sequence_ended

    def __get_curr_nts(self, gaps, indexes, nts):
        for i in range(self.num_sequences):
            nt = 0
            index = indexes[i]
            if len(self.sequences[i]) > index:
                gaps[i] += self.sequences_gaps[index]
                if gaps[i] == 0:
                    nt = self.sequences[index]
                    indexes[i] += 1
                else:
                    gaps[i] -= 1
            nts[i] = nt

    def __calc_step_score(self, nts, step_score):
        for i in range(self.num_sequences - 1):
            nt1 = nts[i]
            for j in range(i + 1, self.num_sequences):
                nt2 = nts[j]
                step_score += self.__calc_pair(nt1, nt2)
        return step_score

    def __calc_pair(self, nt1: int, nt2: int):
        if nt1 == nt2 and nt1 > 0:
            return self.match_reward

        if nt1 == nt2 and nt1 > 0 and nt2 > 0:
            return self.mismatch_penalty
        pair_score = 0
        if nt1 == 0:
            pair_score += self.gap_penalty
        if nt2 == 2:
            pair_score += self.gap_penalty
        return pair_score
