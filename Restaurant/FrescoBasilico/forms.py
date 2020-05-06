from django import forms
from FrescoBasilico.models import Reservation
from django.core.validators import URLValidator, validate_email
from django.core.exceptions import ValidationError
from django.utils import timezone

table_choices = (
    (1, "two guests table no 1"),
    (2, 'two guests table no 2'),
    (3, "two guests table no 3"),
    (4, 'two guests table no 4'),
    (5, "two guests table no 5"),
    (6, 'two guests table no 6'),
    (7, "four guests table no 7"),
    (8, 'four guests table no 8'),
    (9, "four guests table no 9"),
    (10, 'four guests table no 10'),
    (11, 'four guests table no 11'),
    (12, 'eight guests table no 12'),
    (13, 'three guests table no 13'),
)

time_choices = (
    ('10:00:00', '10 AM'),
    ('11:00:00', '11 AM'),
    ('12:00:00', 'Noon'),
    ('13:00:00', '01 PM'),
    ('14:00:00', '02 PM'),
    ('15:00:00', '03 PM'),
    ('16:00:00', '04 PM'),
    ('17:00:00', '05 PM'),
    ('18:00:00', '06 PM'),
    ('19:00:00', '07 PM'),
    ('20:00:00', '08 PM'),
    ('21:00:00', '09 PM'),

)

class ReservationForm(forms.Form):
    first_name = forms.CharField(label="Name", max_length=64, widget=forms.TextInput
                                 (attrs={'placeholder': "Your Name"}))
    last_name = forms.CharField(label="Surname", max_length=64, widget=forms.TextInput
                                 (attrs={'placeholder': "Your Surname"}))
    email = forms.EmailField(widget=forms.TextInput
                                 (attrs={'id': 'reservation_email',
                                         'placeholder': "Your Email"}))
    phone_no = forms.CharField( max_length=12)

    reservation_date = forms.DateField(widget=forms.TextInput
                                 (attrs={'placeholder': "YYYY-MM-DD"}))
    reservation_time = forms.ChoiceField(choices=time_choices)
    table_number = forms.ChoiceField(choices=table_choices)
    special_needs = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":35, 'placeholder': "If you have some ;)"}),
                                  required=False)


class CommentForm(forms.Form):
    author = forms.CharField(max_length=64)
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":40}))
