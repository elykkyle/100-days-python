import turtle
import pandas

FONT = ('Courier', 8, 'normal')

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states = data.state.to_list()
num_states = len(states)
correct_answers = []

typewriter = turtle.Turtle()
typewriter.penup()
typewriter.hideturtle()


while len(correct_answers) < num_states:
    num_correct = len(correct_answers)
    answer_state = screen.textinput(title=f"{num_correct}/{num_states} States Correct", prompt="What is the name of a "
                                                                                               "state?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_answers]
        # for state in states:
        #     if state not in correct_answers:
        #         missing_states.append(state)

        df = pandas.DataFrame(data=missing_states, columns=["States"])
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        correct_answers.append(answer_state)
        state_data = data[data.state == answer_state]
        typewriter.goto(int(state_data.iloc[0].x), int(state_data.iloc[0].y))
        typewriter.write(answer_state, align='center', font=FONT)



