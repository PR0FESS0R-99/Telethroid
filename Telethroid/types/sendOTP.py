import random
from Telethroid.clients import TelethroidClient

class Send_OTP:
    def __init__(self, telethroid_client: TelethroidClient):
        self.telethroid_client = telethroid_client
    
    def generate_otp(self):
        return str(random.randint(100000, 999999))
    
    def send_otp(self, phone_number: str):
        otp = self.generate_otp()
        message = f"Your OTP is {otp}."
        
        params = {'phone_number': phone_number, 'message': message}
        result = self.telethroid_client('send_otp', params)
        if result.get('status') == 'ok':
            return otp
        else:
            return False
