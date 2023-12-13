from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
from camera_display_frame_v1 import CameraDisplay  # Import the CameraDisplay class from the other file


class Feedback:
    default_text_latitude = "Enter the latitude"
    default_text_longitude = "Enter the longitude"
    default_text_altitude = "Enter the altitude"

    def __init__(self, master):
        self.master=master
        #Level 0 Configuration
        master.title("SPxY Observation Interface")
        master.resizable(False,False)
        #master.configure(background='#add8e6')

        self.style=ttk.Style()
        #self.style.configure('TFrame',background ='#add8e6')
        #self.style.configure('TButton',background ='#add8e6')
        #self.style.configure('TLabel',background ='#add8e6')
        self.style.configure('TLabel',font=('Arial',10))

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
        
        #Level 1 Master Frame division
        self.selection_frame = ttk.Frame(master)
        self.selection_frame.grid(row =0, column =0,pady=5)
        self.command_frame=ttk.Frame(master)
        self.command_frame.grid(row =1, column =0,pady=5)
        self.display_frame=ttk.Frame(master)
        self.display_frame.grid(row =0, column =1, rowspan=2,pady=5)

        #Level 2 selection_Frame organisation
        original_image = Image.open('C:\\Users\\rayen\\OneDrive\\Bureau\\EST\\GUI design\\Chess_mission_logo.png') # Open and convert PNG image to Tkinter-compatible format
        resized_image = original_image.resize((original_image.width // 10, original_image.height // 10)) # Resize the image to achieve subsampling effect
        self.chess_logo = ImageTk.PhotoImage(resized_image) # Convert the resized image to a Tkinter-compatible format
        
        TLE = StringVar()
        TLE_selection = ttk.Combobox(self.selection_frame, textvariable = TLE)
        TLE_selection.config(values = ('TLE1', 'TLE2', 'TLE3'))
        
        Mode = StringVar()
        Mode_selection = ttk.Combobox(self.selection_frame, textvariable = Mode)
        Mode_selection.config(values = ('Mode1', 'Mode2', 'Mode3'))
        
        ttk.Label(self.selection_frame, image=self.chess_logo).grid(row=0,padx=5,pady=10,sticky='SE')
        ttk.Label(self.selection_frame, text= "TLE selection").grid(row=1,padx=5,pady=(5,0))
        TLE_selection.grid(row=2,padx=5,pady=(0,10))
        ttk.Label(self.selection_frame, text="Mode selection").grid(row=3,padx=5,pady=(5,0))
        Mode_selection.grid(row=4,padx=5,pady=(0,10))

        #Level 2 command_Frame organisation
        Track_antenna = ttk.Button(self.command_frame, text = "Track satellite",command= self.tracking_message)
        Latitude = ttk.Entry(self.command_frame, width = 20)
        Latitude.insert(0, self.default_text_latitude)
            # Bind the function to the <FocusIn> event
        Latitude.bind('<FocusIn>', lambda event: clear_default_text(event, Latitude, self.default_text_latitude))
        Latitude.bind('<FocusOut>', lambda event: restore_default_text(event, Latitude, self.default_text_latitude))

        Longitude = ttk.Entry(self.command_frame, width = 20)
        Longitude.insert(0, self.default_text_longitude)
        Longitude.bind('<FocusIn>', lambda event: clear_default_text(event, Longitude, self.default_text_longitude))
        Longitude.bind('<FocusOut>', lambda event: restore_default_text(event, Longitude, self.default_text_longitude))

        Altitude = ttk.Entry(self.command_frame, width = 20)
        Altitude.insert(0, self.default_text_altitude)
        Altitude.bind('<FocusIn>', lambda event: clear_default_text(event, Altitude, self.default_text_altitude))
        Altitude.bind('<FocusOut>', lambda event: restore_default_text(event, Altitude, self.default_text_altitude))

         # Function to clear default text on focus
        def clear_default_text(event, entry_widget, default_text):
            current_text = entry_widget.get()
            if current_text == default_text :
                entry_widget.delete(0, 'end')
        def restore_default_text(event, entry_widget, default_text):
            current_text = entry_widget.get()
            if not current_text:
                entry_widget.insert(0, default_text)

        Move_to_position = ttk.Button(self.command_frame, text = "Move to indicated position",command= self.moving_message)

        Stop = ttk.Button(self.command_frame, text = "!! EMERGENCY STOP !!",command= self.emergency_message)

        Track_antenna.grid(row=0, columnspan=3,pady=(10,10))
        ttk.Label(self.command_frame, text="Latitude").grid(row=1,column=0,pady=(10,0))
        Latitude.grid(row=2,column=0,padx=5,pady=(0,10))
        ttk.Label(self.command_frame, text="Longitude").grid(row=1,column=1,pady=(10,0))
        Longitude.grid(row=2,column=1,padx=5,pady=(0,10))
        ttk.Label(self.command_frame, text="Altitude").grid(row=1,column=2,pady=(10,0))
        Altitude.grid(row=2,column=2,padx=5,pady=(0,10))
        Move_to_position.grid(row=3,columnspan=3,pady=(0,10))
        Stop.grid(row=4,columnspan=3,pady=10)

        #Level 2 display_frame organisation
        self.state_frame=ttk.Frame(self.display_frame)
        self.data_display_frame=ttk.Frame(self.display_frame)
        self.graphic_display_frame=ttk.Frame(self.display_frame)
        self.state_frame.grid(row=0,column=0,columnspan=2)
        self.data_display_frame.grid(row=1,column=0)
        self.graphic_display_frame.grid(row=1,column=1)

        #Level 3 state_frame
        ttk.Label(self.state_frame, text="General information:").grid(row=0,column=0,columnspan=2,sticky="w")
            # Add Text widget for information display
        self.general_info_display = Text(self.state_frame, width=100, height=3,font=('Arial',8))
        self.general_info_display.grid(row=1,column=0,columnspan=2, pady=5,sticky="w")

        #Level 3 data_display_frame
        self.general_data_display = Text(self.data_display_frame, width=70, height=3,font=('Arial',8))
        self.signal_data_display = Text(self.data_display_frame, width=70, height=5,font=('Arial',8))
        ttk.Label(self.data_display_frame, text="General data:").grid(row=0,pady=(10,0),sticky="sw")
        self.general_data_display.grid(row=1, pady=5)
        ttk.Label(self.data_display_frame, text="Signal data:").grid(row=2,pady=(10,0),sticky="sw")
        self.signal_data_display.grid(row=3, pady=5)

        #Level 3 graphic_display_frame
        ttk.Label(self.graphic_display_frame, text="Camera display").grid(row=0,padx=100,pady=(10,0))
        ttk.Label(self.graphic_display_frame, text="Model trajectory").grid(row=2,padx=100,pady=(120,0))
        # Button to open the camera display
        open_camera_button = ttk.Button(self.graphic_display_frame, text="Open Camera Display", command=self.open_camera_display)
        open_camera_button.grid(row=1, padx=100, pady=(10, 0))

 ########################################    
    def tracking_message(self):
        messagebox.showinfo("Tracking", "The sattelite is being tracked.")
    def moving_message(self):
        messagebox.showinfo("Moving to position", "The antenna is moving.")
    def emergency_message(self):
        answer=messagebox.askquestion("Emergency", "Are you sure?")
        if answer == 'yes':
            messagebox.showinfo("Emergency Stop", "The antenna is stopped!!") # Stop the antenna and display a message
        else:
            pass # User clicked 'no', do nothing or handle accordingly
    def open_camera_display(self):
        # Instantiate the CameraDisplay class and create a new window
        camera_display_window = Toplevel(self.master)
        camera_display = CameraDisplay(camera_display_window)

def main(): 
    root = Tk()
    feedback= Feedback(root)
    root.mainloop()

if __name__=="__main__": 
    main()
