# cart page
import random   

def generate_random_number():
    return random.randint(1000, 9999)

def take_screenshot(page, name):
    page.screenshot(path=f"screenshots/{name}.png", full_page=True)


# contact
def handle_alert(dialog):

    print("Popup Message Is :", dialog.message)

    dialog.accept()



# home

def print_message(msg):

    print(msg)



# signup

def handle_signup_alert(dialog):

    print("Signup Message:", dialog.message)

    assert dialog.message in [
        "Sign up successful.",
        "This user already exist."
    ]

    dialog.accept()



# login

def handle_login_alert(dialog):

    print("Login Message:", dialog.message)

    assert dialog.message in [
        "Wrong password.",
        "User does not exist."
    ]

    dialog.accept()

