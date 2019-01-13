from tkinter import *
from PIL import Image, ImageTk
from osgeo import gdal
import numpy as np
import os

root = Tk()

ip_file_text = StringVar()
op_file_text = StringVar()
r_text = StringVar()
g_text = StringVar()
b_text = StringVar()
grayscale_radio_option = IntVar()
input_image_name = None
input_image = None
input_image_preview = None
image_label: Label = None
dataset: gdal.Dataset = None
new_dataset: gdal.Dataset = None

def save():
    # Save the constructed image with op_file_text
    pass


def preview():
    # Construct new image and display
    # new = cv2.resize(original, (800, 600))

    pass


def original():
    # Show the original image
    input_image_name = ip_file_text.get()
    if os.path.isfile(input_image_name):
        dataset: gdal.Dataset = gdal.Open("Junagadhoutput.tif", gdal.GA_ReadOnly)
        if not os.path.isfile("temp_"+input_image_name):
            driver = dataset.GetDriver()
            new_dataset = driver.CreateCopy("temp_"+input_image_name, dataset, strict=0)
        if not os.path.isfile("preview_" + input_image_name[:-3] + ".bmp"):
            # Generate preview
            new = cv2.resize(original, (800, 600))

            pass
        original = Image.open("preview_" + input_image_name[:-3] + ".bmp")
        resized = original.resize((300, 300))
        image = ImageTk.PhotoImage(resized)
        image_label.image = image


if __name__ == "__main__":
    ip_frame = Frame(root)
    ip_frame.pack()
    ip_file_label = Label(ip_frame, text="Input file")
    ip_file_label.pack(side=LEFT)
    ip_file_entry = Entry(ip_frame, bd=5, textvariable=ip_file_text)
    ip_file_entry.pack(side=LEFT)

    op_frame = Frame(root)
    op_frame.pack()
    op_file_label = Label(op_frame, text="Output file")
    op_file_label.pack(side=LEFT)
    op_file_entry = Entry(op_frame, bd=5, textvariable=op_file_text)
    op_file_entry.pack(side=LEFT)

    image_label = Label(root)
    image_label.pack()

    r_frame = Frame(root)
    r_frame.pack()
    r_label = Label(r_frame, text="R:")
    r_label.pack(side=LEFT)
    r_entry = Entry(r_frame, bd=5, textvariable=r_text)
    r_entry.pack(side=LEFT)

    g_frame = Frame(root)
    g_frame.pack()
    g_label = Label(g_frame, text="G:")
    g_label.pack(side=LEFT)
    g_entry = Entry(g_frame, bd=5, textvariable=g_text)
    g_entry.pack(side=LEFT)

    b_frame = Frame(root)
    b_frame.pack()
    b_label = Label(b_frame, text="B:")
    b_label.pack(side=LEFT)
    b_entry = Entry(b_frame, bd=5, textvariable=b_text)
    b_entry.pack(side=LEFT)

    gray_frame = Frame(root)
    gray_frame.pack()
    Radio_label = Label(gray_frame, text="Grayscale ")
    Radio_label.pack(side=LEFT)

    None_radio = Radiobutton(gray_frame, text="None", variable=grayscale_radio_option, value=0)
    None_radio.pack(side=LEFT)
    R_radio = Radiobutton(gray_frame, text="R", variable=grayscale_radio_option, value=1)
    R_radio.pack(side=LEFT)
    B_radio = Radiobutton(gray_frame, text="B", variable=grayscale_radio_option, value=2)
    B_radio.pack(side=LEFT)
    G_radio = Radiobutton(gray_frame, text="G", variable=grayscale_radio_option, value=3)
    G_radio.pack(side=LEFT)
    H_radio = Radiobutton(gray_frame, text="H", variable=grayscale_radio_option, value=4)
    H_radio.pack(side=LEFT)
    S_radio = Radiobutton(gray_frame, text="S", variable=grayscale_radio_option, value=5)
    S_radio.pack(side=LEFT)
    V_radio = Radiobutton(gray_frame, text="V", variable=grayscale_radio_option, value=6)
    V_radio.pack(side=LEFT)

    button_frame = Frame(root)
    button_frame.pack()
    save_button = Button(button_frame, text="Save shit", command=save)
    save_button.pack(side=LEFT)
    preview_button = Button(button_frame, text="Preview shit", command=preview)
    preview_button.pack(side=LEFT)
    original_button = Button(button_frame, text="The original shit", command=original)
    original_button.pack(side=LEFT)

    root.mainloop()
