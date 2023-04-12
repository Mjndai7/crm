from django.test import TestCase
from .managers import CustomUserManager
import json

# Create your tests here.
test_users = [
    {"email": "demo@mam-laka.com", "password": "mamlakatest"},
    {"email": "support@mam-laka.com", "password": "mamlakauser"},
]

class LoginTest(TestCase):
    def setUp(self):
        for user in test_users:
            new_user = CustomUserManager.create(username=user["email"])
            new_user.set_password(user["password"])
            new_user.save()
    
    def test_login(self):
        USER1 = test_users[0]
        res = self.client.post('/api/token',
                                 data=json.dumps({
                                    'email': USER1["email"],
                                    'password': USER1["password"],
                                 }),
                                 content_type='application/json',
                                 )
        result = json.loads(res.content)
        self.assertTrue("access" in result)
        
