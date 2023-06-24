from tkinter import *
import random
import ctypes
import sys

class Grid:
    all = []
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.is_empty = True
        self.cell_btn_obj = None
        self.number = None
        self.color = None
        Grid.all.append(self)

    def create_btn_object(self,location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        self.cell_btn_obj = btn
    
    @staticmethod
    def select_num_and_color():
        num_col = [[2,'#6666CD'],
                    [4,'#EEEED2']]
        num = random.sample(num_col,1)
        return num

    @staticmethod
    def initialize():
        i = 0
        index_list = []
        for ind in Grid.all:
            if ind.is_empty == True:
                index_list.append(i)
            i += 1
        if len(index_list) >= 1:
            rand_index = random.sample(index_list,1)
            print(rand_index)
            rand_cell = Grid.all[rand_index[0]]
            rand_cell.is_empty = False
            num_and_color = Grid.select_num_and_color()[0]
            print(num_and_color)
            rand_cell.number = num_and_color[0]
            rand_cell.color = num_and_color[1]
            rand_cell.is_empty = False
            print("random cell == ",rand_cell.x,rand_cell.y)
            rand_cell.cell_btn_obj.configure(
                text = num_and_color[0],
                bg = num_and_color[1]
                )
    @staticmethod
    def bind_event(frame):
        frame.bind('<Key>',Grid.enter)
        frame.focus()
        # frame.pack()
    @staticmethod
    def get_cell_by_coord(x,y):
        for cell in Grid.all:
            if cell.x == x and cell.y == y:
                return cell
    @staticmethod
    def get_cells(col,row):
        cells = []
        if col == -1:
            #get row 
            for cell in Grid.all:
                if cell.y == row and cell.is_empty == False:
                    print("found cell at ",cell.x,cell.y)
                    cells.append(cell)
        if row == -1:
            for cell in Grid.all:
                if cell.x == col and cell.is_empty == False:
                    print('found one cell at ',cell.x,cell.y)
                    print("and the cell is ",cell.is_empty)
                    cells.append(cell)
        return cells

    @staticmethod 
    def all_cell_full():
        for cell in Grid.all:
            if cell.is_empty == True:
                return True
        return False

    @staticmethod
    def move_possible():
        del_x = [0,1,0,-1]
        del_y = [-1,0,1,0]

        for cell in Grid.all:
            x = cell.x
            y = cell.y
            adj_cell = []
            cell_up = Grid.get_cell_by_coord(x+ del_x[0],y + del_y[0])
            cell_right = Grid.get_cell_by_coord(x + del_x[1] , y + del_y[1]) 
            cell_down = Grid.get_cell_by_coord(x + del_x[2], y + del_y[2])
            cell_left = Grid.get_cell_by_coord(x + del_x[3] , y + del_y[3])
            adj_cell = [cell_up,cell_right,cell_down,cell_left]
            for adj in adj_cell:
                if adj is not None:
                    if cell.number == adj.number:
                        return True
        
        return False

    @staticmethod
    def cell_2048():
        for cell in Grid.all:
            if cell.number == 2048:
                return True
        return False

    @staticmethod
    def cell_equal(cell , other_cell):
        other_cell.cell_btn_obj.configure(
            text = cell.number + other_cell.number,
            bg = cell.color
        )
        other_cell.number = other_cell.number + cell.number
        other_cell.color = cell.color
        cell.number = None
        cell.color = None
        cell.is_empty = True
        cell.cell_btn_obj.configure(
            text = "",
            bg = "SystemButtonFace"
        )

    @staticmethod
    def cell_not_equal(cell,other_cell):
        num = cell.number
        color = cell.color
        cell.is_empty = True
        cell.number = None
        cell.color = None
        cell.cell_btn_obj.configure(
            text = "",
            bg = "SystemButtonFace"
        )
        other_cell.number = num
        other_cell.color = color
        other_cell.is_empty = False
        other_cell.cell_btn_obj.configure(
            text = num,
            bg = color
        )

    @staticmethod
    def go_left():
        col = 1
        while col < 4:
            cells = Grid.get_cells(col,-1)
            print("got only ",len(cells), "cells")
            for cell in cells:
                x = cell.x
                y = cell.y
                temp_col = col
                flag = 0
                while temp_col > 0:
                    cell_to_left = Grid.get_cell_by_coord(temp_col-1,y)
                    if cell_to_left.is_empty == False:
                        if cell_to_left.number == cell.number:
                            flag = 1
                            Grid.cell_equal(cell,cell_to_left)
                        break
                    temp_col -= 1
                if flag == 0:
                    cell_to_left = Grid.get_cell_by_coord(temp_col,y)
                    Grid.cell_not_equal(cell,cell_to_left)
                    # print("configuration of cell ",cell_to_left.x,cell_to_left.y,"==",cell_to_left.number,cell_to_left.color)
            col += 1

        if Grid.all_cell_full() and not Grid.move_possible():
            print("game over bitch")
            ctypes.windll.user32.MessageBoxW(0,'Such a loser',0)
            sys.exit()
        else:
            Grid.initialize()

    @staticmethod
    def go_right():
        col = 2
        while col >= 0:
            cells = Grid.get_cells(col,-1)
            print("got only ",len(cells), "cells")
            for cell in cells:
                x = cell.x
                y = cell.y
                temp_col = col
                flag = 0
                while temp_col < 3:
                    cell_to_right = Grid.get_cell_by_coord(temp_col+1,y)
                    if cell_to_right.is_empty == False:
                        if cell_to_right.number == cell.number:
                            flag = 1
                            Grid.cell_equal(cell,cell_to_right)
                        break
                    temp_col += 1
                if flag == 0:
                    cell_to_right = Grid.get_cell_by_coord(temp_col,y)
                    Grid.cell_not_equal(cell,cell_to_right)
            col -= 1
        if Grid.all_cell_full() and not Grid.move_possible():
            print("game over bitch")
            ctypes.windll.user32.MessageBoxW(0,'Such a loser',0)
            sys.exit()
        else:
            Grid.initialize()
    
    @staticmethod
    def go_down():
        row = 2
        while row >= 0:
            cells = Grid.get_cells(-1,row)
            for cell in cells:
                x = cell.x
                y = cell.y
                temp_row = row
                flag = 0
                while temp_row < 3:
                    cell_to_down = Grid.get_cell_by_coord(x,temp_row+1)
                    if cell_to_down.is_empty == False:
                        if cell_to_down.number == cell.number:
                            flag = 1
                            Grid.cell_equal(cell,cell_to_down)
                        break
                    temp_row += 1
                if flag == 0:
                    cell_to_down = Grid.get_cell_by_coord(x,temp_row)
                    Grid.cell_not_equal(cell,cell_to_down)
            row -= 1
        if Grid.all_cell_full() and not Grid.move_possible():
            #print("game over bitch")
            ctypes.windll.user32.MessageBoxW(0,'Such a loser',0)
            sys.exit()
        else:
            Grid.initialize()

    @staticmethod
    def go_up():
        row = 1
        while row < 4:
            cells = Grid.get_cells(-1,row)
            for cell in cells:
                x = cell.x
                y = cell.y
                temp_row = row
                flag = 0
                while temp_row > 0:
                    cell_to_up = Grid.get_cell_by_coord(x,temp_row-1)
                    if cell_to_up.is_empty == False:
                        if cell_to_up.number == cell.number:
                            flag = 1
                            Grid.cell_equal(cell,cell_to_up)
                        break
                    temp_row -= 1
                if flag == 0:
                    cell_to_up = Grid.get_cell_by_coord(x,temp_row)
                    Grid.cell_not_equal(cell,cell_to_up)
            row += 1
        if Grid.all_cell_full() and not Grid.move_possible():
            # print("game over bitch")
            ctypes.windll.user32.MessageBoxW(0,'Such a loser',0)
            sys.exit()
        else:
            Grid.initialize()


    @staticmethod
    def enter(event):

        print("event",event.char)
        if event.char == 'a':
            Grid.go_left()
        if event.char == 's':
            Grid.go_down()
        if event.char == 'w':
            Grid.go_up()
        if event.char == 'd':
            Grid.go_right()
        
        if Grid.cell_2048():
            ctypes.windll.user32.MessageBoxW(0,'We have a winner',0)
        # print('left key preseed')


        
        
