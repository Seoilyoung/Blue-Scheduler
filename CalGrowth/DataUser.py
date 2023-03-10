class dataset:
    def __init__(self,name):
        self.ID = name
        self.Report = 0
        self.Credit = [0,0]
        self.ScretNote = 0
        self.Oparts = {
            "네브라" :[0,0,0,0],
            "파에스토스" :[0,0,0,0],
            "볼프세크" :[0,0,0,0],
            "님루드" :[0,0,0,0],
            "만드라고라" :[0,0,0,0],
            "로혼치" :[0,0,0,0],
            "에테르" :[0,0,0,0],
            "안티키테라" :[0,0,0,0],
            "보이니치" :[0,0,0,0],
            "하니와" :[0,0,0,0],
            "토템폴" :[0,0,0,0],
            "전지" :[0,0,0,0],
            "콜간테" :[0,0,0,0],
            "위니페소키" :[0,0,0,0]
        }
        self.Bd = {
            "백귀야행" :[0,0,0,0],
            "붉은겨울" :[0,0,0,0],
            "트리니티" :[0,0,0,0],
            "게헨나" :[0,0,0,0],
            "아비도스" :[0,0,0,0],
            "밀레니엄" :[0,0,0,0],
            "아리우스" :[0,0,0,0],
            "산해경" :[0,0,0,0],
            "발키리" :[0,0,0,0]
        }
        self.Note = {
            "백귀야행" :[0,0,0,0],
            "붉은겨울" :[0,0,0,0],
            "트리니티" :[0,0,0,0],
            "게헨나" :[0,0,0,0],
            "아비도스" :[0,0,0,0],
            "밀레니엄" :[0,0,0,0],
            "아리우스" :[0,0,0,0],
            "산해경" :[0,0,0,0],
            "발키리" :[0,0,0,0]
        }
    def all(self):
        print("ID :", self.ID, "\n보고서 :", format(self.Report,','), "\n크레딧[ 스킬 , 레벨 ] : [", format(self.Credit[0], ','), ",", format(self.Credit[1],","),"]", "\n비의서 :", self.ScretNote, "\n오파츠 :",
              self.Oparts, "\nBD :", self.Bd, "\n노트 :", self.Note)
        
    def increase(self, A, B, list):
        if A == 'Bd':
            for i in range(0,4):
                self.Bd[B][i] += list[i] 
        elif A == 'Note':
            for i in range(0,4):
                self.Note[B][i] += list[i]
        else:
            print('Target Error')

    def increaseOparts(self, A, A_A, B, list, num):
        if A == 'OpartsBd':
            if A_A == 'Main':
                self.Oparts[B][int(num)-2] += list[int(num)-2]
            elif A_A == 'Sub' and int(num) >= 3:
                self.Oparts[B][int(num)-3] += list[int(num)-2]
            else:
                return
        elif A == 'OpartsNote':
            if A_A == 'Main' or A_A == 'Sub':
                if num == '4':
                    num2 = 0
                elif num == '5' or num == '6':
                    num2 = 1
                elif num == '7':
                    num2 = 2
                elif num == '8' or num == '9':
                    num2 = 3
                else:
                    return
                if A_A == 'Sub':
                    num2 -= 1
            else:
                print('Sub Target Error')
                return
            if num2 >= 0:
                self.Oparts[B][num2] += list[int(num)-2]
        else:
            print('Target Error')

    def decrease(self, A, B, list):
        if A == 'Bd':
            target = self.Bd
        elif A == 'Note':
            target = self.Note
        elif A == 'Oparts':
            target = self.Oparts
        else:
            print('Target Error')
        for i in range(0,4):
            target[0][B][i] -= list[i]  