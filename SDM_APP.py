from Tkinter import*
import tkMessageBox
import ttk
import matplotlib.pyplot as grafik
import serial
import xlsxwriter
import time

soil_moisture = []
temp = []
ph = []
plant = []
quality = []
suggestion = []

splash_screen = Tk()
splash_screen.overrideredirect(True)
width = splash_screen.winfo_screenwidth()
height = splash_screen.winfo_screenheight()
splash_screen.geometry("%dx%d+%d+%d" % (300,200,width*0.4,height*0.35) )
splash_screen.title("Soil Data Monitoring")
splash_screen['bg']="olive"

logo_app = PhotoImage(file="logo_aplikasi.gif")
logo_app_1 = logo_app.subsample(30,30)

label_logo_app = Label(splash_screen,image=logo_app_1,bg="olive")
label_logo_app.pack()

label_title = Label(splash_screen,font=("autos bold",20),text="Soil Data Monitoring",fg="white",bg="olive")
label_title.pack()

progresbar = ttk.Progressbar(splash_screen,orient='horizontal',mode='determinate',length=300,maximum=100)   
progresbar.place(x=0,y=100)

label_progres = Label(splash_screen,font=('verdana',9),fg='black',anchor='w')
label_progres.place(x=100,y=130)

for i in range (101):
    time.sleep(0.001)
    progresbar["value"]=i
    label_progres['text']='Loading...'+str(i)+'%'
    progresbar.update()
    if i==100:
        splash_screen.destroy()
        
splash_screen.mainloop()

