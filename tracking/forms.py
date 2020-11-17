from django import forms
from django.forms import ModelForm
from .models import CustomerRequirement


class CustomerRequirementForm(forms.Form):
    # int_tracking_potential_customers_id = forms.IntegerField(required=False)
    int_min_rental_fee = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'class': 'validate'}),
                                         required=False)
    int_max_rental_fee = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'class': 'validate'}),
                                         required=False)
    # 構造

    construction_choices = [("", "指定なし"), ("test1", "鉄筋系"), ("test2", "鉄骨系"), ("test3", "木造"), ("test4", "その他")]
    construction = forms.MultipleChoiceField(widget=forms.SelectMultiple(),
                                             choices=construction_choices, required = False)

    # class Meta:
    #     model = CustomerRequirement
    #     fields = '__all__'

    # bol_construction_iron = forms.BooleanField(required=False)
    # bol_construction_steel = forms.BooleanField(required=False)
    # bol_construction_wooden = forms.BooleanField(required=False)
    # bol_construction_other = forms.BooleanField(required=False)
    # bol_layout_one_room = forms.BooleanField(required=False)
    # bol_layout_1k = forms.BooleanField(required=False)
    # bol_layout_1dk = forms.BooleanField(required=False)
    # bol_layout_1ldk = forms.BooleanField(required=False)
    # bol_layout_2k = forms.BooleanField(required=False)
    # bol_layout_2dk = forms.BooleanField(required=False)
    # bol_layout_2ldk = forms.BooleanField(required=False)
    # bol_layout_3k = forms.BooleanField(required=False)
    # bol_layout_3dk = forms.BooleanField(required=False)
    # bol_layout_3ldk = forms.BooleanField(required=False)
    # bol_layout_4k = forms.BooleanField(required=False)
    # bol_layout_4dk = forms.BooleanField(required=False)
    # bol_layout_4ldk = forms.BooleanField(required=False)
    # int_line1 = forms.IntegerField(required=False)
    # int_station1 = forms.IntegerField(required=False)
    # int_line2 = forms.IntegerField(required=False)
    # int_station2 = forms.IntegerField(required=False)
    # int_line3 = forms.IntegerField(required=False)
    # int_station3 = forms.IntegerField(required=False)
    # bol_area1 = forms.BooleanField(required=False)
    # bol_area2 = forms.BooleanField(required=False)
    # bol_area3 = forms.BooleanField(required=False)
    # bol_area4 = forms.BooleanField(required=False)
    # int_school_area1 = forms.IntegerField(required=False)
    # int_school_area2 = forms.IntegerField(required=False)
    # int_school_area3 = forms.IntegerField(required=False)
    # int_school_area4 = forms.IntegerField(required=False)
    # bol_other_conditions_pet = forms.BooleanField(required=False)
    # bol_other_conditions_city_gas = forms.BooleanField(required=False)
    # bol_other_conditions_second_floor = forms.BooleanField(required=False)
    # bol_other_conditions_bath_toilet = forms.BooleanField(required=False)
