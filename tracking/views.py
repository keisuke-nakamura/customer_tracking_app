from django.http import Http404
from django.shortcuts import render
from .models import PotentialCustomers, TUser, Authority, CustomerRequirement
from .forms import CustomerRequirementForm, CustomerDetailForm


# from django.db.models import Prefetch

# ログイン
def login(request):
    return render(request, 'login.html')


# 見込客一覧
def index(request):
    try:
        potential_customers = PotentialCustomers.objects.filter(bol_assigned=True).select_related(
            'int_media').select_related('int_information_premise').order_by('id')
    except PotentialCustomers.DoesNotExist:
        raise Http404('customer does not exists')
    context = {'potential_customers': potential_customers}
    return render(request, 'index.html', context)


def index_tour(request):
    try:
        potential_customers = PotentialCustomers.objects.filter(bol_assigned=True).select_related(
            'int_media').select_related('int_information_premise').order_by('id')
    except PotentialCustomers.DoesNotExist:
        raise Http404('customer does not exists')
    context = {'potential_customers': potential_customers}
    return render(request, 'index_tour.html', context)


def customer_detail(request, potential_customer_id):
    form = CustomerRequirementForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        save_customer_requirement(request, form, potential_customer_id)
    try:
        potential_customer = PotentialCustomers.objects.select_related('int_information_premise').get(
            pk=potential_customer_id)
        requirements = CustomerRequirement.objects.get(int_tracking_potential_customers_id=potential_customer_id)
        form = init_customer_requirement_field(potential_customer_id, form)
    except PotentialCustomers.DoesNotExist:
        raise Http404("customer does not exist")
    except CustomerRequirement.DoesNotExist:
        requirements = None

    context = {'potential_customer': potential_customer,
               'requirements': requirements,
               'customer_requirement_form': form}

    return render(request, 'customer_detail.html', context)


def customer_detail_tour(request, potential_customer_id):
    form = CustomerRequirementForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        save_customer_requirement(request, form, potential_customer_id)
    try:
        potential_customer = PotentialCustomers.objects.select_related('int_information_premise').get(
            pk=potential_customer_id)
        requirements = CustomerRequirement.objects.get(int_tracking_potential_customers_id=potential_customer_id)
        form = init_customer_requirement_field(potential_customer_id, form)
    except PotentialCustomers.DoesNotExist:
        raise Http404("customer does not exist")
    except CustomerRequirement.DoesNotExist:
        requirements = None

    context = {'potential_customer': potential_customer,
               'requirements': requirements,
               'customer_requirement_form': form}

    return render(request, 'customer_detail.html', context)


def registration(request):
    return render(request, 'customer_registration.html')


def registration_tour(request):
    return render(request, 'customer_registration_tour.html')


def unassigned(request):
    try:
        potential_customers = PotentialCustomers.objects.filter(bol_assigned=False).select_related(
            'int_media').select_related('int_information_premise').order_by('id')
    except PotentialCustomers.DoesNotExist:
        raise Http404("customer does not exists")
    context = {'potential_customers': potential_customers}
    return render(request, 'unassigned.html', context)


def unassigned_detail(request, potential_customer_id):
    form = CustomerDetailForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        save_customer_detail(request, form, potential_customer_id)
    try:
        unassigned_customer = PotentialCustomers.objects.filter(bol_assigned=False).select_related(
            'int_media').select_related('int_information_premise').order_by('id')
        form = init_customer_detail_field(potential_customer_id, form)
    except PotentialCustomers.DoesNotExist:
        raise Http404("customer does not exist")

    context = {'unassigned_customer': unassigned_customer,
               'customer_detail_form': form,
               'potential_customer_id': potential_customer_id}

    return render(request, 'unassigned_detail.html', context)


def unassigned_tour(request):
    try:
        potential_customers = PotentialCustomers.objects.filter(bol_assigned=False).select_related(
            'int_media').select_related('int_information_premise').order_by('id')
    except PotentialCustomers.DoesNotExist:
        raise Http404("customer does not exists")
    context = {'potential_customers': potential_customers}
    return render(request, 'unassigned_tour.html', context)


