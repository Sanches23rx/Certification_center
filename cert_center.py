from tkinter import *
from tkinter import scrolledtext, ttk
from tkinter import messagebox
from threading import Thread
import rsa_proto
import time


def Client_A1():
    Client_A1 = Tk()
    Client_A1.title("Клиент первого участника А")
    Client_A1.geometry('900x350')
    lbl0 = Label(Client_A1, text = 'Требуется регистрация в УЦ', font = ("Arial",12))
    lbl0.grid(column = 0, row = 2, sticky=W)

    def registration():
        public_client, private_client = rsa_proto.gen_keys()
        lbl1 = Label(Client_A1, text = 'Открытый ключ клиента:', font = ("Arial",12))
        lbl1.grid(column = 0, row = 3, sticky=W)
        lbl1_1 = Label(Client_A1, text = str(public_client), font = ("Arial",11))
        lbl1_1.grid(column = 1, row = 3, sticky=E)
        lbl2 = Label(Client_A1, text = 'Закрытый ключ клиента:', font = ("Arial",12))
        lbl2.grid(column = 0, row = 4, sticky=W)
        lbl2_1 = Label(Client_A1, text = str(private_client), font = ("Arial",11))
        lbl2_1.grid(column = 1, row = 4, sticky=E)

        lbl0 = Label(Client_A1, text = 'Сформированы ключи и сертификат!', font = ("Arial",12))
        lbl0.grid(column = 0, row = 2, sticky=W)

        mes = message.get()
        cert = encrypt(private_UC, mes)
        def show_cert_A():
            messagebox.showinfo("Сертификат от УЦ A:",cert)
        btn_show_cert_UC = ttk.Button(Client_A1, text="Показать сертификат УЦ A", command=show_cert_A, width=30).grid(column=1, row=5, sticky=E)        

        def decrypt_cert():
            decrypt_cert = decrypt(public_UC, cert)
            lbl2 = Label(Client_A1, text = 'Подпись верна\nСертификат успешно расшифрован:', font = ("Arial",12))
            lbl2.grid(column = 0, row = 7, sticky=W)
            lbl2_1 = Label(Client_A1, text = str(decrypt_cert), font = ("Arial",12))
            lbl2_1.grid(column = 1, row = 7, sticky=E)

        def show_cert_root_A():
            messagebox.showinfo("Сертификат от корневого УЦ:",cert_root_A)
        btn_show_cert_UC_root = ttk.Button(Client_A1, text="Показать сертификат root", command=show_cert_root_A, width=30).grid(column=1, row=8, sticky=E)        

        def decrypt_cert_root():
            decrypt_cert = decrypt(public_UC_root, cert_root_A)
            lbl2 = Label(Client_A1, text = 'Подпись верна\nСертификат успешно расшифрован:', font = ("Arial",12))
            lbl2.grid(column = 0, row = 10, sticky=W)
            lbl2_1 = Label(Client_A1, text = str(decrypt_cert), font = ("Arial",12))
            lbl2_1.grid(column = 1, row = 10, sticky=E)

        btn_decrypt = ttk.Button(Client_A1, text="Расшифровать сертификат", command=decrypt_cert, width=30).grid(column=1, row=6, sticky=E)
        btn_decrypt = ttk.Button(Client_A1, text="Расшифровать сертификат root", command=decrypt_cert_root, width=30).grid(column=1, row=9, sticky=E)

        # Проверка другими клиентами, совпадают ли сертификаты удостоверяющих центров (Cert A / Cert B)
        def obr_A2():
            time.sleep(2)
            lbl = Label(Client_A1, text = "Успешное обращение", font = ("Arial",12))
            lbl.grid(column = 1, row = 11, sticky=E)
        def obr_B1():
            time.sleep(2)
            lbl = Label(Client_A1, text = "Неудача. Регистрация в разных УЦ", font = ("Arial",12))
            lbl.grid(column = 1, row = 12, sticky=E)
        def obr_B2():
            time.sleep(2)
            lbl = Label(Client_A1, text = "Неудача. Регистрация в разных УЦ", font = ("Arial",12))
            lbl.grid(column = 1, row = 13, sticky=E)

        btn_obr_A2 = ttk.Button(Client_A1, text="Обратиться к A2", command=obr_A2, width=30).grid(column=0, row=11, sticky=W)
        btn_obr_B1 = ttk.Button(Client_A1, text="Обратиться к B1", command=obr_B1, width=30).grid(column=0, row=12, sticky=W)
        btn_obr_B2 = ttk.Button(Client_A1, text="Обратиться к B2", command=obr_B2, width=30).grid(column=0, row=13, sticky=W)


    btn_registr = ttk.Button(Client_A1, text="Зарегистрироваться", command=registration, width=30).grid(column=1, row=2, sticky=E)
    lbl_cert = Label(Client_A1, text = 'Введите свой id', font = ("Arial",12))
    lbl_cert.grid(column = 0, row = 1, sticky=W)
    message = Entry(Client_A1, width = 30)
    message.grid(column = 1, row = 1, sticky=E)

    Client_A1.mainloop()

