import tkinter as tk
from tkinter import ttk
import streamlit as st
import pandas as pd

# Tytuł aplikacji
st.title("Moja aplikacja z danymi")

# Wprowadzenie
st.write("Tutaj możesz zobaczyć przykładowe dane!")

# Tworzenie tabeli
df = pd.DataFrame({
    "Imię": ["Jan", "Anna", "Piotr"],
    "Wiek": [25, 30, 35],
    "Miasto": ["Warszawa", "Kraków", "Gdańsk"]
})

# Wyświetlenie tabeli
st.table(df)

# Pole do wpisywania tekstu
user_input = st.text_input("Wpisz swoje imię:")
if user_input:
    st.write(f"Witaj, {user_input}!")


# Funkcja do przejścia z ekranu powitalnego do ekranu głównego
def start_main_screen():
    welcome_frame.pack_forget()  # Ukrywa ekran powitalny
    main_screen_frame.pack(fill=tk.BOTH, expand=True)  # Pokazuje ekran główny

# Funkcja do aktualizacji rocznika i pola tekstowego w dolnej części
def update_details():
    selected_registration = registration_combobox.get()
    if selected_registration in car_years:
        year_label.config(text=f"Rocznik auta: {car_years[selected_registration]}")
    else:
        year_label.config(text="Rocznik auta: Brak danych")

    # Aktualizacja tekstu w polu tekstowym
    if selected_registration in car_details:
        details_text.delete(1.0, tk.END)  # Czyszczenie pola tekstowego
        details_text.insert(tk.END, car_details[selected_registration])
    else:
        details_text.delete(1.0, tk.END)
        details_text.insert(tk.END, "Brak danych dla wybranego numeru rejestracyjnego.")

# Funkcja do zaznaczenia wybranego wiersza tabeli
def select_cell(event):
    global selected_item
    selected_item = table.selection()[0]  # Pobierz wybrany element
    selected_values = table.item(selected_item, "values")

    # Ustaw aktualnie wybrane wartości w odpowiednich menu
    route_combobox.set(selected_values[0])
    registration_combobox.set(selected_values[1])
    passenger_combobox.set(selected_values[2])
    time_combobox.set(selected_values[3])  # Nowe menu godziny
    update_details()

# Funkcja do aktualizacji komórki po zmianie wartości w menu
def on_combobox_select(event):
    global selected_item
    # Pobierz dane z menu
    selected_route = route_combobox.get()
    selected_registration = registration_combobox.get()
    selected_passenger_count = passenger_combobox.get()
    selected_time = time_combobox.get()  # Nowe menu godziny

    # Upewnij się, że wszystkie menu mają wybraną wartość
    if selected_route != "Wybierz kierunek" and selected_registration != "Wybierz rejestrację" and selected_passenger_count != "Wybierz ilość pasażerów" and selected_time != "Wybierz godzinę" and selected_item:
        # Zaktualizuj wybraną komórkę w tabeli
        table.item(selected_item, values=(selected_route, selected_registration, selected_passenger_count, selected_time))
        update_details()

# Tworzenie aplikacji
root = tk.Tk()
root.title("Master Premium")
root.geometry("800x800")

# Słownik z numerami rejestracyjnymi i odpowiadającymi rocznikami aut
car_years = {
    "ZS 024MV":2014,
    "ZS 025MV":2014,
    "ZS 078PN":2015,
"ZS 079PN":2015,
"ZS 101UC":2024,
"ZS 102UC":2024,
"ZS 103UC":2024,
"ZS 105MX":2013,
"ZS 180PF":2007,
"ZS 263LU":2015,
"ZS 395MR":2013,
"ZS 396MR":2014,
"ZS 498LM":2013,
"ZS 604PS":2015,
"ZS 607PS":2016,
"ZS 608PS":2015,
"ZS 724NY":2014,
"ZS 736LE":2019,
"ZS 741LE":2019,
"ZS 742LE":2019,
"ZS 745LE":2019,
"ZS 749PM":2015,
"ZS 808HE":2017,
"ZS 845MJ":2013,
"ZS 846MJ":2013,
"ZS 856PP":2006,
"ZS 869MW":2013,
"ZS 871MW":2013,
"ZS 881MX":2014,
"ZS 895PS":2014,
"ZS 912PM":2014,
"ZS 913PM":2014,
"ZS 920NP":2013,
"ZS 974KN":2018,
"ZST 77194":2009,
"ZS716NY":2010,
 
}

