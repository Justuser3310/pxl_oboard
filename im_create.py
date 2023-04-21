from tkinter import *

####DRAW BLOCK
import requests
from time import sleep
from tqdm import tqdm

def draw(cords):
    for i in tqdm(range(len(cords))):
        sleep(0.2)
        try:
            payload = {'x': cords[i][1], 'y': cords[i][0], 'color': cords[i][2]}
        except:
            payload = {'x': cords[i][1], 'y': cords[i][0], 'color': "b" }
        
        response = requests.post('http://pb.dmcraft.online', data=payload)
        #print(response)
        
        while str(response) != "<Response [200]>":
            response = requests.post('http://pb.dmcraft.online', data=payload)
            print("Error, retrying...")
            #print(response)
    print("!!!DONE!!!")




class PixelArt:

    def __init__(self, master):
        self.master = master
        self.master.title("Pixel Art")
        self.canvas = Canvas(self.master, width=128*12, height=128*12, bg="white")
        self.canvas.pack(side=LEFT, padx=5, pady=5)
        self.colors = ["red", "green", "blue", "white","black"]
        self.current_color = "red"
        self.button_frame = Frame(self.master)
        
        self.button_frame.pack(side=LEFT, padx=5, pady=5)
        self.export_button = Button(self.button_frame, text="Export", command=self.export_image)
        self.export_button.pack(side=TOP, padx=5, pady=5)

        self.button_frame.pack(side=LEFT, padx=5, pady=5)
        self.export_button = Button(self.button_frame, text="Clean", command=self.clean_image)
        self.export_button.pack(side=TOP, padx=5, pady=5)

        self.button_frame.pack(side=LEFT, padx=5, pady=5)
        self.export_button = Button(self.button_frame, text="Upload", command=self.upload_image)
        self.export_button.pack(side=TOP, padx=5, pady=5)

        self.color_buttons = []
        for color in self.colors:
            button = Button(self.button_frame, bg=color, width=3, height=1, command=lambda c=color: self.set_color(c))
            button.pack(side=TOP, padx=5, pady=5)
            self.color_buttons.append(button)
        for i in range(129):
            self.canvas.create_line(i*12, 0, i*12, 128*12, fill="white")
            self.canvas.create_line(0, i*12, 128*12, i*12, fill="white")
        self.canvas.bind("<Button-1>", self.draw_pixel)

    def draw_pixel(self, event):
        x = int(event.x / 12)
        y = int(event.y / 12)
        self.canvas.create_rectangle(x*12, y*12, x*12 + 12, y*12 + 12, fill=self.current_color)

    def set_color(self, color):
        self.current_color = color

    def clean_image(self):
        items = self.canvas.find_all()
        for item in items:
            self.canvas.delete(item)

    def upload_image(self):
        pixel_data = []
        for i in range(128):
            for j in range(128):
                color = self.canvas.itemcget(self.canvas.find_closest(i*12+6, j*12+6), "fill")
                if color != "white":
                    match self.colors.index(color):
                        case 0:
                            color = "red"
                        case 1:
                            color = "green"
                        case 2:
                            color = "blue"
                        case 3:
                            color = "black"
                    pixel_data.append([i, 127-j, color])
        print("!!!START UPLOAD!!!")
        draw(pixel_data)

    def export_image(self):
        pixel_data = []
        for i in range(128):
            for j in range(128):
                color = self.canvas.itemcget(self.canvas.find_closest(i*12+6, j*12+6), "fill")
                if color != "white":
                    match self.colors.index(color):
                        case 0:
                            color = "red"
                        case 1:
                            color = "green"
                        case 2:
                            color = "blue"
                        case 3:
                            color = "black"
                    pixel_data.append([i, 127-j, color])
        f = open('out.txt', 'w')
        f.write(str(pixel_data))
        f.close()

if __name__ == "__main__":
    root = Tk()
    pixel_art = PixelArt(root)
    root.mainloop()
