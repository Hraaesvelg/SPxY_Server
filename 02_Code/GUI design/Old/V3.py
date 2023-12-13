from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk


class Feedback:
    def __init__(self, master):
        master.title("SPxY Observation Interface")
        master.resizable(False,False)
        #master.configure(background='#add8e6')

        self.style=ttk.Style()
        #self.style.configure('TFrame',background ='#add8e6')
        #self.style.configure('TButton',background ='#add8e6')
        #self.style.configure('TLabel',background ='#add8e6')
        self.style.configure('TLabel',font=('Arial',10))
########################################
        self.selection_frame = ttk.Frame(master)
        self.selection_frame.grid(row =0, column =0 ,rowspan= 3)
        # Open and convert PNG image to Tkinter-compatible format
        original_image = Image.open('C:\\Users\\rayen\\OneDrive\\Bureau\\EST\\GUI design\\Chess_mission_logo.png')
        # Resize the image to achieve subsampling effect
        resized_image = original_image.resize((original_image.width // 10, original_image.height // 10))
        # Convert the resized image to a Tkinter-compatible format
        self.tk_image = ImageTk.PhotoImage(resized_image)
        ttk.Label(self.selection_frame, image=self.tk_image).grid(row=0)

        ttk.Label(self.selection_frame, text= "TLE selection").grid(row=1)
        TLE = StringVar()
        TLE_selection = ttk.Combobox(self.selection_frame, textvariable = TLE)
        TLE_selection.config(values = ('TLE1', 'TLE2', 'TLE3'))
        TLE_selection.grid(row=2,pady=(0,10))
        ttk.Label(self.selection_frame, text="Mode selection").grid(row=3)
        Mode = StringVar()
        Mode_selection = ttk.Combobox(self.selection_frame, textvariable = Mode)
        Mode_selection.config(values = ('Mode1', 'Mode2', 'Mode3'))
        Mode_selection.grid(row=4,pady=(0,10))
########################################
        self.command_frame=ttk.Frame(master)
        self.command_frame.grid(row =3, column =0 ,rowspan= 3)
        Track_antenna = ttk.Button(self.command_frame, text = "Track satellite",command= self.tracking_message)
        Track_antenna.grid(row=0,column=0, columnspan=3,pady=(0,10))

        # Function to clear default text on focus
        def clear_default_text(event, entry_widget, default_text):
            current_text = entry_widget.get()
            if current_text == default_text :
                entry_widget.delete(0, 'end')
        def restore_default_text(event, entry_widget, default_text):
            current_text = entry_widget.get()
            if not current_text:
                entry_widget.insert(0, default_text)
        ttk.Label(self.command_frame, text="Latitude").grid(row=1,column=0)
        Latitude = ttk.Entry(self.command_frame, width = 20)
        Latitude.grid(row=2,column=0,padx=5,pady=(0,10))
        Latitude.insert(0, 'Enter the latitude')
        # Bind the function to the <FocusIn> event
        Latitude.bind('<FocusIn>', lambda event: clear_default_text(event, Latitude, 'Enter the latitude'))
        Latitude.bind('<FocusOut>', lambda event: restore_default_text(event, Latitude, 'Enter the latitude'))

        ttk.Label(self.command_frame, text="Longitude").grid(row=1,column=1)
        Longitude = ttk.Entry(self.command_frame, width = 20)
        Longitude.grid(row=2,column=1,padx=5,pady=(0,10))
        Longitude.insert(0, 'Enter the longitude')
        Longitude.bind('<FocusIn>', lambda event: clear_default_text(event, Longitude, 'Enter the longitude'))
        Longitude.bind('<FocusOut>', lambda event: restore_default_text(event, Longitude, 'Enter the longitude'))

        ttk.Label(self.command_frame, text="Altitude").grid(row=1,column=2)
        Altitude = ttk.Entry(self.command_frame, width = 20)
        Altitude.grid(row=2,column=2,padx=5,pady=(0,10))
        Altitude.insert(0, 'Enter the altitude')
        Altitude.bind('<FocusIn>', lambda event: clear_default_text(event, Altitude, 'Enter the altitude'))
        Altitude.bind('<FocusOut>', lambda event: restore_default_text(event, Altitude, 'Enter the altitude'))

        Move_to_position = ttk.Button(self.command_frame, text = "Move to indicated position",command= self.moving_message)
        Move_to_position.grid(row=3,column=0,columnspan=3,pady=10)

        Stop = ttk.Button(self.command_frame, text = "!! EMERGENCY STOP !!",command= self.emergency_message)
        Stop.grid(row=4,column=0,columnspan=3,pady=10)
########################################
        self.display_frame=ttk.Frame(master)
        self.display_frame.grid(row =0, column =1) #rowspan=6,columnspan= 2
################
        self.state_frame=ttk.Frame(self.display_frame)
        self.state_frame.grid(row=0,column=0,rowspan=1,columnspan=1)
        ttk.Label(self.state_frame, text="General information:").grid(row=0,sticky="sw")
        # Add Text widget for information display
        self.general_info_display = Text(self.state_frame, width=50, height=3,font=('Arial',8))
        self.general_info_display.grid(row=1, padx=10, pady=5)
################
        self.data_display_frame=ttk.Frame(self.display_frame)
        self.data_display_frame.grid(row=1,column=0,rowspan=5,columnspan=1)
        ttk.Label(self.data_display_frame, text="General data:").grid(row=0,column=0,columnspan=2,pady=(10,0),sticky="sw")
        self.general_data_display = Text(self.data_display_frame, width=50, height=3,font=('Arial',8))
        self.general_data_display.grid(row=1, pady=5)
        ttk.Label(self.data_display_frame, text="Signal data:").grid(row=2,column=0,columnspan=2,pady=(10,0),sticky="sw")
        self.signal_data_display = Text(self.data_display_frame, width=70, height=5,font=('Arial',8))
        self.signal_data_display.grid(row=3, pady=5)
        self.graphic_display_frame=ttk.Frame(self.display_frame)
        self.graphic_display_frame.grid(row=0,column=1)
        ttk.Label(self.graphic_display_frame, text="Camera display").grid(row=0,pady=(10,0))
        ttk.Label(self.graphic_display_frame, text="Model trajectory").grid(row=3,pady=(10,0))
 ########################################   

        # Disable tear-off menus in the menubar

        # Create a menubar
        menubar = Menu(master)
        master.config(menu=menubar)

        # Create menu options: File, Edit, Help
        file = Menu(menubar)
        edit = Menu(menubar)
        help_ = Menu(menubar)

        # Add menus to the menubar
        menubar.add_cascade(menu=file, label='File')
        menubar.add_cascade(menu=edit, label='Edit')
        menubar.add_cascade(menu=help_, label='Help')

        # Create menu items under the 'File' menu
        file.add_command(label='New')
        file.add_separator()  # Add a separator line in the menu
        file.add_command(label='Open...')

        # Configure menu items
        file.entryconfig('New', accelerator='Ctrl+N')  # Add an accelerator key
        file.entryconfig('Open...', accelerator='Ctrl+O')  # state='disabled',Disable the 'Open...' menu item

        # Create a cascading menu under 'File'
        save = Menu(file)
        file.add_cascade(menu=save, label='Save')

        # Add options to the 'Save' cascading menu
        save.add_command(label='Save As') #command=lambda: print('Saving As...')
        save.add_command(label='Save All') #command=lambda: print('Saving All...')
        save.entryconfig('Save As',accelerator='Ctrl+Shift+S')
        save.entryconfig('Save All',accelerator='Ctrl+S')

        # Create a variable to store the selected radiobutton choice
        choice = IntVar()

        # Add radiobuttons to the 'Edit' menu
        edit.add_radiobutton(label='One', variable=choice, value=1)
        edit.add_radiobutton(label='Two', variable=choice, value=2)
        edit.add_radiobutton(label='Three', variable=choice, value=3)

 ########################################    
    def tracking_message(self):
        messagebox.showinfo("Tracking", "The sattelite is being tracked.")
    def moving_message(self):
        messagebox.showinfo("Moving to position", "The antenna is moving.")
    def emergency_message(self):
        messagebox.showwarning("Emergency", "The antenna is stopped!!")
def main(): 
    root = Tk()
    feedback= Feedback(root)
    root.mainloop()

if __name__=="__main__": 
    main()
