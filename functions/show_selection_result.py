

def show_selection_result(selected_value, cars_value_selected, engine_selected, continent_selected,
                          engine_selected_type, entr, color_combo_box, nw_check):
    if nw_check.get() == 0:
        selection_text = (f"Скільки років: {selected_value.get()}\n Марка автомобіля: {cars_value_selected.get()}\n"
                          f" Об'єм двигуна: {engine_selected.get()}\n Континент виробника: {continent_selected.get()}"
                          f"\n Тип двигуна: {engine_selected_type.get()}\n Колір: {color_combo_box.get()}")
        entr.delete(0, 'end')
        entr.insert(0, selection_text)
    else:
        selection_text = (
            f"Стан авто: новий автомобіль\n Марка автомобіля: {cars_value_selected.get()}\n"
            f" Об'єм двигуна: {engine_selected.get()}\n"
            f" Континент виробника: {continent_selected.get()}\n "
            f"Тип двигуна: {engine_selected_type.get()}"
            f"\n Колір: {color_combo_box.get()}")
        entr.delete(0, 'end')
        entr.insert(0, selection_text)