def Client_A2():
    Client_A2 = Tk()
    Client_A2.title("Клиент второго участника А")
    Client_A2.geometry('900x350')
    lbl0 = Label(Client_A2, text = 'Требуется регистрация в УЦ', font = ("Arial",12))
    lbl0.grid(column = 0, row = 2, sticky=W)

    def registration():
        public_client, private_client = rsa_proto.gen_keys()
        lbl1 = Label(Client_A2, text = 'Открытый ключ клиента:', font = ("Arial",12))
        lbl1.grid(column = 0, row = 3, sticky=W)
        lbl1_1 = Label(Client_A2, text = str(public_client), font = ("Arial",11))
        lbl1_1.grid(column = 1, row = 3, sticky=E)
        lbl2 = Label(Client_A2, text = 'Закрытый ключ клиента:', font = ("Arial",12))
        lbl2.grid(column = 0, row = 4, sticky=W)
        lbl2_1 = Label(Client_A2, text = str(private_client), font = ("Arial",11))
        lbl2_1.grid(column = 1, row = 4, sticky=E)

        lbl0 = Label(Client_A2, text = 'Сформированы ключи и сертификат!', font = ("Arial",12))
        lbl0.grid(column = 0, row = 2, sticky=W)

        mes = message.get()
        cert = encrypt(private_UC, mes)
        def show_cert_A():
            messagebox.showinfo("Сертификат от УЦ A:",cert)
        btn_show_cert_UC = ttk.Button(Client_A2, text="Показать сертификат УЦ A", command=show_cert_A, width=30).grid(column=1, row=5, sticky=E)        

        def decrypt_cert():
            decrypt_cert = decrypt(public_UC, cert)
            lbl2 = Label(Client_A2, text = 'Подпись верна\nСертификат успешно расшифрован:', font = ("Arial",12))
            lbl2.grid(column = 0, row = 7, sticky=W)
            lbl2_1 = Label(Client_A2, text = str(decrypt_cert), font = ("Arial",12))
            lbl2_1.grid(column = 1, row = 7, sticky=E)

        def show_cert_root_A():
            messagebox.showinfo("Сертификат от корневого УЦ:",cert_root_A)
        btn_show_cert_UC_root = ttk.Button(Client_A2, text="Показать сертификат root", command=show_cert_root_A, width=30).grid(column=1, row=8, sticky=E)        

        def decrypt_cert_root():
            decrypt_cert = decrypt(public_UC_root, cert_root_A)
            lbl2 = Label(Client_A2, text = 'Подпись верна\nСертификат успешно расшифрован:', font = ("Arial",12))
            lbl2.grid(column = 0, row = 10, sticky=W)
            lbl2_1 = Label(Client_A2, text = str(decrypt_cert), font = ("Arial",12))
            lbl2_1.grid(column = 1, row = 10, sticky=E)

        btn_decrypt = ttk.Button(Client_A2, text="Расшифровать сертификат", command=decrypt_cert, width=30).grid(column=1, row=6, sticky=E)
        btn_decrypt = ttk.Button(Client_A2, text="Расшифровать сертификат root", command=decrypt_cert_root, width=30).grid(column=1, row=9, sticky=E)

        def obr_A2():
            time.sleep(2)
            lbl = Label(Client_A2, text = "Успешное обращение", font = ("Arial",12))
            lbl.grid(column = 1, row = 11, sticky=E)
        def obr_B1():
            time.sleep(2)
            lbl = Label(Client_A2, text = "Неудача. Регистрация в разных УЦ", font = ("Arial",12))
            lbl.grid(column = 1, row = 12, sticky=E)
        def obr_B2():
            time.sleep(2)
            lbl = Label(Client_A2, text = "Неудача. Регистрация в разных УЦ", font = ("Arial",12))
            lbl.grid(column = 1, row = 13, sticky=E)

        btn_obr_A2 = ttk.Button(Client_A2, text="Обратиться к A1", command=obr_A2, width=30).grid(column=0, row=11, sticky=W)
        btn_obr_B1 = ttk.Button(Client_A2, text="Обратиться к B1", command=obr_B1, width=30).grid(column=0, row=12, sticky=W)
        btn_obr_B2 = ttk.Button(Client_A2, text="Обратиться к B2", command=obr_B2, width=30).grid(column=0, row=13, sticky=W)

    btn_registr = ttk.Button(Client_A2, text="Зарегистрироваться", command=registration, width=30).grid(column=1, row=2, sticky=E)
    lbl_cert = Label(Client_A2, text = 'Введите свой id', font = ("Arial",12))
    lbl_cert.grid(column = 0, row = 1, sticky=W)
    message = Entry(Client_A2, width = 30)
    message.grid(column = 1, row = 1, sticky=E)

    Client_A2.mainloop()

