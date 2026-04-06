import pandas as pd

class JobSystem:
    def __init__(self):
        self.users = {}
        self.jobs = None

    def load_jobs(self, file_path):
        try:
            self.jobs = pd.read_csv(file_path)
            self.jobs["skills"] = self.jobs["skills"].apply(lambda x: x.split(","))
            print("Jobs loaded successfully!")
        except FileNotFoundError:
            print("File not found! Check the file path.")
        except Exception as e:
            print(f"Error loading file: {e}")

    def register_user(self, username):
        try:
            if username in self.users:
                raise ValueError("User already exists!")

            self.users[username] = {
                "skills" : [],
                "applied_jobs": []
            }
            print(f"User '{username}' registered successfully")

        except ValueError as e:
            print(f"{e}")

    def add_skills(self,username, *skills):
        try:
            user = self.users[username]
            new_skills = [skill.lower().strip() for skill in skills]
            user["skills"] = list(set(user["skills"] + new_skills))

            print(f"Skills added for '{username}' : {user['skills']}")
        except KeyError:
            print("User not found")

    def view_jobs(self):
        try:
            if self.jobs is None:
                raise ValueError("Jobs data not loaded!")
            print("Available Jobs:\n")

            for index, row in self.jobs.iterrows():
                skills = ",".join(row["skills"])
                print(f"{index + 1 }. {row['title']} -> Skills: {skills}")
        except ValueError as e:
            print(f"{e}")
        except Exception as e:
            print(f"Error: {e}")

    def get_recommendations(self, username):
        try:
            user = self.users[username]

            if self.jobs is None:
                raise ValueError("Jobs data not loaded!")

            if not user["skills"]:
                raise ValueError("No skills found for user!")

            user_skills = user["skills"]

            scores = []

            for index, row in self.jobs.iterrows():
                job_skills = row["skills"]

                matching  = [skill for skill in job_skills if skill in user_skills]

                score = len(matching)
                scores.append(score)

            self.jobs["score"] = scores
            sorted_jobs = self.jobs.sort_values(by="score", ascending=False)

            print("Recommended Jobs:\n")

            for index, row in sorted_jobs.iterrows():
                if row["score"] > 0:
                    print(f"{row['title']} -> Match Score: {row['score']}")
        except KeyError:
            print("User not found")
        except ValueError as e:
            print(f"{e}")
        except Exception as e:
            print(f"Error: {e}")
    def apply_job(self, username, job_number):
        try:
            user = self.users[username]

            if self.jobs is None:
                raise ValueError("Jobs data not loaded!")

            job_index = int(job_number) - 1

            job = self.jobs.iloc[job_index]
            job_title = job["title"]

            if job_title in user["applied_jobs"]:
                raise ValueError("You have already applied for this job!")

            user["applied_jobs"].append(job_title)
            print(f"Successfully applied for '{job_title}'")
        except KeyError:
            print("User not found")
        except IndexError:
            print("Invalid job number!")
        except ValueError as e:
            print(f"{e}")
        except Exception as e:
            print(f"Error: {e}")

    def view_applied_jobs(self, username):
        try:
            user = self.users[username]

            if not user["applied_jobs"]:
                raise ValueError("No jobs applied yet!")

            print("Your Applied Jobs:\n")

            for job in user["applied_jobs"]:
                print(f"- {job}")

        except KeyError:
            print("User not found!")
        except ValueError as e:
            print(f"{e}")
        except Exception as e:
            print(f"Error: {e}")

system = JobSystem()
system.load_jobs("job_dataset.csv")

while True:
    print("\n===== Job Recommendation System =====")
    print("1. Register User")
    print("2. Add skills")
    print("3. View Jobs")
    print("4.Get Recommendations")
    print("5. Apply for Job")
    print("6. View Applied Jobs")
    print("7. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            username = input("Enter username: ")
            system.register_user(username)

        elif choice == 2:
            username = input("Enter username: ")
            skills = input("Enter skills (comma separated): ").split(",")
            system.add_skills(username, *skills)

        elif choice == 3:
            system.view_jobs()

        elif choice == 4:
            username = input("Enter username: ")
            system.get_recommendations(username)

        elif choice == 5:
            username = input("Enter username: ")
            job_number = input("Enter job number: ")
            system.apply_job(username, job_number)

        elif choice == 6:
            username = input("Enter username: ")
            system.view_applied_jobs(username)

        elif choice == 7:
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("⚠️ Invalid choice!")

    except ValueError:
        print("❌ Please enter a valid number!")