# Słownik z numerami rejestracyjnymi i szczegółowymi danymi
car_details = {
    "ZS 024MV": 
"MAN Numer rejestracyjny ZS024MV Pojazd MAN, LIONS COACH C, AUTOBUS, TURYSTYCZNY Dane podstawowe Rok produkcji 2014 Numer VIN WMAR09ZZ8ET020521 Data wydania dowodu rejestracyjnego 29.01.2024 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 847 404 KM Termin ważności badania technicznego DO 04.04.2025 Dane techniczne Liczba miejsc ogółem 57 Liczba miejsc siedzących 57 Liczba miejsc stojących Masa własna pojazdu 15 525 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność 8 395 KG Liczba osi 3",
    "ZS 025MV":"MAN Rok produkcji 2014 Numer VIN WMAR09ZZ6ET020520 Data wydania dowodu rejestracyjnego 27.01.2025 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 749 016 KM Termin ważności badania technicznego DO 20.07.2025 Dane techniczne Liczba miejsc ogółem 57 Liczba miejsc siedzących 57 Liczba miejsc stojących Masa własna pojazdu 15 475 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność 8 445 KG Maksymalna masa przyczepy z hamulcem Maksymalna masa przyczepy bez hamulca Liczba osi 3",
    "ZS 078PN":"MAN Rok produkcj 2015 Numer VIN WMAR08ZZ1GT023287 Data wydania dowodu rejestracyjnego 05.02.2025 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 793 972 KM Termin ważności badania technicznego DO 21.07.2025 Dane techniczne Liczba miejsc ogółem 57 Liczba miejsc siedzących 57 Liczba miejsc stojących Masa własna pojazdu 15 875 KG Dopuszczalna masa całkowita 25 530 KG Dopuszczalna ładowność 9 655 KG Maksymalna masa przyczepy z hamulcem 3 000 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 079PN":"MAN Rok produkcj 2015 Numer VIN WMAR08ZZ2GT022889 Data wydania dowodu rejestracyjnego 19.12.2024 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 967 251 KM Termin ważności badania technicznego DO 02.06.2025 Dane techniczne Liczba miejsc ogółem 57 Liczba miejsc siedzących 57 Liczba miejsc stojących Masa własna pojazdu 15 561 KG Dopuszczalna masa całkowita 25 530 KG Dopuszczalna ładowność 9 969 KG Maksymalna masa przyczepy z hamulcem 3 000 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 101UC":"MAN Rok produkcji 2024 Numer VIN WMAR08ZZ1RT044532 Data wydania dowodu rejestracyjnego 20.01.2025 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 2 166 KM Termin ważności badania technicznego DO 20.01.2026 Dane techniczne Liczba miejsc ogółem 61 Liczba miejsc siedzących 61 Liczba miejsc stojących Masa własna pojazdu 15 622 KGnnDopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność Maksymalna masa przyczepy z hamulcem 3 000 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 102UC":"MAN Rok produkcji 2024 Numer VIN WMAR08ZZ3RT044533 Data wydania dowodu rejestracyjnego 20.01.2025 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 4 011 KM Termin ważności badania technicznego DO 20.01.2026 Dane techniczne Liczba miejsc ogółem 61 Liczba miejsc siedzących 61 Liczba miejsc stojących Masa własna pojazdu 15 562 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność Maksymalna masa przyczepy z hamulcem 3 000 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 103UC":"MAN Rok produkcji 2024 Numer VIN WMAR08ZZ8RT044558 Data wydania dowodu rejestracyjnego 21.01.2025 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 2 403 KM Termin ważności badania technicznego DO 20.01.2026 Dane techniczne Liczba miejsc ogółem 61 Liczba miejsc siedzących 61 Liczba miejsc stojących Masa własna pojazdu 15 547 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność Maksymalna masa przyczepy z hamulcem 3 000 KG Maksymalna masa przyczepy bez hamulca Liczba osi 3",
"ZS 105MX":"MAN Rok produkcji 2013 Numer VIN WMAR08ZZ6ET020351 Data wydania dowodu rejestracyjnego 28.12.2023 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 729 087 KM Termin ważności badania technicznego DO 13.06.2025 Dane techniczne Liczba miejsc ogółem 59 Liczba miejsc siedzących 59 Liczba miejsc stojących Masa własna pojazdu 15 825 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność 8 095 KG Maksymalna masa przyczepy z hamulcem Maksymalna masa przyczepy bez hamulca Liczba osi 3",
"ZS 180PF":"BOVA Rok produkcji 2007 Numer VIN XL9AA39R733003346 Data wydania dowodu rejestracyjnego 17.09.2024 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 947 992 KM Termin ważności badania technicznego DO 11.03.2025 Dane techniczne Liczba miejsc ogółem 59 Liczba miejsc siedzących 59 Liczba miejsc stojących Masa własna pojazdu 12 390 KG Dopuszczalna masa całkowita 18 000 KG Dopuszczalna ładowność 6 510 KG Maksymalna masa przyczepy z hamulcem 3 500 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 2",
"ZS 263LU":"MAN Rok produkcji 2015 Numer VIN WMAR08ZZ3GT022979 Data wydania dowodu rejestracyjnego 20.04.2023 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 843 207 KM Termin ważności badania technicznego DO 14.03.2025 Dane techniczne Liczba miejsc ogółem 59 Liczba miejsc siedzących 59 Liczba miejsc stojących Masa własna pojazdu 15 576 KG Dopuszczalna masa całkowita 25 530 KGDopuszczalna ładowność 9 954 KG Maksymalna masa przyczepy z hamulcem Maksymalna masa przyczepy bez hamulca Liczba osi 3",
"ZS 395MR":"MAN Rok produkcji 2013 Numer VIN WMAR09ZZXET020469 Data wydania dowodu rejestracyjnego 18.10.2023 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 534 231 KM Termin ważności badania technicznego DO 18.03.2025 Dane techniczne Liczba miejsc ogółem 57 Liczba miejsc siedzących 57 Liczba miejsc stojących Masa własna pojazdu 15 500 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność 8 420 KGMaksymalna masa przyczepy z hamulcem 2 500 KG Maksymalna masa przyczepy bez hamulca Liczba osi 3",
"ZS 396MR":"MAN Rok produkcji 2014 Numer VIN WMAR09ZZ0DT020110 Data wydania dowodu rejestracyjnego 28.09.2023 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 713 117 KM Termin ważności badania technicznego DO 25.03.2025 Dane techniczne Liczba miejsc ogółem 57 Liczba miejsc siedzących 57 Liczba miejsc stojących Masa własna pojazdu 15 500 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność  8 420 KG Maksymalna masa przyczepy z hamulcem 2 500 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 498LM":"MAN Rok produkcji 2013 Numer VIN WMAR09ZZ6DT019205 Data wydania dowodu rejestracyjnego 18.11.2022 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 809 468 KM Termin ważności badania technicznego DO 08.05.2025 Dane techniczne Liczba miejsc ogółem 57 Liczba miejsc siedzących 57 Liczba miejsc stojących Masa własna pojazdu 15 525 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność  8 395 KG Maksymalna masa przyczepy z hamulcem 2 500 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 604PS":"MAN Rok produkcji 2015 Numer VIN WMAR08ZZ7FT021803 Data wydania dowodu rejestracyjnego 21.04.2022 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 443 247 KM Termin ważności badania technicznego DO 07.04.2025 Dane techniczne Liczba miejsc ogółem 59 Liczba miejsc siedzących 59 Liczba miejsc stojących Masa własna pojazdu 15 450 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność 8 470 KG Maksymalna masa przyczepy z hamulcem 2 500 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 607PS":"MAN 2016 Numer VIN WMAR08ZZ7GT024296 Data wydania dowodu rejestracyjnego 21.04.2022 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 952 310 KM Termin ważności badania technicznego DO 21.03.2025 Dane techniczne Liczba miejsc ogółem 57 Liczba miejsc siedzących 57 Liczba miejsc stojących Masa własna pojazdu 16 506 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność 7 414 KG Maksymalna masa przyczepy z hamulcem 3 000 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 608PS":"MAN Rok produkcji 2015 Numer VIN WMAR09ZZ2FT022167 Data wydania dowodu rejestracyjnego 21.04.2022 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 507 232 KM Termin ważności badania technicznego DO 17.03.2025 Dane techniczne Liczba miejsc ogółem 57 Liczba miejsc siedzących 57 Liczba miejsc stojących Masa własna pojazdu 15 175 KG Dopuszczalna masa całkowita 23 290 KG Dopuszczalna ładowność 8 745 KG Maksymalna masa przyczepy z hamulcem 2 500 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 724NY":"MAN Rok produkcji 2014 Numer VIN WMAR08ZZ3ET021053 Data wydania dowodu rejestracyjnego 19.09.2024 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 54 756 KM Termin ważności badania technicznego DO 02.03.2025 Dane techniczne Liczba miejsc ogółem 59 Liczba miejsc siedzących 59 Liczba miejsc stojących Masa własna pojazdu 15 725 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność 8 195 KG Maksymalna masa przyczepy z hamulcem 2 500 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 736LE":"POLSTER BUS Rok produkcji 2019 Numer VIN WDB9076571P120787 Data wydania dowodu rejestracyjnego 03.09.2022 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 412 773 KM Termin ważności badania technicznego DO 24.02.2025 Dane techniczne Liczba miejsc ogółem 21 Liczba miejsc siedzących 21 Liczba miejsc stojących Masa własna pojazdu 3 435 KG Dopuszczalna masa całkowita 5 300 KG Dopuszczalna ładowność Maksymalna masa przyczepy z hamulcem 800 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 2",
"ZS 741LE":"POLSTER BUS2019 Numer VIN WDB9076571P120788 Data wydania dowodu rejestracyjnego 03.09.2022 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 407 632 KM Termin ważności badania technicznego DO 08.03.2025 Dane techniczne Liczba miejsc ogółem 21 Liczba miejsc siedzących 21 Liczba miejsc stojących Masa własna pojazdu 3 435 KG Dopuszczalna masa całkowita 5 300 KG Dopuszczalna ładowność Maksymalna masa przyczepy z hamulcem 800 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 2",
"ZS 742LE":"POLSTER BUS Rok produkcji 2019 Numer VIN WDB9076571P170164 Data wydania dowodu rejestracyjnego 17.03.2023 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 400 027 KM Termin ważności badania technicznego DO 02.06.2025 Dane techniczne Liczba miejsc ogółem 21 Liczba miejsc siedzących 21 Liczba miejsc stojących Masa własna pojazdu 3 420 KG Dopuszczalna masa całkowita 5 300 KG Dopuszczalna ładowność Maksymalna masa przyczepy z hamulcem 800 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 2",
"ZS 745LE":"POLSTER BUS Rok produkcji 2019 Numer VIN WDB9076571P159094 Data wydania dowodu rejestracyjnego 02.03.2023 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 369 199 KM Termin ważności badania technicznego DO 22.05.2025 Dane techniczne Liczba miejsc ogółem 21 Liczba miejsc siedzących 21 Liczba miejsc stojących Masa własna pojazdu 3 420 KG Dopuszczalna masa całkowita 5 300 KG Dopuszczalna ładowność Maksymalna masa przyczepy z hamulcem 800 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 2",
"ZS 749PM":"MAN Rok produkcji 2015 Numer VIN WMAR08ZZ9GT022923 Data wydania dowodu rejestracyjnego 06.07.2023 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 949 899 KM Termin ważności badania technicznego DO 16.07.2025 Dane techniczne Liczba miejsc ogółem 57 Liczba miejsc siedzących 57 Liczba miejsc stojących Masa własna pojazdu 15 000 KG Dopuszczalna masa całkowita 25 530 KG Dopuszczalna ładowność 10 530 KG Maksymalna masa przyczepy z hamulcem 3 000 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 808HE":"Volvo 2017 Numer VIN YV3T2U821H1185641 Data wydania dowodu rejestracyjnego 21.11.2023 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 526 194 KM Termin ważności badania technicznego DO 05.05.2025 Dane techniczne Liczba miejsc ogółem 63 Liczba miejsc siedzących 63 Liczba miejsc stojących Masa własna pojazdu 16 038 KG Dopuszczalna masa całkowita 24 750 KG Dopuszczalna ładowność Maksymalna masa przyczepy z hamulcem 2 800 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 846MJ":"MAN, LION'S COACH C, AUTOBUS, TURYSTYCZNY Dane podstawowe Rok produkcji 2013 Numer VIN WMAR09ZZXET020522 Data wydania dowodu rejestracyjnego 04.08.2023 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 924 317 KM Termin ważności badania technicznego DO 13.07.2025 Dane techniczne Liczba miejsc ogółem 57 Liczba miejsc siedzących 57 Liczba miejsc stojących Masa własna pojazdu 16 000 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność 7 920 KG Maksymalna masa przyczepy z hamulcem Maksymalna masa przyczepy bez hamulca Liczba osi 3",
"ZS 856PP":"Pojazd SETRA, S 319 UL, AUTOBUS, MIĘDZYMIASTOWY Dane podstawowe Rok produkcji 2006 Numer VIN WKK62712113100814 Data wydania dowodu rejestracyjnego 16.03.2022 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 892 825 KM Termin ważności badania technicznego DO 11.07.2025 Dane techniczne Liczba miejsc ogółem 128 Liczba miejsc siedzących 70 Liczba miejsc stojących 58 Masa własna pojazdu 14 900 KG Dopuszczalna masa całkowita 24 000 KG Dopuszczalna ładowność Maksymalna masa przyczepy z hamulcem Maksymalna masa przyczepy bez hamulca Liczba osi 3",
"ZS 869MW":"Pojazd MAN, LION'S COACH L, AUTOBUS, TURYSTYCZNY Dane podstawowe Rok produkcji 2013 Numer VIN WMAR08ZZ0ET020331 Data wydania dowodu rejestracyjnego 22.02.2024 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 727 875 KM Termin ważności badania technicznego DO 01.08.2025 Dane techniczne Liczba miejsc ogółem 59 Liczba miejsc siedzących 59 Liczba miejsc stojących Masa własna pojazdu 15 800 KG  Dopuszczalna masa całkowita 26 420 KG Dopuszczalna ładowność 8 120 KG Maksymalna masa przyczepy z hamulcem Maksymalna masa przyczepy bez hamulca Liczba osi 3",
"ZS 871MW":"Pojazd MAN, LION'S COACH L, AUTOBUS, TURYSTYCZNY Dane podstawowe Rok produkcji 2013 Numer VIN WMAR08ZZ4ET020350 Data wydania dowodu rejestracyjnego 18.12.2023 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 755 348 KM Termin ważności badania technicznego DO 19.06.2025 Dane techniczne Liczba miejsc ogółem 59 Liczba miejsc siedzących 59 Liczba miejsc stojących Masa własna pojazdu 15 825 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność 8 095 KG Maksymalna masa przyczepy z hamulcem 2 500 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 881MX":"Pojazd MAN, LION'S COACH C, AUTOBUS, TURYSTYCZNY Dane podstawowe Rok produkcji 2014 Numer VIN WMAR09ZZ5ET020542 Data wydania dowodu rejestracyjnego 18.12.2023 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 698 482 KM Termin ważności badania technicznego DO 21.05.2025 Dane techniczne Liczba miejsc ogółem 54 Liczba miejsc siedzących 54 Liczba miejsc stojących Masa własna pojazdu 15 375 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność 8 545 KG Maksymalna masa przyczepy z hamulcem Maksymalna masa przyczepy bez hamulca Liczba osi 3",
"ZS 895PS":"MAN, LIONS COACH L, AUTOBUS, MIĘDZYMIASTOWY Dane podstawowe Rok produkcji 2014 Numer VIN WMAR09ZZ3FT021299 Data wydania dowodu rejestracyjnego 01.08.2023 Województwo, w którym zarejestrowano pojazdnZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 590 287 KM Termin ważności badania technicznego DO 02.03.2025 Dane techniczne Liczba miejsc ogółem 54 Liczba miejsc siedzących 54 Liczba miejsc stojących Masa własna pojazdu 15 576 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność Maksymalna masa przyczepy z hamulcem Maksymalna masa przyczepy bez hamulca Liczba osi 3",
"ZS 912PM":"MAN, LIONS COACH L, AUTOBUS, TURYSTYCZNY Dane podstawowe Rok produkcji 2014 Numer VIN WMAR08ZZ1ET021052 Data wydania dowodu rejestracyjnego 03.02.2025 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 586 426 KM Termin ważności badania technicznego DO 20.07.2025 Dane techniczne Liczba miejsc ogółem 59 Liczba miejsc siedzących 59 Liczba miejsc stojących Masa własna pojazdu 15 600 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność 8 320 KG Maksymalna masa przyczepy z hamulcem 2 500 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 913PM":"MAN, LIONS COACH C, AUTOBUS, TURYSTYCZNY Dane podstawowe Rok produkcji 2014 Numer VIN WMAR09ZZ7ET020915 Data wydania dowodu rejestracyjnego 21.07.2023 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 811 521 KM Termin ważności badania technicznego DO 07.08.2025 Dane techniczne Liczba miejsc ogółem 54 Liczba miejsc siedzących 54 Liczba miejsc stojących Masa własna pojazdu 15 475 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność Maksymalna masa przyczepy z hamulcem 2 710 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 920NP":"Pojazd NEOPLAN, N2216/3, AUTOBUS, TURYSTYCZNY Dane podstawowe Rok produkcji 2013 Numer VIN WAGP22ZZ5DT019427 Data wydania dowodu rejestracyjnego 03.06.2024 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 636 550 KM Termin ważności badania technicznego DO 17.05.2025 Dane techniczne Liczba miejsc ogółem 59 Liczba miejsc siedzących 59 Liczba miejsc stojących Masa własna pojazdu 15 500 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność 8 420 KGMaksymalna masa przyczepy z hamulcem 2 500 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 3",
"ZS 974KN":"Pojazd MAN, LION'S COACH, AUTOBUS, TURYSTYCZNY Dane podstawowe Rok produkcji 2018 Numer VIN WMAR07ZZ1JT027891 Data wydania dowodu rejestracyjnego 27.05.2022 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 471 133 KM Termin ważności badania technicznego DO 28.02.2025 Dane techniczne Liczba miejsc ogółem 51 Liczba miejsc siedzących 51 Liczba miejsc stojących Masa własna pojazdu 13 553 KG Dopuszczalna masa całkowita 18 000 KG Dopuszczalna ładowność 4 447 KG Maksymalna masa przyczepy z hamulcem Maksymalna masa przyczepy bez hamulca Liczba osi 2",
"ZST 77194":"Pojazd SETRA, S 415, AUTOBUS, TURYSTYCZNY Dane podstawowe Rok produkcji 2009 Numer VIN WKK63213113106440 Data wydania dowodu rejestracyjnego 06.02.2025 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 82 925 KM termin ważności badania technicznego DO 04.08.2025 Dane techniczne Liczba miejsc ogółem 52 Liczba miejsc siedzących 52 Liczba miejsc stojących Masa własna pojazdu 13 700 KG Dopuszczalna masa całkowita 18 000 KG Dopuszczalna ładowność Maksymalna masa przyczepy z hamulcem 2 900 KG Maksymalna masa przyczepy bez hamulca 750 KG Liczba osi 2",
"ZS716NY":"Pojazd SETRA, S 431 DT, AUTOBUS, TURYSTYCZNY Dane podstawowe Rok produkcji 2010 Numer VIN WKK41000113110979 Data wydania dowodu rejestracyjnego 17.10.2024 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 774 655 KM Termin ważności badania technicznego DO 03.04.2025 Dane techniczne Liczba miejsc ogółem80 Liczba miejsc siedzących 80 Liczba miejsc stojących Masa własna pojazdu 19 400 KG Dopuszczalna masa całkowita 26 000 KG Dopuszczalna ładowność 6 600 KG Maksymalna masa przyczepy z hamulcem Maksymalna masa przyczepy bez hamulca Liczba osi 3",
"ZS 845MJ":"Pojazd MAN, LION'S COACH C, AUTOBUS, TURYSTYCZNY Dane podstawowe Rok produkcji 2013 Numer VIN WMAR09ZZ1DT019547 Data wydania dowodu rejestracyjnego 28.09.2023 Województwo, w którym zarejestrowano pojazd ZACHODNIOPOMORSKIE Ostatni stan licznika z badania technicznego 768 033 KM Termin ważności badania technicznego DO 18.03.2025 Dane techniczne Liczba miejsc ogółem 57 Liczba miejsc siedzących 57 Liczba miejsc stojących Masa własna pojazdu 15 196 KG Dopuszczalna masa całkowita 23 920 KG Dopuszczalna ładowność 8 724 KG Maksymalna masa przyczepy z hamulcem Maksymalna masa przyczepy bez hamulca Liczba osi 3",

}

