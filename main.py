from customtkinter import CTk, set_appearance_mode, set_default_color_theme, CTkLabel, CTkFrame, CTkButton, \
    CTkCheckBox

from functions import generete


def main():
    root = CTk()
    set_appearance_mode("light")
    set_default_color_theme("dark-blue")
    w = 700
    h = 850
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - w) // 2
    y = (screen_height - h) // 2
    root.geometry(f"{w}x{h}+{x}+{y}")
    root.update_idletasks()

    lab_data = CTkLabel(root, text="Введіть попередні дані про автомобіль", font=("helvetica", 12))
    lab_data.grid(row=0, column=0, pady=(30, 0), padx=(35, 0), sticky="nw")

    frame = CTkFrame(root, border_width=1)
    frame.grid(row=1, column=0, pady=(0, 0), padx=(30, 0), sticky="nw")

    nw_check = CTkCheckBox(frame, text="новий автомобіль")
    nw_check.grid(row=0, column=0, pady=(20, 20), padx=(20, 60))
    od_check = CTkCheckBox(frame, text="іноземного виробництва")
    od_check.grid(row=1, column=0, pady=(0, 20), padx=(20, 20))

    btn = CTkButton(root, text="Основні питання", border_color="grey", fg_color="white", text_color="grey",
                    border_width=1, hover_color="#A9A9A9", command=lambda: generete(root, nw_check, btn, od_check))
    btn.grid(row=1, column=1, rowspan=2, padx=(100, 20), pady=(40, 20), sticky="ne")

    root.mainloop()


if __name__ == "__main__":
    main()
