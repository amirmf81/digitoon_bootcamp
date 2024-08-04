import os


def clear():
    os.system('clear')


class User:
    def __init__(self, username: str):
        self.username = username
        self.score = 0

    def update_score(self):
        self.score += 1

    def __gt__(self, other):
        return self.username > other.username

    @staticmethod
    def get_username():
        return input("Enter username ")


class ScoreBoard:
    def __init__(self):
        self.list = []

    def add_user(self, user: User):
        self.list.append([user.score, user])
        self.list.sort()

    def update(self):
        for i in range(0, len(self.list)):
            user = self.list[i][1]
            self.list[i] = [user.score, user]
        self.list.sort()

    def print(self):
        for item in self.list:
            print(f"user {item[1].username} scores : {item[0]}")


class UserCreation:
    @staticmethod
    def create_new_user(username):
        user = User(username=username)
        return CreateAns.get_ans(method="1", user=user)

    @staticmethod
    def validate_user(users_list, username):
        if username in users_list:
            return False
        return True

    @staticmethod
    def get_username():
        return User.get_username()


class CreateAns:
    @staticmethod
    def get_ans(method, user):
        return [{"method": method}, user]


class MatchMaker:
    options = ["rock", "paper", "scissors"]

    @staticmethod
    def get_users():
        first = User.get_username()
        second = User.get_username()
        return [first, second]

    @staticmethod
    def validate_users(users: list, all_users: list):
        for user in users:
            if user not in all_users:
                return False
        return True

    @classmethod
    def make_match(cls, user1, user2):
        commands = cls.get_users_command()
        result = cls.result_handler(commands=commands)
        if result == "first":
            return CreateAns.get_ans(method="2", user=user1)
        return CreateAns.get_ans(method="2", user=user2)

    @staticmethod
    def result_handler(commands: list):
        f = "first"
        s = "second"
        if commands[0] == "rock":
            if commands[1] == "scissors":
                return f
            return s
        if commands[0] == "paper":
            if commands[1] == "rock":
                return f
            return s
        if commands[0] == "scissors":
            if commands[1] == "paper":
                return f
            return s

    @classmethod
    def get_users_command(cls):
        while True:
            temp2 = input("press Enter")
            clear()
            print("first user command : ")
            cls.print_options()
            first_command = input()
            temp1 = input("press Enter")
            clear()
            print("second user command : ")
            cls.print_options()
            second_command = input()
            if cls.validate_command(
                    command=first_command
            ) and cls.validate_command(
                command=second_command
            ):
                if cls.is_different(first_comm=first_command,second_comm=second_command):
                    print("ok")
                    return [first_command, second_command]
                print("its a tie. choose again")
            else:
                temp3 = input("press Enter")
                clear()
                print("you should choose one of options")

    @classmethod
    def print_options(cls):
        for i in range(0, len(cls.options)):
            print(f"{cls.options[i]}")

    @classmethod
    def validate_command(cls, command):
        if command in cls.options:
            return True
        return False

    @classmethod
    def is_different(cls, first_comm, second_comm):
        if first_comm != second_comm:
            return True
        return False


class Menu:
    @staticmethod
    def start(users_list):
        while True:
            temp = input("press Enter")
            clear()
            print("1) create new user")
            print("2) make a match")
            print("3) see score board")
            print("4) exit")
            command = input()
            if command == "1":
                clear()
                username = UserCreation.get_username()
                if UserCreation.validate_user(users_list=users_list, username=username):
                    return UserCreation.create_new_user(username=username)
                print("this username has been used before")
            elif command == "2":
                clear()
                users = MatchMaker.get_users()
                if MatchMaker.validate_users(users=users, all_users=users_list):
                    return MatchMaker.make_match(user1=users[0],user2=users[1])
                print("users does not exist")
            elif command == "3":
                return [{"method": "3"}]
            elif command == "4":
                return [{"method": "4"}]
            else:
                print("you should choose one of options")


class Game:
    def __init__(self, users_list: list, scoreboard: ScoreBoard):
        self.users_list = users_list
        self.scoreboard = scoreboard

    def game_handler(self):
        while True:
            ans = Menu.start(self.get_usernames_list())
            ans_method = self.get_method(ans)
            if ans_method == "1":
                self.first_method(user=ans[1])
            elif ans_method == "2":
                self.second_method(username=ans[1])
            elif ans_method == "3":
                self.scoreboard.print()
            else:
                print("finished")
                break

    @staticmethod
    def get_method(our_list):
        return our_list[0]["method"]

    def first_method(self, user):
        self.users_list.append(user)
        self.scoreboard.add_user(user=user)

    def second_method(self, username):
        user = self.get_user(username=username)
        user.update_score()
        self.scoreboard.update()

    def get_user(self, username):
        for user in self.users_list:
            if user.username == username:
                return user

    def get_usernames_list(self):
        ans = []
        for user in self.users_list:
            ans.append(user.username)
        return ans


if __name__ == "__main__":
    our_scoreboard = ScoreBoard()
    game = Game(users_list=[], scoreboard=our_scoreboard)
    game.game_handler()

    