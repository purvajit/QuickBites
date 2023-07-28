from django import forms
from .models import city,user,restaurant,dish


class userlogin(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(label='Enter Password', widget=forms.PasswordInput(),max_length=20)
    



class usersignup(forms.Form):
    username=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=50)
    phone=forms.IntegerField()
    address=forms.CharField(max_length=400)
    city = forms.ModelChoiceField(queryset=city.objects.all(),widget=forms.Select(attrs={'placeholder': 'Select City'}))
    zip=forms.IntegerField()
    password1=forms.CharField(label='Enter Password', widget=forms.PasswordInput(),max_length=20)
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(),max_length=20)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(str(phone)) != 10:
            raise forms.ValidationError("Phone number must be 10 digits.")
        return phone

    def clean_zip(self):
        zip_code = self.cleaned_data['zip']
        if len(str(zip_code)) != 6:
            raise forms.ValidationError("Zip code must be 6 digits.")
        return zip_code

    def clean_password2(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
    

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        # Check if the username already exists
        if user.objects.filter(username=username).exists():
            self.add_error('username', 'This username is already taken.')

        # Check if the email already exists
        if user.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already registered.')

        return cleaned_data


class restaurant_login_form(forms.Form):
    restaurantname=forms.CharField(max_length=50,label="Restaurant Name")
    password=forms.CharField(label='Enter Password', widget=forms.PasswordInput(),max_length=20)


class restaurant_signup_form(forms.Form):
    restaurant_name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=300)
    address = forms.CharField(max_length=400)
    city = forms.ModelChoiceField(queryset=city.objects.all(),widget=forms.Select(attrs={'placeholder': 'Select City'}))
    zip = forms.IntegerField()
    phone = forms.IntegerField()
    email = forms.EmailField(max_length=50)
    image = forms.ImageField(required=False)
    password1=forms.CharField(label='Enter Password', widget=forms.PasswordInput(),max_length=20)
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(),max_length=20)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(str(phone)) != 10:
            raise forms.ValidationError("Phone number must be 10 digits.")
        return phone

    def clean_zip(self):
        zip_code = self.cleaned_data['zip']
        if len(str(zip_code)) != 6:
            raise forms.ValidationError("Zip code must be 6 digits.")
        return zip_code

    def clean_password2(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
    

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('restaurant_name')
        email = cleaned_data.get('email')

        # Check if the username already exists
        if restaurant.objects.filter(name=username).exists():
            self.add_error('username', 'This username is already taken.')

        # Check if the email already exists
        if restaurant.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already registered.')

        return cleaned_data

    # username=forms.CharField(max_length=50)
    # email=forms.EmailField(max_length=50)
    # phone=forms.IntegerField()
    # address=forms.CharField(max_length=400)
    # city = forms.ModelChoiceField(queryset=city.objects.all(),widget=forms.Select(attrs={'placeholder': 'Select City'}))
    # zip=forms.IntegerField()
    # password1=forms.CharField(label='Enter Password', widget=forms.PasswordInput(),max_length=20)
    # password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(),max_length=20)


class DishForm(forms.ModelForm):
    class Meta:
        model = dish
        exclude = ['restaurant_id']
        # fields = ['name', 'description', 'price', 'spiciness_Level', 'image']