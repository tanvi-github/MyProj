from django import forms
class RegistrationForm(forms.Form):
    name = forms.CharField(label="Enter Your Name", max_length=30)
    email = forms.CharField(label="Enter Your Email", max_length=30, widget=forms.EmailInput)
    contact = forms.CharField(label="Enter Your Contact", max_length=10)
    address = forms.CharField(label="Enter Your Address", max_length=100)
    password = forms.CharField(label="Enter Your Password", max_length=8,min_length=6,widget=forms.PasswordInput)
    CHOICES=[('Male','Male'),('Female','Female')]
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

class LoginForm(forms.Form):
 email=forms.CharField(label="enter your email",max_length=200,widget=forms.EmailInput)
 password=forms.CharField(label="enter your password",max_length=50,widget=forms.PasswordInput)

"""class Basic(forms.Form):
    name=forms.CharField(label="enter your name",max_length=20)
    age=forms.IntegerField(label="enter you age",max_value=100,widget=forms.NumberInput)
    gender=forms.CharField(label="enter your gender",widget=forms.CharField)"""

class Employee(forms.Form):
    name=forms.CharField(label="enter your name")
    salary=forms.IntegerField(label="enter your salary")
    job_title=forms.CharField(label="enter your job title")
