from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, justify="center", fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(background="white", highlightthickness=0, height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Loading questions...",
                                                     font=QUESTION_FONT,
                                                     fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz!\n"
                                                            f"Final score: {self.quiz.score}/"
                                                            f"{len(self.quiz.question_list)}")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