def unassigned_detail_tour(request, potential_customer_id):
    try:
        potential_customer = PotentialCustomers.objects.select_related('int_information_premise').get(
            pk=potential_customer_id)
    except PotentialCustomers.DoesNotExist:
        raise Http404("customer does not exist")
    context = {'potential_customer': potential_customer}
    return render(request, 'unassigned_detail_tour.html', context)


def authority(request):
    return render(request, 'authority.html')


def authority_tour(request):
    return render(request, 'authority_tour.html')


def account(request):
    try:
        users = Authority.objects.select_related('int_user', 'int_auth', 'int_user__int_dealer__int_name').order_by(
            'int_user')
    except TUser.DoesNotExist:
        raise Http404("user does not exists")
    context = {'users': users}
    return render(request, 'account.html', context)


def account_tour(request):
    try:
        users = Authority.objects.select_related('int_user', 'int_auth', 'int_user__int_dealer__int_name').order_by(
            'int_user')

    except TUser.DoesNotExist:
        raise Http404("user does not exists")
    context = {'users': users}
    return render(request, 'account_tour.html', context)


def tour(request):
    return render(request, 'tour.html')


# 顧客詳細　未割当詳細：顧客情報
def init_customer_detail_field(id, form):
    str_name = PotentialCustomers.objects.values_list('str_name', flat=True).get(
        pk=id)
    str_email = PotentialCustomers.objects.values_list('str_email', flat=True).get(
        pk=id)

    form.fields['str_name'].initial = str_name or None
    form.fields['str_email'].initial = str_email or None

    return form


def save_customer_detail(request, form, id):
    str_name = form.cleaned_data['str_name'] or None
    str_email = form.cleaned_data['str_email'] or None
    obj, created = CustomerRequirement.objects.update_or_create(int_tracking_potential_customers_id=id,
                                                                defaults={'str_name': str_name,
                                                                          'str_email': str_email})


