from django.db import models
import phonenumbers
import random


class UserProfle(models.Model):
    phone = models.CharField(max_length=20)
    
    def save(self, *args, **kwargs):
        try:
            parsed_number = phonenumbers.parse(self.phone, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValueError("Invalid phone number")
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
            self.phone = formatted_number
        except phonenumbers.NumberParseException:
            raise ValueError("Unable to parse phone number")

        super().save(*args, **kwargs)
    
    def generate_random_number(self):
        while True:
            number = random.randint(100000, 999999)
            if not self.objects.filter(personal_invite_code=number).exists():
                return number

    personal_invite_code = models.IntegerField(default=generate_random_number)
    stranger_invite_code = models.IntegerField(null=True)
