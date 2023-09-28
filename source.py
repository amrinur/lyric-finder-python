from tkinter import *
from tkinter import messagebox, ttk
from lyrics_extractor import SongLyrics
from PIL import Image, ImageTk
import googletrans
import textblob
from datetime import datetime

def get_lyrics():
    try:
        extract_lyrics = SongLyrics("AIzaSyANAlg2YPNGFJAMYs7Ig1jsAomuhEiHFTU", "0666459650d114110")
        
        temp = extract_lyrics.get_lyrics(str(input_user.get()))
        res = temp['lyrics']
        result.insert(END, res)

        # Menyimpan input_user ke dalam file teks username.txt
        username_file = login.username + ".txt"
        with open(username_file, "a") as file:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{current_time}: {input_user.get()}\n")

    except Exception as e:
        messagebox.showerror("Translator", e)

def login():
    # Membuat window baru
    login_window = Tk()

    # Fungsi untuk meng-handle aksi saat tombol "Submit" ditekan
    def submit():
        login.username = username_entry.get()
        if login.username != "":
            # Menutup window login
            login_window.destroy()
            # Menampilkan pesan sukses
            messagebox.showinfo("Login", "Login berhasil!")
        else:
            # Menampilkan pesan error jika username kosong
            messagebox.showerror("Login", "Username tidak boleh kosong!")

    # Membuat label dan entry untuk username
    username_label = Label(login_window, text="Username:")
    username_label.pack()
    username_entry = Entry(login_window)
    username_entry.pack()

    # Membuat tombol "Submit"
    submit_button = Button(login_window, text="Submit", command=submit)
    submit_button.pack()

    # Menjalankan window login
    login_window.mainloop()


def history():
    history_window = Tk()

    try:
        filename = login.username + ".txt"
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        content = "File not found"

    # Membuat label untuk menampilkan konten
    label = Label(history_window, text=content)
    label.pack()

    history_window.mainloop()

def clear():
    result.delete(1.0, END)
    translated_text.delete(1.0, END)

def translate_it():
	# Delete Any Previous Translations
	translated_text.delete(1.0, END)

	try:
		# Get Languages From Dictionary Keys
		# Get the From Langauage Key
		for key, value in languages.items():
			if (value == original_combo.get()):
				from_language_key = key

		# Get the To Language Key
		for key, value in languages.items():
			if (value == translated_combo.get()):
				to_language_key = key

		# Turn Original Text into a TextBlob
		words = textblob.TextBlob(result.get(1.0, END))

		# Translate Text
		words = words.translate(from_lang=from_language_key , to=to_language_key)

		# Output translated text to screen
		translated_text.insert(1.0, words)
		
	except Exception as e:
		messagebox.showerror("Translator", e)

# Grab Language List From GoogleTrans
languages = googletrans.LANGUAGES

# Convert to list
language_list = list(languages.values())
    
# object of tkinter
# and background set to light grey
master = Tk()
master.title("Lyric Finder by Kelompok Petruk")
#master.iconbitmap("unslogo.ico")
master.geometry("1000x600")

# Variable Classes in tkinter
result = StringVar()

# Creating label for each information
# name using widget Label
Label(master, text="Enter Song name:",
       bg = "#282C34", foreground= "#ABB2BF",).place(x= 100, y= 14)


# Creating input user
input_user = Entry(master, width=50)
input_user.place(x= 350, y= 14)

# creating a button using the widget
show = Button(master, text="Show",
		command=get_lyrics, bg="Gold")
show.place(x= 700, y= 14)


# Clear button
clear_button = Button(master, text="Clear", bg="#61AFEF", foreground="#E06C75",
font=("123Marker", 10), command=clear )
clear_button.place(x= 580, y= 530)


#login or signup
log_up= Button(master, text= "Login&SignUp", command=login, bg="Blue")
log_up.place(x= 900, y= 14)

#lyricframe
result_frame = Frame(master)
result_frame.place (x=10, y = 50)
result = Text(result_frame, bg = "#282C34", foreground= "#ABB2BF", 
             font=("Moesubs Sans", 11) , height=26, width=65, wrap=WORD)
result.pack(side=TOP, fill=BOTH)

#translatedframe
translated_text_frame = Frame(master)
translated_text_frame.place (x=510, y = 50)
translated_text = Text(translated_text_frame, bg = "#282C34", foreground= "#ABB2BF", 
                       font=("Moesubs Sans", 11) , height=26, width=65, insertbackground= "white")
translated_text.pack(side=TOP, fill=BOTH)

#translated button
translate_button = Button(master, text="Translate!", bg = "#282C34", foreground= "#ABB2BF",
                          font=("book antiqua", 18,), command=translate_it)
translate_button.place(x= 300, y= 540)

# Combo boxes
original_combo = ttk.Combobox(master, width=20, value=language_list)
original_combo.current(21)
original_combo.place(x= 100, y= 500)

translated_combo = ttk.Combobox(master, width=20, value=language_list)
translated_combo.current(43)
translated_combo.place(x= 600, y= 500)

history_button = Button (master, text= "History", command=history, bg="Red")
history_button.place(x= 850, y= 14)

mainloop()