# 顧客詳細：必須条件
def init_customer_requirement_field(id, form):
    int_min_rental_fee = CustomerRequirement.objects.values_list('int_min_rental_fee', flat=True).get(
        int_tracking_potential_customers_id=id)
    int_max_rental_fee = CustomerRequirement.objects.values_list('int_max_rental_fee', flat=True).get(
        int_tracking_potential_customers_id=id)
    bol_construction_iron = '1' if CustomerRequirement.objects.values_list('bol_construction_iron', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_construction_steel = '2' if CustomerRequirement.objects.values_list('bol_construction_steel', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_construction_wooden = '3' if CustomerRequirement.objects.values_list('bol_construction_wooden', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_construction_other = '4' if CustomerRequirement.objects.values_list('bol_construction_other', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    construction_list = [bol_construction_iron, bol_construction_steel, bol_construction_wooden, bol_construction_other]
    bol_layout_oneroom = '1' if CustomerRequirement.objects.values_list('bol_layout_one_room', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_layout_1k = '2' if CustomerRequirement.objects.values_list('bol_layout_1k', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_layout_1dk = '3' if CustomerRequirement.objects.values_list('bol_layout_1dk', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_layout_1ldk = '4' if CustomerRequirement.objects.values_list('bol_layout_1ldk', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_layout_2k = '5' if CustomerRequirement.objects.values_list('bol_layout_2k', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_layout_2dk = '6' if CustomerRequirement.objects.values_list('bol_layout_2dk', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_layout_2ldk = '7' if CustomerRequirement.objects.values_list('bol_layout_2ldk', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_layout_3k = '8' if CustomerRequirement.objects.values_list('bol_layout_3k', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_layout_3dk = '9' if CustomerRequirement.objects.values_list('bol_layout_3dk', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_layout_3ldk = '10' if CustomerRequirement.objects.values_list('bol_layout_3ldk', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_layout_4k = '11' if CustomerRequirement.objects.values_list('bol_layout_4k', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_layout_4dk = '12' if CustomerRequirement.objects.values_list('bol_layout_4dk', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_layout_4ldk = '13' if CustomerRequirement.objects.values_list('bol_layout_4ldk', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    layout_list = [bol_layout_oneroom, bol_layout_1k, bol_layout_1dk, bol_layout_1ldk, bol_layout_2k, bol_layout_2dk,
                   bol_layout_2ldk, bol_layout_3k, bol_layout_3dk, bol_layout_3ldk, bol_layout_4k, bol_layout_4dk,
                   bol_layout_4ldk]
    int_line1 = CustomerRequirement.objects.values_list('int_line1', flat=True).get(
        int_tracking_potential_customers_id=id)
    int_station1 = CustomerRequirement.objects.values_list('int_station1', flat=True).get(
        int_tracking_potential_customers_id=id)
    int_line2 = CustomerRequirement.objects.values_list('int_line2', flat=True).get(
        int_tracking_potential_customers_id=id)
    int_station2 = CustomerRequirement.objects.values_list('int_station2', flat=True).get(
        int_tracking_potential_customers_id=id)
    int_line3 = CustomerRequirement.objects.values_list('int_line3', flat=True).get(
        int_tracking_potential_customers_id=id)
    int_station3 = CustomerRequirement.objects.values_list('int_station3', flat=True).get(
        int_tracking_potential_customers_id=id)
    bol_area1 = '1' if CustomerRequirement.objects.values_list('bol_area1', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_area2 = '2' if CustomerRequirement.objects.values_list('bol_area2', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_area3 = '3' if CustomerRequirement.objects.values_list('bol_area3', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_area4 = '4' if CustomerRequirement.objects.values_list('bol_area4', flat=True).get(
        int_tracking_potential_customers_id=id) else None
    area_list = [bol_area1, bol_area2, bol_area3, bol_area4]
    bol_other_condition1 = '1' if CustomerRequirement.objects.values_list('bol_other_conditions_pet',
                                                                          flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_other_condition2 = '2' if CustomerRequirement.objects.values_list('bol_other_conditions_city_gas',
                                                                          flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_other_condition3 = '3' if CustomerRequirement.objects.values_list('bol_other_conditions_second_floor',
                                                                          flat=True).get(
        int_tracking_potential_customers_id=id) else None
    bol_other_condition4 = '4' if CustomerRequirement.objects.values_list('bol_other_conditions_bath_toilet',
                                                                          flat=True).get(
        int_tracking_potential_customers_id=id) else None
    other_condition_list = [bol_other_condition1, bol_other_condition2, bol_other_condition3, bol_other_condition4]
    form.fields['int_min_rental_fee'].initial = int_min_rental_fee or None
    form.fields['int_max_rental_fee'].initial = int_max_rental_fee or None
    form.fields['construction'].initial = construction_list
    form.fields['layout'].initial = layout_list
    form.fields['int_line1'].initial = int_line1
    form.fields['int_station1'].initial = int_station1
    form.fields['int_line2'].initial = int_line2
    form.fields['int_station2'].initial = int_station2
    form.fields['int_line3'].initial = int_line3
    form.fields['int_station3'].initial = int_station3
    form.fields['area'].initial = area_list
    form.fields['other_condition'].initial = other_condition_list

    return form


def save_customer_requirement(request, form, id):
    int_min_rental_fee = form.cleaned_data['int_min_rental_fee'] or None
    int_max_rental_fee = form.cleaned_data['int_max_rental_fee'] or None
    construction = form.cleaned_data['construction']
    layout = form.cleaned_data['layout']
    int_line1 = form.cleaned_data['int_line1'] or None
    int_station1 = form.cleaned_data['int_station1'] or None
    int_line2 = form.cleaned_data['int_line2'] or None
    int_station2 = form.cleaned_data['int_station2'] or None
    int_line3 = form.cleaned_data['int_line3'] or None
    int_station3 = form.cleaned_data['int_station3'] or None
    area = form.cleaned_data['area']
    school_area = form.cleaned_data['school_area']
    other_condition = form.cleaned_data['other_condition']

    bol_construction_iron = True if '1' in construction else False
    bol_construction_steel = True if '2' in construction else False
    bol_construction_wooden = True if '3' in construction else False
    bol_construction_other = True if '4' in construction else False
    bol_layout_one_room = True if '1' in layout else False
    bol_layout_1k = True if '2' in layout else False
    bol_layout_1dk = True if '3' in layout else False
    bol_layout_1ldk = True if '4' in layout else False
    bol_layout_2k = True if '5' in layout else False
    bol_layout_2dk = True if '6' in layout else False
    bol_layout_2ldk = True if '7' in layout else False
    bol_layout_3k = True if '8' in layout else False
    bol_layout_3dk = True if '9' in layout else False
    bol_layout_3ldk = True if '10' in layout else False
    bol_layout_4k = True if '11' in layout else False
    bol_layout_4dk = True if '12' in layout else False
    bol_layout_4ldk = True if '13' in layout else False
    bol_area1 = True if '1' in area else False
    bol_area2 = True if '2' in area else False
    bol_area3 = True if '3' in area else False
    bol_area4 = True if '4' in area else False
    bol_school_area1 = True if '1' in school_area else False
    bol_school_area2 = True if '2' in school_area else False
    bol_school_area3 = True if '3' in school_area else False
    bol_school_area4 = True if '4' in school_area else False
    bol_other_condition1 = True if '1' in other_condition else False
    bol_other_condition2 = True if '2' in other_condition else False
    bol_other_condition3 = True if '3' in other_condition else False
    bol_other_condition4 = True if '4' in other_condition else False

    obj, created = CustomerRequirement.objects.update_or_create(int_tracking_potential_customers_id=id,
                                                                defaults={'int_tracking_potential_customers_id': id,
                                                                          'int_min_rental_fee': int_min_rental_fee,
                                                                          'int_max_rental_fee': int_max_rental_fee,
                                                                          'bol_construction_iron': bol_construction_iron,
                                                                          'bol_construction_steel': bol_construction_steel,
                                                                          'bol_construction_wooden': bol_construction_wooden,
                                                                          'bol_construction_other': bol_construction_other,
                                                                          'bol_layout_one_room': bol_layout_one_room,
                                                                          'bol_layout_1k': bol_layout_1k,
                                                                          'bol_layout_1dk': bol_layout_1dk,
                                                                          'bol_layout_1ldk': bol_layout_1ldk,
                                                                          'bol_layout_2k': bol_layout_2k,
                                                                          'bol_layout_2dk': bol_layout_2dk,
                                                                          'bol_layout_2ldk': bol_layout_2ldk,
                                                                          'bol_layout_3k': bol_layout_3k,
                                                                          'bol_layout_3dk': bol_layout_3dk,
                                                                          'bol_layout_3ldk': bol_layout_3ldk,
                                                                          'bol_layout_4k': bol_layout_4k,
                                                                          'bol_layout_4dk': bol_layout_4dk,
                                                                          'bol_layout_4ldk': bol_layout_4ldk,
                                                                          'int_line1': int_line1,
                                                                          'int_station1': int_station1,
                                                                          'int_line2': int_line2,
                                                                          'int_station2': int_station2,
                                                                          'int_line3': int_line3,
                                                                          'int_station3': int_station3,
                                                                          'bol_area1': bol_area1,
                                                                          'bol_area2': bol_area2,
                                                                          'bol_area3': bol_area3,
                                                                          'bol_area4': bol_area4,
                                                                          'bol_school_area1': bol_school_area1,
                                                                          'bol_school_area2': bol_school_area2,
                                                                          'bol_school_area3': bol_school_area3,
                                                                          'bol_school_area4': bol_school_area4,
                                                                          'bol_other_condition1': bol_other_condition1,
                                                                          'bol_other_condition2': bol_other_condition2,
                                                                          'bol_other_condition3': bol_other_condition3,
                                                                          'bol_other_condition4': bol_other_condition4,
                                                                          },
                                                                )
