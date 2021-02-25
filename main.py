from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image, ImageDraw, ImageFont

BG_COLOR = "#1e2022"
FONT_COLOR = "#f0f5f9"
BTN_COLOR = '#52616b'


class WMark:

    def __init__(self):
        # None variables get checked inside functions many times
        self.filename = None
        self.wtm_filename = None
        self.img = None
        self.wtm = None
        self.text = None
        self.text_size = None

        # Window
        window = Tk()
        window.title("WMark 1.1")
        window.resizable(width=True, height=True)
        window.config(bg=BG_COLOR)

        # Logo
        self.label_logo = Label(bg=BG_COLOR)
        logo_img = Image.open('images/logo.png')
        logo_img.thumbnail((350, 350), Image.ANTIALIAS)
        img_logo = ImageTk.PhotoImage(logo_img)
        self.label_logo.image = img_logo
        self.label_logo.configure(image=img_logo)
        self.label_logo.grid(row=0, column=1, rowspan=8, columnspan=3)

        # Panel
        self.panel_img = Label()
        self.panel_wtm = Label(highlightthickness=0)
        self.panel_wtm_text = Label(highlightthickness=0)

        # IMAGE LAYOUT #
        # Image label
        label_img_size = Label(text='Image\nSize', font=('calibre', 10, 'bold'), bg=BG_COLOR, fg=FONT_COLOR)
        label_img_size.grid(row=0, column=1, pady=(3, 3), padx=(3, 3))

        # Image size input
        self.entry_img_size = Entry(justify='center')
        self.entry_img_size.grid(row=0, column=2, sticky="EW", ipady=5, pady=(3, 3), padx=(3, 3))
        self.entry_img_size.insert(END, '20')

        # Open image button
        button_img = Button(text="Open Image", command=self.image_to_open, bg=BTN_COLOR, fg=FONT_COLOR)
        button_img.grid(row=0, column=3, sticky="we", pady=(3, 3), padx=(3, 3), ipady=2)

        # WTM IMG LAYOUT #
        # Watermark image size label
        label_wtm_size = Label(text='Watermark\nSize', font=('calibre', 10, 'bold'), bg=BG_COLOR, fg=FONT_COLOR)
        label_wtm_size.grid(row=1, column=1, pady=(3, 3), padx=(3, 3))

        # Watermark image size input
        self.entry_wtm_size = Entry(justify='center')
        self.entry_wtm_size.grid(row=1, column=2, sticky="EW", ipady=5, pady=(3, 3), padx=(3, 3))
        self.entry_wtm_size.insert(END, '100')

        # Open watermark button
        button_wtm = Button(text="Open Watermark", command=self.open_watermark, bg=BTN_COLOR, fg=FONT_COLOR)
        button_wtm.grid(row=1, column=3, sticky="we", pady=(3, 3), padx=(3, 3), ipady=2)

        # Watermark position labels
        label_pos_x = Label(text='Watermark Pos X', font=('calibre', 10, 'bold'), bg=BG_COLOR, fg=FONT_COLOR)
        label_pos_x.grid(row=2, column=1, pady=(3, 3), padx=(3, 3))
        label_pos_y = Label(text='Watermark Pos Y', font=('calibre', 10, 'bold'), bg=BG_COLOR, fg=FONT_COLOR)
        label_pos_y.grid(row=2, column=2, pady=(3, 3), padx=(3, 3))

        # Watermark position input
        self.entry_wtm_img_x = Entry(justify='center')
        self.entry_wtm_img_x.grid(row=3, column=1, sticky="EW", ipady=5, pady=(3, 3), padx=(3, 3))
        self.entry_wtm_img_x.insert(END, '0')
        self.entry_wtm_img_y = Entry(justify='center')
        self.entry_wtm_img_y.grid(row=3, column=2, sticky="EW", ipady=5, pady=(3, 3), padx=(3, 3))
        self.entry_wtm_img_y.insert(END, '0')

        # Refresh watermark button
        button_update = Button(text="Refresh", command=self.update_screen, bg=BTN_COLOR, fg=FONT_COLOR)
        button_update.grid(row=3, column=3, sticky="we", pady=(3, 3), padx=(3, 3), ipady=2)

        # WATERMARK TEXT LAYOUT #
        # Watermark text labels
        label_wtm_text = Label(text='Watermark Text', font=('calibre', 10, 'bold'), bg=BG_COLOR, fg=FONT_COLOR)
        label_wtm_text.grid(row=4, column=1, pady=(3, 3), padx=(3, 3))

        label_wtm_text_size = Label(text='Text Size', font=('calibre', 10, 'bold'), bg=BG_COLOR, fg=FONT_COLOR)
        label_wtm_text_size.grid(row=4, column=3, pady=(3, 3), padx=(3, 3))

        # Watermark text input
        self.entry_wtm_text = Entry(justify='center')
        self.entry_wtm_text.grid(row=5, column=1, columnspan=2, sticky="EW", ipady=5, pady=(3, 3), padx=(3, 3))

        # Watermark text size input
        self.entry_wtm_text_size = Entry(justify='center')
        self.entry_wtm_text_size.grid(row=5, column=3, sticky="EW", ipady=5, pady=(3, 3), padx=(3, 3))
        self.entry_wtm_text_size.insert(END, '10')

        # Watermark text pos labels
        label_txt_x = Label(text='Text Pos X', font=('calibre', 10, 'bold'), bg=BG_COLOR, fg=FONT_COLOR)
        label_txt_x.grid(row=6, column=1, pady=(3, 3), padx=(3, 3))
        label_txt_y = Label(text='Text Pos Y', font=('calibre', 10, 'bold'), bg=BG_COLOR, fg=FONT_COLOR)
        label_txt_y.grid(row=6, column=2, pady=(3, 3), padx=(3, 3))

        # Watermark text position
        self.entry_wtm_x = Entry(justify='center')
        self.entry_wtm_x.grid(row=7, column=1, sticky="EW", ipady=5, pady=(3, 3), padx=(3, 3))
        self.entry_wtm_x.insert(END, '0')
        self.entry_wtm_y = Entry(width=10, justify='center')
        self.entry_wtm_y.grid(row=7, column=2, sticky="EW", ipady=5, pady=(3, 3), padx=(3, 3))
        self.entry_wtm_y.insert(END, '0')

        # Watermark text button
        button_text = Button(text="Refresh", command=self.watermark_text, bg=BTN_COLOR, fg=FONT_COLOR)
        button_text.grid(row=7, column=3, sticky="we", ipady=2, pady=(3, 3), padx=(3, 3))

        # SAVE BUTTON #
        button_save = Button(text="Save WTMark Image", command=self.save_file, bg=BTN_COLOR, fg=FONT_COLOR)
        button_save.grid(row=8, column=1, columnspan=2, sticky="we", ipady=2, pady=(3, 5), padx=(3, 3))

        # ABOUT POPUP #
        def about_message():
            messagebox.showinfo(
                "WMark v1.1", "This app can open your image, add and paste watermark in it. "
                              "Watermark can be image or/and text. Can save just png format.\n\n"
                              "Version 1.0 - Can add watermark to image save it\n"
                              "Version 1.1 - Added text option for watermark.\n\n"
                              "If you input text as a watermark, make sure image size is 100%\n")

        button_about = Button(text="About", command=about_message, bg=BTN_COLOR, fg=FONT_COLOR)
        button_about.grid(row=8, column=3, sticky="we", ipady=2, pady=(3, 5), padx=(3, 3))

        window.mainloop()

    def image_filename(self):
        self.filename = filedialog.askopenfilename(title='Open Image')
        return self.filename

    def image_to_open(self):
        file = self.image_filename()
        self.open_image(file)

    # Opens image in new label
    def open_image(self, file):
        try:
            self.filename = file
            img_open = Image.open(self.filename)
            self.img = img_open

            # Resize image and show it in label
            img_size = float(self.entry_img_size.get())
            img_resize = self.img.resize((round(self.img.width * img_size / 100),
                                          round(self.img.height * img_size / 100)),
                                         Image.ANTIALIAS)
            img_tk = ImageTk.PhotoImage(img_resize)
            self.panel_img.image = img_tk
            self.panel_img.configure(image=img_tk)
            self.panel_img.grid(row=0, column=0, rowspan=9)
        # If open filedialog and cancel, need pass this error
        except AttributeError:
            pass

    # Opens watermark in new label
    def open_watermark(self):
        try:
            self.wtm_filename = filedialog.askopenfilename(title='Open Watermark Image')
            wtm_open = Image.open(self.wtm_filename)

            # Scaling watermark and paste it in to screen
            self.wtm = wtm_open
            img_size = float(self.entry_img_size.get())
            wtm_size = float(self.entry_wtm_size.get())

            wtm_resize = self.wtm.resize(
                (round(self.wtm.width * img_size / 100 * wtm_size / 100),
                 round(self.wtm.height * img_size / 100 * wtm_size / 100)),
                Image.ANTIALIAS)

            wtm_tk = ImageTk.PhotoImage(wtm_resize)

            self.panel_wtm.image = wtm_tk
            self.panel_wtm.configure(image=wtm_tk)
            self.panel_wtm.place(x=self.entry_wtm_img_x.get(), y=self.entry_wtm_img_y.get())
        # If open filedialog and cancel, need pass this error
        except AttributeError:
            pass

    # Update screen when refresh button is clicked
    def update_screen(self):

        if self.img is not None:
            # Refresh image size
            img_size = float(self.entry_img_size.get())
            img_resize = self.img.resize((round(self.img.width * img_size / 100),
                                          round(self.img.height * img_size / 100)),
                                         Image.ANTIALIAS)
            img_tk = ImageTk.PhotoImage(img_resize)
            self.panel_img.image = img_tk
            self.panel_img.configure(image=img_tk)
            self.panel_img.grid(row=0, column=0, rowspan=9)

        if self.wtm is not None:
            # Refresh watermark position
            self.panel_wtm.place_configure(x=self.entry_wtm_img_x.get(), y=self.entry_wtm_img_y.get())
            # Refresh watermark size
            img_size = float(self.entry_img_size.get())
            wtm_size = float(self.entry_wtm_size.get())

            wtm_resize = self.wtm.resize(
                (round(self.wtm.width * img_size / 100 * wtm_size / 100),
                 round(self.wtm.height * img_size / 100 * wtm_size / 100)),
                Image.ANTIALIAS)

            wtm_tk = ImageTk.PhotoImage(wtm_resize)

            self.panel_wtm.image = wtm_tk
            self.panel_wtm.configure(image=wtm_tk)
            self.panel_wtm.place(x=self.entry_wtm_img_x.get(), y=self.entry_wtm_img_y.get())

    # Get watermark text input and place it in screen
    def watermark_text(self):
        self.text = self.entry_wtm_text.get()
        if self.text is not None:
            image_size = int(self.entry_img_size.get())
            text_size = int(self.entry_wtm_text_size.get())
            self.text_size = round(text_size * (image_size / 100))
            self.panel_wtm_text.config(text=self.text, font=('arial', round(self.text_size), 'bold'))
            self.panel_wtm_text.place(x=self.entry_wtm_x.get(), y=self.entry_wtm_y.get())

    # Save new WTMark file
    def save_file(self):
        # If we have open image
        if self.filename is not None:
            img_to_save = Image.open(self.filename).convert("RGBA")

            # If we have open watermark image
            if self.wtm_filename is not None:
                wtm_to_save = Image.open(self.wtm_filename).convert("RGBA")

                # Get watermark coordinates and size
                wtm_pos_x = int(self.entry_wtm_img_x.get())
                wtm_pos_y = int(self.entry_wtm_img_y.get())
                wtm_size = int(self.entry_wtm_size.get())
                img_size = int(self.entry_img_size.get())
                coord = 100 / img_size
                new_wtm_size = wtm_size / 100

                # Resize watermark image to right scale
                resize_wtm = wtm_to_save.resize(
                    (round(wtm_to_save.width * new_wtm_size), round(wtm_to_save.height * new_wtm_size)),
                    Image.ANTIALIAS)

                # Paste watermark in to image
                img_to_save.paste(resize_wtm, (round(wtm_pos_x * coord), round(wtm_pos_y * coord)), mask=resize_wtm)

            # If we have watermark text in screen
            if self.text is not None:
                # Get text coordinates ans size, and try to scale it right size
                text_pos_x = int(self.entry_wtm_x.get())
                text_pos_y = int(self.entry_wtm_y.get())
                img_size = int(self.entry_img_size.get())
                text_coord = 100 / img_size

                # Draw text in to image
                draw = ImageDraw.Draw(img_to_save)
                text = self.text
                font_size = round(self.text_size)
                font = ImageFont.truetype('arial.ttf', font_size)

                img_fraction = 0.85
                while font.getsize(text)[0] > img_fraction * img_to_save.size[0] * (img_size / 100):
                    font_size -= 1
                    font = ImageFont.truetype('arial.ttf', font_size)

                draw.text((round(text_pos_x * text_coord), round(text_pos_y * text_coord)), text, font=font)

            # Save image with watermark image and/or text
            save_path = filedialog.asksaveasfilename(title='Save image as', defaultextension='.png',
                                                     filetypes=[("png files", '*.png')])
            try:
                img_to_save.save(save_path, format='png')
            # If open filedialog and cancel, need pass this error
            except FileNotFoundError:
                pass
            else:
                self.open_image(save_path)
                self.panel_wtm.destroy()
                self.panel_wtm_text.destroy()
                self.panel_wtm = Label(highlightthickness=0)
                self.panel_wtm_text = Label(highlightthickness=0)


if __name__ == '__main__':
    WMark()