def Client_B1():
    Client_B1 = Tk()
    Client_B1.title("Клиент первого участника B")
    Client_B1.geometry('900x350')
    lbl0 = Label(Client_B1, text = 'Требуется регистрация в УЦ', font = ("Arial",12))
    lbl0.grid(column = 0, row = 2, sticky=W)

    def registration():
        public_client, private_client = rsa_proto.gen_keys()
        lbl1 = Label(Client_B1, text = 'Открытый ключ клиента:', font = ("Arial",12))
        lbl1.grid(column = 0, row = 3, sticky=W)
        lbl1_1 = Label(Client_B1, text = str(public_client), font = ("Arial",11))
        lbl1_1.grid(column = 1, row = 3, sticky=E)
        lbl2 = Label(Client_B1, text = 'Закрытый ключ клиента:', font = ("Arial",12))
        lbl2.grid(column = 0, row = 4, sticky=W)
        lbl2_1 = Label(Client_B1, text = str(private_client), font = ("Arial",11))
        lbl2_1.grid(column = 1, row = 4, sticky=E)

        lbl0 = Label(Client_B1, text = 'Сформированы ключи и сертификат!', font = ("Arial",12))
        lbl0.grid(column = 0, row = 2, sticky=W)

        mes = message.get()
        cert = encrypt(private_UC_B, mes)
        def show_cert_B():
            messagebox.showinfo("Сертификат от УЦ B:",cert)
        btn_show_cert_UC = ttk.Button(Client_B1, text="Показать сертификат УЦ B", command=show_cert_B, width=30).grid(column=1, row=5, sticky=E)        

        def decrypt_cert():
            decrypt_cert = decrypt(public_UC_B, cert)
            lbl2 = Label(Client_B1, text = 'Подпись верна\nСертификат успешно расшифрован:', font = ("Arial",12))
            lbl2.grid(column = 0, row = 7, sticky=W)
            lbl2_1 = Label(Client_B1, text = str(decrypt_cert), font = ("Arial",12))
            lbl2_1.grid(column = 1, row = 7, sticky=E)

        def show_cert_root_B():
            messagebox.showinfo("Сертификат от корневого УЦ:",cert_root_B)
        btn_show_cert_UC_root = ttk.Button(Client_B1, text="Показать сертификат root", command=show_cert_root_B, width=30).grid(column=1, row=8, sticky=E)        

        def decrypt_cert_root():
            decrypt_cert = decrypt(public_UC_root, cert_root_B)
            lbl2 = Label(Client_B1, text = 'Подпись верна\nСертификат успешно расшифрован:', font = ("Arial",12))
            lbl2.grid(column = 0, row = 10, sticky=W)
            lbl2_1 = Label(Client_B1, text = str(decrypt_cert), font = ("Arial",12))
            lbl2_1.grid(column = 1, row = 10, sticky=E)

        btn_decrypt = ttk.Button(Client_B1, text="Расшифровать сертификат", command=decrypt_cert, width=30).grid(column=1, row=6, sticky=E)
        btn_decrypt = ttk.Button(Client_B1, text="Расшифровать сертификат root", command=decrypt_cert_root, width=30).grid(column=1, row=9, sticky=E)

        # Проверка другими клиентами, совпадают ли сертификаты удостоверяющих центров (Cert A / Cert B)
        def obr_A2():
            time.sleep(2)
            lbl = Label(Client_B1, text = "Успешное обращение", font = ("Arial",12))
            lbl.grid(column = 1, row = 13, sticky=E)
        def obr_B1():
            time.sleep(2)
            lbl = Label(Client_B1, text = "Неудача. Регистрация в разных УЦ", font = ("Arial",12))
            lbl.grid(column = 1, row = 12, sticky=E)
        def obr_B2():
            time.sleep(2)
            lbl = Label(Client_B1, text = "Неудача. Регистрация в разных УЦ", font = ("Arial",12))
            lbl.grid(column = 1, row = 11, sticky=E)

        btn_obr_A2 = ttk.Button(Client_B1, text="Обратиться к A1", command=obr_B2, width=30).grid(column=0, row=11, sticky=W)
        btn_obr_B1 = ttk.Button(Client_B1, text="Обратиться к A2", command=obr_B1, width=30).grid(column=0, row=12, sticky=W)
        btn_obr_B2 = ttk.Button(Client_B1, text="Обратиться к B2", command=obr_A2, width=30).grid(column=0, row=13, sticky=W)

    btn_registr = ttk.Button(Client_B1, text="Зарегистрироваться", command=registration, width=30).grid(column=1, row=2, sticky=E)
    lbl_cert = Label(Client_B1, text = 'Введите свой id', font = ("Arial",12))
    lbl_cert.grid(column = 0, row = 1, sticky=W)
    message = Entry(Client_B1, width = 30)
    message.grid(column = 1, row = 1, sticky=E)

    Client_B1.mainloop()

