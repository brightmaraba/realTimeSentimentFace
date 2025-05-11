import customtkinter

from ctk_opencv.ctk.ctk_image_display import CTkImageDisplay


class App(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Sentiment Analysis")
        self.geometry("800x600")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.sentiment_text_var = customtkinter.StringVar(master=self, value="Love")

        self.textbox = customtkinter.CTkEntry(
            master=self,
            corner_radius=10,
            font=("Consolas", 50),
            justify="center",
            placeholder_text="Enter text here...",
            placeholder_text_color="gray",
            textvariable=self.sentiment_text_var,
        )
        self.textbox.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.textbox.focus()

        self.image_display = CTkImageDisplay(self)
        self.image_display.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
