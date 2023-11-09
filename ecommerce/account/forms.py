from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        # todo ตรวจสอบความถูกต้องของ อีเมล
    def clean_email(self):

        email = self.cleaned_data.get("email")

        if User.objects.filter(email.exists):

            raise forms.ValidationError('email นี้ไม่ถูกต้อง')

        if len(email >= 350):

            raise forms.ValidationError('ชื่อ email ยาวไป')








