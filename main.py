from numpy import random as random

class minesweeper:
    def __init__(self):
        self.top=['#','A','B','C','D','E']
        self.row1=[' ']*6
        self.row1[0]='A'
        self.row2=[' ']*6
        self.row2[0]='B'
        self.row3=[' ']*6
        self.row3[0]='C'
        self.row4=[' ']*6
        self.row4[0]='D'
        self.row5=[' ']*6
        self.row5[0]='E'
        self.full_board=[self.top,self.row1,self.row2,self.row3,self.row4,self.row5]
        self.mines=[]
        self.co_ord=[]
        self.user_top=['#','A','B','C','D','E']
        self.user_row1=[' ']*6
        self.user_row1[0]='A'
        self.user_row2=[' ']*6
        self.user_row2[0]='B'
        self.user_row3=[' ']*6
        self.user_row3[0]='C'
        self.user_row4=[' ']*6
        self.user_row4[0]='D'
        self.user_row5=[' ']*6
        self.user_row5[0]='E'
        self.user_full_board=[self.user_top,self.user_row1,self.user_row2,self.user_row3,self.user_row4,self.user_row5]
    def show_board(self):
        for i in self.full_board:
            print (i)
    def user_board(self):
        for i in self.user_full_board:
            print (i)
    def input_user(self):
        while True:
            q=input("enter the row:")
            r=input("enter the column:")
            for a in range(1,6):
                if (r.upper()==self.top[a]):
                    column_input=a
                    break
                else:
                    continue
            for b in range(1,6):
                if (q.upper()==self.full_board[b][0]):
                    row_input=b
                    break
                else:
                    continue
            if self.user_full_board[row_input][column_input]==' ':
                row=row_input
                column=column_input
                break
            else:
                print("output already occupied")
                continue
        self.co_ord=[row,column]
        self.user_full_board[row][column]=self.full_board[row][column]
        
    def modification_win_board(self):
        for i in range(1,6):
            for j in range(1,6):
                if self.win_check_board[i][j]=='X':
                    self.win_check_board[i][j]='F'
                else:
                    continue
    def check_win(self):
        ql=0
        for i in range(1,6):
            for j in range(1,6):
                if self.full_board[i][j]==self.user_full_board[i][j]:
                    ql=ql+1
                elif self.full_board[i][j]=='X' and self.user_full_board[i][j]=='F':
                    ql=ql+1
                else:
                    ql=ql+0
        if ql==25:
            return True
        else:
            return False
        
    def place_flag(self):
       
        while True:
            q=input("enter the row:")
            r=input("enter the column:")
            for a in range(1,6):
                if (r.upper()==self.top[a]):
                    column_input=a
                    break
                else:
                    continue
            for b in range(1,6):
                if (q.upper()==self.full_board[b][0]):
                    row_input=b
                    break
                else:
                    continue
            if self.user_full_board[row_input][column_input]==' ':
                row=row_input
                column=column_input
                break
            else:
                print("output already occupied")
                continue
        self.user_full_board[row][column]='F'

    def bomb_check(self):
        if self.full_board[self.co_ord[0]][self.co_ord[1]]=='X':
            return True
        else:
            return False
    def bomb_board(self):
        while len(self.mines)<7:
            f=random.randint(1,6)
            g=random.randint(1,6)
            if self.full_board[f][g]==' ':
                self.full_board[f][g]='X'
                self.mines.append("X")
            else:
                continue
    def set_numbers(self):
        for i in range(1,6):
                      
                for j in range(1,6):
                    
                    if self.full_board[i][j]=='X':
                        continue
                    elif i==1 and j==1:
                        corner=[self.full_board[1][2],self.full_board[2][2],self.full_board[2][1]]
                        a=corner.count('X')
                        self.full_board[i][j]=str(a)
                    elif i==1 and j==5:
                        corner=[self.full_board[1][4],self.full_board[2][4],self.full_board[2][5]]
                        d=corner.count('X')
                        self.full_board[i][j]=str(d)
                    elif i==5 and j==1:
                        corner=[self.full_board[5][2],self.full_board[4][1],self.full_board[4][2]]
                        e=corner.count('X')
                        self.full_board[i][j]=str(e)
                    elif i==5 and j==5:
                        corner=[self.full_board[4][4],self.full_board[4][5],self.full_board[5][4]]
                        h=corner.count('X')
                        self.full_board[i][j]=str(h)
                    elif i==1:
                        corner=[self.full_board[i][j-1],self.full_board[i][j+1],self.full_board[i+1][j+1],self.full_board[i+1][j],self.full_board[i+1][j-1]]
                        b=corner.count('X')
                        self.full_board[i][j]=str(b)
                    elif j==1:
                        corner=[self.full_board[i][j+1],self.full_board[i+1][j+1],self.full_board[i+1][j],self.full_board[i-1][j],self.full_board[i-1][j+1]]
                        c=corner.count('X')
                        self.full_board[i][j]=str(c)
                    elif j==5:
                        corner=[self.full_board[i-1][j-1],self.full_board[i-1][j],self.full_board[i][j-1],self.full_board[i+1][j-1],self.full_board[i+1][j]]
                        x=corner.count('X')
                        self.full_board[i][j]=str(x)
                    elif i==5:
                        corner=[self.full_board[i][j-1],self.full_board[i-1][j-1],self.full_board[i-1][j],self.full_board[i-1][j+1],self.full_board[i][j+1]]
                        y=corner.count('X')
                        self.full_board[i][j]=str(y)
                    else:
                        corner=[self.full_board[i-1][j],self.full_board[i-1][j-1],self.full_board[i-1][j+1],self.full_board[i][j-1],self.full_board[i][j+1],self.full_board[i+1][j-1],self.full_board[i+1][j],self.full_board[i+1][j+1]]
                        z=corner.count('X')
                        self.full_board[i][j]=str(z)
print ("welcome to minesweeper")
           
while True:
    while True:
        vg=input("are you ready to play minesweeper(y/n):")
        if vg.lower() in ['y','n']:
            break
        else:
            continue
    if vg.lower()=='n':
        continue

    ok=0
    a=minesweeper()
    a.bomb_board()
    a.set_numbers()
    a.user_board()
    while True:
        if a.check_win()==True:
            print ("Congrats you won the game")
            break
        while True:
            vl=input("do you want to place a marker(y/n):")
            if vl.lower() in ['y','n']:
                break
            else:
                continue
        if vl.lower()=='y':
            a.input_user()
            a.user_board()
            if a.bomb_check()==True:
                print('\n')
                print("you lost the game")
                print("this is the board")
                print('\n')
                a.show_board()
                break
        if ok==7:
            continue
        else:
             while True:
                 zl=input("do you want to place flag(y/n):")
                 if zl.lower() in ['y','n']:
                    break
                 else:
                    continue
             if zl.lower()=='y':
                 a.place_flag()
                 a.user_board()
                 ok=ok+1
             else:
                 ok=ok+0
    while True:
        bm=input("do you want to continue(y/n):")
        if bm.lower() in ['y','n']:
            break
        else:
            continue
    if bm.lower()=='y':
        continue
    else:
        break