# Ekran powitalny
welcome_frame = tk.Frame(root, bg="black")
welcome_frame.pack(fill=tk.BOTH, expand=True)

welcome_label = tk.Label(welcome_frame, text="Master Premium", font=("Arial", 40), fg="red", bg="black")
welcome_label.pack(pady=100)

sub_label = tk.Label(welcome_frame, text="BusLite(PKS)", font=("Arial", 30), fg="white", bg="black")
sub_label.pack()

# Opóźnienie 2 sekundy, przejście do ekranu głównego
root.after(2000, start_main_screen)

# Ekran główny
main_screen_frame = tk.Frame(root)
main_screen_frame.pack(fill=tk.BOTH, expand=True)

# Podział na górną i dolną część
upper_frame = tk.Frame(main_screen_frame)
upper_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

lower_frame = tk.Frame(main_screen_frame, bg="lightgray")
lower_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Tabela w górnej części
columns = ("Kierunek", "Rejestracja", "Pasażerowie", "Godzina")  # Zaktualizowana tabela o kolumnę "Godzina"
table = ttk.Treeview(upper_frame, columns=columns, show="headings", height=10)

# Dodawanie nagłówków do tabeli
for col in columns:
    table.heading(col, text=col)

# Wypełnianie tabeli przykładowymi danymi
for i in range(15):
    table.insert("", "end", values=("Kierunek " + str(i+1), "Rej " + str(i+1), "15", "12:00"))

