def imena(ime):
    if ime == "sara" or ime == "najdan":
        print("pripada grupi strebera")
    elif ime == "milan":
        print("elon musk 2")
    elif ime == "milovan" or ime == "stefan":
        print("pripada grupi molera")
    elif ime == "aleksa" or ime == "mihajlo":
        print("pripada grupi hakera")
    else:
        print("ime nije u ponudjenima¯\_(ツ)_/¯")
ime = (input("unesite ime nekoga sa radionica: "))
imena(ime)