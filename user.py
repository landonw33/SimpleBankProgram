class User:
    # email, name, password, address, user id
    def __init__(self, email, name, password, address_street_number, address_street_name, address_city, address_state, address_zip, user_id):
        self.email = email
        self.name = name
        self.password = password
        self.address_street_number = address_street_number
        self.address_street_name = address_street_name
        self.address_city = address_city
        self.address_state = address_state
        self.address_zip = address_zip
        self.user_id = user_id

    # function for the class
    def change_email(self, new_email):
        self.email = new_email

    def change_password(self, new_password):
        self.password = new_password

    def change_address(self, new_address_street_number, new_address_street_name, new_address_city, new_address_state, new_address_zip):
        self.address_street_number = new_address_street_number
        self.address_street_name = new_address_street_name
        self.address_city = new_address_city
        self.address_state = new_address_state
        self.address_zip = new_address_zip

    # retrieve all of a users info
    def get_user_info(self):
        print(f"Email: {self.email}")
        print(f"Address: {self.address_street_number} {self.address_street_name},{self.address_city},{self.address_state},{self.address_zip}")
