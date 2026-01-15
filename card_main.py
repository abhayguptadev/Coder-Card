import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont

# ------------------ ROUND CORNER FUNCTION ------------------
def round_corners(image, radius):
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0) + image.size, radius=radius, fill=255)
    rounded = Image.new("RGBA", image.size)
    rounded.paste(image, (0, 0), mask=mask)
    return rounded

# ------------------ SETUP ------------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")
app = ctk.CTk()
app.geometry("900x900")
app.title("Coder Card")
app.resizable(False, False)

# ------------------ MAIN FRAME ------------------
frame = ctk.CTkFrame(app, corner_radius=50, width=880, height=800)
frame.pack_propagate(False)
frame.pack(pady=15)

# ------------------ BACKGROUND IMAGE ------------------
bg_img = Image.open(r"D:\My_Doc\Python\CustomTkinter\Coder Card\background.jpg").resize((900, 900))
rounded_base0 = round_corners(bg_img, radius=20)
ctk_img0 = ctk.CTkImage(light_image=rounded_base0 , size=(900,900))

bg_label = ctk.CTkLabel(frame, image=ctk_img0, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ------------------ FRAMES ON TOP (unchanged size/properties) ------------------
frame1 = ctk.CTkFrame(frame, width=400, height=500, bg_color="white")
frame1.pack_propagate(False)
frame1.pack(pady=(50, 50), padx=(0, 25), side="right")

frame2 = ctk.CTkFrame(frame, width=400, height=500,bg_color="transparent")
frame2.pack_propagate(False)
frame2.pack(pady=(50, 50), padx=(25, 0), side="left")

# ------------------ IMAGE LOAD ------------------
base_image = Image.open(r"D:\My_Doc\Python\CustomTkinter\Coder Card\image.jpg").resize((360, 300))
rounded_base = round_corners(base_image, radius=30)
ctk_img = ctk.CTkImage(light_image=rounded_base, size=(360, 300))

label_img = ctk.CTkLabel(frame2, image=ctk_img, text="")
label_img.pack(pady=20)

# ------------------ ENTRY FIELDS ------------------
frame3 = ctk.CTkFrame(frame1, corner_radius=20, fg_color="black")
frame3.pack(pady=40, padx=10, fill="x")

label1 = ctk.CTkLabel(frame3, text="Make Your Coder Card", font=("Arial", 30, "bold"), text_color="light blue")
label1.pack(pady=5)

labelname = ctk.CTkLabel(frame1, text="Name", font=("Arial", 25, "bold"), anchor="w")
labelname.pack(pady=(20, 2), padx=10, fill="x")

entry_name = ctk.CTkEntry(frame1, placeholder_text="Enter Name", width=250)
entry_name.pack(pady=5, padx=10, fill="x")

labelname = ctk.CTkLabel(frame1, text="Work", font=("Arial", 25, "bold"), anchor="w")
labelname.pack(pady=(10, 2), padx=10, fill="x")

entry_work = ctk.CTkEntry(frame1, placeholder_text="Enter Work", width=250)
entry_work.pack(pady=5, padx=10, fill="x")

labelname = ctk.CTkLabel(frame1, text="Contact", font=("Arial", 25, "bold"), anchor="w")
labelname.pack(pady=(10, 2), padx=10, fill="x")

entry_contact = ctk.CTkEntry(frame1, placeholder_text="Enter Gmail Contact", width=250)
entry_contact.pack(pady=5, padx=10, fill="x")

# ------------------ UPDATE FUNCTION ------------------
def update_image(event=None):
    name = entry_name.get()
    work = entry_work.get()
    contact = entry_contact.get()

    # Copy and draw on rounded image
    img_copy = rounded_base.copy()
    draw = ImageDraw.Draw(img_copy)

    # Load fonts
    try:
        font_name = ImageFont.truetype("C:\\Windows\\Fonts\\COPRGTB.TTF", 30)  # Copperplate Gothic Bold
        font_work = ImageFont.truetype("C:\\Windows\\Fonts\\ENGR.TTF", 18)   # Engravers MT
        font_contact = ImageFont.truetype("C:\\Windows\\Fonts\\BELL.TTF", 18)
    except IOError:
        font_name = ImageFont.load_default()
        font_work = ImageFont.load_default()
        font_contact = ImageFont.load_default()

    # Draw text
    draw.text((50, 170), name, font=font_name, fill="black")
    draw.text((40, 210), work, font=font_work, fill="black")
    draw.text((160, 10), contact, font=font_contact, fill="black")

    updated_ctk_img = ctk.CTkImage(light_image=img_copy, size=(360, 300))
    label_img.configure(image=updated_ctk_img)
    label_img.image = updated_ctk_img
    label_img.img_copy = img_copy  # for saving

# ------------------ SAVE FUNCTION ------------------
def save_image():
    if hasattr(label_img, "img_copy"):
        img_to_save = label_img.img_copy.convert("RGB")
        img_to_save.save("coder_card.jpg")
        messagebox.showinfo("Save Image", "Your Coder Card Saved! File Name: coder_card.jpg")
        print("✅ Visiting card saved as coder_card.jpg")

# ------------------ EVENTS ------------------
entry_name.bind("<KeyRelease>", update_image)
entry_work.bind("<KeyRelease>", update_image)
entry_contact.bind("<KeyRelease>", update_image)

# ------------------ SAVE BUTTON ------------------
save_btn = ctk.CTkButton(frame2, text="Save Your Card", font=("Arial", 16, "bold"),
                         command=save_image, hover_color="light blue", text_color="black")
save_btn.pack(pady=10, padx=10, fill="x")

# ------------------ RUN ------------------
app.mainloop()