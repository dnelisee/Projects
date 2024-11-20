from turtle import *



def tracer(lenght, line_width=2, line_color='blue') :
    "cette fonction permet de tracer un trait avec les paramètres en entrée"

    color(line_color)
    width(line_width)
    forward(lenght)

def trace_lsysteme(string : str) :
    "cette fonction permet de tracer un L-système correspondant à la chaîne de caractère 'string'"

    speed(0)

    pile = []

    for i in range(len(string)) :

        letter = string[i]

        if letter == 'A' or letter == 'B' :
            tracer(20)
        elif letter == 'g' :
            left(20)
        elif letter == 'd' :
            right(20)
        elif letter == 'a' :
            up()
            tracer(20)
            down()
        elif letter == '[' :
            pile.append(
                (position(), heading())
            )
        elif letter == ']' :
            last = pile.pop()
            setheading(last[1])
            up()
            goto(last[0])
            down()

    # pour que la fênetre ne se ferme pas automatiquement après l'execution du programme
    # la fenetre se fermera lorsqu'on cliquera dessus

    exitonclick()

def remplacer_1(string, letter, pattern) :
    "cette fonction remplace dans 'string' chaque lettre 'letter' par le motif 'pattern' qui est une chaine de caractère"
    
    return string.replace(letter, pattern)

def remplacer_2(string, letter1, pattern1, letter2, pattern2) :
    "cette fonction effectue le changement comme remplacer_1 mais pour deux motifs simultanèment"

    array = list(string)

    for i in range(len(array)) :
        if array[i] == letter1 :
            array[i] = pattern1
        elif array[i] == letter2 :
            array[i] = pattern2

    return "".join(array)

def iterer_lsysteme_1(start : str, rule : tuple[str], k : int) :
    "cette fonction effectue k fois la règle de transformation donnée par 'rule' et ce à partir de la chaine de depart 'start'"

    for i in range(1, k) :
        start = remplacer_1(start, rule[0], rule[1])

    up()
    goto(-300, 100)
    down()
    trace_lsysteme(start)

def iterer_lsysteme_2(start : str, rule1 : tuple[str], rule2 : tuple[str], k : int) :
    "cette fonction est l'amélioration à deux règles de la fonction iterer_lsysteme_1"

    for i in range(1, k) :
        start = remplacer_2(string=start, letter1=rule1[0], pattern1=rule1[1],
                             letter2=rule2[0], pattern2=rule2[1])

    up()
    goto(0, 0)
    down()
    trace_lsysteme(start)
 

iterer_lsysteme_1("A", ("A","A[gA]A[dA][A]"), 5)

#iterer_lsysteme_2(start="AdAdAdA", rule1=("A","AgadAAgAgAAgAagAAdagAAdAdAAdAadAAA"), rule2=("a","aaaaaa"), k=3)