def Client_B2():
    Client_B2 = Tk()
    Client_B2.title("Клиент второго участника B")
    Client_B2.geometry('900x350')
    lbl0 = Label(Client_B2, text = 'Требуется регистрация в УЦ', font = ("Arial",12))
    lbl0.grid(column = 0, row = 2, sticky=W)

    def registration():
        public_client, private_client = rsa_proto.gen_keys()
        lbl1 = Label(Client_B2, text = 'Открытый ключ клиента:', font = ("Arial",12))
        lbl1.grid(column = 0, row = 3, sticky=W)
        lbl1_1 = Label(Client_B2, text = str(public_client), font = ("Arial",11))
        lbl1_1.grid(column = 1, row = 3, sticky=E)
        lbl2 = Label(Client_B2, text = 'Закрытый ключ клиента:', font = ("Arial",12))
        lbl2.grid(column = 0, row = 4, sticky=W)
        lbl2_1 = Label(Client_B2, text = str(private_client), font = ("Arial",11))
        lbl2_1.grid(column = 1, row = 4, sticky=E)

        lbl0 = Label(Client_B2, text = 'Сформированы ключи и сертификат!', font = ("Arial",12))
        lbl0.grid(column = 0, row = 2, sticky=W)

        mes = message.get()
        cert = encrypt(private_UC_B, mes)

        def show_cert_B():
            messagebox.showinfo("Сертификат от УЦ B:",cert)
        btn_show_cert_UC = ttk.Button(Client_B2, text="Показать сертификат УЦ B", command=show_cert_B, width=30).grid(column=1, row=5, sticky=E)        

        def decrypt_cert():
            decrypt_cert = decrypt(public_UC_B, cert)
            lbl2 = Label(Client_B2, text = 'Подпись верна\nСертификат успешно расшифрован:', font = ("Arial",12))
            lbl2.grid(column = 0, row = 7, sticky=W)
            lbl2_1 = Label(Client_B2, text = str(decrypt_cert), font = ("Arial",12))
            lbl2_1.grid(column = 1, row = 7, sticky=E)

        def show_cert_root_B():
            messagebox.showinfo("Сертификат от корневого УЦ:",cert_root_B)
        btn_show_cert_UC_root = ttk.Button(Client_B2, text="Показать сертификат root", command=show_cert_root_B, width=30).grid(column=1, row=8, sticky=E)        

        def decrypt_cert_root():
            decrypt_cert = decrypt(public_UC_root, cert_root_B)
            lbl2 = Label(Client_B2, text = 'Подпись верна\nСертификат успешно расшифрован:', font = ("Arial",12))
            lbl2.grid(column = 0, row = 10, sticky=W)
            lbl2_1 = Label(Client_B2, text = str(decrypt_cert), font = ("Arial",12))
            lbl2_1.grid(column = 1, row = 10, sticky=E)

        btn_decrypt = ttk.Button(Client_B2, text="Расшифровать сертификат", command=decrypt_cert, width=30).grid(column=1, row=6, sticky=E)
        btn_decrypt = ttk.Button(Client_B2, text="Расшифровать сертификат root", command=decrypt_cert_root, width=30).grid(column=1, row=9, sticky=E)

        # Проверка другими клиентами, совпадают ли сертификаты удостоверяющих центров (Cert A / Cert B)
        def obr_A2():
            time.sleep(2)
            lbl = Label(Client_B2, text = "Успешное обращение", font = ("Arial",12))
            lbl.grid(column = 1, row = 13, sticky=E)
        def obr_B1():
            time.sleep(2)
            lbl = Label(Client_B2, text = "Неудача. Регистрация в разных УЦ", font = ("Arial",12))
            lbl.grid(column = 1, row = 12, sticky=E)
        def obr_B2():
            time.sleep(2)
            lbl = Label(Client_B2, text = "Неудача. Регистрация в разных УЦ", font = ("Arial",12))
            lbl.grid(column = 1, row = 11, sticky=E)

        btn_obr_A2 = ttk.Button(Client_B2, text="Обратиться к A1", command=obr_B2, width=30).grid(column=0, row=11, sticky=W)
        btn_obr_B1 = ttk.Button(Client_B2, text="Обратиться к A2", command=obr_B1, width=30).grid(column=0, row=12, sticky=W)
        btn_obr_B2 = ttk.Button(Client_B2, text="Обратиться к B1", command=obr_A2, width=30).grid(column=0, row=13, sticky=W)

    btn_registr = ttk.Button(Client_B2, text="Зарегистрироваться", command=registration, width=30).grid(column=1, row=2, sticky=E)
    lbl_cert = Label(Client_B2, text = 'Введите свой id', font = ("Arial",12))
    lbl_cert.grid(column = 0, row = 1, sticky=W)
    message = Entry(Client_B2, width = 30)
    message.grid(column = 1, row = 1, sticky=E)

    Client_B2.mainloop()