table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Menu w dolnej części
menu_frame = tk.Frame(lower_frame)
menu_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# 1. Menu z nazwami kierunków
routes = ["Centrum Pomorzany", "Niebuszewo", "Pogodno Gumieńce", "Police", "Dąbie"]
route_combobox = ttk.Combobox(menu_frame, values=routes, state="readonly")
route_combobox.set("Wybierz kierunek")
route_combobox.pack(fill=tk.X, padx=5, pady=5)

# 2. Menu z numerami rejestracyjnymi pojazdów
registrations = ["ZS 024MV",
"ZS 025MV",
"ZS 078PN",
"ZS 079PN",
"ZS 101UC",
"ZS 102UC",
"ZS 103UC",
"ZS 105MX",
"ZS 180PF",
"ZS 263LU",
"ZS 395MR",
"ZS 396MR",
"ZS 498LM",
"ZS 604PS",
"ZS 607PS",
"ZS 608PS",
"ZS716NY",
"ZS 724NY",
"ZS 736LE",
"ZS 741LE",
"ZS 742LE",
"ZS 745LE",
"ZS 749PM",
"ZS 808HE",
"ZS 845MJ",
"ZS 846MJ",
"ZS 856PP",
"ZS 869MW",
"ZS 871MW",
"ZS 881MX",
"ZS 895PS",
"ZS 912PM",
"ZS 913PM",
"ZS 920NP",
"ZS 974KN",
"ZST 77194",
]
registration_combobox = ttk.Combobox(menu_frame, values=registrations, state="readonly")
registration_combobox.set("Wybierz rejestrację")
registration_combobox.pack(fill=tk.X, padx=5, pady=5)

