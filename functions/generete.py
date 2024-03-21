from customtkinter import CTkFrame, StringVar, CTkRadioButton, CTkLabel, CTkComboBox, CTkButton, CTkEntry

from functions import show_selection_result, save_configuration, new_survey


def generete(root, nw_check, btn, od_check):
    btn.configure(state="disabled")
    nw_check.configure(state="disabled")
    od_check.configure(state="disabled")
    if nw_check.get() == 1:
        how_old_lab = CTkLabel(root, text="Скільки років")
        how_old_lab.grid(row=2, column=0, pady=(30, 0), padx=(35, 0), sticky="nw")
        frame1 = CTkFrame(root, border_width=1)
        frame1.grid(row=3, column=0, pady=(0, 0), padx=(30, 0), sticky="nw")

        selected_value = StringVar()
        values = ["до 5 років", "6-10 років", "11-15 років", "більше 15 років"]

        five_years = CTkRadioButton(frame1, text=values[0], variable=selected_value, value=values[0], state="disabled")
        five_years.grid(row=0, column=0, padx=(20, 40), pady=(20, 10))

        six_to_ten = CTkRadioButton(frame1, text=values[1], variable=selected_value, value=values[1], state="disabled")
        six_to_ten.grid(row=1, column=0, padx=(20, 40), pady=(0, 10))

        eleven_to_fifteen = CTkRadioButton(frame1, text=values[2], variable=selected_value, value=values[2],
                                           state="disabled")
        eleven_to_fifteen.grid(row=2, column=0, padx=(20, 40), pady=(0, 10))

        more_than_fifteen = CTkRadioButton(frame1, text=values[3], variable=selected_value, value=values[3],
                                           state="disabled")
        more_than_fifteen.grid(row=3, column=0, padx=(20, 20), pady=(0, 20))
    else:
        how_old_lab = CTkLabel(root, text="Скільки років")
        how_old_lab.grid(row=2, column=0, pady=(30, 0), padx=(35, 0), sticky="nw")
        frame1 = CTkFrame(root, border_width=1)
        frame1.grid(row=3, column=0, pady=(0, 0), padx=(30, 0), sticky="nw")

        selected_value = StringVar()
        values = ["до 5 років", "6-10 років", "11-15 років", "більше 15 років"]

        five_years = CTkRadioButton(frame1, text=values[0], variable=selected_value, value=values[0])
        five_years.grid(row=0, column=0, padx=(20, 40), pady=(20, 10))

        six_to_ten = CTkRadioButton(frame1, text=values[1], variable=selected_value, value=values[1])
        six_to_ten.grid(row=1, column=0, padx=(20, 40), pady=(0, 10))

        eleven_to_fifteen = CTkRadioButton(frame1, text=values[2], variable=selected_value, value=values[2])
        eleven_to_fifteen.grid(row=2, column=0, padx=(20, 40), pady=(0, 10))

        more_than_fifteen = CTkRadioButton(frame1, text=values[3], variable=selected_value, value=values[3])
        more_than_fifteen.grid(row=3, column=0, padx=(20, 20), pady=(0, 20))
    car_brands_lab = CTkLabel(root, text="Марки автомобілів")
    car_brands_lab.grid(row=2, column=1, pady=(30, 0), padx=(0, 0), sticky="nw")
    cars = ["BMW", "Mersedes", "Wolcsvagen", "Mazda", "Audi"]
    car_brands_frame = CTkFrame(root, border_width=1)
    car_brands_frame.grid(row=3, column=1, pady=(0, 0), padx=(0, 0), sticky="nw")
    cars_value_selected = StringVar()
    for index, car in enumerate(cars):
        CTkRadioButton(car_brands_frame, text=car, variable=cars_value_selected, value=car).grid(row=index,
                                                                                                 column=0,
                                                                                                 padx=(20, 20),
                                                                                                 pady=(5, 5))
    engine_volume_lab = CTkLabel(root, text="Об'єм двигуна")
    engine_volume_lab.grid(row=2, column=2, pady=(30, 0), padx=(0, 0), sticky="nw")
    engine_volume_frame = CTkFrame(root, border_width=1)
    engine_volume_frame.grid(row=3, column=2, pady=(0, 0), padx=(0, 0), sticky="nw")
    engine_values = ["1.0L", "1.5L", "2.0L", "2.5L"]
    engine_selected = StringVar()
    for index, engine in enumerate(engine_values):
        CTkRadioButton(engine_volume_frame, text=engine, variable=engine_selected, value=engine).grid(row=index,
                                                                                                      column=0,
                                                                                                      padx=(20, 20),
                                                                                                      pady=(5, 5))
    manufacturer_continent_lab = CTkLabel(root, text="Континент виробника")
    manufacturer_continent_lab.grid(row=4, column=0, pady=(30, 0), padx=(35, 0), sticky="nw")
    manufacturer_continent_frame = CTkFrame(root, border_width=1)
    manufacturer_continent_frame.grid(row=5, column=0, pady=(0, 30), padx=(30, 0), sticky="nw")
    continents = ["Зх. Європа", "Сх. Європа", "Азія", "Америка"]
    continent_selected = StringVar()
    for index, continent in enumerate(continents):
        CTkRadioButton(manufacturer_continent_frame, text=continent, variable=continent_selected,
                       value=continent).grid(
            row=index, column=0,
            padx=(20, 20),
            pady=(5, 5))

    engine_type_lab = CTkLabel(root, text="Тип двигуна")
    engine_type_lab.grid(row=4, column=1, pady=(30, 0), padx=(5, 0), sticky="nw")
    engine_type_frame = CTkFrame(root, border_width=1)
    engine_type_frame.grid(row=5, column=1, pady=(0, 30), padx=(0, 0), sticky="nw")
    engine_type = ["Дизель", "Бензин"]
    engine_selected_type = StringVar()
    for index, engine in enumerate(engine_type):
        CTkRadioButton(engine_type_frame, text=engine, variable=engine_selected_type, value=engine).grid(
            row=index, column=0,
            padx=(20, 20),
            pady=(20, 20))

    color_label = CTkLabel(root, text="Колір")
    color_label.grid(row=4, column=2, pady=(30, 0), padx=(5, 0), sticky="nw")

    color_options = {
        "Червоний": "red",
        "Синій": "blue",
        "Зелений": "green",
        "Жовтий": "yellow",
        "Чорний": "black",
        "Білий": "white",
    }

    def update_color(label, options, value):
        color_name = value
        label.configure(text_color=options[color_name], fg_color=options[color_name])

    color_display_label = CTkLabel(root, width=125, height=70, fg_color="red", text_color="red")
    color_display_label.grid(row=5, column=2, pady=(40, 20), padx=(0, 0), sticky="nw")

    color_combo_box = CTkComboBox(root, values=list(color_options.keys()),
                                  command=lambda value: update_color(color_display_label, color_options,
                                                                     value))
    color_combo_box.grid(row=5, column=2, pady=(0, 30), padx=(0, 0), sticky="nw")

    choice_result = CTkLabel(root, text="Результат вибору")
    choice_result.grid(row=6, column=0, pady=(0, 0), padx=(35, 0), sticky="nw")

    entr = CTkEntry(root, height=90)
    entr.grid(row=7, column=0, columnspan=3, pady=(0, 0), padx=(35, 35), sticky="ew")

    result_btn = CTkButton(root, text="Результат вибору", border_color="grey", fg_color="white", text_color="grey",
                           border_width=1, hover_color="#A9A9A9",
                           command=lambda: show_selection_result(selected_value, cars_value_selected, engine_selected,
                                                                 continent_selected, engine_selected_type, entr,
                                                                 color_combo_box, nw_check))
    result_btn.grid(row=8, column=2, pady=(20, 0), padx=(0, 35), sticky="ew")

    save_btn = CTkButton(root, text="Зберегти конфігурацію", border_color="grey", fg_color="white", text_color="grey",
                         border_width=1, hover_color="#A9A9A9",
                         command=lambda: save_configuration(entr))
    save_btn.grid(row=8, column=0, pady=(20, 0), padx=(35, 0), sticky="ew")

    new_survey_btn = CTkButton(root, text="Нове опитування", border_color="grey", fg_color="white", text_color="grey",
                               border_width=1, hover_color="#A9A9A9", command=lambda: new_survey(root))
    new_survey_btn.grid(row=9, column=1, pady=(20, 0), padx=(0, 35), sticky="ew")
