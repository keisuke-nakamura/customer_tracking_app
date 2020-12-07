from django import forms
from django.forms import ModelForm
from .models import UlMainStructureCategory, UlLayoutCategory, TlLine, TlStation, TlArea, TlSchoolArea, TlOtherCondition


class CustomerRequirementForm(forms.Form):

    int_min_rental_fee = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'class': 'validate'}),
                                         required=False)
    int_max_rental_fee = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'class': 'validate'}),
                                         required=False)
    # 構造
    construction_choices = list(UlMainStructureCategory.objects.values_list('pk', 'str_main_structure').order_by('pk').all())
    construction = forms.MultipleChoiceField(widget=forms.SelectMultiple(),
                                             choices=construction_choices, required=False)

    # 間取
    layout_choices = list(UlLayoutCategory.objects.values_list('pk', 'str_layout').order_by('pk').all())
    layout = forms.MultipleChoiceField(widget=forms.SelectMultiple(), choices=layout_choices, required=False)

    # 沿線1
    line_choices1 = list(TlLine.objects.values_list('int_line_id', 'str_line').order_by('int_line_id').all())
    int_line1 = forms.ChoiceField(widget=forms.Select(), choices=line_choices1, required=False)

    # 駅1
    station_choices1 = list(TlStation.objects.values_list('int_station_id', 'str_station').order_by('int_station_id').all())
    int_station1 = forms.ChoiceField(widget=forms.Select(), choices=station_choices1, required=False)

    # 沿線2
    line_choices2 = list(TlLine.objects.values_list('int_line_id', 'str_line').order_by('int_line_id').all())
    int_line2 = forms.ChoiceField(widget=forms.Select(), choices=line_choices2, required=False)

    # 駅2
    station_choices2 = list(TlStation.objects.values_list('int_station_id', 'str_station').order_by('int_station_id').all())
    int_station2 = forms.ChoiceField(widget=forms.Select(), choices=station_choices2, required=False)

    # 沿線3
    line_choices3 = list(TlLine.objects.values_list('int_line_id', 'str_line').order_by('int_line_id').all())
    int_line3 = forms.ChoiceField(widget=forms.Select(), choices=line_choices3, required=False)

    # 駅3
    station_choices3 = list(TlStation.objects.values_list('int_station_id', 'str_station').order_by('int_station_id').all())
    int_station3 = forms.ChoiceField(widget=forms.Select(), choices=station_choices3, required=False)

    # エリア
    area_choices = list(TlArea.objects.values_list('int_area_id', 'str_area').order_by('int_area_id').all())
    area = forms.MultipleChoiceField(widget=forms.SelectMultiple(), choices=area_choices, required=False)

    # 学区
    school_area_choices = list(TlSchoolArea.objects.values_list('int_school_area_id', 'str_school_area').order_by('int_school_area_id').all())
    school_area = forms.MultipleChoiceField(widget=forms.SelectMultiple(), choices=school_area_choices, required=False)

    # その他条件
    other_condition_choices = list(TlOtherCondition.objects.values_list('int_other_condition_id', 'str_other_condition').order_by('int_other_condition_id').all())
    other_condition = forms.MultipleChoiceField(widget=forms.SelectMultiple(), choices=other_condition_choices, required=False)


class CustomerDetailForm(forms.Form):

    str_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '名前', 'class': 'validate'}),
                                         required=False)
    str_email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'メールアドレス', 'class': 'validate'}),
                                         required=False)
