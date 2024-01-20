import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t=turtle.Turtle()
t.hideturtle()
t.penup()
score = 0
State_list = data["state"].to_list()
correct_list=[]
while score != 50:  
    if score > 0:
        answer_state = screen.textinput(title=f" {score}/50 ", prompt="What's another state name?").title()
        if answer_state == "Exit":
            
            break
    elif score == 0:
        answer_state = screen.textinput(title=f" Guess the state ", prompt="What's a name of a state?").title()
        if answer_state == "Exit":
            break
    if answer_state in State_list and answer_state not in correct_list:
        x_coor = data["x"][data["state"] == answer_state]
        y_coor = data["y"][data["state"] == answer_state]
        t.goto(int(x_coor),int(y_coor))
        t.write(answer_state)
        score = score + 1
        correct_list.append(answer_state)
    else: 
        continue

for x in State_list:
    if x in correct_list:
        State_list.remove(x)

new_csv =pandas.DataFrame(State_list)
new_csv.to_csv("remaining.States.csv")