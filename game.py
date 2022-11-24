import english_words as eng
import random 
class wordle:

    hard_5_word = [x for x in eng.english_words_lower_set if len(x) == 5]
    easy_5_word = ['dream', 'india', 'angry', 'sheep', 'fault', 'stone', 'trend', 'sweet'
    , 'mouth', 'agree', 'storm', 'apple', 'think']
    def __init__(self):
        self.game_count = 0
        self.green = '\033[92m'
        self.grey = '\033[90m'
        self.yellow = '\033[33m'
        self.game_progress = list('_' * 30)
        self.wordle = random.choice(self.hard_5_word)

    def user_input(self):
        user_input = input('유효한 영단어를 입력해주세요:')
        return user_input

    def correct_answer(self, user_input):
        for idx_1 in range(len(self.wordle)):
            for idx_2 in range(len(user_input)):
                if user_input[idx_2] not in self.wordle:
                    self.game_progress[self.game_count * 5 + idx_2] = self.grey + user_input[idx_2] + '\033[0m'
                else:
                    if user_input[idx_2] == self.wordle[idx_1]:
                        if idx_1 == idx_2:
                            self.game_progress[self.game_count * 5 + idx_1] = self.green + user_input[idx_2] + '\033[0m'         
                        else: 
                            self.game_progress[self.game_count * 5 + idx_2] = self.yellow + user_input[idx_2] + '\033[0m'

    @classmethod
    def is_valid_word(self, user_input):
        return len(user_input) == 5 and user_input.isalpha()
    
    def print_game_status(self):
        count = 1
        for i in self.game_progress:
            print(i, end = ' ')
            if count % 5 == 0:
                print()
                count += 1
                continue
            count += 1   
    
    def game_mode(self):
        print('\n\033[1mwordle\033[0m 게임을 시작합니다!')
        input_game = input('게임모드를 설정합니다. 어려운 모드를 플레이 하실거면 ''y'' 쉬운 모드를 플레이 하려면 ''n''을 입력해주세요.')
        print('\n\033[1m게임 설명:\033[0m 정답과 위치가 같은 글자는 \033[92m초록색\033[0m 으로 표시되고 글자는 같지만 정답과 위치가 다른 글자는 \033[33m노란색\033[0m으로 표시됩니다. \n 그외의 글자는 \033[90m회색\033[0m으로 표시됩니다.')
        
        while True:
            if input_game == 'y':
                self.wordle = random.choice(self.hard_5_word)
                break
            elif input_game == 'n':
                self.wordle = random.choice(self.easy_5_word)
                break
            else:
                input_game = input('재대로 입력해주세요.')
                continue

    def play(self):
        self.game_mode()
        while True:
            print(self.wordle)
            self.print_game_status()
            user_input = self.user_input()
            if wordle.is_valid_word(user_input):
                self.correct_answer(user_input)
                self.game_count += 1
            else:
                print('다시 입력해주세요.')

            if user_input == self.wordle:
                print('단어를 맞추었습니다. 축하합니다.')
                break
            if self.game_count > 6:
                print(self.print_game_status())
                print('단어를 맞추지 못하였습니다.')
                break