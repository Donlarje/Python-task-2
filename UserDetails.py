import random
import string


# collecting user data
def user_details():
    first_name = input("Enter your first name: ")
    last_name = input("enter your last name: ")
    email = input("enter your email: ")
    details = [first_name, last_name, email]
    return details


# password generation
def user_password(details):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(5))
    password = str(details[0][0:2] + details[1][-2:] + random_string)
    return password


status = True
container = []

while status:
    details = user_details()
    password = user_password(details)
    print("your password is " + password)

    # check if user is ok with the generated password
    like_password = str.upper(input("are you ok with the generated password. reply with YES or NO: "))

    # create conditionals for password
    password_status = True

    while password_status:
        if like_password == "YES":
            details.append(password)
            container.append(details)

        elif like_password == "NO":
            # user to enter preferred password
            new_password = str(input("enter your preferred password: "))

            # create conditions for accepting new password
            password_length = True

            while password_length:
                if len(new_password) >= 7:
                    # change password to new password and store new password in container
                    details.append(new_password)
                    container.append(details)

                else:
                    print("password must be up to 7 characters")
                    new_password = str(input("enter your preferred password: "))

                    while len(new_password) < 7:
                        # ensure password is up to 7 characters
                        print("password must be up to 7 characters")
                        new_password = str(input("enter your preferred password: "))
                        if len(new_password) >= 7:
                            # change password to new password and store new password in container
                            details.append(new_password)
                            container.append(details)
                        break
                    break
                break
            break
        else:
            print("please enter YES or NO")
            like_password = str.upper(input("are you ok with the generated password. reply with YES or NO: "))

            if like_password == "YES":
                details.append(password)
                container.append(details)

            elif like_password != "YES":
                # user to enter preferred password
                new_password = str(input("enter your preferred password: "))
                # create conditions for accepting new password
                password_length = True

                while password_length:
                    if len(new_password) >= 7:
                        # change password to new password and store new password in container
                        details.append(new_password)
                        container.append(details)

                    else:
                        print("password must be up to 7 characters")
                        new_password = str(input("enter your preferred password: "))

                        while len(new_password) < 7:
                            # ensure password is up to 7 characters
                            print("password must be up to 7 characters")
                            new_password = str(input("enter your preferred password: "))
                            if len(new_password) >= 7:
                                # change password to new password and store new password in container
                                details.append(new_password)
                                container.append(details)
                            break
                        break
                    break
                break
            break
        break

    # for new user
    new_user = str.upper(input("would you like to enter another user? reply YES or NO: "))
    if new_user == "NO":
        status = False
        for data in container:
            print(data)
    elif new_user == "YES":
        status = True
