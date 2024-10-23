from django import forms
from django.contrib.auth.models import User
from .models import Farmer,Product
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Ensure these fields are here

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username


class FarmerRegistrationForm(forms.ModelForm):
    INTEREST_CHOICES = [
        ('crops', 'Crops'),
        ('livestock', 'Livestock'),
        ('dairy', 'Dairy'),
        ('organic', 'Organic Farming'),
        ('sustainable', 'Sustainable Practices'),
        # Add more interests as needed
    ]

    interests = forms.MultipleChoiceField(
        choices=INTEREST_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Interests",
    )

    class Meta:
        model = Farmer
        fields = ['name', 'phone', 'state', 'district', 'city', 'profile_picture', 'interests']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Farmer.objects.filter(phone=phone).exists():
            raise forms.ValidationError("This phone number is already registered.")
        return phone
    
from django import forms
from .models import Product
from datetime import timedelta  # Import timedelta
from django.utils import timezone
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'expiry_date']  # Add other fields as necessary

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Set default expiry_date to 10 days from now if not provided
        if not self.instance.pk and not self.data.get('expiry_date'):
            self.fields['expiry_date'].initial = timezone.now().date() + timedelta(days=10)