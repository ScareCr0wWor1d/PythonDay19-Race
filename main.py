# Race

import turtle as t
from random import randint
from tkinter import messagebox
from time import sleep

couleur = ["red", "orange", "yellow", "green", "blue", "purple"]

my_screen = t.setup(600,600)
my_turtle = []
winner = ""

def move_f(t):
    my_turtle[t].forward(10)
    sleep(0.05)
    if my_turtle[t].xcor() == 250:
        return my_turtle[t].color()
    return ""


for i in range(6):
    my_turtle.append(t.Turtle())
    my_turtle[i].shape("turtle")
    my_turtle[i].color(couleur[i])
    my_turtle[i].penup()
    my_turtle[i].goto(-250, -250 + (i * (600 / 6)))
    my_turtle[i].pensize(5)
    my_turtle[i].pendown()

finish_line = t.Turtle()
finish_line.hideturtle()
finish_line.pensize(5)
for y in range(-275, 275, 20):
    finish_line.penup()
    finish_line.goto(250, y+10)
    finish_line.pendown()
    finish_line.goto(250, y+15)

your_bet = t.textinput("Faites votre choix", "Quelle couleur gagnera (red, orange, yellow, green, blue, purple) ? ")

while winner == "":
    tur = randint(0, 5)
    winner = move_f(tur)

if winner[0] == your_bet:
    messagebox.showinfo("Résultat", f"Bravo le gagnant est {winner[0]}")
else:
    messagebox.showinfo("Résultat", f"Malheureusement le gagnant est {winner[0]}")
t.exitonclick()