def start_1():
    main1 =Tk()
    main1.geometry("%dx%d+%d+%d" % (400,375,500,250))
    main1['bg'] = 'olive'
    main1.title("Soil Data Monitoring")

    logo_itk1 = PhotoImage(file="itk.gif")
    logo_itk = logo_itk1.subsample(30,30)
    logo_pimnas1 = PhotoImage(file="pimnas_logo.gif")
    logo_pimnas = logo_pimnas1.subsample(50,50)
    logo_app2 = PhotoImage(file="logo_aplikasi.gif")
    logo_app = logo_app2.subsample(40,40)
    main1.tk.call('wm','iconphoto',main1._w,logo_app2)

    label_logo_app = Label(main1,image=logo_app,bg='olive')
    label_logo_app.place(x=350,y=328)

    label_logo_itk= Label(main1,image=logo_itk,bg='olive')
    label_logo_itk.place(x=250,y=330)

    label_logo_pimnas= Label(main1,image=logo_pimnas,bg='olive')
    label_logo_pimnas.place(x=305,y=332)

    label_pembuka1 = Label(main1,font=('autobus bold',24),text="Welcome !",fg="white",bg="olive")
    label_pembuka1.place(x=120,y=50)

    def analisis():
        main1.destroy()
        def start_2():
            main2 = Tk()
            main2.geometry("%dx%d+%d+%d" % (950,730,150,20))
            main2['bg']='olive'
            main2.title("Soil Data Monitoring")

            itk_pic = PhotoImage(file='itk.gif')
            pimnas_pic = PhotoImage(file='pimnas_logo.gif')
            app_pic = PhotoImage(file='logo_aplikasi.gif')
            logo_itk = itk_pic.subsample(30,30)
            logo_pimnas = pimnas_pic.subsample(50,50)
            logo_app = app_pic.subsample(40,40)

            main2.tk.call('wm','iconphoto',main2._w,app_pic)

            label_logo_app = Label(main2,image=logo_app,bg='olive')
            label_logo_app.place(x=900,y=4)

            label_logo_itk= Label(main2,image=logo_itk,bg='olive')
            label_logo_itk.place(x=800,y=5)

            label_logo_pimnas= Label(main2,image=logo_pimnas,bg='olive')
            label_logo_pimnas.place(x=856,y=7)

            style=ttk.Style()
            style.configure("Treeview.Heading",font=("arial",11))
            #make table of data from arduino
            label_table_data = Label(main2,font=('adobe haiti std',12,'bold'),text="Tabel Data",fg="white",bg='olive')
            label_table_data.place(x=10,y=5)
            
            vsc = ttk.Scrollbar(main2,orient='vertical')
            vsc.place(x=12+40+110+115+90,y=26,height=325)

            table_data = ttk.Treeview(main2,height=15,yscrollcommand = vsc.set)
            table_data['columns']=('kel_t','suhu','ph')
            table_data.place(x=10,y=25)

            vsc.config(command = table_data.yview)

            table_data.column('#0',width=40,anchor='center')
            table_data.heading('#0',text='No')

            table_data.column('kel_t',width=110,anchor='center')
            table_data.heading('kel_t',text='Kel. Tanah (%)')

            table_data.column('suhu',width=115,anchor='center')
            table_data.heading('suhu',text='Suhu Udara(C)')

            table_data.column('ph',width=90,anchor='center')
            table_data.heading('ph',text='pH Tanah')

            #make table plant for the selection
            label_table_plant = Label(main2,font=('adobe haiti std',12,'bold'),text="Tabel Tanaman",fg="white",bg='olive')
            label_table_plant.place(x=10,y=370)
            
            vsb = ttk.Scrollbar(main2,orient="vertical")
            vsb.place(x=12+40+320+80+450,y=391,height=325)

            table_plant = ttk.Treeview(main2,height=15,yscrollcommand=vsb.set)
            table_plant['columns'] = ('plant_type','quality','suggestion')
            table_plant.place(x=10,y=390)

            vsb.config(command = table_plant.yview)

            table_plant.column('#0',width=40,anchor='center')
            table_plant.heading('#0',text='No')

            table_plant.column('plant_type',width=320,anchor='w')
            table_plant.heading('plant_type',text='Jenis Tanaman')

            table_plant.column('quality',width=80,anchor='center')
            table_plant.heading('quality',text='Kualitas')

            table_plant.column('suggestion',width=480,anchor='center')
            table_plant.heading('suggestion',text='Saran')

            table_plant.tag_configure("quality1",background="light green",font=("arial",11))
            table_plant.tag_configure("quality2",background="yellow",font=("arial",11))
            table_plant.tag_configure("quality3",background="red",font=("arial",11))

            repetition = DoubleVar()

            label_repetition = Label(main2,font=('adobe haiti std',12,'bold'),text="Banyak Data",fg="white",bg='olive')
            label_repetition.place(x=420,y=40)

            entry_repetition = Entry(main2,font=('adobe haiti std',12),text = repetition,bd=3,width=8)
            entry_repetition.place(x=550,y=40)

            def back_1():
                main2.destroy()
                start_1()

            def analysis():
                try:
                    data_sensor = serial.Serial('com4',9600)
                except:
                    tkMessageBox.showerror("Error","Perangkat tidak terhubung!")

                repeat = repetition.get()
                data_to = 1
                the_table_data = table_data.get_children()
                if the_table_data!='()':
                    for child in the_table_data:
                        table_data.delete(child)
                    b = len(temp)
                    while b>0:
                        del soil_moisture[0]
                        del temp[0]
                        del ph[0]
                        b = b-1
                while repeat>0 :
                    if data_sensor.inWaiting()>0:
                        data = data_sensor.readline()
                        dividing_data = data.split(',')
                        sm = float(dividing_data[0])
                        tt = float(dividing_data[1])
                        PH = float(dividing_data[2])
                        not_important = (dividing_data[3])

                        soil_moisture.append(sm)
                        temp.append(tt)
                        ph.append(PH)
                        repeat = repeat-1
                        
                        table_data.insert("","end",text=str(data_to),values=(str(sm),str(tt),str(PH)))
                        data_to = data_to+1
                        main2.update()

                average_sm = sum(soil_moisture)/float(len(soil_moisture))
                average_tt = sum(temp)/float(len(temp))
                average_ph = sum(ph)/float(len(ph))

                the_table_plant = table_plant.get_children()
                data_to2 = 1
                if the_table_plant != '()':
                    for child in the_table_plant:
                        table_plant.delete(child)

                if 24<=average_sm<29:
                    if 30<=average_tt<90:
                        if 5.5<=average_ph<7:
                            table_plant.insert("","end",text=str(data_to2),values=("Oriza Sativa (Sistem Irigasi)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Oriza Sativa (Sistem Irigasi)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 22<=average_sm<24 or 29<=average_sm<32:
                    if 30<=average_tt<33:
                        if 4.5<=average_ph<5.5 or 7<=average_ph<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Oriza Sativa (Sistem Irigasi)","S2","24<kelembaban tanah<29,","5.5<pH<7"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Oriza Sativa (Sistem Irigasi)")
                            quality.append("S2")
                            suggestion.append("24<kelembaban tanah<29,","5.5<pH<7")
                elif 18<=average_sm<22 or 32<=average_sm<35:
                    if average_tt<30 or average_tt>90:
                        if average_ph<4.5 or average_ph>8:
                            table_plant.insert("","end",text=str(data_to2),values=("Oriza Sativa (Sistem Irigasi)","S3","24<kelembaban tanah<29, 30<suhu<90, 5.5<pH<7"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Oriza Sativa (Sistem Irigasi)")
                            quality.append("S3")
                            suggestion.append("24<kelembaban tanah<29, 30<suhu<90, 5.5<pH<7")
                if 24<=average_sm<29:
                    if 33<=average_tt<90:
                        if 5.5<=average_ph<8.2:
                            table_plant.insert("","end",text=str(data_to2),values=("Oriza Sativa (Tadah Hujan)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Oriza Sativa (Tadah Hujan)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 22<=average_sm<24 or 29<=average_sm<32:
                    if 30<=average_tt<33:
                        if 5<=average_ph<5.5 or 8.2<=average_ph<8.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Oriza Sativa (Tadah Hujan)","S2","24<kelembaban tanah<29,","5.5<pH<8.2"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Oriza Sativa (Tadah Hujan)")
                            quality.append("S2")
                            suggestion.append("24<kelembaban tanah<29,","5.5<pH<8.2")
                elif 18<=average_sm<22 or 32<=average_sm<35:
                    if average_tt<30 or average_tt>90:
                        if average_ph<5 or average_ph>8.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Oriza Sativa (Tadah Hujan)","S3","24<kelembaban tanah<29, 33<suhu<90, 5.5<pH<8.2"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Oriza Sativa (Tadah Hujan)")
                            quality.append("S3")
                            suggestion.append("24<kelembaban tanah<29, 33<suhu<90, 5.5<pH<8.2")
                if 33<=average_sm<90:
                    if 24<=average_tt<29:
                        if 5.5<=average_ph<7.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Padi Gogo","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Padi Gogo")
                            quality.append("S1")
                            suggestion.append("-")
                elif 30<=average_sm<33:
                    if 22<=average_tt<24 or 29<=average_tt<32:
                        if 5<=average_ph<7.9:
                            if average_ph<5.5 or average_ph>7.5:
                                suggest = "24<suhu<29, 5.5<ph<7.5"
                            else:
                                suggest = "24<suhu<29"
                            table_plant.insert("","end",text=str(data_to2),values=("Padi Gogo","S2",suggest),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Padi Gogo")
                            quality.append("S2")
                            suggestion.append(suggest)
                elif average_sm<30 or average_sm>90:
                    if 18<=average_tt<22 or 32<=average_tt<35:
                        if average_ph<5 or average_ph>7.9:
                            table_plant.insert("","end",text=str(data_to2),values=("Padi Gogo","S3",suggest),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Padi Gogo")
                            quality.append("S3")
                            suggestion.append("33<kelembaban tanah<90, 24<suhu<29, 5.5<ph<7.5")
                if 33<=average_sm<90:
                    if 24<=average_tt<29:
                        if 5.5<=average_ph<8.2:
                            table_plant.insert("","end",text=str(data_to2),values=("Padi Sawah Lebak","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Padi Gogo")
                            quality.append("S1")
                            suggestion.append("-")
                elif 30<=average_sm<33:
                    if 22<=average_tt<24 or 29<=average_tt<32:
                        if 5<=average_ph<5.5 or 8.2<=average_ph<8.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Padi Sawah Lebak","S2","24<suhu<29, 5.5<pH<8.2"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Padi Gogo")
                            quality.append("S2")
                            suggestion.append("24<suhu<29, 5.5<pH<8.2")
                elif average_sm<30 or average_sm>90:
                    if 18<=average_tt<22 or 32<=average_tt<35:
                        if average_ph<5 or average_ph>8.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Padi Sawah Lebak","S3","33<kelembaban tanah<90, 24<suhu<29, 5.5<pH<8.2"),tags="quality")
                            data_to2 = data_to2+1
                            plant.append("Padi Gogo")
                            quality.append("S2")
                            suggestion.append("33<kelembaban tanah<90, 24<suhu<29, 5.5<pH<8.2")
                if average_sm<75:
                    if 25<=average_tt<27:
                        if 5.5<=average_ph<8.2:
                            table_plant.insert("","end",text=str(data_to2),values=("Sorgum (Shorgum Bicolor)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Sorgum (Shorgum Bicolor)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 75<=average_sm<85:
                    if 27<=average_tt<30 or 18<=average_tt<25:
                        if 5.3<=average_ph<5.5 or 8.2<average_ph<8.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Sorgum (Shorgum Bicolor)","S2","kelembaban tanah<75, 25<suhu<27, 5.5<ph<8.2"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Sorgum (Shorgum Bicolor)")
                            quality.append("S2")
                            suggestion.append("kelembaban tanah<75, 25<suhu<27, 5.5<ph<8.2")
                elif average_sm>85:
                    if 30<=average_tt<35 or 15<=average_tt<18:
                        if average_ph<5.3 or average_ph>8.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Sorgum (Shorgum Bicolor)","S3","kelembaban tanah<75, 25<suhu<27, 5.5<ph<8.2"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Sorgum (Shorgum Bicolor)")
                            quality.append("S3")
                            suggestion.append("kelembaban tanah<75, 25<suhu<27, 5.5<pH<8.2")
                if 12<=average_tt<23:
                    if 6<=average_ph<8.2:
                        table_plant.insert("","end",text=str(data_to2),values=("Gandum (Truticum aestivum)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Sorgum (Shorgum Bicolor)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 10<=average_tt<12 or 23<=average_tt<25:
                    if 5.6<=average_ph<6 or 8.2<=average_ph<8.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Gandum (Truticum aestivum)","S2","12<suhu<23, 6<pH<8.2"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Sorgum (Shorgum Bicolor)")
                        quality.append("S2")
                        suggestion.append("12<suhu<23, 6<pH<8.2")
                elif 10<=average_tt<12 or 23<=average_tt<25:
                    if average_ph<5.6 or average_ph>8.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Gandum (Truticum aestivum)","S3","12<suhu<23, 6<pH<8.2"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Sorgum (Shorgum Bicolor)")
                        quality.append("S3")
                        suggestion.append("12<suhu<23, 6<pH<8.2")
                if average_sm>42:
                    if 20<=average_tt<26:
                        if 5.8<=average_ph<7.8:
                            table_plant.insert("","end",text=str(data_to2),values=("Jagung (Zea Mays)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Jagung (Zea Mays)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 36<=average_sm<42:
                    if 26<=average_tt<30:
                        if 5.5<=average_ph<5.8 or 7.8<=average_ph<8.2:
                            table_plant.insert("","end",text=str(data_to2),values=("Jagung (Zea Mays)","S2","kelembaban tanah>42, 20<suhu<26, 5.8<pH<7.8"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Jagung (Zea Mays)")
                            quality.append("S2")
                            suggestion.append("kelembaban tanah>42, 20<suhu<26, 5.8<pH<7.8")
                elif 30<=average_sm<36:
                    if 16<=average_tt<20 or 30<=average_tt<32:
                        if average_ph<5.5 or average_ph>8.2:
                            table_plant.insert("","end",text=str(data_to2),values=("Jagung (Zea Mays)","S3","kelembaban tanah>42, 20<suhu<26, 5.8<pH<7.8"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Jagung (Zea Mays)")
                            quality.append("S3")
                            suggestion.append("kelembaban tanah>42, 20<suhu<26, 5.8<pH<7.8")
                if 22<=average_tt<28:
                    if 5.2<=average_ph<7:
                        table_plant.insert("","end",text=str(data_to2),values=("Ubi Kayu(Manihot Esculenta)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Ubi Kayu(Manihot Esculenta)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 28<=average_tt<30:
                    if 4.8<=average_ph<5.2 or 7<average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Ubi Kayu(Manihot Esculenta)","S2","22<suhu<28, 5.2<ph<7"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Ubi Kayu(Manihot Esculenta)")
                        quality.append("S2")
                        suggestion.append("22<suhu<28, 5.2<ph<7")
                elif 18<=average_tt<20 or 30<=average_tt<35:
                    if average_ph<4.8 or average_ph>7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Ubi Kayu(Manihot Esculenta)","S3","22<suhu<28, 5.2<ph<7"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Ubi Kayu(Manihot Esculenta)")
                        quality.append("S3")
                        suggestion.append("22<suhu<28, 5.2<ph<7")
                if average_sm<75:
                    if 22<=average_tt<25:
                        if 5.2<=average_ph<8.2:
                            table_plant.insert("","end",text=str(data_to2),values=("Ubi Jalar(Ipomoea Batatas)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Ubi Jalar(Ipomoea Batatas)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 27<=average_sm<85:
                    if 25<=average_tt<30 or 20<=average_tt<22:
                        if 4.8<=average_ph<5.2 or 8.2<=average_ph<8.4:
                            if average_sm>75:
                                suggest = "kelembaban tanah<75, 22<suhu<25, 5.2<pH<8.2"
                            else:
                                suggest = "22<suhu<25, 5.2<pH<8.2"
                            table_plant.insert("","end",text=str(data_to2),values=("Ubi Jalar(Ipomoea Batatas)","S2",suggest),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Ubi Jalar(Ipomoea Batatas)")
                            quality.append("S2")
                            suggestion.append(suggest)
                elif average_sm>85:
                    if 30<=average_tt<35 or 18<=average_tt<20:
                        if average_ph<4.8 or average_ph>8.4:
                            table_plant.insert("","end",text=str(data_to2),values=("Ubi Jalar(Ipomoea Batatas)","S3","kelembaban tanah<75, 22<suhu<25, 5.2<pH<8.2"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Ubi Jalar(Ipomoea Batatas)")
                            quality.append("S3")
                            suggestion.append("kelembaban tanah<75, 22<suhu<25, 5.2<pH<8.2")
                if 25<=average_tt<31:
                    if 5.5<=average_ph<6.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Talas(Colocasia Asculenta SCHOTT)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Ubi Jalar(Ipomoea Batatas)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 22<=average_tt<25 or average_tt>32:
                    if 5<=average_ph<5.5 or 6.5<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Talas(Colocasia Asculenta SCHOTT)","S2","25<suhu<31, 5.5<pH<6.5"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Ubi Jalar(Ipomoea Batatas)")
                        quality.append("S2")
                        suggestion.append("25<suhu<31, 5.5<pH<6.5")
                elif 20<=average_tt<22:
                    if average_ph<5 or average_ph>7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Talas(Colocasia Asculenta SCHOTT)","S3","25<suhu<31, 5.5<pH<6.5"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Ubi Jalar(Ipomoea Batatas)")
                        quality.append("S3")
                        suggestion.append("25<suhu<31, 5.5<pH<6.5")
                if 26<=average_tt<30:
                    if 5<=average_ph<7:
                        table_plant.insert("","end",text=str(data_to2),values=("Iles-Iles (Amorphophalus Ancophyllus)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Iles-Iles (Amorphophalus Ancophyllus)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 18<=average_tt<32:
                    if 4<=average_ph<5 or 7<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Iles-Iles (Amorphophalus Ancophyllus)","S2","26<suhu<30, 5<pH<7"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Iles-Iles (Amorphophalus Ancophyllus)")
                        quality.append("S2")
                        suggestion.append("26<suhu<30, 5<pH<7")
                elif 18<=average_tt<32:
                    if average_ph<4 or 7<=average_ph>7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Iles-Iles (Amorphophalus Ancophyllus)","S3","26<suhu<30, 5<pH<7"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Iles-Iles (Amorphophalus Ancophyllus)")
                        quality.append("S3")
                        suggestion.append("26<suhu<30, 5<pH<7")
                if 22<=average_tt<25:
                    if 5.5<=average_ph<6.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Hui","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Hui")
                        quality.append("S1")
                        suggestion.append("-")
                elif 20<=average_tt<22 or 25<=average_tt<30:
                    if 6.5<=average_ph<7.5 or 5<=average_ph<5.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Hui","S2","22<suhu<25, 5.5<pH<6.5"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Hui")
                        quality.append("S2")
                        suggestion.append("22<suhu<25, 5.5<pH<6.5")
                elif 30<=average_tt<32 or 18<=average_tt<20:
                    if 7.5<=average_ph<8.5 or 4.5<=average_ph<5:
                        table_plant.insert("","end",text=str(data_to2),values=("Hui","S3","22<suhu<25, 5.5<pH<6.5"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Hui")
                        quality.append("S3")
                        suggestion.append("22<suhu<25, 5.5<pH<6.5")
                if 24<=average_sm<80:
                    if 23<=average_tt<25:
                        if 5.5<=average_ph<7.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Kedelai(Glycine Max)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Kedelai(Glycine Max)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 20<=average_sm<24 or 80<=average_sm<85:
                    if 20<=average_tt<23 or 25<=average_tt<28:
                        if 5<=average_ph<5.5 or 7.5<=average_ph<7.8:
                            table_plant.insert("","end",text=str(data_to2),values=("Kedelai(Glycine Max)","S2","24<kelembaban tanah<80, 23<suhu<25, 5.5<pH<7.5"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Kedelai(Glycine Max)")
                            quality.append("S2")
                            suggestion.append("24<kelembaban tanah<80, 23<suhu<25, 5.5<pH<7.5")
                elif average_sm<20 or average_sm>85:
                    if 18<=average_tt<20 or 28<=average_tt<32:
                        if average_ph<5 or average_ph>7.8:
                            table_plant.insert("","end",text=str(data_to2),values=("Kedelai(Glycine Max)","S3","24<kelembaban tanah<80, 23<suhu<25, 5.5<pH<7.5"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Kedelai(Glycine Max)")
                            quality.append("S3")
                            suggestion.append("24<kelembaban tanah<80, 23<suhu<25, 5.5<pH<7.5")
                if 50<=average_sm<80:
                    if 25<=average_tt<27:
                        if 6<=average_ph<7:
                            table_plant.insert("","end",text=str(data_to2),values=("Kacang Tanah(Arachis Hypogea)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Kacang Tanah(Arachis Hypogea)")
                            quality.append("S1")
                            suggestion.append("-")
                elif average_sm<50 or average_sm>80:
                    if 20<=average_tt<25 or 27<=average_tt<30:
                        if 5<=average_ph<6 or 7<=average_ph<7.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Kacang Tanah(Arachis Hypogea)","S2","50<kelembaban tanah<80, 25<suhu<27, 6<pH<7"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Kacang Tanah(Arachis Hypogea)")
                            quality.append("S2")
                            suggestion.append("50<kelembaban tanah<80, 25<suhu<27, 6<pH<7")
                elif average_sm<50 or average_sm>80:
                    if 18<=average_tt<20 or 30<=average_tt<34:
                        if average_ph<5 or average>7.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Kacang Tanah(Arachis Hypogea)","S3","50<kelembaban tanah<80, 25<suhu<27, 6<pH<7"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Kacang Tanah(Arachis Hypogea)")
                            quality.append("S3")
                            suggestion.append("50<kelembaban tanah<80, 25<suhu<27, 6<pH<7")
                if 42<=average_sm<75:
                    if 12<=average_tt<24:
                        if 5.6<=average_ph<7.6:
                            table_plant.insert("","end",text=str(data_to2),values=("Kacang Hijau(Phaseolus Radiatus LINN)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Kacang Hijau(Phaseolus Radiatus LINN)")
                            quality.append("S1")
                            suggestion.append("-")       
                elif 36<=average_sm<42 or 75<=average_sm<90:
                    if 10<=average_tt<12 or 24<=average_tt<27:
                        if 5.4<=average_ph<5.6 or 7.6<=average_ph<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Kacang Hijau(Phaseolus Radiatus LINN)","S2","42<kelembaban tanah<75, 12<suhu<24, 5.6<pH<7.6"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Kacang Hijau(Phaseolus Radiatus LINN)")
                            quality.append("S2")
                            suggestion.append("42<kelembaban tanah<75, 12<suhu<24, 5.6<pH<7.6")
                elif 30<=average_sm<36 or average_sm>90:
                    if 27<=average_tt<30 or 8<=average_tt<10:
                        if average_ph<5.4 or average_ph>8:
                            table_plant.insert("","end",text=str(data_to2),values=("Kacang Hijau(Phaseolus Radiatus LINN)","S3","42<kelembaban tanah<75, 12<suhu<24, 5.6<pH<7.6"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Kacang Hijau(Phaseolus Radiatus LINN)")
                            quality.append("S3")
                            suggestion.append("42<kelembaban tanah<75, 12<suhu<24, 5.6<pH<7.6")
                if average_sm<80:
                    if 20<=average_tt<30:
                        if 6<=average_ph<7.7:
                            table_plant.insert("","end",text=str(data_to2),values=("Kacang Tunggang(Vigna Unguiculata)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Kacang Tunggang(Vigna Unguiculata)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 80<=average_sm<90:
                    if 19<=average_tt<20 or 30<=average_tt<32:
                        if 5.5<=average_ph<6 or 7.8<=average_ph<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Kacang Tunggang(Vigna Unguiculata)","S2","kelembaban tanah<80, 20<suhu<30, 6<pH<7.8"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Kacang Tunggang(Vigna Unguiculata)")
                            quality.append("S2")
                            suggestion.append("kelembaban tanah<80, 20<suhu<30, 6<pH<7.8")
                elif average_sm>90:
                    if 16<=average_tt<18 or 32<=average_tt<35:
                        if average_ph<5.5 or average_ph>8:
                            table_plant.insert("","end",text=str(data_to2),values=("Kacang Tunggang(Vigna Unguiculata)","S3","kelembaban tanah<80, 20<suhu<30, 6<pH<7.8"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Kacang Tunggang(Vigna Unguiculata)")
                            quality.append("S3")
                            suggestion.append("kelembaban tanah<80, 20<suhu<30, 6<pH<7.8")
                if 16<=average_tt<23:
                    if 6<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Arab(Cicer Arietinum)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Kacang Arab(Cicer Arietinum)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 14<=average_tt<16 or 23<=average_tt<25:
                    if 5.6<=average_ph<6 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Arab(Cicer Arietinum)","S2","16<suhu<23, 6<pH<7.6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Kacang Arab(Cicer Arietinum)")
                        quality.append("S2")
                        suggestion.append("16<suhu<23, 6<pH<7.6")
                elif 12<=average_tt<14 or 25<=average_tt<28:
                    if average_ph<5.6 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Arab(Cicer Arietinum)","S3","16<suhu<23, 6<pH<7.6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Kacang Arab(Cicer Arietinum)")
                        quality.append("S3")
                        suggestion.append("16<suhu<23, 6<pH<7.6")
                if 16<=average_tt<18:
                    if 5.6<=average_ph<7:
                        table_plant.insert("","end",text=str(data_to2),values=("Kentang(Solanum Tuberosum)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Kentang(Solanum Tuberosum)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 14<=average_tt<16 or 18<=average_tt<20:
                    if 5.2<=average_ph<5.6 or 7<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kentang(Solanum Tuberosum)","S2","16<suhu<18, 5.6<pH<7"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Kentang(Solanum Tuberosum)")
                        quality.append("S2")
                        suggestion.append("16<suhu<18, 5.6<pH<7")
                elif 12<=average_tt<14 or 20<=average_tt<23:
                    if average_ph<5.2 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kentang(Solanum Tuberosum)","S3","16<suhu<18, 5.6<pH<7"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Kentang(Solanum Tuberosum)")
                        quality.append("S3")
                        suggestion.append("16<suhu<18, 5.6<pH<7")
                if 40<=average_sm<80:
                    if 16<=average_tt<18:
                        if 6<=average_ph<7:
                            table_plant.insert("","end",text=str(data_to2),values=("Wortel(Daucus Carota)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Wortel(Daucus Carota)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 20<=average_sm<40 or 80<=average_sm<90:
                    if 18<=average_tt<20 or 14<=average_tt<16:
                        if 5.7<=average_ph<6 or 7<=average_ph<7.6:
                            table_plant.insert("","end",text=str(data_to2),values=("Wortel(Daucus Carota)","S2","40<kelembaban tanah<80, 16<suhu<18, 6<pH<7"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Wortel(Daucus Carota)")
                            quality.append("S2")
                            suggestion.append("40<kelembaban tanah<80, 16<suhu<18, 6<pH<7")
                elif average_sm<20 or average_sm>90:
                    if 20<=average_tt<23 or 12<=average_tt<16:
                        if average_ph<5.7 or average_ph>7.6:
                            table_plant.insert("","end",text=str(data_to2),values=("Wortel(Daucus Carota)","S3","40<kelembaban tanah<80, 16<suhu<18, 6<pH<7"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Wortel(Daucus Carota)")
                            quality.append("S3")
                            suggestion.append("40<kelembaban tanah<80, 16<suhu<18, 6<pH<7")
                if 16<=average_tt<18:
                    if 6<=average_ph<7:
                        table_plant.insert("","end",text=str(data_to2),values=("Lobak(Raphanus Sativur)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Lobak(Raphanus Sativur)")
                        quality.append("S1")
                        suggestion.append("-")
                if 18<=average_tt<20 or 14<average_tt<16:
                    if 5.7<=average_ph<6 or 7<average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Lobak(Raphanus Sativur)","S2","16<suhu<18, 6<pH<7"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Lobak(Raphanus Sativur)")
                        quality.append("S2")
                        suggestion.append("16<suhu<18, 6<pH<7")
                elif 20<=average_tt<23 or 12<average_tt<16:
                    if average_ph>7.6 or average_ph<5.7:
                        table_plant.insert("","end",text=str(i),values=("Lobak(Raphanus Sativur)","S3","16<suhu<18, 6<pH<7"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Lobak(Raphanus Sativur)")
                        quality.append("S3")
                        suggestion.append("16<suhu<18, 6<pH<7")
                if 20<=average_tt<25:
                    if 6<=average_ph<7.8:
                        table_plant.insert("","end",text=str(data_to2),values=("Bawang Merah(Aillium Ascolonicum)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Bawang Merah(Aillium Ascolonicum)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 25<=average_tt<30 or 18<=average_tt<20:
                    if 5.8<=average_ph<6 or 7.8<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Bawang Merah(Aillium Ascolonicum)","S2","20<suhu<25, 6<pH<7.8"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Bawang Merah(Aillium Ascolonicum)")
                        quality.append("S2")
                        suggestion.append("20<suhu<25, 6<pH<7.8")
                elif 30<=average_tt<35 or 15<=average_tt<18:
                    if average_ph<5.8 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Bawang Merah(Aillium Ascolonicum)","S3","20<suhu<25, 6<pH<7.8"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Bawang Merah(Aillium Ascolonicum)")
                        quality.append("S3")
                        suggestion.append("20<suhu<25, 6<pH<7.8")
                if 16<=average_tt<18:
                    if 6<=average_ph<7.8:
                        table_plant.insert("","end",text=str(data_to2),values=("Bawang Putih(Aillium Sativum)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Bawang Putih(Aillium Sativum)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 18<=average_tt<20 or 14<=average_tt<16:
                    if 5.8<=average_ph<6 or 7.8<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Bawang Putih(Aillium Sativum)","S2","16<suhu<18, 6<pH<7.8"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Bawang Putih(Aillium Sativum)")
                        quality.append("S2")
                        suggestion.append("16<suhu<18, 6<pH<7.8")
                elif 20<=average_tt<23 or 12<=average_tt<16:
                    if average_ph<5.8 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Bawang Putih(Aillium Sativum)","S3","16<suhu<18, 6<pH<7.8"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Bawang Putih(Aillium Sativum)")
                        quality.append("S3")
                        suggestion.append("16<suhu<18, 6<pH<7.8")
                if 21<=average_tt<27:
                    if 6<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Cabai Merah(Capsicum annuum)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Cabai Merah(Capsicum annuum)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 16<=average_tt<21 or 27<=average_tt<28:
                    if 5.5<=average_ph<6 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Cabai Merah(Capsicum annuum)","S2","21<suhu<27, 6<ph<7.6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Cabai Merah(Capsicum annuum)")
                        quality.append("S2")
                        suggestion.append("21<suhu<27, 6<ph<7.6")
                elif 14<=average_tt<16 or 28<=average_tt<30:
                    if average_ph<5.5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Cabai Merah(Capsicum annuum)","S3","21<suhu<27, 6<ph<7.6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Cabai Merah(Capsicum annuum)")
                        quality.append("S3")
                        suggestion.append("21<suhu<27, 6<ph<7.6")
                if 18<=average_tt<26:
                    if 6<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Paprika(Capsium Sp.)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Paprika(Capsium Sp.)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 16<=average_tt<18 or 26<=average_tt<27:
                    if 5.5<=average_ph<6 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Paprika(Capsium Sp.)","S2","18<suhu<26, 6<ph<7.6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Paprika(Capsium Sp.)")
                        quality.append("S2")
                        suggestion.append("18<suhu<26, 6<ph<7.6")
                elif 14<=average_tt<16 or 27<=average_tt<28:
                    if average_ph<5.5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Paprika(Capsium Sp.)","S3","18<suhu<26, 6<ph<7.6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Paprika(Capsium Sp.)")
                        quality.append("S3")
                        suggestion.append("18<suhu<26, 6<ph<7.6")
                if 13<=average_tt<24:
                    if 6<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Kubis(Brassica Oleracea L.)","S1","13<suhu<24, 6<pH<7.6"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Kubis(Brassica Oleracea L.)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 10<=average_tt<13 or 24<=average_tt<30:
                    if 5.5<=average_ph<6 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kubis(Brassica Oleracea L.)","S2","13<suhu<24, 6<pH<7.6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Kubis(Brassica Oleracea L.)")
                        quality.append("S2")
                        suggestion.append("13<suhu<24, 6<pH<7.6")
                elif 5<=average_tt<10 or 30<=average_tt<35:
                    if average_ph<5.5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kubis(Brassica Oleracea L.)","S3","13<suhu<24, 6<pH<7.6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Kubis(Brassica Oleracea L.)")
                        quality.append("S3")
                        suggestion.append("13<suhu<24, 6<pH<7.6")
                if 13<=average_tt<24:
                    if 6<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Lettuce(Lacuce Sativa)","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Lettuce(Lacuce Sativa)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 22<=average_tt<28:
                    if 5.7<=average_ph<6 or 7<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Lettuce(Lacuce Sativa)","S2","13<suhu<24, 6<pH<7.6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Lettuce(Lacuce Sativa)")
                        quality.append("S2")
                        suggestion.append("16<suhu<22, 6<pH<7")
                elif 28<=average_tt<35:
                    if average_ph>7.6 or average_ph<5.7:
                        table_plant.insert("","end",text=str(data_to2),values=("Lettuce(Lacuce Sativa)","S3","13<suhu<24, 6<pH<7.6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Lettuce(Lacuce Sativa)")
                        quality.append("S3")
                        suggestion.append("16<suhu<22, 6<pH<7")
                if 16<=average_tt<22:
                    if 6<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Petsai (Brassica Purpureum SCHUM)","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Petsai (Brassica Purpureum SCHUM)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 22<=average_tt<28 or 13<average_tt<16:
                    if 5.7<=average_ph<6 or 7<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Petsai (Brassica Purpureum SCHUM)","S2","16<suhu<22, 6<pH<7"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Petsai (Brassica Purpureum SCHUM)")
                        quality.append("S2")
                        suggestion.append("16<suhu<22, 6<pH<7")
                elif 28<=average_tt<35 or 4<average_tt<13:
                    if average_ph<5.7 or average_ph>7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Petsai (Brassica Purpureum SCHUM)","S3","16<suhu<22, 6<pH<7"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Petsai (Brassica Purpureum SCHUM)")
                        quality.append("S3")
                        suggestion.append("16<suhu<22, 6<pH<7")
                if 16<=average_tt<22:
                    if 6<=average_ph<7:
                        table_plant.insert("","end",text=str(data_to2),values=("Sawi (Brassica Rugosa SCHUM)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Sawi (Brassica Rugosa SCHUM)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 22<=average_tt<28 or 13<=average_ph<16:
                    if 7<=average_ph<7.6 or 5.7<=average_ph<6:
                        table_plant.insert("","end",text=str(data_to2),values=("Sawi (Brassica Rugosa SCHUM)","S2","16<suhu<22, 6<pH<7"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Sawi (Brassica Rugosa SCHUM)")
                        quality.append("S2")
                        suggestion.append("16<suhu<22, 6<pH<7")
                elif 4<=average_tt<13 or 28<=average_ph<35:
                    if average_ph<5.6 or average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Sawi (Brassica Rugosa SCHUM)","S3","16<suhu<22, 6<pH<7"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Sawi (Brassica Rugosa SCHUM)")
                        quality.append("S3")
                        suggestion.append("16<suhu<22, 6<pH<7")
                if 12<=average_tt<24:
                    if 5.6<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Bayam(Amaranthus Spe.div)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Bayam(Amaranthus Spe.div)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 10<=average_tt<12 or 24<=average_tt<27:
                    if 5.4<=average_ph<5.6 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Bayam(Amaranthus Spe.div)","S2","12<suhu<24, 5.6<pH<7.6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Bayam(Amaranthus Spe.div)")
                        quality.append("S2")
                        suggestion.append("12<suhu<24, 5.6<pH<7.6")
                elif 27<=average_tt<30 or 8<=average_tt<10:
                    if average_ph<5.4 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Bayam(Amaranthus Spe.div)","S3","12<suhu<24, 5.6<pH<7.6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Bayam(Amaranthus Spe.div)")
                        quality.append("S3")
                        suggestion.append("12<suhu<24, 5.6<pH<7.6")
                if 12<=average_tt<24:
                    if 5.6<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Buncis(Phaseolus Vulgaris)","S1","12<suhu<24, 5.6<pH<7.6"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Buncis(Phaseolus Vulgaris)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 10<=average_tt<12 or 24<=average_tt<27:
                    if 5.4<=average_ph<5.6 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Buncis(Phaseolus Vulgaris)","S2","12<suhu<24, 5.6<pH<7.6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Buncis(Phaseolus Vulgaris)")
                        quality.append("S2")
                        suggestion.append("12<suhu<24, 5.6<pH<7.6")
                elif 27<=average_tt<30 or 8<=average_tt<12:
                    if average_ph<5.4 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Buncis(Phaseolus Vulgaris)","S3","12<suhu<24, 5.6<pH<7.6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Buncis(Phaseolus Vulgaris)")
                        quality.append("S3")
                        suggestion.append("12<suhu<24, 5.6<pH<7.6")
                if 12<=average_tt<24:
                    if 5.6<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Panjang(Vigina Sinensis ENDL)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Kacang Panjang(Vigina Sinensis ENDL)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 10<=average_tt<12 or 24<=average_tt<27:
                    if 5.4<=average_ph<5.6 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Panjang(Vigina Sinensis ENDL)","S2","12<suhu<24, 5.6<pH<7.6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Kacang Panjang(Vigina Sinensis ENDL)")
                        quality.append("S2")
                        suggestion.append("12<suhu<24, 5.6<pH<7.6")
                elif 27<=average_tt<30 or 8<=average_tt<10:
                    if average_ph<5.4 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Panjang(Vigina Sinensis ENDL)","S3","12<suhu<24, 5.6<pH<7.6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Kacang Panjang(Vigina Sinensis ENDL)")
                        quality.append("S3")
                        suggestion.append("12<suhu<24, 5.6<pH<7.6")
                if 14<=average_tt<20:
                    if 6<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Kapri(Pisum Sativum)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Kacang Kapri(Pisum Sativum)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 10<=average_tt<14 or 20<=average_tt<23:
                    if 5.8<=average_ph<6 or 7.5<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Kapri(Pisum Sativum)","S2","14<suhu<20, 6<pH<7.5"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Kacang Kapri(Pisum Sativum)")
                        quality.append("S2")
                        suggestion.append("14<suhu<20, 6<pH<7.5")
                elif 8<=average_tt<10 or 23<=average_tt<25:
                    if average_ph<5.8 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Kapri(Pisum Sativum)","S3","14<suhu<20, 6<pH<7.5"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Kacang Kapri(Pisum Sativum)")
                        quality.append("S3")
                        suggestion.append("14<suhu<20, 6<pH<7.5")
                if 22<=average_tt<30:
                    if 5.8<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Mentimun(Cucumis Sativus LINN)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Mentimun(Cucumis Sativus LINN)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 30<=average_tt<32 or 20<=average_tt<22:
                    if 5.5<=average_ph<5.8 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Mentimun(Cucumis Sativus LINN)","S2","22<suhu<30, 5.8<pH<7.6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Mentimun(Cucumis Sativus LINN)")
                        quality.append("S2")
                        suggestion.append("22<suhu<30, 5.8<pH<7.6")
                elif 32<=average_tt<35 or 18<=average_tt<20:
                    if average_ph<5.5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Mentimun(Cucumis Sativus LINN)","S3","22<suhu<30, 5.8<pH<7.6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Mentimun(Cucumis Sativus LINN)")
                        quality.append("S3")
                        suggestion.append("22<suhu<30, 5.8<pH<7.6")
                if 18<=average_tt<26:
                    if 6<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Terung(Solannum Melongen LINN)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Terung(Solannum Melongen LINN)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 16<=average_tt<18 or 26<=average_tt<30:
                    if 5.5<=average_ph<6 or 7.5<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Terung(Solannum Melongen LINN)","S2","18<suhu<26, 6<pH<7.5"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Terung(Solannum Melongen LINN)")
                        quality.append("S2")
                        suggestion.append("18<suhu<26, 6<pH<7.5")
                elif 30<=average_tt<35 or 13<=average_tt<16:
                    if average_ph<5.5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Terung(Solannum Melongen LINN)","S3","18<suhu<26, 6<pH<7.5"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Terung(Solannum Melongen LINN)")
                        quality.append("S3")
                        suggestion.append("18<suhu<26, 6<pH<7.5")
                if 18<=average_tt<25:
                    if 5.5<=average_ph<7.8:
                        table_plant.insert("","end",text=str(data_to2),values=("Pare(Momordica Charantia LINN)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Pare(Momordica Charantia LINN)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 15<=average_tt<18 or 25<=average_tt<30:
                    if 5<=average_ph<5.5 or 7.8<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Pare(Momordica Charantia LINN)","S2","18<suhu<25, 5.5<pH<7.8"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Pare(Momordica Charantia LINN)")
                        quality.append("S2")
                        suggestion.append("18<suhu<25, 5.5<pH<7.8")
                elif 30<=average_tt<35 or 10<=average_tt<15:
                    if average_ph<5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Pare(Momordica Charantia LINN)","S3","18<suhu<25, 5.5<pH<7.8"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Pare(Momordica Charantia LINN)")
                        quality.append("S3")
                        suggestion.append("18<suhu<25, 5.5<pH<7.8")
                if 13<=average_tt<24:
                    if 6<=average_ph<7.8:
                        table_plant.insert("","end",text=str(data_to2),values=("Brokoli(Brassica)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Brokoli(Brassica)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 10<=average_tt<13 or 24<=average_tt<30:
                    if 5.6<=average_ph<6 or 7.8<average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Brokoli(Brassica)","S2","13<suhu<24, 6<pH<7.8"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Brokoli(Brassica)")
                        quality.append("S2")
                        suggestion.append("13<suhu<24, 6<pH<7.8")
                elif 30<=average_tt<35 or 5<=average_tt<10:
                    if average_ph<5.6 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Brokoli(Brassica)","S3","13<suhu<24, 6<pH<7.8"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Brokoli(Brassica)")
                        quality.append("S3")
                        suggestion.append("13<suhu<24, 6<pH<7.8")
                if 12<=average_tt<24:
                    if 5.6<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Asparagus(Asparagus Officinnalis LINN)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Asparagus(Asparagus Officinnalis LINN)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 10<=average_tt<12 or 24<=average_tt<27:
                    if 5.4<=average_ph<5.6 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Asparagus(Asparagus Officinnalis LINN)","S2","12<suhu<24, 5.6<pH<7.6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Asparagus(Asparagus Officinnalis LINN)")
                        quality.append("S2")
                        suggestion.append("12<suhu<24, 5.6<pH<7.6")
                elif 8<=average_tt<10 or 27<=average_tt<30:
                    if average_ph<5.4 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Asparagus(Asparagus Officinnalis LINN)","S3","12<suhu<24, 5.6<pH<7.6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Asparagus(Asparagus Officinnalis LINN)")
                        quality.append("S3")
                        suggestion.append("12<suhu<24, 5.6<pH<7.6")
                if 40<=average_sm<80:
                    if 16<=average_tt<22:
                        if 6<=average_ph<7:
                            table_plant.insert("","end",text=str(data_to2),values=("Biet(Beta Vulgaris L.)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Biet(Beta Vulgaris L.)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 20<=average_sm<40 or 80<=average_sm<90:
                    if 22<=average_tt<28 or 13<=average_tt<16:
                        if 5.7<=average_ph<6 or 7<=average_ph<7.6:
                            table_plant.insert("","end",text=str(data_to2),values=("Biet(Beta Vulgaris L.)","S2","40<kelembaban tanah<80, 16<suhu<22, 6<pH<7"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Biet(Beta Vulgaris L.)")
                            quality.append("S2")
                            suggestion.append("40<kelembaban tanah<80, 16<suhu<22, 6<pH<7")
                elif average_sm<20 or average_sm>90:
                    if 28<=average_tt<35 or 4<=average_tt<13:
                        if average_ph<5.7 or average_ph>7.6:
                            table_plant.insert("","end",text=str(data_to2),values=("Biet(Beta Vulgaris L.)","S3","40<kelembaban tanah<80, 16<suhu<22, 6<pH<7"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Biet(Beta Vulgaris L.)")
                            quality.append("S3")
                            suggestion.append("40<kelembaban tanah<80, 16<suhu<22, 6<pH<7")
                if 40<=average_sm<80:
                    if 16<=average_tt<22:
                        if 6<=average_ph<7:
                            table_plant.insert("","end",text=str(data_to2),values=("Kalian(Brassica Oleracea Var. Acephala)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Kalian(Brassica Oleracea Var. Acephala)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 20<=average_sm<40 or 80<=average_sm<90:
                    if 22<=average_tt<28 or 13<=average_tt<16:
                        if 5.7<=average_ph<6 or 7<=average_ph<7.6:
                            table_plant.insert("","end",text=str(data_to2),values=("Kalian(Brassica Oleracea Var. Acephala)","S2","40<kelembaban tanah<80, 16<suhu<22, 6<pH<7"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Kalian(Brassica Oleracea Var. Acephala)")
                            quality.append("S2")
                            suggestion.append("40<kelembaban tanah<80, 16<suhu<22, 6<pH<7")
                elif average_sm<20 or average_sm>90:
                    if 28<=average_tt<35 or 4<=average_tt<13:
                        if average_ph<5.7 or average_ph>7.6:
                            table_plant.insert("","end",text=str(data_to2),values=("Kalian(Brassica Oleracea Var. Acephala)","S3","40<kelembaban tanah<80, 16<suhu<22, 6<pH<7"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Kalian(Brassica Oleracea Var. Acephala)")
                            quality.append("S3")
                            suggestion.append("40<kelembaban tanah<80, 16<suhu<22, 6<pH<7")
                if 24<=average_sm<80:
                    if 18<=average_tt<26:
                        if 6<=average_ph<7.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Tomat Sayur(Solanum Lycopersicon esculenta LINN)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Tomat Sayur(Solanum Lycopersicon esculenta LINN)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 20<=average_sm<24 or 80<=average_sm<90:
                    if 26<=average_tt<30 or 16<=average_tt<18:
                        if 5.5<=average_ph<6 or 7.5<=average_ph<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Tomat Sayur(Solanum Lycopersicon esculenta LINN)","S2","24<kelembaban tanah<80, 18<suhu<26, 6<pH<7.5"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Tomat Sayur(Solanum Lycopersicon esculenta LINN)")
                            quality.append("S2")
                            suggestion.append("24<kelembaban tanah<80, 18<suhu<26, 6<pH<7.5")
                elif average_sm>90 or average_sm<20:
                    if 30<=average_tt<35 or 13<=average_tt<16:
                        if average_ph<5.5 or average_ph>8:
                            table_plant.insert("","end",text=str(data_to2),values=("Tomat Sayur(Solanum Lycopersicon esculenta LINN)","S3","18<24<kelembaban tanah<80, suhu<26, 6<pH<7.5"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Tomat Sayur(Solanum Lycopersicon esculenta LINN)")
                            quality.append("S3")
                            suggestion.append("24<kelembaban tanah<80, 18<suhu<26, 6<pH<7.5")
                if average_sm>42:
                    if 18<=average_tt<25:
                        if 5.5<=average_ph<7.8:
                            table_plant.insert("","end",text=str(data_to2),values=("Petai(Parkia Speciosa HASSK)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Petai(Parkia Speciosa HASSK)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 36<=average_sm<42:
                    if 15<=average_tt<18 or 25<=average_tt<30:
                        if 5<=average_ph<5.5 or 7.8<=average_ph<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Petai(Parkia Speciosa HASSK)","S2","kelembaban tanah>42, 18<suhu<25, 5.5<pH<7.8"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Petai(Parkia Speciosa HASSK)")
                            quality.append("S2")
                            suggestion.append("kelembaban tanah>42, 18<suhu<25, 5.5<pH<7.8")
                elif 30<=average_sm<36:
                    if 30<=average_tt<35 or 10<=average_tt<15:
                        if average_ph<5 or average_ph>8:
                            table_plant.insert("","end",text=str(data_to2),values=("Petai(Parkia Speciosa HASSK)","S3","kelembaban tanah>42, 18<suhu<25, 5.5<pH<7.8"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Petai(Parkia Speciosa HASSK)")
                            quality.append("S3")
                            suggestion.append("kelembaban tanah>42, 18<suhu<25, 5.5<pH<7.8")
                if average_sm>60:
                    if 25<=average_tt<27:
                        if 5.6<=average_ph<7.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Pisang(Musa Acuminate COLLA)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Pisang(Musa Acuminate COLLA)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 50<=average_sm<60:
                    if 22<=average_tt<25 or 27<=average_tt<30:
                        if 5.2<=average_ph<5.6 or 7.5<=average_ph<8.2:
                            table_plant.insert("","end",text=str(data_to2),values=("Pisang(Musa Acuminate COLLA)","S2","kelembaban tanah>60, 25<suhu<27, 5.6<pH<7.5"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Pisang(Musa Acuminate COLLA)")
                            quality.append("S2")
                            suggestion.append("kelembaban tanah>60, 25<suhu<27, 5.6<pH<7.5")
                elif 30<=average_sm<50:
                    if 30<=average_tt<35 or 22<=average_tt<25:
                        if average_ph<5.2 or average_ph>8.2: 
                            table_plant.insert("","end",text=str(data_to2),values=("Pisang(Musa Acuminate COLLA)","S3","kelembaban tanah>60, 25<suhu<27, 5.6<pH<7.5"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Pisang(Musa Acuminate COLLA)")
                            quality.append("S3")
                            suggestion.append("kelembaban tanah>60, 25<suhu<27, 5.6<pH<7.5")
                if 24<=average_sm<80:
                    if 25<=average_tt<28:
                        if 6<=average_ph<6.6:
                            table_plant.insert("","end",text=str(data_to2),values=("Papaya(Carica Papaya L)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Papaya(Carica Papaya L)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 20<=average_sm<24 or 80<=average_sm<90:
                    if 28<=average_tt<34 or 20<=average_tt<25:
                        if 5.5<=average_ph<6 or average_ph>6.6:
                            table_plant.insert("","end",text=str(data_to2),values=("Papaya(Carica Papaya L)","S2","24<kelembaban tanah<80, 25<suhu<28, 6<pH<6.6"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Papaya(Carica Papaya L)")
                            quality.append("S2")
                            suggestion.append("24<kelembaban tanah<80, 25<suhu<28, 6<pH<6.6")
                elif average_sm<20 or average_sm>90:
                    if 34<=average_tt<38 or 15<=average_tt<20:
                        if average_ph<5.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Papaya(Carica Papaya L)","S3","24<kelembaban tanah<80, 25<suhu<28, 6<pH<6.6"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Papaya(Carica Papaya L)")
                            quality.append("S3")
                            suggestion.append("24<kelembaban tanah<80, 25<suhu<28, 6<pH<6.6")
                if 24<=average_sm<80:
                    if 18<=average_tt<26:
                        if 6<=average_ph<7.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Tomat buah(Solamun lycopersicon)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Tomat buah/ Solamun lycopersicon")
                            quality.append("S1")
                            suggestion.append("-")
                elif 20<=average_sm<24 or 80<=average_sm<90:
                    if 26<=average_tt<30 or 16<=average_tt<18:
                        if 5.5<=average_ph<6 or 7.5<=average_tt<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Tomat buah(Solamun lycopersicon)","S2","24<kelembaban tanah<80, 18<suhu<26, 6<pH<7.5"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Tomat buah/ Solamun lycopersicon")
                            quality.append("S2")
                            suggestion.append("24<kelembaban tanah<80, 18<suhu<26, 6<pH<7.5")
                elif average_sm>90 or average_sm<24:
                    if 30<=average_tt<35 or 13<=average_tt<16:
                        if average_ph<5.5 or average_tt>8:
                            table_plant.insert("","end",text=str(data_to2),values=("Tomat buah(Solamun lycopersicon)","S3","24<kelembaban tanah<80, 18<suhu<26, 6<pH<7.5"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Tomat buah/ Solamun lycopersicon")
                            quality.append("S3")
                            suggestion.append("24<kelembaban tanah<80, 18<suhu<26, 6<pH<7.5")
                if 50<=average_sm<90:
                    if 19<=average_tt<33:
                        if 5.5<=average_ph<7.6:
                            table_plant.insert("","end",text=str(data_to2),values=("Jeruk(Citrus aurantium)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Jeruk(Citrus aurantium)")
                            quality.append("S1")
                            suggestion.append("-")
                elif average_sm>90 or average_sm<50:
                    if 16<=average_tt<19 or 33<=average_tt<36:
                        if 5.2<=average_ph<5.5 or 7.6<=average_ph<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Jeruk(Citrus aurantium)","S2","50<kelembaban tanah<90, 19<suhu<33, 5.5<pH<7.6"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Jeruk(Citrus aurantium)")
                            quality.append("S2")
                            suggestion.append("50<kelembaban tanah<90, 19<suhu<33, 5.5<pH<7.6")
                elif 16<=average_tt<19 or 33<=average_tt<36:
                    if 5.2<=average_ph<5.5 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Jeruk(Citrus aurantium)","S3","50<kelembaban tanah<90, 19<suhu<33, 5.5<pH<7.6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Jeruk(Citrus aurantium)")
                        quality.append("S3")
                        suggestion.append("50<kelembaban tanah<90, 19<suhu<33, 5.5<pH<7.6")
                if average_sm>42:
                    if 16<=average_tt<20:
                        if 5.5<=average_ph<7.8:
                            table_plant.insert("","end",text=str(data_to2),values=("Apel(Malus silveris MILL)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Apel(Malus silveris MILL)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 36<=average_sm<42:
                    if 13<=average_tt<26 or 20<average_tt<25:
                        if 5<=average_ph<5.5 or 7.8<=average_ph<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Apel(Malus silveris MILL)","S2","kelembaban tanah>42, 16<suhu<20, 5.5<pH<7.8"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Apel(Malus silveris MILL)")
                            quality.append("S2")
                            suggestion.append("kelembaban tanah>42, 16<suhu<20, 5.5<pH<7.8")
                elif 25<=average_sm<36:
                    if 10<=average_tt<13 or 25<average_tt<27:
                        if average_ph<5 or average_ph>8:
                            table_plant.insert("","end",text=str(data_to2),values=("Apel(Malus silveris MILL)","S3","kelembaban tanah>42, 16<suhu<20, 5.5<pH<7.8"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Apel(Malus silveris MILL)")
                            quality.append("S3")
                            suggestion.append("kelembaban tanah>42, 16<suhu<20, 5.5<pH<7.8")
                if 18<=average_tt<26 :
                    if 5<average_ph<6.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Alpukat(Persea americana)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Alpukat(Persea americana)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 26<=average_tt<30 or 15<=average_tt<18 :
                    if 4.6<average_ph<5 or 6.5<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Alpukat(Persea americana)","S2","18<suhu<26, 5<pH<6.5"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Alpukat(Persea americana)")
                        quality.append("S2")
                        suggestion.append("18<suhu<26, 5<pH<6.5")
                elif average_tt>30 or 10<=average_tt<15 :
                    if average_ph<4.6 or average_ph>7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Alpukat(Persea americana)","S3","18<suhu<26, 5<pH<6.5"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Alpukat(Persea americana)")
                        quality.append("S3")
                        suggestion.append("18<suhu<26, 5<pH<6.5")
                if average_sm>42:
                    if 22<=average_tt<28:
                        if 5.5<=average_ph<7.8:
                            table_plant.insert("","end",text=str(data_to2),values=("Manga(Mangifera indic)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Manga(Mangifera indica)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 36<=average_sm<42:
                    if 18<=average_tt<22 or 28<=average_tt<34:
                        if 5<=average_ph<5.5 or 7.8<=average_tt<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Manga(Mangifera indic)","S2","kelembaban tanah>42, 22<suhu<28, 5.5<pH<7.8"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Manga(Mangifera indica)")
                            quality.append("S2")
                            suggestion.append("kelembaban tanah>42, 22<suhu<28, 5.5<pH<7.8")
                elif 30<=average_sm<36:
                    if 15<=average_tt<18 or 34<=average_tt<40:
                        if average_ph<5 or average_ph>8:
                            table_plant.insert("","end",text=str(data_to2),values=("Manga(Mangifera indic)","S3","kelembaban tanah>42, 22<suhu<28, 5.5<pH<7.8"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Manga(Mangifera indica)")
                            quality.append("S3")
                            suggestion.append("kelembaban tanah>42, 22<suhu<28, 5.5<pH<7.8")
                if 25<=average_tt<28:
                    if 5<=average_ph<6:
                        table_plant.insert("","end",text=str(data_to2),values=("Rambutan(Nephelium lappaceun LINN)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Rambutan(Nephelium lappaceun LINN)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 28<=average_tt<32 or 22<=average_tt<25:
                    if 4.5<=average_ph<5 or 6<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Rambutan(Nephelium lappaceun LINN)","S2","25<suhu<28, 5<pH<6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Rambutan(Nephelium lappaceun LINN)")
                        quality.append("S2")
                        suggestion.append("25<suhu<28, 5<pH<6")
                elif 32<=average_tt<35 or 20<=average_tt<22:
                    if average_ph<4.5 or average_ph>7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Rambutan(Nephelium lappaceun LINN)","S3","25<suhu<28, 5<pH<6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Rambutan(Nephelium lappaceun LINN)")
                        quality.append("S3")
                        suggestion.append("25<suhu<28, 5<pH<6")
                if 22<=average_tt<28:
                    if 5<=average_ph<6:
                        table_plant.insert("","end",text=str(data_to2),values=("Jambu biji(Psidium guajava LINN)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Jambu biji(Psidium guajava LINN)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 28<=average_tt<34 or 18<=average_tt<22:
                    if 4.5<=average_ph<5 or 6<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Jambu biji(Psidium guajava LINN)","S2","22<suhu<28, 5<pH<6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Jambu biji(Psidium guajava LINN)")
                        quality.append("S2")
                        suggestion.append("22<suhu<28, 5<pH<6")
                elif 34<=average_tt<40 or 15<=average_tt<18:
                    if average_ph<4.5 or average_ph>7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Jambu biji(Psidium guajava LINN)","S3","22<suhu<28, 5<pH<6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Jambu biji(Psidium guajava LINN)")
                        quality.append("S3")
                        suggestion.append("22<suhu<28, 5<pH<6")
                if 22<=average_tt<28:
                    if 5<=average_ph<6:
                        table_plant.insert("","end",text=str(data_to2),values=("Jambu siam(Psidium guajava)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Jambu siam(Psidium guajava)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 28<=average_tt<34 or 18<=average_tt<22:
                    if 4.5<=average_ph<5 or 6<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Jambu siam(Psidium guajava)","S2","22<suhu<28, 5<pH<6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Jambu siam(Psidium guajava)")
                        quality.append("S2")
                        suggestion.append("22<suhu<28, 5<pH<6")
                elif 34<=average_tt<40 or 15<=average_tt<18:
                    if average_ph<4.5 or average_ph>7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Jambu siam(Psidium guajava)","S3","22<suhu<28, 5<pH<6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Jambu siam(Psidium guajava)")
                        quality.append("S3")
                        suggestion.append("22<suhu<28, 5<pH<6")
                if average_sm>42:
                    if 25<=average_tt<28:
                        if 5.5<=average_ph<7.8:
                            table_plant.insert("","end",text=str(data_to2),values=("Durian(Durio zibethinus MURR)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Durian(Durio zibethinus MURR)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 36<=average_sm<42:
                    if 22<=average_tt<25 or 28<=average_tt<32:
                        if 5<=average_ph<5.5 or 7.8<=average_ph<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Durian(Durio zibethinus MURR)","S2","kelembaban tanah>42, 25<suhu<28, 5.5<pH<7.8"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Durian(Durio zibethinus MURR)")
                            quality.append("S2")
                            suggestion.append("kelembaban tanah>42, 25<suhu<28, 5.5<pH<7.8")
                elif 30<=average_sm<36:
                    if 32<=average_tt<35 or 20<=average_tt<22:
                        if average_ph<5 or average_ph>8:
                            table_plant.insert("","end",text=str(data_to2),values=("Durian(Durio zibethinus MURR)","S3","kelembaban tanah>42, 25<suhu<28, 5.5<pH<7.8"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Durian(Durio zibethinus MURR)")
                            quality.append("S3")
                            suggestion.append("kelembaban tanah>42, 25<suhu<28, 5.5<pH<7.8")
                if average_sm>42:
                    if 22<=average_tt<25:
                        if 5.5<=average_ph<7.8:
                            table_plant.insert("","end",text=str(data_to2),values=("Belimbing(Averrhoa bilimbi)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Belimbing(Averrhoa bilimbi)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 36<=average_sm<42:
                    if 22<=average_tt<18 or 25<=average_tt<30:
                        if 5<=average_ph<5.5 or 7.8<=average_ph<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Belimbing(Averrhoa bilimbi)","S2","kelembaban tanah>42, 22<suhu<25, 5.5<pH<7.8"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Belimbing(Averrhoa bilimbi)")
                            quality.append("S2")
                            suggestion.append("kelembaban tanah>42, 25<suhu<28, 5.5<pH<7.8")
                elif 30<=average_sm<36:
                    if 30<=average_tt<35 or 10<=average_tt<18:
                        if average_ph<5 or average_ph>8:
                            table_plant.insert("","end",text=str(data_to2),values=("Belimbing(Averrhoa bilimbi)","S3","kelembaban tanah>42, 22<suhu<25, 5.5<pH<7.8"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Belimbing(Averrhoa bilimbi)")
                            quality.append("S3")
                            suggestion.append("kelembaban tanah>42, 22<suhu<25, 5.5<pH<7.8")
                if 24<=average_sm<80:
                    if 22<=average_tt<30:
                        if 5.8<=average_ph<7.6:
                            table_plant.insert("","end",text=str(data_to2),values=("Semangka(Colocynthis citrullus)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Semangka(Colocynthis citrullus)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 20<=average_sm<24 or 80<=average_sm<90:
                    if 30<=average_tt<32 or 20<=average_tt<22:
                        if 5.5<=average_ph<5.8 or 7.6<=average_ph<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Semangka(Colocynthis citrullus)","S2","24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Semangka(Colocynthis citrullus)")
                            quality.append("S2")
                            suggestion.append("24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6")
                elif average_sm<20 or average_sm>90:
                    if 33<=average_tt<35 or 18<=average_tt<20:
                        if average_ph<5.5 or average_ph>8:
                            table_plant.insert("","end",text=str(data_to2),values=("Semangka(Colocynthis citrullus)","S3","24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Semangka(Colocynthis citrullus)")
                            quality.append("S3")
                            suggestion.append("24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6")
                if 24<=average_sm<80:
                    if 22<=average_tt<30:
                        if 5.8<=average_ph<7.6:
                            table_plant.insert("","end",text=str(data_to2),values=("Blewah(Passiflora quadranglaria LINN)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Blewah(Passiflora quadranglaria LINN)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 20<=average_sm<24 or 80<=average_sm<90:
                    if 30<=average_tt<32 or 20<=average_tt<22:
                        if 5.5<=average_ph<5.8 or 7.6<=average_ph<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Blewah(Passiflora quadranglaria LINN)","S2","24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Blewah(Passiflora quadranglaria LINN)")
                            quality.append("S2")
                            suggestion.append("24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6")
                elif average_sm<20 or average_sm>90:
                    if 33<=average_tt<35 or 18<=average_tt<20:
                        if average_ph<5.5 or average_ph>8:
                            table_plant.insert("","end",text=str(data_to2),values=("Blewah(Passiflora quadranglaria LINN)","S3","24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Blewah(Passiflora quadranglaria LINN)")
                            quality.append("S3")
                            suggestion.append("24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6")
                if 24<=average_sm<80:
                    if 22<=average_tt<30:
                        if 5.8<=average_ph<7.6:
                            table_plant.insert("","end",text=str(data_to2),values=("Melon(Citrulus vulgaris SHRAD)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Melon(Citrulus vulgaris SHRAD)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 20<=average_sm<24 or 80<=average_sm<90:
                    if 30<=average_tt<32 or 20<=average_tt<22:
                        if 5.5<=average_ph<5.8 or 7.6<=average_ph<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Melon(Citrulus vulgaris SHRAD)","S2","24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Melon(Citrulus vulgaris SHRAD)")
                            quality.append("S2")
                            suggestion.append("24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6")
                elif average_sm<20 or average_sm>90:
                    if 33<=average_tt<35 or 18<=average_tt<20:
                        if average_ph<5.5 or average_ph>8:
                            table_plant.insert("","end",text=str(data_to2),values=("Melon(Citrulus vulgaris SHRAD)","S3","24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Melon(Citrulus vulgaris SHRAD)")
                            quality.append("S3")
                            suggestion.append("24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6")
                if 25<=average_tt<28:
                    if 5<=average_ph<6:
                        table_plant.insert("","end",text=str(data_to2),values=("Duku(Lansium domesticum CORR)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Duku(Lansium domesticum CORR)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 28<=average_tt<32 or 22<=average_tt<25:
                    if 4.5<=average_ph<5 or 6<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Duku(Lansium domesticum CORR)","S2","25<suhu<28, 5<pH<6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Duku(Lansium domesticum CORR)")
                        quality.append("S2")
                        suggestion.append("25<suhu<28, 5<pH<6")
                elif 32<=average_tt<35 or 20<=average_tt<22:
                    if average_ph<4.5 or 6<=average_ph>7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Duku(Lansium domesticum CORR)","S3","25<suhu<28, 5<pH<6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Duku(Lansium domesticum CORR)")
                        quality.append("S3")
                        suggestion.append("25<suhu<28, 5<pH<6")
                if 22<=average_tt<28:
                    if 5<=average_ph<6:
                        table_plant.insert("","end",text=str(data_to2),values=("Cempedak(Artocarpus champeden SPRENG)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Cempedak(Artocarpus champeden SPRENG)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 28<=average_tt<34 or 18<=average_tt<22:
                    if 4.5<=average_ph<5 or 6<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Cempedak(Artocarpus champeden SPRENG)","S2","22<suhu<28, 5<pH<6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Cempedak(Artocarpus champeden SPRENG)")
                        quality.append("S2")
                        suggestion.append("22<suhu<28, 5<pH<6")
                elif 34<=average_tt<40 or 15<=average_tt<18:
                    if average_ph<4.5 or 6<=average_ph>7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Cempedak(Artocarpus champeden SPRENG)","S3","22<suhu<28, 5<pH<6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Cempedak(Artocarpus champeden SPRENG)")
                        quality.append("S3")
                        suggestion.append("22<suhu<28, 5<pH<6")
                if 22<=average_tt<28:
                    if 5<=average_ph<6:
                        table_plant.insert("","end",text=str(data_to2),values=("Nangka(Artocarpus integra MERR)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
                        plant.append("Nangka(Artocarpus integra MERR)")
                        quality.append("S1")
                        suggestion.append("-")
                elif 28<=average_tt<34 or 18<=average_tt<22:
                    if 4.5<=average_ph<5 or 6<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Nangka(Artocarpus integra MERR)","S2","22<suhu<28, 5<pH<6"),tags="quality2")
                        data_to2 = data_to2+1
                        plant.append("Nangka(Artocarpus integra MERR)")
                        quality.append("S2")
                        suggestion.append("22<suhu<28, 5<pH<6")
                elif 34<=average_tt<40 or 15<=average_tt<18:
                    if average_ph<4.5 or 6<=average_ph>7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Nangka(Artocarpus integra MERR)","S3","22<suhu<28, 5<pH<6"),tags="quality3")
                        data_to2 = data_to2+1
                        plant.append("Nangka(Artocarpus integra MERR)")
                        quality.append("S3")
                        suggestion.append("22<suhu<28, 5<pH<6")
                if average_sm<42:
                    if 18<=average_tt<25:
                        if 5.5<=average_ph<6.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Sirsak(Annona muricta LINN)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Sirsak(Annona muricta LINN)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 36<=average_sm<42:
                    if 25<=average_tt<30 or 15<=average_tt<18:
                        if 5<=average_ph<5.5 or 6.5<=average_ph<8:
                            table_plant.insert("","end",text=str(data_to2),values=("Sirsak(Annona muricta LINN)","S2","kelembaban tanah>42, 18<suhu<25, 5.5<pH<6.5"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Sirsak(Annona muricta LINN)")
                            quality.append("S2")
                            suggestion.append("kelembaban tanah>42, 18<suhu<25, 5.5<pH<6.5")
                elif 30<=average_sm<36:
                    if 30<=average_tt<35 or 10<=average_tt<15:
                        if average_ph<5 or average_ph>8:
                            table_plant.insert("","end",text=str(data_to2),values=("Sirsak(Annona muricta LINN)","S3","kelembaban tanah>42, 18<suhu<25, 5.5<pH<6.5"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Sirsak(Annona muricta LINN)")
                            quality.append("S3")
                            suggestion.append("kelembaban tanah>42, 18<suhu<25, 5.5<pH<6.5")
                if average_sm<42:
                    if 18<=average_tt<25:
                        if 5.5<=average_ph<6.5:
                            table_plant.insert("","end",text=str(data_to2),values=("Srikaya(Annona squamosa)","S1","-"),tags="quality1")
                            data_to2 = data_to2+1
                            plant.append("Srikaya(Annona squamosa)")
                            quality.append("S1")
                            suggestion.append("-")
                elif 36<=average_sm<42:
                    if 25<=average_tt<30 or 15<=average_tt<18:
                        if 4.2<=average_ph<5.5 or 6.5<=average_ph<7:
                            table_plant.insert("","end",text=str(data_to2),values=("Srikaya(Annona squamosa)","S2","kelembaban tanah>42, 18<suhu<25, 5.5<pH<6.5"),tags="quality2")
                            data_to2 = data_to2+1
                            plant.append("Srikaya(Annona squamosa)")
                            quality.append("S2")
                            suggestion.append("kelembaban tanah>42, 18<suhu<25, 5.5<pH<6.5")
                elif 30<=average_sm<36:
                    if 30<=average_tt<35 or 10<=average_tt<15:
                        if average_ph<4.2 or average_ph>7:
                            table_plant.insert("","end",text=str(data_to2),values=("Srikaya(Annona squamosa)","S3","kelembaban tanah>42, 18<suhu<25, 5.5<pH<6.5"),tags="quality3")
                            data_to2 = data_to2+1
                            plant.append("Srikaya(Annona squamosa)")
                            quality.append("S3")
                            suggestion.append("kelembaban tanah>42, 18<suhu<25, 5.5<pH<6.5")
                


            def my_graph():
                the_graph = grafik.figure()
                the_graph.subplots_adjust(wspace=0.5,hspace=0.6)
                x=[]
                y=[]
                z=[]
                for o in range(1,len(temp)+1):
                    x.append(o)
                    y.append(o)
                    z.append(o)
                graph_soil_moisture = the_graph.add_subplot(221)
                graph_soil_moisture.plot(x,soil_moisture,'r--o')
                graph_soil_moisture.set_title("Kelembaban Tanah")

                graph_temperature = the_graph.add_subplot(222)
                graph_temperature.plot(y,temp,'g--o')
                graph_temperature.set_title('Suhu Udara')

                graph_ph = the_graph.add_subplot(223)
                graph_ph.plot(z,ph,'b--o')
                graph_ph.set_title('pH Tanah')

                the_graph.show()

            def excel_file():
                main2.destroy()
                main3=Tk()
                main3.geometry("%dx%d+%d+%d" % (400,150,500,300))
                main3['bg']='olive'
                main3.title("Soil Data Monitoring")

                itk_pic = PhotoImage(file='itk.gif')
                pimnas_pic = PhotoImage(file='pimnas_logo.gif')
                app_pic = PhotoImage(file='logo_aplikasi.gif')
                logo_itk = itk_pic.subsample(30,30)
                logo_pimnas = pimnas_pic.subsample(50,50)
                logo_app = app_pic.subsample(40,40)

                label_logo_app = Label(main3,image=logo_app,bg='olive')
                label_logo_app.place(x=350,y=98)

                label_logo_itk= Label(main3,image=logo_itk,bg='olive')
                label_logo_itk.place(x=250,y=100)

                label_logo_pimnas= Label(main3,image=logo_pimnas,bg='olive')
                label_logo_pimnas.place(x=305,y=102)

                file_name = StringVar()

                label_namefile = Label(main3,font=('verdana',12),text="Nama File",fg="white",bg="olive")
                label_namefile.place(x=10,y=10)
                entry_namefile = Entry(main3,font=('verdana',12),text=file_name,bd=2)
                entry_namefile.place(x=110,y=10)

                text1 = """file berada pada 1 folder
    yang sama dengan aplikasi"""
                label_info = Label(main3,font=('verdana',8),text=text1 ,fg="white",bg="olive")
                label_info.place(x=100,y=40)

                def create_file():
                    sum_kelembaban = sum(soil_moisture)/float(len(soil_moisture))
                    sum_temp = sum(temp)/float(len(temp))
                    sum_ph = sum(temp)/float(len(ph))
                    workbook = xlsxwriter.Workbook(file_name.get()+'.xlsx')
                    sheet = workbook.add_worksheet()
                    format1 = workbook.add_format({"border":1})
                    format2 = workbook.add_format({"bg_color": "#00ff00"})
                    sheet.write('A1','Nomor',format1)
                    sheet.write('B1','Kelembaban Tanah (%)',format1)
                    sheet.write('C1','Suhu Udara (C)',format1)
                    sheet.write('D1','pH Tanah',format1)
                    sheet.set_column("B:B",25)
                    sheet.set_column("C:C",15)
                    sheet.set_column("D:D",15)

                    sheet.write('G1','Nomor',format1)
                    sheet.write('H1','Jenis Tanaman',format1)
                    sheet.write('I1','Klasifikasi Tanah',format1)
                    sheet.write('J1','Saran',format1)
                    format_1 = workbook.add_format({"border":1,"bg_color":"#00ff00"})
                    format_2 = workbook.add_format({"border":1,"bg_color":"#f4f122"})
                    format_3 = workbook.add_format({"border":1,"bg_color":"#fc251e"})
                    sheet.set_column("H:H",40)
                    sheet.set_column("I:I",15)
                    sheet.set_column("J:J",50)
                    
                    for i in range (len(temp)):
                        sheet.write('A'+str(i+2),str(i+1),format1)
                        sheet.write('B'+str(i+2),str(soil_moisture[i]),format1)
                        sheet.write('C'+str(i+2),str(temp[i]),format1)
                        sheet.write('D'+str(i+2),str(ph[i]),format1)
                    sheet.write('A'+str(len(suhu)+2),str("rata-rata"),format2)
                    sheet.write('B'+str(len(suhu)+2),str(k),format2)
                    sheet.write('C'+str(len(suhu)+2),str(s),format2)
                    sheet.write('D'+str(len(suhu)+2),str(p),format2)

                    for p in range(len(plant)):
                        if quality[p] == 'S1':
                            sheet.write('G'+str(p+2),str(p+1),format_1)
                            sheet.write('H'+str(p+2),plant[p],format_1)
                            sheet.write('I'+str(p+2),quality[p],format_1)
                            sheet.write('J'+str(p+2),suggestion[p],format_1)
                        elif quality[p] == 'S2':
                            sheet.write('G'+str(p+2),str(p+1),format_2)
                            sheet.write('H'+str(p+2),plant[p],format_2)
                            sheet.write('I'+str(p+2),quality[p],format_2)
                            sheet.write('J'+str(p+2),suggestion[p],format_2)
                        elif quality[p] == 'S3':
                            sheet.write('G'+str(p+2),str(p+1),format_3)
                            sheet.write('H'+str(p+2),plant[p],format_3)
                            sheet.write('I'+str(p+2),quality[p],format_3)
                            sheet.write('J'+str(p+2),suggestion[p],format_3)
                    workbook.close()
                    tkMessageBox.showinfo("Information",'file has been successfully created')
                    for q in range(len(plant)):
                        del plant[0]
                        del quality[0]
                        del suggestion[0]
                    for r in range(len(tempt)):
                        del tempt[0]
                        del soil_moisture[0]
                        del ph[0]
                    main3.destroy()
                    start_2()

                def go_back():
                    main3.destroy()
                    start_2()
                    
                button_create = Button(main3,font=('verdana',12),text="Buat",fg="white",bg="black",bd=4,command=create_file)
                button_create.place(x=330,y=3)

                button_back = Button(main3,bg="white",bd=4,command = go_back)
                panah = PhotoImage(file="arrow.gif")
                button_back.config(image=panah,width="60",height="40")
                button_back.place(x=10,y=80)
                main3.mainloop()
                

            button_start=Button(main2,font=('verdana',12),text="Ambil Data",fg="white",bg="black",bd=4,command=analysis)
            button_start.place(x=550,y=70)

            button_back = Button(main2,bg="white",bd=4,command = back_1)
            panah = PhotoImage(file="arrow.gif")
            button_back.config(image=panah,width="60",height="40")
            button_back.place(x=400,y=300)

            button_grafik = Button(main2,bg="white",bd=4,command = my_graph)
            logo_grafik1 = PhotoImage(file="grafik.gif")
            logo_grafik = logo_grafik1.subsample(2,2)
            button_grafik.config(image=logo_grafik,width="60",height="40")
            button_grafik.place(x=474,y=300)

            button_excel = Button(main2,bg="white",bd=4,command = excel_file)
            logo_excel = PhotoImage(file="excel.gif")
            button_excel.config(image=logo_excel,width="60",height="40")
            button_excel.place(x=550,y=300)

            main2.mainloop()
        start_2()
            
    def klasifikasi():
        main1.destroy()
        main4 = Tk()
        main4['bg']="olive"
        main4.title("Soil Data Monitoring")
        main4.geometry("%dx%d+%d+%d" % (950,550,400,100))

        itk_pic = PhotoImage(file='itk.gif')
        pimnas_pic = PhotoImage(file='pimnas_logo.gif')
        app_pic = PhotoImage(file='logo_aplikasi.gif')
        logo_itk = itk_pic.subsample(30,30)
        logo_pimnas = pimnas_pic.subsample(50,50)
        logo_app = app_pic.subsample(40,40)

        label_logo_app = Label(main4,image=logo_app,bg='olive')
        label_logo_app.place(x=900,y=5)

        label_logo_itk= Label(main4,image=logo_itk,bg='olive')
        label_logo_itk.place(x=800,y=7)

        label_logo_pimnas= Label(main4,image=logo_pimnas,bg='olive')
        label_logo_pimnas.place(x=855,y=9)

        vsb = ttk.Scrollbar(main4,orient="vertical")
        vsb.place(x=10+60+280+442+130,y=131,height=325)

        table_plant = ttk.Treeview(main4,height=15,yscrollcommand=vsb.set)
        table_plant['columns'] = ('jenis_tanaman','kualitas','saran')
        table_plant.place(x=10,y=130)
        a=ttk.Style()
        a.configure("Treeview.Heading",font=("arial",10))

        vsb.config(command = table_plant.yview)

        table_plant.column('#0',width=60,anchor='center')
        table_plant.heading('#0',text='Nomor')

        table_plant.column('jenis_tanaman',width=280,anchor='w')
        table_plant.heading('jenis_tanaman',text='Jenis Tanaman')

        table_plant.column('kualitas',width=130,anchor='center')
        table_plant.heading('kualitas',text='Kualitas Tanah')

        table_plant.column('saran',width=440,anchor='center')
        table_plant.heading('saran',text='Saran')

        table_plant.tag_configure("quality1",background="light green",font=("arial",12))
        table_plant.tag_configure("quality2",background="yellow",font=("arial",12))
        table_plant.tag_configure("quality3",background="red",font=("arial",12))

        D1 = DoubleVar()
        D2 = DoubleVar()
        D3 = DoubleVar()
        label_D1 = Label(main4, font=('verdana',12),fg="white",bg="olive",text="Kelembaban Tanah")
        label_D1.place(x=10,y=10)
        entry_D1 = Entry(main4,font=('verdana',12),fg="black",bg="white",text=D1,width=8)
        entry_D1.place(x=200,y=10)

        label_D2 = Label(main4, font=('verdana',12),fg="white",bg="olive",text="Suhu Udara")
        label_D2.place(x=10,y=40)
        entry_D2 = Entry(main4,font=('verdana',12),fg="black",bg="white",text=D2,width=8)
        entry_D2.place(x=200,y=40)

        label_D3 = Label(main4, font=('verdana',12),fg="white",bg="olive",text="pH Tanah")
        label_D3.place(x=10,y=70)
        entry_D3 = Entry(main4,font=('verdana',12),fg="black",bg="white",text=D3,width=8)
        entry_D3.place(x=200,y=70)
        def clasify():
            average_sm = D1.get()
            average_tt = D2.get()
            average_ph = D3.get()
            the_table_plant = table_plant.get_children()
            data_to2 = 1
            if the_table_plant != '()':
                for child in the_table_plant:
                    table_plant.delete(child)
            if 24<=average_sm<29:
                if 30<=average_tt<90:
                    if 5.5<=average_ph<7:
                        table_plant.insert("","end",text=str(data_to2),values=("Oriza Sativa (Sistem Irigasi)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 22<=average_sm<24 or 29<=average_sm<32:
                if 30<=average_tt<33:
                    if 4.5<=average_ph<5.5 or 7<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Oriza Sativa (Sistem Irigasi)","S2","24<kelembaban tanah<29,","5.5<pH<7"),tags="quality2")
                        data_to2 = data_to2+1
            elif 18<=average_sm<22 or 32<=average_sm<35:
                if average_tt<30 or average_tt>90:
                    if average_ph<4.5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Oriza Sativa (Sistem Irigasi)","S3","24<kelembaban tanah<29, 30<suhu<90, 5.5<pH<7"),tags="quality3")
                        data_to2 = data_to2+1
            if 24<=average_sm<29:
                if 33<=average_tt<90:
                    if 5.5<=average_ph<8.2:
                        table_plant.insert("","end",text=str(data_to2),values=("Oriza Sativa (Tadah Hujan)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 22<=average_sm<24 or 29<=average_sm<32:
                if 30<=average_tt<33:
                    if 5<=average_ph<5.5 or 8.2<=average_ph<8.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Oriza Sativa (Tadah Hujan)","S2","24<kelembaban tanah<29,","5.5<pH<8.2"),tags="quality2")
                        data_to2 = data_to2+1
            elif 18<=average_sm<22 or 32<=average_sm<35:
                if average_tt<30 or average_tt>90:
                    if average_ph<5 or average_ph>8.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Oriza Sativa (Tadah Hujan)","S3","24<kelembaban tanah<29, 33<suhu<90, 5.5<pH<8.2"),tags="quality3")
                        data_to2 = data_to2+1
            if 33<=average_sm<90:
                if 24<=average_tt<29:
                    if 5.5<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Padi Gogo","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 30<=average_sm<33:
                if 22<=average_tt<24 or 29<=average_tt<32:
                    if 5<=average_ph<7.9:
                        if average_ph<5.5 or average_ph>7.5:
                            suggest = "24<suhu<29, 5.5<ph<7.5"
                        else:
                            suggest = "24<suhu<29"
                        table_plant.insert("","end",text=str(data_to2),values=("Padi Gogo","S2",suggest),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm<30 or average_sm>90:
                if 18<=average_tt<22 or 32<=average_tt<35:
                    if average_ph<5 or average_ph>7.9:
                        table_plant.insert("","end",text=str(data_to2),values=("Padi Gogo","S3",suggest),tags="quality3")
                        data_to2 = data_to2+1
            if 33<=average_sm<90:
                if 24<=average_tt<29:
                    if 5.5<=average_ph<8.2:
                        table_plant.insert("","end",text=str(data_to2),values=("Padi Sawah Lebak","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 30<=average_sm<33:
                if 22<=average_tt<24 or 29<=average_tt<32:
                    if 5<=average_ph<5.5 or 8.2<=average_ph<8.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Padi Sawah Lebak","S2","24<suhu<29, 5.5<pH<8.2"),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm<30 or average_sm>90:
                if 18<=average_tt<22 or 32<=average_tt<35:
                    if average_ph<5 or average_ph>8.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Padi Sawah Lebak","S3","33<kelembaban tanah<90, 24<suhu<29, 5.5<pH<8.2"),tags="quality")
                        data_to2 = data_to2+1
            if average_sm<75:
                if 25<=average_tt<27:
                    if 5.5<=average_ph<8.2:
                        table_plant.insert("","end",text=str(data_to2),values=("Sorgum (Shorgum Bicolor)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 75<=average_sm<85:
                if 27<=average_tt<30 or 18<=average_tt<25:
                    if 5.3<=average_ph<5.5 or 8.2<average_ph<8.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Sorgum (Shorgum Bicolor)","S2","kelembaban tanah<75, 25<suhu<27, 5.5<ph<8.2"),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm>85:
                if 30<=average_tt<35 or 15<=average_tt<18:
                    if average_ph<5.3 or average_ph>8.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Sorgum (Shorgum Bicolor)","S3","kelembaban tanah<75, 25<suhu<27, 5.5<ph<8.2"),tags="quality3")
                        data_to2 = data_to2+1
            if 12<=average_tt<23:
                if 6<=average_ph<8.2:
                    table_plant.insert("","end",text=str(data_to2),values=("Gandum (Truticum aestivum)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 10<=average_tt<12 or 23<=average_tt<25:
                if 5.6<=average_ph<6 or 8.2<=average_ph<8.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Gandum (Truticum aestivum)","S2","12<suhu<23, 6<pH<8.2"),tags="quality2")
                    data_to2 = data_to2+1
            elif 10<=average_tt<12 or 23<=average_tt<25:
                if average_ph<5.6 or average_ph>8.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Gandum (Truticum aestivum)","S3","12<suhu<23, 6<pH<8.2"),tags="quality3")
                    data_to2 = data_to2+1
            if average_sm>42:
                if 20<=average_tt<26:
                    if 5.8<=average_ph<7.8:
                        table_plant.insert("","end",text=str(data_to2),values=("Jagung (Zea Mays)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 36<=average_sm<42:
                if 26<=average_tt<30:
                    if 5.5<=average_ph<5.8 or 7.8<=average_ph<8.2:
                        table_plant.insert("","end",text=str(data_to2),values=("Jagung (Zea Mays)","S2","kelembaban tanah>42, 20<suhu<26, 5.8<pH<7.8"),tags="quality2")
                        data_to2 = data_to2+1
            elif 30<=average_sm<36:
                if 16<=average_tt<20 or 30<=average_tt<32:
                    if average_ph<5.5 or average_ph>8.2:
                        table_plant.insert("","end",text=str(data_to2),values=("Jagung (Zea Mays)","S3","kelembaban tanah>42, 20<suhu<26, 5.8<pH<7.8"),tags="quality3")
                        data_to2 = data_to2+1
            if 22<=average_tt<28:
                if 5.2<=average_ph<7:
                    table_plant.insert("","end",text=str(data_to2),values=("Ubi Kayu(Manihot Esculenta)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 28<=average_tt<30:
                if 4.8<=average_ph<5.2 or 7<average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Ubi Kayu(Manihot Esculenta)","S2","22<suhu<28, 5.2<ph<7"),tags="quality2")
                    data_to2 = data_to2+1
            elif 18<=average_tt<20 or 30<=average_tt<35:
                if average_ph<4.8 or average_ph>7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Ubi Kayu(Manihot Esculenta)","S3","22<suhu<28, 5.2<ph<7"),tags="quality3")
                    data_to2 = data_to2+1
            if average_sm<75:
                if 22<=average_tt<25:
                    if 5.2<=average_ph<8.2:
                        table_plant.insert("","end",text=str(data_to2),values=("Ubi Jalar(Ipomoea Batatas)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 27<=average_sm<85:
                if 25<=average_tt<30 or 20<=average_tt<22:
                    if 4.8<=average_ph<5.2 or 8.2<=average_ph<8.4:
                        if average_sm>75:
                            suggest = "kelembaban tanah<75, 22<suhu<25, 5.2<pH<8.2"
                        else:
                            suggest = "22<suhu<25, 5.2<pH<8.2"
                        table_plant.insert("","end",text=str(data_to2),values=("Ubi Jalar(Ipomoea Batatas)","S2",suggest),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm>85:
                if 30<=average_tt<35 or 18<=average_tt<20:
                    if average_ph<4.8 or average_ph>8.4:
                        table_plant.insert("","end",text=str(data_to2),values=("Ubi Jalar(Ipomoea Batatas)","S3","kelembaban tanah<75, 22<suhu<25, 5.2<pH<8.2"),tags="quality3")
                        data_to2 = data_to2+1
            if 25<=average_tt<31:
                if 5.5<=average_ph<6.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Talas(Colocasia Asculenta SCHOTT)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 22<=average_tt<25 or average_tt>32:
                if 5<=average_ph<5.5 or 6.5<=average_ph<7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Talas(Colocasia Asculenta SCHOTT)","S2","25<suhu<31, 5.5<pH<6.5"),tags="quality2")
                    data_to2 = data_to2+1
            elif 20<=average_tt<22:
                if average_ph<5 or average_ph>7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Talas(Colocasia Asculenta SCHOTT)","S3","25<suhu<31, 5.5<pH<6.5"),tags="quality3")
                    data_to2 = data_to2+1
            if 26<=average_tt<30:
                if 5<=average_ph<7:
                    table_plant.insert("","end",text=str(data_to2),values=("Iles-Iles (Amorphophalus Ancophyllus)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 18<=average_tt<32:
                if 4<=average_ph<5 or 7<=average_ph<7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Iles-Iles (Amorphophalus Ancophyllus)","S2","26<suhu<30, 5<pH<7"),tags="quality2")
                    data_to2 = data_to2+1
            elif 18<=average_tt<32:
                if average_ph<4 or 7<=average_ph>7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Iles-Iles (Amorphophalus Ancophyllus)","S3","26<suhu<30, 5<pH<7"),tags="quality3")
                    data_to2 = data_to2+1
            if 22<=average_tt<25:
                if 5.5<=average_ph<6.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Hui","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 20<=average_tt<22 or 25<=average_tt<30:
                if 6.5<=average_ph<7.5 or 5<=average_ph<5.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Hui","S2","22<suhu<25, 5.5<pH<6.5"),tags="quality2")
                    data_to2 = data_to2+1
            elif 30<=average_tt<32 or 18<=average_tt<20:
                if 7.5<=average_ph<8.5 or 4.5<=average_ph<5:
                    table_plant.insert("","end",text=str(data_to2),values=("Hui","S3","22<suhu<25, 5.5<pH<6.5"),tags="quality3")
                    data_to2 = data_to2+1
            if 24<=average_sm<80:
                if 23<=average_tt<25:
                    if 5.5<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Kedelai(Glycine Max)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 20<=average_sm<24 or 80<=average_sm<85:
                if 20<=average_tt<23 or 25<=average_tt<28:
                    if 5<=average_ph<5.5 or 7.5<=average_ph<7.8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kedelai(Glycine Max)","S2","24<kelembaban tanah<80, 23<suhu<25, 5.5<pH<7.5"),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm<20 or average_sm>85:
                if 18<=average_tt<20 or 28<=average_tt<32:
                    if average_ph<5 or average_ph>7.8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kedelai(Glycine Max)","S3","24<kelembaban tanah<80, 23<suhu<25, 5.5<pH<7.5"),tags="quality3")
                        data_to2 = data_to2+1
            if 50<=average_sm<80:
                if 25<=average_tt<27:
                    if 6<=average_ph<7:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Tanah(Arachis Hypogea)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif average_sm<50 or average_sm>80:
                if 20<=average_tt<25 or 27<=average_tt<30:
                    if 5<=average_ph<6 or 7<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Tanah(Arachis Hypogea)","S2","50<kelembaban tanah<80, 25<suhu<27, 6<pH<7"),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm<50 or average_sm>80:
                if 18<=average_tt<20 or 30<=average_tt<34:
                    if average_ph<5 or average>7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Tanah(Arachis Hypogea)","S3","50<kelembaban tanah<80, 25<suhu<27, 6<pH<7"),tags="quality3")
                        data_to2 = data_to2+1
            if 42<=average_sm<75:
                if 12<=average_tt<24:
                    if 5.6<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Hijau(Phaseolus Radiatus LINN)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1    
            elif 36<=average_sm<42 or 75<=average_sm<90:
                if 10<=average_tt<12 or 24<=average_tt<27:
                    if 5.4<=average_ph<5.6 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Hijau(Phaseolus Radiatus LINN)","S2","42<kelembaban tanah<75, 12<suhu<24, 5.6<pH<7.6"),tags="quality2")
                        data_to2 = data_to2+1
            elif 30<=average_sm<36 or average_sm>90:
                if 27<=average_tt<30 or 8<=average_tt<10:
                    if average_ph<5.4 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Hijau(Phaseolus Radiatus LINN)","S3","42<kelembaban tanah<75, 12<suhu<24, 5.6<pH<7.6"),tags="quality3")
                        data_to2 = data_to2+1
            if average_sm<80:
                if 20<=average_tt<30:
                    if 6<=average_ph<7.7:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Tunggang(Vigna Unguiculata)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 80<=average_sm<90:
                if 19<=average_tt<20 or 30<=average_tt<32:
                    if 5.5<=average_ph<6 or 7.8<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Tunggang(Vigna Unguiculata)","S2","kelembaban tanah<80, 20<suhu<30, 6<pH<7.8"),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm>90:
                if 16<=average_tt<18 or 32<=average_tt<35:
                    if average_ph<5.5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Kacang Tunggang(Vigna Unguiculata)","S3","kelembaban tanah<80, 20<suhu<30, 6<pH<7.8"),tags="quality3")
                        data_to2 = data_to2+1
            if 16<=average_tt<23:
                if 6<=average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Kacang Arab(Cicer Arietinum)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 14<=average_tt<16 or 23<=average_tt<25:
                if 5.6<=average_ph<6 or 7.6<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Kacang Arab(Cicer Arietinum)","S2","16<suhu<23, 6<pH<7.6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 12<=average_tt<14 or 25<=average_tt<28:
                if average_ph<5.6 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Kacang Arab(Cicer Arietinum)","S3","16<suhu<23, 6<pH<7.6"),tags="quality3")
                    data_to2 = data_to2+1
            if 16<=average_tt<18:
                if 5.6<=average_ph<7:
                    table_plant.insert("","end",text=str(data_to2),values=("Kentang(Solanum Tuberosum)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 14<=average_tt<16 or 18<=average_tt<20:
                if 5.2<=average_ph<5.6 or 7<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Kentang(Solanum Tuberosum)","S2","16<suhu<18, 5.6<pH<7"),tags="quality2")
                    data_to2 = data_to2+1
            elif 12<=average_tt<14 or 20<=average_tt<23:
                if average_ph<5.2 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Kentang(Solanum Tuberosum)","S3","16<suhu<18, 5.6<pH<7"),tags="quality3")
                    data_to2 = data_to2+1
            if 40<=average_sm<80:
                if 16<=average_tt<18:
                    if 6<=average_ph<7:
                        table_plant.insert("","end",text=str(data_to2),values=("Wortel(Daucus Carota)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 20<=average_sm<40 or 80<=average_sm<90:
                if 18<=average_tt<20 or 14<=average_tt<16:
                    if 5.7<=average_ph<6 or 7<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Wortel(Daucus Carota)","S2","40<kelembaban tanah<80, 16<suhu<18, 6<pH<7"),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm<20 or average_sm>90:
                if 20<=average_tt<23 or 12<=average_tt<16:
                    if average_ph<5.7 or average_ph>7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Wortel(Daucus Carota)","S3","40<kelembaban tanah<80, 16<suhu<18, 6<pH<7"),tags="quality3")
                        data_to2 = data_to2+1
            if 16<=average_tt<18:
                if 6<=average_ph<7:
                    table_plant.insert("","end",text=str(data_to2),values=("Lobak(Raphanus Sativur)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            if 18<=average_tt<20 or 14<average_tt<16:
                if 5.7<=average_ph<6 or 7<average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Lobak(Raphanus Sativur)","S2","16<suhu<18, 6<pH<7"),tags="quality2")
                    data_to2 = data_to2+1
            elif 20<=average_tt<23 or 12<average_tt<16:
                if average_ph>7.6 or average_ph<5.7:
                    table_plant.insert("","end",text=str(i),values=("Lobak(Raphanus Sativur)","S3","16<suhu<18, 6<pH<7"),tags="quality3")
                    data_to2 = data_to2+1
            if 20<=average_tt<25:
                if 6<=average_ph<7.8:
                    table_plant.insert("","end",text=str(data_to2),values=("Bawang Merah(Aillium Ascolonicum)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 25<=average_tt<30 or 18<=average_tt<20:
                if 5.8<=average_ph<6 or 7.8<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Bawang Merah(Aillium Ascolonicum)","S2","20<suhu<25, 6<pH<7.8"),tags="quality2")
                    data_to2 = data_to2+1
            elif 30<=average_tt<35 or 15<=average_tt<18:
                if average_ph<5.8 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Bawang Merah(Aillium Ascolonicum)","S3","20<suhu<25, 6<pH<7.8"),tags="quality3")
                    data_to2 = data_to2+1
            if 16<=average_tt<18:
                if 6<=average_ph<7.8:
                    table_plant.insert("","end",text=str(data_to2),values=("Bawang Putih(Aillium Sativum)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 18<=average_tt<20 or 14<=average_tt<16:
                if 5.8<=average_ph<6 or 7.8<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Bawang Putih(Aillium Sativum)","S2","16<suhu<18, 6<pH<7.8"),tags="quality2")
                    data_to2 = data_to2+1
            elif 20<=average_tt<23 or 12<=average_tt<16:
                if average_ph<5.8 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Bawang Putih(Aillium Sativum)","S3","16<suhu<18, 6<pH<7.8"),tags="quality3")
                    data_to2 = data_to2+1
            if 21<=average_tt<27:
                if 6<=average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Cabai Merah(Capsicum annuum)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 16<=average_tt<21 or 27<=average_tt<28:
                if 5.5<=average_ph<6 or 7.6<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Cabai Merah(Capsicum annuum)","S2","21<suhu<27, 6<ph<7.6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 14<=average_tt<16 or 28<=average_tt<30:
                if average_ph<5.5 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Cabai Merah(Capsicum annuum)","S3","21<suhu<27, 6<ph<7.6"),tags="quality3")
                    data_to2 = data_to2+1
            if 18<=average_tt<26:
                if 6<=average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Paprika(Capsium Sp.)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 16<=average_tt<18 or 26<=average_tt<27:
                if 5.5<=average_ph<6 or 7.6<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Paprika(Capsium Sp.)","S2","18<suhu<26, 6<ph<7.6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 14<=average_tt<16 or 27<=average_tt<28:
                if average_ph<5.5 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Paprika(Capsium Sp.)","S3","18<suhu<26, 6<ph<7.6"),tags="quality3")
                    data_to2 = data_to2+1
            if 13<=average_tt<24:
                if 6<=average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Kubis(Brassica Oleracea L.)","S1","13<suhu<24, 6<pH<7.6"),tags="quality1")
                    data_to2 = data_to2+1
            elif 10<=average_tt<13 or 24<=average_tt<30:
                if 5.5<=average_ph<6 or 7.6<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Kubis(Brassica Oleracea L.)","S2","13<suhu<24, 6<pH<7.6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 5<=average_tt<10 or 30<=average_tt<35:
                if average_ph<5.5 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Kubis(Brassica Oleracea L.)","S3","13<suhu<24, 6<pH<7.6"),tags="quality3")
                    data_to2 = data_to2+1
            if 13<=average_tt<24:
                if 6<=average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Lettuce(Lacuce Sativa)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 22<=average_tt<28:
                if 5.7<=average_ph<6 or 7<=average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Lettuce(Lacuce Sativa)","S2","13<suhu<24, 6<pH<7.6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 28<=average_tt<35:
                if average_ph>7.6 or average_ph<5.7:
                    table_plant.insert("","end",text=str(data_to2),values=("Lettuce(Lacuce Sativa)","S3","13<suhu<24, 6<pH<7.6"),tags="quality3")
                    data_to2 = data_to2+1
            if 16<=average_tt<22:
                if 6<=average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Petsai (Brassica Purpureum SCHUM)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 22<=average_tt<28 or 13<average_tt<16:
                if 5.7<=average_ph<6 or 7<=average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Petsai (Brassica Purpureum SCHUM)","S2","16<suhu<22, 6<pH<7"),tags="quality2")
                    data_to2 = data_to2+1
            elif 28<=average_tt<35 or 4<average_tt<13:
                if average_ph<5.7 or average_ph>7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Petsai (Brassica Purpureum SCHUM)","S3","16<suhu<22, 6<pH<7"),tags="quality3")
                    data_to2 = data_to2+1
            if 16<=average_tt<22:
                if 6<=average_ph<7:
                    table_plant.insert("","end",text=str(data_to2),values=("Sawi (Brassica Rugosa SCHUM)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 22<=average_tt<28 or 13<=average_ph<16:
                if 7<=average_ph<7.6 or 5.7<=average_ph<6:
                    table_plant.insert("","end",text=str(data_to2),values=("Sawi (Brassica Rugosa SCHUM)","S2","16<suhu<22, 6<pH<7"),tags="quality2")
                    data_to2 = data_to2+1
            elif 4<=average_tt<13 or 28<=average_ph<35:
                if average_ph<5.6 or average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Sawi (Brassica Rugosa SCHUM)","S3","16<suhu<22, 6<pH<7"),tags="quality3")
                    data_to2 = data_to2+1
            if 12<=average_tt<24:
                if 5.6<=average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Bayam(Amaranthus Spe.div)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 10<=average_tt<12 or 24<=average_tt<27:
                if 5.4<=average_ph<5.6 or 7.6<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Bayam(Amaranthus Spe.div)","S2","12<suhu<24, 5.6<pH<7.6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 27<=average_tt<30 or 8<=average_tt<10:
                if average_ph<5.4 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Bayam(Amaranthus Spe.div)","S3","12<suhu<24, 5.6<pH<7.6"),tags="quality3")
                    data_to2 = data_to2+1
            if 12<=average_tt<24:
                if 5.6<=average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Buncis(Phaseolus Vulgaris)","S1","12<suhu<24, 5.6<pH<7.6"),tags="quality1")
                    data_to2 = data_to2+1
            elif 10<=average_tt<12 or 24<=average_tt<27:
                if 5.4<=average_ph<5.6 or 7.6<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Buncis(Phaseolus Vulgaris)","S2","12<suhu<24, 5.6<pH<7.6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 27<=average_tt<30 or 8<=average_tt<12:
                if average_ph<5.4 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Buncis(Phaseolus Vulgaris)","S3","12<suhu<24, 5.6<pH<7.6"),tags="quality3")
                    data_to2 = data_to2+1
            if 12<=average_tt<24:
                if 5.6<=average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Kacang Panjang(Vigina Sinensis ENDL)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 10<=average_tt<12 or 24<=average_tt<27:
                if 5.4<=average_ph<5.6 or 7.6<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Kacang Panjang(Vigina Sinensis ENDL)","S2","12<suhu<24, 5.6<pH<7.6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 27<=average_tt<30 or 8<=average_tt<10:
                if average_ph<5.4 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Kacang Panjang(Vigina Sinensis ENDL)","S3","12<suhu<24, 5.6<pH<7.6"),tags="quality3")
                    data_to2 = data_to2+1
            if 14<=average_tt<20:
                if 6<=average_ph<7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Kacang Kapri(Pisum Sativum)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 10<=average_tt<14 or 20<=average_tt<23:
                if 5.8<=average_ph<6 or 7.5<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Kacang Kapri(Pisum Sativum)","S2","14<suhu<20, 6<pH<7.5"),tags="quality2")
                    data_to2 = data_to2+1
            elif 8<=average_tt<10 or 23<=average_tt<25:
                if average_ph<5.8 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Kacang Kapri(Pisum Sativum)","S3","14<suhu<20, 6<pH<7.5"),tags="quality3")
                    data_to2 = data_to2+1
            if 22<=average_tt<30:
                if 5.8<=average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Mentimun(Cucumis Sativus LINN)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 30<=average_tt<32 or 20<=average_tt<22:
                if 5.5<=average_ph<5.8 or 7.6<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Mentimun(Cucumis Sativus LINN)","S2","22<suhu<30, 5.8<pH<7.6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 32<=average_tt<35 or 18<=average_tt<20:
                if average_ph<5.5 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Mentimun(Cucumis Sativus LINN)","S3","22<suhu<30, 5.8<pH<7.6"),tags="quality3")
                    data_to2 = data_to2+1
            if 18<=average_tt<26:
                if 6<=average_ph<7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Terung(Solannum Melongen LINN)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 16<=average_tt<18 or 26<=average_tt<30:
                if 5.5<=average_ph<6 or 7.5<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Terung(Solannum Melongen LINN)","S2","18<suhu<26, 6<pH<7.5"),tags="quality2")
                    data_to2 = data_to2+1
            elif 30<=average_tt<35 or 13<=average_tt<16:
                if average_ph<5.5 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Terung(Solannum Melongen LINN)","S3","18<suhu<26, 6<pH<7.5"),tags="quality3")
                    data_to2 = data_to2+1
            if 18<=average_tt<25:
                if 5.5<=average_ph<7.8:
                    table_plant.insert("","end",text=str(data_to2),values=("Pare(Momordica Charantia LINN)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 15<=average_tt<18 or 25<=average_tt<30:
                if 5<=average_ph<5.5 or 7.8<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Pare(Momordica Charantia LINN)","S2","18<suhu<25, 5.5<pH<7.8"),tags="quality2")
                    data_to2 = data_to2+1
            elif 30<=average_tt<35 or 10<=average_tt<15:
                if average_ph<5 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Pare(Momordica Charantia LINN)","S3","18<suhu<25, 5.5<pH<7.8"),tags="quality3")
                    data_to2 = data_to2+1
            if 13<=average_tt<24:
                if 6<=average_ph<7.8:
                    table_plant.insert("","end",text=str(data_to2),values=("Brokoli(Brassica)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 10<=average_tt<13 or 24<=average_tt<30:
                if 5.6<=average_ph<6 or 7.8<average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Brokoli(Brassica)","S2","13<suhu<24, 6<pH<7.8"),tags="quality2")
                    data_to2 = data_to2+1
            elif 30<=average_tt<35 or 5<=average_tt<10:
                if average_ph<5.6 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Brokoli(Brassica)","S3","13<suhu<24, 6<pH<7.8"),tags="quality3")
                    data_to2 = data_to2+1
            if 12<=average_tt<24:
                if 5.6<=average_ph<7.6:
                    table_plant.insert("","end",text=str(data_to2),values=("Asparagus(Asparagus Officinnalis LINN)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 10<=average_tt<12 or 24<=average_tt<27:
                if 5.4<=average_ph<5.6 or 7.6<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Asparagus(Asparagus Officinnalis LINN)","S2","12<suhu<24, 5.6<pH<7.6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 8<=average_tt<10 or 27<=average_tt<30:
                if average_ph<5.4 or average_ph>8:
                    table_plant.insert("","end",text=str(data_to2),values=("Asparagus(Asparagus Officinnalis LINN)","S3","12<suhu<24, 5.6<pH<7.6"),tags="quality3")
                    data_to2 = data_to2+1
            if 40<=average_sm<80:
                if 16<=average_tt<22:
                    if 6<=average_ph<7:
                        table_plant.insert("","end",text=str(data_to2),values=("Biet(Beta Vulgaris L.)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 20<=average_sm<40 or 80<=average_sm<90:
                if 22<=average_tt<28 or 13<=average_tt<16:
                    if 5.7<=average_ph<6 or 7<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Biet(Beta Vulgaris L.)","S2","40<kelembaban tanah<80, 16<suhu<22, 6<pH<7"),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm<20 or average_sm>90:
                if 28<=average_tt<35 or 4<=average_tt<13:
                    if average_ph<5.7 or average_ph>7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Biet(Beta Vulgaris L.)","S3","40<kelembaban tanah<80, 16<suhu<22, 6<pH<7"),tags="quality3")
                        data_to2 = data_to2+1
            if 40<=average_sm<80:
                if 16<=average_tt<22:
                    if 6<=average_ph<7:
                        table_plant.insert("","end",text=str(data_to2),values=("Kalian(Brassica Oleracea Var. Acephala)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 20<=average_sm<40 or 80<=average_sm<90:
                if 22<=average_tt<28 or 13<=average_tt<16:
                    if 5.7<=average_ph<6 or 7<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Kalian(Brassica Oleracea Var. Acephala)","S2","40<kelembaban tanah<80, 16<suhu<22, 6<pH<7"),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm<20 or average_sm>90:
                if 28<=average_tt<35 or 4<=average_tt<13:
                    if average_ph<5.7 or average_ph>7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Kalian(Brassica Oleracea Var. Acephala)","S3","40<kelembaban tanah<80, 16<suhu<22, 6<pH<7"),tags="quality3")
                        data_to2 = data_to2+1
            if 24<=average_sm<80:
                if 18<=average_tt<26:
                    if 6<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Tomat Sayur(Solanum Lycopersicon esculenta LINN)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 20<=average_sm<24 or 80<=average_sm<90:
                if 26<=average_tt<30 or 16<=average_tt<18:
                    if 5.5<=average_ph<6 or 7.5<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Tomat Sayur(Solanum Lycopersicon esculenta LINN)","S2","24<kelembaban tanah<80, 18<suhu<26, 6<pH<7.5"),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm>90 or average_sm<20:
                if 30<=average_tt<35 or 13<=average_tt<16:
                    if average_ph<5.5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Tomat Sayur(Solanum Lycopersicon esculenta LINN)","S3","18<24<kelembaban tanah<80, suhu<26, 6<pH<7.5"),tags="quality3")
                        data_to2 = data_to2+1
            if average_sm>42:
                if 18<=average_tt<25:
                    if 5.5<=average_ph<7.8:
                        table_plant.insert("","end",text=str(data_to2),values=("Petai(Parkia Speciosa HASSK)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 36<=average_sm<42:
                if 15<=average_tt<18 or 25<=average_tt<30:
                    if 5<=average_ph<5.5 or 7.8<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Petai(Parkia Speciosa HASSK)","S2","kelembaban tanah>42, 18<suhu<25, 5.5<pH<7.8"),tags="quality2")
                        data_to2 = data_to2+1
            elif 30<=average_sm<36:
                if 30<=average_tt<35 or 10<=average_tt<15:
                    if average_ph<5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Petai(Parkia Speciosa HASSK)","S3","kelembaban tanah>42, 18<suhu<25, 5.5<pH<7.8"),tags="quality3")
                        data_to2 = data_to2+1
            if average_sm>60:
                if 25<=average_tt<27:
                    if 5.6<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Pisang(Musa Acuminate COLLA)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 50<=average_sm<60:
                if 22<=average_tt<25 or 27<=average_tt<30:
                    if 5.2<=average_ph<5.6 or 7.5<=average_ph<8.2:
                        table_plant.insert("","end",text=str(data_to2),values=("Pisang(Musa Acuminate COLLA)","S2","kelembaban tanah>60, 25<suhu<27, 5.6<pH<7.5"),tags="quality2")
                        data_to2 = data_to2+1
            elif 30<=average_sm<50:
                if 30<=average_tt<35 or 22<=average_tt<25:
                    if average_ph<5.2 or average_ph>8.2: 
                        table_plant.insert("","end",text=str(data_to2),values=("Pisang(Musa Acuminate COLLA)","S3","kelembaban tanah>60, 25<suhu<27, 5.6<pH<7.5"),tags="quality3")
                        data_to2 = data_to2+1
            if 24<=average_sm<80:
                if 25<=average_tt<28:
                    if 6<=average_ph<6.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Papaya(Carica Papaya L)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 20<=average_sm<24 or 80<=average_sm<90:
                if 28<=average_tt<34 or 20<=average_tt<25:
                    if 5.5<=average_ph<6 or average_ph>6.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Papaya(Carica Papaya L)","S2","24<kelembaban tanah<80, 25<suhu<28, 6<pH<6.6"),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm<20 or average_sm>90:
                if 34<=average_tt<38 or 15<=average_tt<20:
                    if average_ph<5.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Papaya(Carica Papaya L)","S3","24<kelembaban tanah<80, 25<suhu<28, 6<pH<6.6"),tags="quality3")
                        data_to2 = data_to2+1
            if 24<=average_sm<80:
                if 18<=average_tt<26:
                    if 6<=average_ph<7.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Tomat buah(Solamun lycopersicon)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 20<=average_sm<24 or 80<=average_sm<90:
                if 26<=average_tt<30 or 16<=average_tt<18:
                    if 5.5<=average_ph<6 or 7.5<=average_tt<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Tomat buah(Solamun lycopersicon)","S2","24<kelembaban tanah<80, 18<suhu<26, 6<pH<7.5"),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm>90 or average_sm<24:
                if 30<=average_tt<35 or 13<=average_tt<16:
                    if average_ph<5.5 or average_tt>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Tomat buah(Solamun lycopersicon)","S3","24<kelembaban tanah<80, 18<suhu<26, 6<pH<7.5"),tags="quality3")
                        data_to2 = data_to2+1
            if 50<=average_sm<90:
                if 19<=average_tt<33:
                    if 5.5<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Jeruk(Citrus aurantium)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif average_sm>90 or average_sm<50:
                if 16<=average_tt<19 or 33<=average_tt<36:
                    if 5.2<=average_ph<5.5 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Jeruk(Citrus aurantium)","S2","50<kelembaban tanah<90, 19<suhu<33, 5.5<pH<7.6"),tags="quality2")
                        data_to2 = data_to2+1
            elif 16<=average_tt<19 or 33<=average_tt<36:
                if 5.2<=average_ph<5.5 or 7.6<=average_ph<8:
                    table_plant.insert("","end",text=str(data_to2),values=("Jeruk(Citrus aurantium)","S3","50<kelembaban tanah<90, 19<suhu<33, 5.5<pH<7.6"),tags="quality3")
                    data_to2 = data_to2+1
            if average_sm>42:
                if 16<=average_tt<20:
                    if 5.5<=average_ph<7.8:
                        table_plant.insert("","end",text=str(data_to2),values=("Apel(Malus silveris MILL)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 36<=average_sm<42:
                if 13<=average_tt<26 or 20<average_tt<25:
                    if 5<=average_ph<5.5 or 7.8<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Apel(Malus silveris MILL)","S2","kelembaban tanah>42, 16<suhu<20, 5.5<pH<7.8"),tags="quality2")
                        data_to2 = data_to2+1
            elif 25<=average_sm<36:
                if 10<=average_tt<13 or 25<average_tt<27:
                    if average_ph<5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Apel(Malus silveris MILL)","S3","kelembaban tanah>42, 16<suhu<20, 5.5<pH<7.8"),tags="quality3")
                        data_to2 = data_to2+1
            if 18<=average_tt<26 :
                if 5<average_ph<6.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Alpukat(Persea americana)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 26<=average_tt<30 or 15<=average_tt<18 :
                if 4.6<average_ph<5 or 6.5<=average_ph<7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Alpukat(Persea americana)","S2","18<suhu<26, 5<pH<6.5"),tags="quality2")
                    data_to2 = data_to2+1
            elif average_tt>30 or 10<=average_tt<15 :
                if average_ph<4.6 or average_ph>7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Alpukat(Persea americana)","S3","18<suhu<26, 5<pH<6.5"),tags="quality3")
                    data_to2 = data_to2+1
            if average_sm>42:
                if 22<=average_tt<28:
                    if 5.5<=average_ph<7.8:
                        table_plant.insert("","end",text=str(data_to2),values=("Manga(Mangifera indic)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 36<=average_sm<42:
                if 18<=average_tt<22 or 28<=average_tt<34:
                    if 5<=average_ph<5.5 or 7.8<=average_tt<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Manga(Mangifera indic)","S2","kelembaban tanah>42, 22<suhu<28, 5.5<pH<7.8"),tags="quality2")
                        data_to2 = data_to2+1
            elif 30<=average_sm<36:
                if 15<=average_tt<18 or 34<=average_tt<40:
                    if average_ph<5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Manga(Mangifera indic)","S3","kelembaban tanah>42, 22<suhu<28, 5.5<pH<7.8"),tags="quality3")
                        data_to2 = data_to2+1
            if 25<=average_tt<28:
                if 5<=average_ph<6:
                    table_plant.insert("","end",text=str(data_to2),values=("Rambutan(Nephelium lappaceun LINN)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 28<=average_tt<32 or 22<=average_tt<25:
                if 4.5<=average_ph<5 or 6<=average_ph<7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Rambutan(Nephelium lappaceun LINN)","S2","25<suhu<28, 5<pH<6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 32<=average_tt<35 or 20<=average_tt<22:
                if average_ph<4.5 or average_ph>7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Rambutan(Nephelium lappaceun LINN)","S3","25<suhu<28, 5<pH<6"),tags="quality3")
                    data_to2 = data_to2+1
            if 22<=average_tt<28:
                if 5<=average_ph<6:
                    table_plant.insert("","end",text=str(data_to2),values=("Jambu biji(Psidium guajava LINN)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 28<=average_tt<34 or 18<=average_tt<22:
                if 4.5<=average_ph<5 or 6<=average_ph<7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Jambu biji(Psidium guajava LINN)","S2","22<suhu<28, 5<pH<6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 34<=average_tt<40 or 15<=average_tt<18:
                if average_ph<4.5 or average_ph>7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Jambu biji(Psidium guajava LINN)","S3","22<suhu<28, 5<pH<6"),tags="quality3")
                    data_to2 = data_to2+1
            if 22<=average_tt<28:
                if 5<=average_ph<6:
                    table_plant.insert("","end",text=str(data_to2),values=("Jambu siam(Psidium guajava)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 28<=average_tt<34 or 18<=average_tt<22:
                if 4.5<=average_ph<5 or 6<=average_ph<7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Jambu siam(Psidium guajava)","S2","22<suhu<28, 5<pH<6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 34<=average_tt<40 or 15<=average_tt<18:
                if average_ph<4.5 or average_ph>7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Jambu siam(Psidium guajava)","S3","22<suhu<28, 5<pH<6"),tags="quality3")
                    data_to2 = data_to2+1
            if average_sm>42:
                if 25<=average_tt<28:
                    if 5.5<=average_ph<7.8:
                        table_plant.insert("","end",text=str(data_to2),values=("Durian(Durio zibethinus MURR)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 36<=average_sm<42:
                if 22<=average_tt<25 or 28<=average_tt<32:
                    if 5<=average_ph<5.5 or 7.8<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Durian(Durio zibethinus MURR)","S2","kelembaban tanah>42, 25<suhu<28, 5.5<pH<7.8"),tags="quality2")
                        data_to2 = data_to2+1
            elif 30<=average_sm<36:
                if 32<=average_tt<35 or 20<=average_tt<22:
                    if average_ph<5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Durian(Durio zibethinus MURR)","S3","kelembaban tanah>42, 25<suhu<28, 5.5<pH<7.8"),tags="quality3")
                        data_to2 = data_to2+1
            if average_sm>42:
                if 22<=average_tt<25:
                    if 5.5<=average_ph<7.8:
                        table_plant.insert("","end",text=str(data_to2),values=("Belimbing(Averrhoa bilimbi)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 36<=average_sm<42:
                if 22<=average_tt<18 or 25<=average_tt<30:
                    if 5<=average_ph<5.5 or 7.8<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Belimbing(Averrhoa bilimbi)","S2","kelembaban tanah>42, 22<suhu<25, 5.5<pH<7.8"),tags="quality2")
                        data_to2 = data_to2+1
            elif 30<=average_sm<36:
                if 30<=average_tt<35 or 10<=average_tt<18:
                    if average_ph<5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Belimbing(Averrhoa bilimbi)","S3","kelembaban tanah>42, 22<suhu<25, 5.5<pH<7.8"),tags="quality3")
                        data_to2 = data_to2+1
            if 24<=average_sm<80:
                if 22<=average_tt<30:
                    if 5.8<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Semangka(Colocynthis citrullus)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 20<=average_sm<24 or 80<=average_sm<90:
                if 30<=average_tt<32 or 20<=average_tt<22:
                    if 5.5<=average_ph<5.8 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Semangka(Colocynthis citrullus)","S2","24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6"),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm<20 or average_sm>90:
                if 33<=average_tt<35 or 18<=average_tt<20:
                    if average_ph<5.5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Semangka(Colocynthis citrullus)","S3","24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6"),tags="quality3")
                        data_to2 = data_to2+1
            if 24<=average_sm<80:
                if 22<=average_tt<30:
                    if 5.8<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Blewah(Passiflora quadranglaria LINN)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 20<=average_sm<24 or 80<=average_sm<90:
                if 30<=average_tt<32 or 20<=average_tt<22:
                    if 5.5<=average_ph<5.8 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Blewah(Passiflora quadranglaria LINN)","S2","24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6"),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm<20 or average_sm>90:
                if 33<=average_tt<35 or 18<=average_tt<20:
                    if average_ph<5.5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Blewah(Passiflora quadranglaria LINN)","S3","24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6"),tags="quality3")
                        data_to2 = data_to2+1
            if 24<=average_sm<80:
                if 22<=average_tt<30:
                    if 5.8<=average_ph<7.6:
                        table_plant.insert("","end",text=str(data_to2),values=("Melon(Citrulus vulgaris SHRAD)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 20<=average_sm<24 or 80<=average_sm<90:
                if 30<=average_tt<32 or 20<=average_tt<22:
                    if 5.5<=average_ph<5.8 or 7.6<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Melon(Citrulus vulgaris SHRAD)","S2","24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6"),tags="quality2")
                        data_to2 = data_to2+1
            elif average_sm<20 or average_sm>90:
                if 33<=average_tt<35 or 18<=average_tt<20:
                    if average_ph<5.5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Melon(Citrulus vulgaris SHRAD)","S3","24<kelembaban tanah<80, 22<suhu<30, 5.8<pH<7.6"),tags="quality3")
                        data_to2 = data_to2+1
            if 25<=average_tt<28:
                if 5<=average_ph<6:
                    table_plant.insert("","end",text=str(data_to2),values=("Duku(Lansium domesticum CORR)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 28<=average_tt<32 or 22<=average_tt<25:
                if 4.5<=average_ph<5 or 6<=average_ph<7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Duku(Lansium domesticum CORR)","S2","25<suhu<28, 5<pH<6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 32<=average_tt<35 or 20<=average_tt<22:
                if average_ph<4.5 or 6<=average_ph>7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Duku(Lansium domesticum CORR)","S3","25<suhu<28, 5<pH<6"),tags="quality3")
                    data_to2 = data_to2+1
            if 22<=average_tt<28:
                if 5<=average_ph<6:
                    table_plant.insert("","end",text=str(data_to2),values=("Cempedak(Artocarpus champeden SPRENG)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 28<=average_tt<34 or 18<=average_tt<22:
                if 4.5<=average_ph<5 or 6<=average_ph<7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Cempedak(Artocarpus champeden SPRENG)","S2","22<suhu<28, 5<pH<6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 34<=average_tt<40 or 15<=average_tt<18:
                if average_ph<4.5 or 6<=average_ph>7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Cempedak(Artocarpus champeden SPRENG)","S3","22<suhu<28, 5<pH<6"),tags="quality3")
                    data_to2 = data_to2+1
            if 22<=average_tt<28:
                if 5<=average_ph<6:
                    table_plant.insert("","end",text=str(data_to2),values=("Nangka(Artocarpus integra MERR)","S1","-"),tags="quality1")
                    data_to2 = data_to2+1
            elif 28<=average_tt<34 or 18<=average_tt<22:
                if 4.5<=average_ph<5 or 6<=average_ph<7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Nangka(Artocarpus integra MERR)","S2","22<suhu<28, 5<pH<6"),tags="quality2")
                    data_to2 = data_to2+1
            elif 34<=average_tt<40 or 15<=average_tt<18:
                if average_ph<4.5 or 6<=average_ph>7.5:
                    table_plant.insert("","end",text=str(data_to2),values=("Nangka(Artocarpus integra MERR)","S3","22<suhu<28, 5<pH<6"),tags="quality3")
                    data_to2 = data_to2+1
            if average_sm<42:
                if 18<=average_tt<25:
                    if 5.5<=average_ph<6.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Sirsak(Annona muricta LINN)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 36<=average_sm<42:
                if 25<=average_tt<30 or 15<=average_tt<18:
                    if 5<=average_ph<5.5 or 6.5<=average_ph<8:
                        table_plant.insert("","end",text=str(data_to2),values=("Sirsak(Annona muricta LINN)","S2","kelembaban tanah>42, 18<suhu<25, 5.5<pH<6.5"),tags="quality2")
                        data_to2 = data_to2+1
            elif 30<=average_sm<36:
                if 30<=average_tt<35 or 10<=average_tt<15:
                    if average_ph<5 or average_ph>8:
                        table_plant.insert("","end",text=str(data_to2),values=("Sirsak(Annona muricta LINN)","S3","kelembaban tanah>42, 18<suhu<25, 5.5<pH<6.5"),tags="quality3")
                        data_to2 = data_to2+1
            if average_sm<42:
                if 18<=average_tt<25:
                    if 5.5<=average_ph<6.5:
                        table_plant.insert("","end",text=str(data_to2),values=("Srikaya(Annona squamosa)","S1","-"),tags="quality1")
                        data_to2 = data_to2+1
            elif 36<=average_sm<42:
                if 25<=average_tt<30 or 15<=average_tt<18:
                    if 4.2<=average_ph<5.5 or 6.5<=average_ph<7:
                        table_plant.insert("","end",text=str(data_to2),values=("Srikaya(Annona squamosa)","S2","kelembaban tanah>42, 18<suhu<25, 5.5<pH<6.5"),tags="quality2")
                        data_to2 = data_to2+1
            elif 30<=average_sm<36:
                if 30<=average_tt<35 or 10<=average_tt<15:
                    if average_ph<4.2 or average_ph>7:
                        table_plant.insert("","end",text=str(data_to2),values=("Srikaya(Annona squamosa)","S3","kelembaban tanah>42, 18<suhu<25, 5.5<pH<6.5"),tags="quality3")
                        data_to2 = data_to2+1

        def go():
            main4.destroy()
            start_1()
        
        button_oke = Button(main4,font=('verdana',13),text="OKE",fg="white",bg="black",bd=8,command=clasify)
        button_oke.place(x=300,y=46)

        button_go = Button(main4,bg="white",bd=4,command=go)
        panahku = PhotoImage(file="arrow.gif")
        button_go.config(image=panahku,width="60",height="40")
        button_go.place(x=10,y=480)
        
        main4.mainloop()

    button_analysis = Button(main1,font=('verdana',13),text="ANALISIS",fg="white",bg="black",bd=8,command=analisis)
    button_analysis.place(x=50,y=170)

    button_classification = Button(main1,font=('verdana',13),text="KLASIFIKASI",fg="white",bg="black",bd=8,command=klasifikasi)
    button_classification.place(x=200,y=170)

    main1.mainloop()
start_1()