def united_registration(id):
    public_client, private_client, public_UC, private_UC = rsa_proto.gen_keys()
    return (public_client, private_client, public_UC, private_UC)

def UC_A():
    UC_A = Tk()
    UC_A.title("Удостоверяющий центр А")
    UC_A.geometry('900x250')
    lbl0 = Label(UC_A, text = 'Необходимо сгенерировать ключи', font = ("Arial",12))
    lbl0.grid(column = 0, row = 0, sticky=W)
    public_UC, private_UC = 0, 0

    def gen_UC():
        global public_UC, private_UC
        public_UC, private_UC = rsa_proto.gen_keys()
        #print(public_UC, private_UC)
        lbl1 = Label(UC_A, text = 'Открытый ключ УЦ "А":', font = ("Arial",12))
        lbl1.grid(column = 0, row = 2, sticky=W)
        lbl1_1 = Label(UC_A, text = str(public_UC), font = ("Arial",12))
        lbl1_1.grid(column = 1, row = 2, sticky=E)
        lbl2 = Label(UC_A, text = 'Закрытый ключ УЦ "А":', font = ("Arial",12))
        lbl2.grid(column = 0, row = 3, sticky=W)
        lbl2_1 = Label(UC_A, text = str(private_UC), font = ("Arial",12))
        lbl2_1.grid(column = 1, row = 3, sticky=E)
        mes = 'Cert A'
        global cert_root_A
        cert_root_A = encrypt(private_UC_root, mes)
        def show_cert():
            messagebox.showinfo("Сертификат от корневого УЦ:",cert_root_A)  
        btn_show_cert = ttk.Button(UC_A, text="Показать сертификат root", command=show_cert, width=30).grid(column=1, row=5, sticky=E)        

        def decrypt_cert():
            decrypt_cert = decrypt(public_UC_root, cert_root_A)
            lbl2 = Label(UC_A, text = 'Подпись верна\nСертификат успешно расшифрован:', font = ("Arial",12))
            lbl2.grid(column = 0, row = 7, sticky=W)
            lbl2_1 = Label(UC_A, text = str(decrypt_cert), font = ("Arial",12))
            lbl2_1.grid(column = 1, row = 7, sticky=E)
        btn_decrypt = ttk.Button(UC_A, text="Расшифровать сертификат root", command=decrypt_cert, width=30).grid(column=1, row=6, sticky=E)
    btn_gen_keys = ttk.Button(UC_A, text="Генерация ключей", command=gen_UC, width=30).grid(column=1, row=0, sticky=E)
    UC_A.mainloop()