# 3. Menu z liczbą pasażerów
passenger_counts = [str(i) for i in range(1, 81)]
passenger_combobox = ttk.Combobox(menu_frame, values=passenger_counts, state="readonly")
passenger_combobox.set("Wybierz ilość pasażerów")
passenger_combobox.pack(fill=tk.X, padx=5, pady=5)

# 4. Menu z godzinami
times = ["4:45","5:50","6:00","6:05","6:10","6:15","6:20","6:25","6:30","6:35","6:40","6:45","6:50","7:00","17:05", "17:10", "17:15", "17:20", "17:25","17:30","17:35","17:40","17:45","17:50","17:55","18:00"]
time_combobox = ttk.Combobox(menu_frame, values=times, state="readonly")
time_combobox.set("Wybierz godzinę")
time_combobox.pack(fill=tk.X, padx=5, pady=5)

# Dolna część
# Rocznik w dolnej części
year_label = tk.Label(lower_frame, text="Rocznik auta: ", font=("Arial", 16), bg="lightgray")
year_label.pack(pady=10)

# Pole tekstowe do wyświetlania szczegółów
text_frame = tk.Frame(lower_frame)
text_frame.pack(pady=10)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

details_text = tk.Text(text_frame, wrap=tk.WORD, height=10, width=70, font=("Arial", 12), yscrollcommand=scrollbar.set)
details_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=details_text.yview)

# Bindowanie kliknięcia na komórkę tabeli do edycji
table.bind("<ButtonRelease-1>", select_cell)

# Bindowanie zmiany wartości z menu do aktualizacji tabeli
route_combobox.bind("<<ComboboxSelected>>", on_combobox_select)
registration_combobox.bind("<<ComboboxSelected>>", on_combobox_select)
passenger_combobox.bind("<<ComboboxSelected>>", on_combobox_select)
time_combobox.bind("<<ComboboxSelected>>", on_combobox_select)  # Nowe menu godziny

# Uruchomienie aplikacji
root.mainloop()
