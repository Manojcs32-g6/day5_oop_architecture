class AIUser:

    def __init__(self, username, plan_type, credits, total_questions):

        self.username = username
        self.plan_type = plan_type
        self.credits = credits
        self.total_questions = total_questions


    def show_profile(self):

        print("\nUsername:", self.username)

        print("Plan Type:", self.plan_type)

        print("Credits:", self.credits)

        print("Total Questions:", self.total_questions)


    def ask_question(self):

        if self.credits >= 1:

            self.total_questions += 1

            self.credits -= 1

            print("Question processed successfully")

        else:

            print("No credits remaining")


    def upgrade_plan(self, new_plan, extra_credits):

        self.plan_type = new_plan

        self.credits += extra_credits

        print("Plan upgraded successfully")


    def is_premium(self):

        if self.credits > 50:

            print("Premium Active User")

        else:

            print("Basic User")


u1 = AIUser("Manoj", "Basic", 5, 0)

u1.show_profile()

u1.ask_question()

u1.ask_question()

u1.show_profile()

u1.upgrade_plan("Pro", 100)

u1.show_profile()

u1.is_premium()