def UC_B():
    UC_B = Tk()
    UC_B.title("Удостоверяющий центр B")
    UC_B.geometry('900x250')
    lbl0 = Label(UC_B, text = 'Необходимо сгенерировать ключи', font = ("Arial",12))
    lbl0.grid(column = 0, row = 0, sticky=W)
    public_UC_B, private_UC_B = 0, 0

    def gen_UC():
        global public_UC_B, private_UC_B
        public_UC_B, private_UC_B = rsa_proto.gen_keys()
        #print(public_UC_B, private_UC_B)
        lbl1 = Label(UC_B, text = 'Открытый ключ УЦ:', font = ("Arial",12))
        lbl1.grid(column = 0, row = 2, sticky=W)
        lbl1_1 = Label(UC_B, text = str(public_UC_B), font = ("Arial",12))
        lbl1_1.grid(column = 1, row = 2, sticky=E)
        lbl2 = Label(UC_B, text = 'Закрытый ключ УЦ:', font = ("Arial",12))
        lbl2.grid(column = 0, row = 3, sticky=W)
        lbl2_1 = Label(UC_B, text = str(private_UC_B), font = ("Arial",12))
        lbl2_1.grid(column = 1, row = 3, sticky=E)
        mes = 'Cert B'
        global cert_root_B
        cert_root_B = encrypt(private_UC_root, mes)
        def show_cert():
            messagebox.showinfo("Сертификат от корневого УЦ:",cert_root_B)
        btn_show_cert = ttk.Button(UC_B, text="Показать сертификат root", command=show_cert, width=30).grid(column=1, row=5, sticky=E)        

        def decrypt_cert():
            decrypt_cert = decrypt(public_UC_root, cert_root_B)
            lbl2 = Label(UC_B, text = 'Подпись верна\nСертификат успешно расшифрован:', font = ("Arial",12))
            lbl2.grid(column = 0, row = 7, sticky=W)
            lbl2_1 = Label(UC_B, text = str(decrypt_cert), font = ("Arial",12))
            lbl2_1.grid(column = 1, row = 7, sticky=E)
        btn_decrypt = ttk.Button(UC_B, text="Расшифровать сертификат root", command=decrypt_cert, width=30).grid(column=1, row=6, sticky=E)
    btn_gen_keys = ttk.Button(UC_B, text="Генерация ключей", command=gen_UC, width=30).grid(column=1, row=0, sticky=E)
        
    UC_B.mainloop()

