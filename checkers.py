import turtle as t 
#next part is to have the grid in the center of the screen
side = 10

t.up()
t.setheading(270)
down_distance = 10 * side
#because the board is 20*20 so to go midway 
t.fd(down_distance)
t.setheading(180)
left_distance = 10 * side
t.fd(left_distance)
t.setheading(0)
t.down()
#code for each pixel 
def square(color):
  t.color(color)
  t.begin_fill()
  for num in range(4):
    t.fd(side)
    t.rt(90)
  t.end_fill()
  t.fd(side)
#code for drawing lines 
line_counter = 0 
while(line_counter < 20):
  
  #code for a single row 
  counter = 1
  while (counter<=20):
    if(line_counter %2 == 0):
      if (counter % 2 == 0):
        square("red")
      else:
        square("black")
    else:
      if (counter % 2 == 0):
        square("black")
      else:
        square("red")

    counter = counter + 1
  #go back to left for first pixel
  t.setheading(180)
  t.penup()
  t.forward(side*20)
  t.setheading(90)
  t.forward(side)
  t.setheading(0)
  t.pendown()

  line_counter = line_counter + 1 