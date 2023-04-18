import tkinter as tk
import numpy as np

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gui Player")

        # play and pause button
        self.play_button = tk.Button(self.root, text="Play", command=self.play_pause)
        self.play_button.pack()

        # volume button
        self.volume_slider = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_slider.pack()

        # Import button
        self.import_button = tk.Button(self.root, text="Import MIDI", command=self.import_button)
        self.import_button.pack()

        # export Button
        self.export_button = tk.Button(self.root, text="Export", command=self.export_button)
        self.export_button.pack()

    def play_pause(self):
        
        pass

    def set_volume(self, volume):
        
        pass

    def import_button(self):
        
        pass

    def export_button(self):
        
        pass  

    def run(self):
        self.root.mainloop()

gui = GUI()
gui.run()