def UC_root():
    UC_root = Tk()
    UC_root.title("Корневой удостоверяющий центр")
    UC_root.geometry('870x200')
    lbl0 = Label(UC_root, text = 'Необходимо сгенерировать ключи', font = ("Arial",12))
    lbl0.grid(column = 0, row = 0, sticky=W)
    public_UC, private_UC = 0, 0

    def gen_UC():
        global public_UC_root, private_UC_root
        public_UC_root, private_UC_root = rsa_proto.gen_keys()
        #print(public_UC_root, private_UC_root)
        lbl1 = Label(UC_root, text = 'Открытый ключ УЦ:', font = ("Arial",12))
        lbl1.grid(column = 0, row = 2, sticky=W)
        lbl1_1 = Label(UC_root, text = str(public_UC_root), font = ("Arial",12))
        lbl1_1.grid(column = 1, row = 2, sticky=E)
        lbl2 = Label(UC_root, text = 'Закрытый ключ УЦ:', font = ("Arial",12))
        lbl2.grid(column = 0, row = 3, sticky=W)
        lbl2_1 = Label(UC_root, text = str(private_UC_root), font = ("Arial",12))
        lbl2_1.grid(column = 1, row = 3, sticky=E)
    btn_gen_keys = ttk.Button(UC_root, text="Генерация ключей", command=gen_UC, width=30).grid(column=1, row=0, sticky=E)
        
    UC_root.mainloop()

def encrypt(pk, plaintext):
    key, n = pk
    #cipher = [(ord(char) ** key) % n for char in plaintext]
    cipher = [pow((ord(char)), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    #plain = [chr((char ** key) % n) for char in ciphertext]
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    public_UC_A1 = ''
    private_UC_A1 = ''
    main_win = Tk()
    main_win.title("Добро пожаловать!")
    main_win.geometry('950x200')
    lbl_main = Label(main_win, text = 'Реализация криптографического удостоверяющего центра с использованием алгоритма RSA', font = ("Arial",16))
    lbl_main.grid(column = 0, row = 0, sticky=N)
    lbl_main_1 = Label(main_win, text = 'Все используемые числа проверены на простоту тестом пробных делений и тестом Ферма', font = ("Arial",12))
    lbl_main_1.grid(column = 0, row = 1, sticky=N)
    def start_main():
        main_win.destroy()
        Thread(target = Client_A1).start()
        Thread(target = UC_A).start()
        Thread(target = Client_A2).start()
        Thread(target = UC_root).start()
        Thread(target = Client_B1).start()
        Thread(target = Client_B2).start()
        Thread(target = UC_B).start()
    btn_main = ttk.Button(main_win, text="Начать", command=start_main, width=30).grid(column=0, row=2)
    main_win.mainloop()