from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        # todo ต้องใส่อีเมล
        self.fields['email'].required = True

        # todo ตรวจสอบความถูกต้องของ อีเมล

    def clean_email(self):

        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():

            raise forms.ValidationError('email นี้ไม่ถูกต้อง')

        if len(email >= 200):

            raise forms.ValidationError('ชื่อ email ยาวไป')

        return email