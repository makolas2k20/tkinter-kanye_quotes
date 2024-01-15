# =============================================================================
# Kanye Quotes from https://kanye.rest/
# Author: Michael Sumaya
# Created as part of Udemy course:
# 100 Days of Code - The Complete Python Pro Bootcamp
# =============================================================================
import requests
from tkinter import *

IMG_BG = "background.png"
IMG_FACE = "kanye.png"
API_URL = "https://api.kanye.rest"
APP_TITLE = "Kanye says..."
MAX_CHAR = 60
FONT_NAME = "Arial"
FONT_BIG = 30
FONT_SMALL = 18
FONT_COLOR = "white"


def get_api_response() -> str:
    response = requests.get(url=API_URL)
    try:
        response.raise_for_status()
    except:
        msg = "I got amnesia. Check back later."
    else:
        msg = response.json()["quote"]
    finally:
        return msg


def get_quote():
    quote = get_api_response()
    if len(quote) <= MAX_CHAR:
        font_size = FONT_BIG
    else:
        font_size = FONT_SMALL
    canvas.itemconfig(
        quote_text,
        text=quote,
        font=(FONT_NAME, font_size, "bold"),
    )


window = Tk()
window.title(APP_TITLE)
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=IMG_BG)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="...my head feels hazy...",
    width=250,
    font=(FONT_NAME, FONT_BIG, "bold"),
    fill=FONT_COLOR,
    justify="center"
)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=IMG_FACE)
kanye_button = Button(
    image=kanye_img,
    highlightthickness=0,
    command=get_quote
)
kanye_button.grid(row=1, column=0)


window.mainloop()
