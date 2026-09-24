##################### Automated Birthday Wisher - Extra Hard Starting Project ######################
#Costruire un programma Python che manda gli auguri di compleanno alle persone memorizzate all'interno del file birthday.csv
#e dopo aver scelto un template di lettera per gli auguri, invia una mail alla persona con il messaggio di auguri

#Macro Requisiti:
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

# ---------------------------- MODULI & IMPORTAZIONE CLASSI ------------ #
import pandas
import datetime as dt
from pathlib import Path
import random
import smtplib
import os

# ---------------------------- CONSTANTI ------------------------------- #

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# ---------------------------- VARIABILI ------------------------------- #

birtday_wisher_list = []


# ---------------------------- FUNZIONI ------------------------------- #



# ---------------------------- SETUP UI ------------------------------- #



# ---------------------------- CORPO DEL CODICE ----------------------- #

birthday_list = pandas.read_csv("birthdays.csv")
birthday_list_dict = birthday_list.to_dict(orient="records")
print(birthday_list_dict)
print(type(birthday_list_dict))

today = dt.datetime.now()

birthday_wisher_list = [birthday_people for birthday_people in birthday_list_dict if birthday_people['day'] == today.day and birthday_people['month'] == today.month]
#questo print sotto è solo un controllo.....può essere eliminato
print(birthday_wisher_list)

# Cartella che contiene i file
folder = Path("letter_templates")

# Ottieni tutti i file .txt della cartella
files = list(folder.glob("*.txt"))

# Seleziona un file casuale
wisher_letter = random.choice(files)

with open(wisher_letter, "r", encoding="utf-8") as f:
    letter_content = f.read()

for people in birthday_wisher_list:
    wisher_name = people["name"]
    custom_letter = letter_content.replace("[NAME]", wisher_name)
    # questo print sotto è solo un controllo.....può essere eliminato
    print(custom_letter)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        #serve per mantenere la connessione criptata e sicura
        connection.starttls()
        #comando che serve per instaurare la connessione con il server
        connection.login(user = MY_EMAIL, password = PASSWORD)
        #comando che serve per inviare la mail, dove devo specificare la mail mittente, la mail destinataria, l'oggetto dell email ed il messaggio
        #della mail da inviare
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = people["email"],
            msg = f"Subject: Happy Birthday\n\n{custom_letter}"
        )
#chiudo il connettore
connection.close()
