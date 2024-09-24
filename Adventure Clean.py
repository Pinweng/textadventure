name = input("Hallo Abenteurer! Wie lautet dein Name?\n")
print("Willkommen", name, "in der Welt von Almenier!")

answer = input(
    "\nDu befindest dich auf einem Waldweg. Vor dir erspähst du eine Wegkabelung. Welchen Weg möchtest du gehen? (links/rechts)\n")

if answer == "links":
    answer = input(
        "\nDu läufst eine Weile und kommst an einem großen See an. Am Rande des Sees entdeckst du eine Fee. Möchtest du mit der Fee sprechen? (y/n)\n")

    if answer == "y":
        answer = input(
            "\nDie Fee begrüßt dich freundlich und du erhältst ein Schwert von ihr, bevor sie verschwindet.\n Möchtest du durch den See schwimmen oder drum herum laufen? (schwimmen/laufen)\n")

        if answer == "schwimmen":
            print(
                "Du schwimmst raus in den See, doch nach einer Weile stellst du fest, dass der See größer als erwartet ist. Du ertrinkst!")
        elif answer == "laufen":
            answer = input(
                "\nEs ist bereits der halbe Tag vergangen durch deinen Marsch, als du an einem Brunnen ankommst.\n Möchtest du den Brunnen genauer betrachten? (y/n)\n")

            if answer == "y":
                answer = input(
                    "\nDu näherst dich dem Brunnen. Daran ist ein Seil mit einer Kurbel angebracht, und vom Inneren des Brunnens ertönt eine Stimme.\n Was möchtest du tun? (drehen/ignorieren)\n")

                if answer == "drehen":
                    answer = input(
                        "\nDu drehst an der Kurbel und zum Vorschein kommt ein Eimer mit einem sprechenden Frosch. Dieser bedankt sich bei dir und schenkt dir ein Schild!\n "
                        "Du machst dich wieder zurück auf deinen Weg und kommst an einer Brücke an.\n Möchtest du diese Brücke überqueren? (y/n)\n")

                    if answer == "y":
                        answer = input(
                            "\nDu überquerst die wackelige Brücke und kommst an einer Höhle an. Plötzlich landet hinter dir ein Drache.\n Möchtest du gegen den Drachen kämpfen? (y/n)\n")

                        if answer == "y":
                            print(
                                "Du besiegst den Drachen und betrittst die Höhle.\n In der Höhle findest du einen riesigen Goldschatz.\n Glückwunsch Abenteurer, du hast das Spiel gewonnen!!!")
                        elif answer == "n":
                            print(
                                "Du versuchst davon zu laufen, doch der Drache erwischt dich.\n Es tut uns leid, Abenteurer, aber du bist gestorben!\n Danke fürs Spielen")
                    elif answer == "n":
                        print(
                            "\nDu überlegst eine Weile und kommst zu dem Entschluss, dass du die Abenteuer lieber anderen überlässt und gehst nach Hause.\n Das Spiel ist vorbei! Danke fürs Spielen.")
                elif answer == "ignorieren":
                    # Rest des Codes bleibt unverändert
                    pass
            elif answer == "n":
                # Rest des Codes bleibt unverändert
                pass
        else:
            print("Ungültige Eingabe. Das Spiel ist vorbei! Danke fürs Spielen.")
    elif answer == "n":
        # Rest des Codes bleibt unverändert
        pass
    else:
        print("Ungültige Eingabe. Das Spiel ist vorbei! Danke fürs Spielen.")
elif answer == "rechts":
    # Rest des Codes bleibt unverändert
    pass
else:
    print("Ungültige Eingabe. Das Spiel ist vorbei! Danke fürs Spielen.")