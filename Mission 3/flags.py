import turtle                # module des graphiques tortue
tortue = turtle.Turtle()     # créer une nouvelle tortue

tortue.speed("fastest")

def square(size, color):
    """Trace un carré plein de taille `size` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(4):
        tortue.forward(size)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()

def rectangle(width, height, color):
	tortue.color(color)
	tortue.pendown()
	tortue.begin_fill()
	for i in range(2):
		tortue.forward(width)
		tortue.right(90)
		tortue.forward(height)
		tortue.right(90)
	tortue.end_fill()
	tortue.penup()

def belgian_flag(width):
	tortue.right(180)
	tortue.forward(width/2)
	tortue.right(90)
	tortue.forward(width/3)
	tortue.right(90)

	couleur = ["black", "yellow", "red"]
	for i in range(3):
		rectangle(width/3, 2*width/3, couleur[i])
		tortue.forward(width/3)

def three_color_flag(width, color1, color2, color3):
	tortue.right(180)
	tortue.forward(width/2)
	tortue.right(90)
	tortue.forward(width/3)
	tortue.right(90)

	couleur = [color1, color2, color3]
	for i in range(3):
		rectangle(width/3, 2*width/3, couleur[i])
		tortue.forward(width/3)

def horizontal_flag(width, color1, color2, color3):
	tortue.right(180)
	tortue.forward(width/2)
	tortue.right(90)
	tortue.forward(width/3)
	tortue.right(90)

	couleur = [color1, color2, color3]
	for i in range(3):
		rectangle(width, 2*width/9, couleur[i])
		tortue.right(90)
		tortue.forward(2*width/9)
		tortue.left(90)

def dutch_flag(width):
	horizontal_flag(width, "red", "white", "blue")

def german_flag(width):
	horizontal_flag(width, "black", "red", "yellow")

def luxembourg_flag(width):
	horizontal_flag(width, "red", "white", "cyan")

def french_flag(width):
	three_color_flag(width, "blue", "white", "red")

def draw_star(width):
	tortue.color("yellow")
	tortue.pendown()

	tortue.begin_fill()

	tortue.setheading(0)
	for k in range(5):
		tortue.forward(width/20)
		tortue.right(144)

	tortue.end_fill()
	tortue.penup()

def european_flag(width):
	tortue.right(180)
	tortue.forward(width/2)
	tortue.right(90)
	tortue.forward(width/3)
	tortue.right(90)
	rectangle(width, 2*width/3, "navy")

	tortue.goto(0, 0)
	tortue.setheading(0)

	for i in range(12):
		tortue.left(90 - 30 * i)
		tortue.forward(2/3 * width/3)
		tortue.right(90)

		draw_star(width)
		tortue.goto(0, 0)
		tortue.setheading(0)

def formation():
	belgian_flag(1600)
	tortue.goto(0, 0)
	european_flag(400)

	tortue.goto(-375, 200)
	belgian_flag(100)
	tortue.goto(-225, 200)
	dutch_flag(100)
	tortue.goto(-75, 200)
	german_flag(100)
	tortue.goto(75, 200)
	luxembourg_flag(100)
	tortue.goto(225, 200)
	french_flag(100)
	tortue.goto(375, 200)
	belgian_flag(100)

	for i in range(4):
		tortue.goto(-375, 100-100*i)
		belgian_flag(100)
		tortue.goto(375, 100-100*i)
		belgian_flag(100)

	for i in range(4):		
		tortue.goto(-225 + 150*i, -200)
		belgian_flag(100)
		
formation()
turtle.mainloop()