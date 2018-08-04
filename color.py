from tkinter import *
import time

root = Tk()
c = Canvas(root, width=1200, height=700, bg='white')
c.pack()

def begin():
    c.delete("all")
    beginning = c.create_text(600,350, font=('arial', '50'), text='Press SPACE To Start', fill='black')

    def start(event):
        nonlocal beginning
        
        player = c.create_rectangle(5, 650, 55, 600, fill='black', outline='white')
        ground = c.create_rectangle(0, 710, 1200, 650, fill='green', outline='black')

        root.unbind('<space>')
        c.delete(beginning)

        alive = True
        right, left, up = False, False, False

       
        def right_down(event):
            nonlocal right
            right = True
            
        def right_s(event):
            nonlocal right
            right = False
            
        def left_down(event):
            nonlocal left
            left = True
            
        def left_s(event):
            nonlocal left
            left = False
            
        def jump(event):
            nonlocal up
            up = True

        def jump_s(event):
            nonlocal up
            up = False
            
            

        root.bind('<KeyPress-Right>', right_down)
        root.bind('<KeyRelease-Right>', right_s)
        root.bind('<KeyPress-Left>', left_down)
        root.bind('<KeyRelease-Left>', left_s)
        root.bind('<space>', jump)
        root.bind('<KeyRelease-space>', jump_s)

        right_down(event)
        right_s(event)
        left_down(event)
        left_s(event)
        jump(event)
        jump_s(event)

        floor_move_right = c.create_rectangle(0, 710, 1200, 650, fill='blue', outline='black')
        floor_move_left = c.create_rectangle(0, 710, 1200, 650, fill='green', outline='black')
        cloud_1 = c.create_rectangle(180, 20, 280, 50, fill='grey', outline='black')
        cloud_2 = c.create_rectangle(420, 20, 520, 50, fill='grey', outline='black')
        cloud_3 = c.create_rectangle(780, 20, 880, 50, fill='grey', outline='black')
        
        cloud_4 = c.create_rectangle(140, 80, 240, 110, fill='grey', outline='black')
        cloud_5 = c.create_rectangle(420, 80, 520, 110, fill='grey', outline='black')
        cloud_6 = c.create_rectangle(740, 80, 840, 110, fill='grey', outline='black')
        
        cloud_7 = c.create_rectangle(140, 160, 240, 190, fill='grey', outline='black')
        cloud_8 = c.create_rectangle(420, 160, 520, 190, fill='grey', outline='black')
        cloud_9 = c.create_rectangle(740, 160, 840, 190, fill='grey', outline='black')
        
        clouds = [cloud_1, cloud_2, cloud_3, cloud_4, cloud_5, cloud_6, cloud_7, cloud_8, cloud_9]
        
        block = c.create_rectangle(1190, 630, 1200, 640, fill='black', outline='black', state='hidden')
        init_block_coords = c.find_overlapping(c.coords(block)[0],c.coords(block)[1],c.coords(block)[2],c.coords(block)[3])

        death_time = 0

        block_left = True
        
        while alive:
            play_time = time.clock()
            elapsed = play_time - death_time
            f = c.find_overlapping(c.coords(player)[0],c.coords(player)[1],c.coords(player)[2],c.coords(player)[3])
            if elapsed > 2:
                current_block_coords = c.find_overlapping(c.coords(block)[0],c.coords(block)[1],c.coords(block)[2],c.coords(block)[3])
                c.itemconfig(block, state='normal')
                
                for i in current_block_coords:
                    for g in f:
                        if g == i:
                            alive = False
                c.update()
                
                if block_left:
                    if c.coords(block)[0] <= 100:
                        block_left = False
                    else:
                        c.move(block, -8, 0)
                else:
                    if c.coords(block)[0] >= 1100:
                        block_left = True
                    else:
                        c.move(block, 8, 0)
                
            if right and c.coords(player)[0] <=780:
                c.move(player, 3, 0)
                c.delete(ground)
                c.itemconfig(floor_move_right, state='normal')
                c.itemconfig(floor_move_left, state='hidden')

            if right and c.coords(player)[0] >=700:
                for cloud in clouds:
                    c.move(cloud, 2, 0)
                    if c.coords(cloud)[2] >=900:
                        c.move(cloud, -800, 0)
                        c.update()
                
            if left and c.coords(player)[2] >=25:
                c.move(player, -3, 0)
                c.itemconfig(floor_move_left, state='normal')
                c.itemconfig(floor_move_right, state='hidden')
                c.delete(ground)
            if up and c.coords(player)[1] >= 300:
                if right:
                    time.sleep(.05)
                    c.move(player, 35, -50)
                    c.update()
                    time.sleep(.05)
                    c.move(player, 30, -95)
                    c.update()
                    time.sleep(.05)
                    c.move(player, 40, 10)
                    c.update()
                    time.sleep(.1)
                    c.move(player, 0, 135)
                    time.sleep(.05)
                    c.update()
                    
                if left:
                    time.sleep(.05)
                    c.move(player, -35, -50)
                    c.update()
                    time.sleep(.05)
                    c.move(player, -30, -95)
                    c.update()
                    time.sleep(.05)
                    c.move(player, -40, 10)
                    c.update()
                    time.sleep(.1)
                    c.move(player, 0, 135)
                    time.sleep(.05)
                    c.update()
                
            c.update()

        def play_again(event):
            nonlocal elapsed
            death_time = time.clock() - elapsed
            c.delete("all")
            begin()

        if alive == False:
            c.create_text(600,350, font=('arial', '50'), text='Press "R" to restart', fill='black')
            root.bind('<r>', play_again)
            
    root.bind('<space>', start)


begin()
root.mainloop()
