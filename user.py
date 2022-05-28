class User:
    def __init__(self, name, email, password, job_title):
        self.name = name
        self.email = email
        self.password = password
        self.job_title = job_title

    def change_password(self, new_password):
        self.password = new_password

    def update_job_title(self, new_job_title):
        self.job_title = new_job_title

    def get_user_details(self):
        print(f"User {self.name} is working as {self.job_title}. You can contact at {self.email}")



