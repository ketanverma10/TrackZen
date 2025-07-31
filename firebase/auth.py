import pyrebase
from firebase.config import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db=firebase.database()

print("DEBUG:", firebaseConfig.get("databaseURL"))  # Check that it prints the URL



def signup_user(email,password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return user
    except Exception as e:
        return str(e)
    
def login_user(email,password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user
    except Exception as e:
        return str(e)
    
def get_account_info(user_token):
    try:
        return auth.get_account_info(user_token)
    except Exception as e:
        return str(e)

def logout_user():
    # Streamlit logout is session based
    return True