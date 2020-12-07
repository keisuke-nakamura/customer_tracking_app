from django.db import models
from django.utils import timezone


# from tsweb
class TPremise(models.Model):
    int_premise_id = models.AutoField(primary_key=True)
    int_user_branch_id = models.IntegerField()
    int_user_section_id = models.IntegerField()
    str_premise_code = models.CharField(max_length=100, blank=True, null=True)
    int_premise_type_id = models.IntegerField()
    int_ownership_form_id = models.IntegerField()
    str_furigana = models.CharField(max_length=100)
    str_name = models.CharField(max_length=100)
    str_name_post = models.CharField(max_length=100, blank=True, null=True)
    str_zip_code_3 = models.CharField(max_length=3, blank=True, null=True)
    str_zip_code_4 = models.CharField(max_length=4, blank=True, null=True)
    str_addr_state = models.CharField(max_length=20)
    str_addr_city = models.CharField(max_length=50)
    str_addr_block = models.CharField(max_length=100, blank=True, null=True)
    str_addr_no = models.CharField(max_length=100, blank=True, null=True)
    str_addr_block_open = models.CharField(max_length=100, blank=True, null=True)
    str_addr_no_open = models.CharField(max_length=100, blank=True, null=True)
    int_area_id = models.IntegerField(blank=True, null=True)
    str_house_number = models.CharField(max_length=255, blank=True, null=True)
    str_traffic = models.CharField(max_length=255, blank=True, null=True)
    int_train_id_1 = models.IntegerField(blank=True, null=True)
    int_station_id_1 = models.IntegerField(blank=True, null=True)
    int_walking_time_station_1 = models.IntegerField(blank=True, null=True)
    int_time_by_bus_1 = models.IntegerField(blank=True, null=True)
    str_bus_stop_name_1 = models.CharField(max_length=60, blank=True, null=True)
    int_train_id_2 = models.IntegerField(blank=True, null=True)
    int_station_id_2 = models.IntegerField(blank=True, null=True)
    int_walking_time_station_2 = models.IntegerField(blank=True, null=True)
    int_time_by_bus_2 = models.IntegerField(blank=True, null=True)
    str_bus_stop_name_2 = models.CharField(max_length=60, blank=True, null=True)
    int_train_id_3 = models.IntegerField(blank=True, null=True)
    int_station_id_3 = models.IntegerField(blank=True, null=True)
    int_walking_time_station_3 = models.IntegerField(blank=True, null=True)
    int_time_by_bus_3 = models.IntegerField(blank=True, null=True)
    str_bus_stop_name_3 = models.CharField(max_length=60, blank=True, null=True)
    int_map_no = models.IntegerField(blank=True, null=True)
    int_layout_plan_no = models.IntegerField(blank=True, null=True)
    int_main_structure_id = models.IntegerField(blank=True, null=True)
    int_num_of_floor_upper = models.IntegerField(blank=True, null=True)
    int_num_of_floor_under = models.IntegerField(blank=True, null=True)
    int_num_of_houses = models.IntegerField(blank=True, null=True)
    int_num_of_car_parking = models.IntegerField(blank=True, null=True)
    bol_newly_built_flg = models.BooleanField(blank=True, null=True)
    int_upkeep_company_id = models.IntegerField(blank=True, null=True)
    int_upkeep_type_id = models.IntegerField(blank=True, null=True)
    str_note_of_upkeep = models.TextField(blank=True, null=True)
    bol_management_consignment_flg = models.BooleanField()
    bol_company_possession_flg = models.BooleanField()
    int_reg_branch_id = models.IntegerField()
    int_reg_section_id = models.IntegerField()
    tim_reg_date = models.DateTimeField()
    int_upd_branch_id = models.IntegerField()
    int_upd_section_id = models.IntegerField()
    tim_upd_date = models.DateTimeField()
    int_reg_user_id = models.IntegerField()
    int_upd_user_id = models.IntegerField()
    dat_completion = models.DateField(blank=True, null=True)
    int_pic_link_id_1 = models.IntegerField(blank=True, null=True)
    int_pic_link_id_2 = models.IntegerField(blank=True, null=True)
    flt_distance_1 = models.FloatField(blank=True, null=True)
    flt_distance_2 = models.FloatField(blank=True, null=True)
    flt_distance_3 = models.FloatField(blank=True, null=True)
    bol_del_flg = models.BooleanField(blank=True, null=True)
    str_design = models.CharField(max_length=50, blank=True, null=True)
    str_construction = models.CharField(max_length=50, blank=True, null=True)
    str_external_finish = models.CharField(max_length=50, blank=True, null=True)
    flt_total_area = models.FloatField(blank=True, null=True)
    flt_lendina_area = models.FloatField(blank=True, null=True)
    flt_building_height = models.FloatField(blank=True, null=True)
    flt_max_floor_weight = models.FloatField(blank=True, null=True)
    str_building_memo = models.TextField(blank=True, null=True)
    int_car_time_1 = models.IntegerField(blank=True, null=True)
    int_car_time_2 = models.IntegerField(blank=True, null=True)
    int_car_time_3 = models.IntegerField(blank=True, null=True)
    int_pic_link_id_3 = models.IntegerField(blank=True, null=True)
    int_pic_link_id_4 = models.IntegerField(blank=True, null=True)
    str_premise_short_name = models.CharField(max_length=20, blank=True, null=True)
    str_adv_point = models.TextField(blank=True, null=True)
    bol_management_rule_flg = models.BooleanField(blank=True, null=True)
    str_structure_info = models.CharField(max_length=50, blank=True, null=True)
    int_origin_id = models.IntegerField(blank=True, null=True)
    int_staff_id = models.IntegerField(blank=True, null=True)
    dat_date_of_pre_investigation = models.DateField(blank=True, null=True)
    dat_date_renewal = models.DateField(blank=True, null=True)
    int_upkeep_type_id_2 = models.IntegerField(blank=True, null=True)
    int_union_dealer = models.IntegerField(blank=True, null=True)
    dat_date_of_union_formation = models.DateField(blank=True, null=True)
    int_sale_type_id = models.IntegerField(blank=True, null=True)
    flt_premise_area = models.FloatField(blank=True, null=True)
    flt_longitude = models.FloatField(blank=True, null=True)
    flt_latitude = models.FloatField(blank=True, null=True)
    str_portal_state = models.CharField(max_length=20, blank=True, null=True)
    str_portal_city = models.CharField(max_length=100, blank=True, null=True)
    str_portal_add1 = models.CharField(max_length=20, blank=True, null=True)
    str_portal_add2 = models.CharField(max_length=20, blank=True, null=True)
    str_portal_add3 = models.CharField(max_length=20, blank=True, null=True)
    str_bus_line_name_1 = models.CharField(max_length=15, blank=True, null=True)
    str_bus_line_name_2 = models.CharField(max_length=15, blank=True, null=True)
    str_bus_line_name_3 = models.CharField(max_length=15, blank=True, null=True)
    str_pic_memo_1 = models.TextField(blank=True, null=True)
    str_pic_memo_2 = models.TextField(blank=True, null=True)
    str_pic_memo_3 = models.TextField(blank=True, null=True)
    bol_post_pic_1 = models.BooleanField()
    bol_post_pic_2 = models.BooleanField()
    bol_post_pic_3 = models.BooleanField()
    str_portal_add4 = models.CharField(max_length=100, blank=True, null=True)
    int_public_code = models.CharField(max_length=5, blank=True, null=True)
    bol_owner_print_flg = models.BooleanField()
    bol_management_change_flg = models.BooleanField()
    dat_date_of_union_start = models.DateField(blank=True, null=True)
    int_upkeep_account_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = u'"public\".\"t_premise"'


class TUnit(models.Model):
    int_unit_id = models.AutoField(primary_key=True)
    int_premise_id = models.IntegerField()
    int_branch_id = models.IntegerField()
    int_section_id = models.IntegerField()
    str_unit_code = models.CharField(max_length=100, blank=True, null=True)
    int_usage_id = models.IntegerField()
    str_usage_type = models.CharField(max_length=100, blank=True, null=True)
    int_contract_type_id = models.IntegerField(blank=True, null=True)
    int_moving_possible_season = models.IntegerField()
    bol_company_possession_flg = models.BooleanField()
    int_origin_id = models.IntegerField(blank=True, null=True)
    bol_introduction_allow_flg = models.BooleanField()
    bol_rent_stop_flg = models.BooleanField()
    int_deal_type_id = models.IntegerField()
    flt_commission_rate = models.FloatField(blank=True, null=True)
    flt_advertising_rate = models.FloatField(blank=True, null=True)
    str_one_point_advertisement = models.TextField(blank=True, null=True)
    str_attached_structure = models.TextField(blank=True, null=True)
    bol_administrative_expenses_disp_flg = models.BooleanField(blank=True, null=True)
    bol_parking_charge_disp_flg = models.BooleanField(blank=True, null=True)
    int_advance_payment = models.IntegerField(blank=True, null=True)
    int_limit_return_money = models.IntegerField(blank=True, null=True)
    int_offers_before_leaving = models.IntegerField(blank=True, null=True)
    flt_rates_of_damage_money = models.FloatField(blank=True, null=True)
    int_days_of_exemption_from_delay = models.IntegerField(blank=True, null=True)
    int_reg_branch_id = models.IntegerField()
    int_reg_section_id = models.IntegerField()
    int_reg_user_id = models.IntegerField()
    tim_reg_date = models.DateTimeField()
    int_upd_branch_id = models.IntegerField()
    int_upd_section_id = models.IntegerField()
    int_upd_user_id = models.IntegerField()
    tim_upd_date = models.DateTimeField()
    bol_del_flg = models.BooleanField(blank=True, null=True)
    str_owner_info_comment = models.TextField(blank=True, null=True)
    str_unit_name = models.CharField(max_length=100)
    str_unit_note = models.TextField(blank=True, null=True)
    str_portal_ary = models.TextField(blank=True, null=True)
    int_pic_link_id_1 = models.IntegerField(blank=True, null=True)
    int_pic_link_id_2 = models.IntegerField(blank=True, null=True)
    int_pic_link_id_3 = models.IntegerField(blank=True, null=True)
    int_pic_link_id_4 = models.IntegerField(blank=True, null=True)
    int_video_link_id = models.IntegerField(blank=True, null=True)
    dat_moving_possible_date = models.DateField(blank=True, null=True)
    int_repayment_target_detail_type_id = models.IntegerField(blank=True, null=True)
    int_repayment_target_detail_id = models.IntegerField(blank=True, null=True)
    bol_insurance_flg = models.BooleanField(blank=True, null=True)
    int_insurance_fee = models.IntegerField(blank=True, null=True)
    bol_guarantee_flg = models.BooleanField(blank=True, null=True)
    int_contract_sts = models.IntegerField(blank=True, null=True)
    int_info_renew = models.IntegerField()
    bol_reform_expense_actual_flg = models.BooleanField(blank=True, null=True)
    int_reform_expense_actual_detail_type_id = models.IntegerField(blank=True, null=True)
    int_reform_expense_actual_detail_id = models.IntegerField(blank=True, null=True)
    bol_commission_tax_flg = models.BooleanField(blank=True, null=True)
    bol_advertising_tax_flg = models.BooleanField(blank=True, null=True)
    int_commission_fixed_amount = models.IntegerField(blank=True, null=True)
    int_advertising_fixed_amount = models.IntegerField(blank=True, null=True)
    dat_origin_check = models.DateField(blank=True, null=True)
    int_commission_tax_type = models.IntegerField(blank=True, null=True)
    int_advertising_tax_type = models.IntegerField(blank=True, null=True)
    int_renew_span = models.IntegerField(blank=True, null=True)
    int_cnt_text_id = models.IntegerField(blank=True, null=True)
    flt_com_origin = models.FloatField(blank=True, null=True)
    flt_com_trader = models.FloatField(blank=True, null=True)
    flt_com_owner_load = models.FloatField(blank=True, null=True)
    flt_com_applicant_load = models.FloatField(blank=True, null=True)
    str_com_comment = models.CharField(max_length=50, blank=True, null=True)
    dat_exp_adv = models.DateField(blank=True, null=True)
    int_pic_link_id_5 = models.IntegerField(blank=True, null=True)
    bol_auto_renew_flg = models.BooleanField(blank=True, null=True)
    bol_representative_flg = models.BooleanField(blank=True, null=True)
    flt_owner_commission_rate = models.FloatField(blank=True, null=True)
    flt_owner_advertising_rate = models.FloatField(blank=True, null=True)
    bol_owner_commission_tax_flg = models.BooleanField(blank=True, null=True)
    bol_owner_advertising_tax_flg = models.BooleanField(blank=True, null=True)
    int_owner_advertising_fixed_amount = models.IntegerField(blank=True, null=True)
    int_owner_commission_fixed_amount = models.IntegerField(blank=True, null=True)
    int_owner_commission_tax_type = models.IntegerField(blank=True, null=True)
    int_owner_advertising_tax_type = models.IntegerField(blank=True, null=True)
    bol_offers_before_leaving = models.BooleanField(blank=True, null=True)
    bol_limit_return_money = models.BooleanField(blank=True, null=True)
    bol_new_flg = models.BooleanField(blank=True, null=True)
    bol_price_falls_flg = models.BooleanField(blank=True, null=True)
    dat_unit_info_update = models.DateField(blank=True, null=True)
    dat_date_of_unit_investigation = models.DateField(blank=True, null=True)
    dat_date_of_register_proclaimed = models.DateField(blank=True, null=True)
    int_comparative_rental_fee = models.IntegerField(blank=True, null=True)
    int_free_rental_fee = models.IntegerField(blank=True, null=True)
    bol_reformming = models.BooleanField(blank=True, null=True)
    bol_other_management_flg = models.BooleanField(blank=True, null=True)
    flt_receipt_rate = models.FloatField(blank=True, null=True)
    str_deal_memo = models.TextField(blank=True, null=True)
    flt_deal_fee_rate = models.FloatField(blank=True, null=True)
    bol_deal_tax_flg = models.BooleanField(blank=True, null=True)
    int_deal_fixed_amount = models.IntegerField(blank=True, null=True)
    int_deal_tax_type = models.IntegerField(blank=True, null=True)
    int_advance_payment_remit_type = models.IntegerField()
    dat_renewal_date = models.DateField(blank=True, null=True)
    dat_recruit_stop_date = models.DateField(blank=True, null=True)
    dat_recruit_start_date = models.DateField(blank=True, null=True)
    dat_sts_date = models.DateField(blank=True, null=True)
    int_insurance_yesrs = models.IntegerField(blank=True, null=True)
    str_guarantee_detail = models.CharField(max_length=100, blank=True, null=True)
    int_offers_before_renewal = models.IntegerField(blank=True, null=True)
    bol_offers_before_renewal = models.BooleanField()
    str_short_leave_memo = models.TextField(blank=True, null=True)
    str_rent_stop_memo = models.TextField(blank=True, null=True)
    dat_add_ad = models.DateField(blank=True, null=True)
    int_unit_assessment_fee = models.IntegerField(blank=True, null=True)
    bol_consultation_flg = models.BooleanField(blank=True, null=True)
    int_unit_dealer_id = models.IntegerField(blank=True, null=True)
    str_pic_memo_1 = models.TextField(blank=True, null=True)
    str_pic_memo_2 = models.TextField(blank=True, null=True)
    str_pic_memo_3 = models.TextField(blank=True, null=True)
    str_pic_memo_4 = models.TextField(blank=True, null=True)
    str_pic_memo_5 = models.TextField(blank=True, null=True)
    bol_post_pic_1 = models.BooleanField()
    bol_post_pic_2 = models.BooleanField()
    bol_post_pic_3 = models.BooleanField()
    bol_post_pic_4 = models.BooleanField()
    bol_post_pic_5 = models.BooleanField()
    bol_sublease_allow_flg = models.BooleanField()
    bol_renotta_flg = models.BooleanField(blank=True, null=True)
    bol_pickup_flg = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = u'"public\".\"t_unit"'


class TNameList(models.Model):
    int_name_list_id = models.AutoField(primary_key=True)
    int_name_type = models.IntegerField()
    str_name = models.CharField(max_length=100)
    str_furigana = models.CharField(max_length=100, blank=True, null=True)
    int_sex = models.IntegerField(blank=True, null=True)
    int_registered_domicile_id = models.IntegerField(blank=True, null=True)
    str_zip_code_3 = models.CharField(max_length=3, blank=True, null=True)
    str_zip_code_4 = models.CharField(max_length=4, blank=True, null=True)
    str_addr_state = models.CharField(max_length=20, blank=True, null=True)
    str_addr = models.CharField(max_length=200, blank=True, null=True)
    str_addr_premise = models.CharField(max_length=200, blank=True, null=True)
    str_tel = models.CharField(max_length=20, blank=True, null=True)
    str_fax = models.CharField(max_length=20, blank=True, null=True)
    str_mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    str_email = models.CharField(max_length=100, blank=True, null=True)
    int_habitation_years = models.IntegerField(blank=True, null=True)
    str_office = models.CharField(max_length=200, blank=True, null=True)
    str_representative = models.CharField(max_length=100, blank=True, null=True)
    int_post_id = models.IntegerField(blank=True, null=True)
    str_office_zip_code_3 = models.CharField(max_length=3, blank=True, null=True)
    str_office_zip_code_4 = models.CharField(max_length=4, blank=True, null=True)
    str_office_addr_state = models.CharField(max_length=20, blank=True, null=True)
    str_office_addr = models.CharField(max_length=200, blank=True, null=True)
    str_office_addr_premise = models.CharField(max_length=200, blank=True, null=True)
    str_office_tel = models.CharField(max_length=20, blank=True, null=True)
    str_office_fax = models.CharField(max_length=20, blank=True, null=True)
    int_office_capital = models.IntegerField(blank=True, null=True)
    int_office_num_of_employees = models.IntegerField(blank=True, null=True)
    str_office_type_of_industry = models.CharField(max_length=100, blank=True, null=True)
    str_section = models.CharField(max_length=50, blank=True, null=True)
    str_type_of_job = models.CharField(max_length=50, blank=True, null=True)
    int_annual_income = models.IntegerField(blank=True, null=True)
    int_length_of_service = models.IntegerField(blank=True, null=True)
    str_memo = models.TextField(blank=True, null=True)
    str_transfer_name_kana_1 = models.CharField(max_length=100, blank=True, null=True)
    str_transfer_name_kana_2 = models.CharField(max_length=100, blank=True, null=True)
    str_transfer_name_kana_3 = models.CharField(max_length=100, blank=True, null=True)
    bol_black_list_flg = models.BooleanField(blank=True, null=True)
    str_note_of_black_list = models.TextField(blank=True, null=True)
    str_university_name = models.CharField(max_length=100, blank=True, null=True)
    int_admission_fiscal_year = models.IntegerField(blank=True, null=True)
    int_grader = models.IntegerField(blank=True, null=True)
    str_part_name = models.CharField(max_length=100, blank=True, null=True)
    str_part_person_name = models.CharField(max_length=100, blank=True, null=True)
    dat_birthday = models.DateField(blank=True, null=True)
    int_part_post_id = models.IntegerField(blank=True, null=True)
    str_url = models.CharField(max_length=200, blank=True, null=True)
    str_holiday = models.CharField(max_length=200, blank=True, null=True)
    dat_office_establishment_year = models.DateField(blank=True, null=True)
    int_representative_post_id = models.IntegerField(blank=True, null=True)
    bol_del_flg = models.BooleanField(blank=True, null=True)
    int_reg_branch_id = models.IntegerField(blank=True, null=True)
    int_reg_section_id = models.IntegerField(blank=True, null=True)
    int_reg_user_id = models.IntegerField(blank=True, null=True)
    tim_reg_date = models.DateTimeField(blank=True, null=True)
    int_upd_branch_id = models.IntegerField(blank=True, null=True)
    int_upd_section_id = models.IntegerField(blank=True, null=True)
    int_upd_user_id = models.IntegerField(blank=True, null=True)
    tim_upd_date = models.DateTimeField(blank=True, null=True)
    str_part_person_name_mob = models.CharField(max_length=20, blank=True, null=True)
    int_part_person_title = models.IntegerField()
    str_mail_name = models.CharField(max_length=100, blank=True, null=True)
    str_mail_zip_code_3 = models.CharField(max_length=3, blank=True, null=True)
    str_mail_zip_code_4 = models.CharField(max_length=4, blank=True, null=True)
    str_mail_addr_state = models.CharField(max_length=20, blank=True, null=True)
    str_mail_addr_city = models.CharField(max_length=50, blank=True, null=True)
    str_mail_addr_block = models.CharField(max_length=100, blank=True, null=True)
    int_mail_type_id = models.IntegerField(blank=True, null=True)
    str_mail_memo = models.TextField(blank=True, null=True)
    str_mail_tel = models.TextField(blank=True, null=True)
    str_mansion_trader_no = models.CharField(max_length=50, blank=True, null=True)
    str_dealer_abbreviation = models.CharField(max_length=50, blank=True, null=True)
    int_smail_part_id = models.IntegerField(blank=True, null=True)
    str_mail_name1 = models.CharField(max_length=100, blank=True, null=True)
    int_graduation_fiscal_year = models.IntegerField(blank=True, null=True)
    bol_dm_flg_1 = models.BooleanField(blank=True, null=True)
    bol_dm_flg_2 = models.BooleanField(blank=True, null=True)
    bol_dm_flg_3 = models.BooleanField(blank=True, null=True)
    bol_dm_flg_4 = models.BooleanField(blank=True, null=True)
    bol_dm_flg_5 = models.BooleanField(blank=True, null=True)
    bol_dm_flg_6 = models.BooleanField(blank=True, null=True)
    bol_dm_flg_7 = models.BooleanField(blank=True, null=True)
    bol_dm_flg_8 = models.BooleanField(blank=True, null=True)
    bol_dm_flg_9 = models.BooleanField(blank=True, null=True)
    bol_dm_flg_10 = models.BooleanField(blank=True, null=True)
    int_black_list_id = models.IntegerField()
    str_black_list_memo = models.TextField(blank=True, null=True)
    bol_long_delinquency_flg = models.BooleanField(blank=True, null=True)
    str_long_delinquency = models.TextField(blank=True, null=True)
    bol_delinquency_history_flg = models.BooleanField(blank=True, null=True)
    str_delinquency_history = models.TextField(blank=True, null=True)
    bol_non_calculation_flg = models.BooleanField(blank=True, null=True)
    str_non_calculation = models.TextField(blank=True, null=True)
    int_warning_reason_id_1 = models.IntegerField(blank=True, null=True)
    str_warning_reason_1 = models.TextField(blank=True, null=True)
    int_warning_reason_id_2 = models.IntegerField(blank=True, null=True)
    str_warning_reason_2 = models.TextField(blank=True, null=True)
    int_ownerweb_report_type_id = models.IntegerField(blank=True, null=True)
    str_ownerweb_email = models.CharField(max_length=100, blank=True, null=True)
    str_ownercode = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = u'"public\".\"t_name_list"'


class TDealer(models.Model):
    int_dealer_id = models.AutoField(primary_key=True)
    int_dealer_type_id = models.IntegerField()
    int_name = models.ForeignKey(TNameList, on_delete=models.SET_DEFAULT, default=0)
    int_account_id = models.IntegerField(blank=True, null=True)
    str_print_owner_name = models.CharField(max_length=100, blank=True, null=True)
    str_print_owner_zip_code_3 = models.CharField(max_length=3, blank=True, null=True)
    str_print_owner_zip_code_4 = models.CharField(max_length=4, blank=True, null=True)
    str_print_owner_addr_state = models.CharField(max_length=20, blank=True, null=True)
    str_print_owner_addr_city = models.CharField(max_length=50, blank=True, null=True)
    str_print_owner_addr_block = models.CharField(max_length=100, blank=True, null=True)
    str_print_owner_addr_no = models.CharField(max_length=100, blank=True, null=True)
    str_mail_owner_name = models.CharField(max_length=100, blank=True, null=True)
    str_mail_owner_zip_code_3 = models.CharField(max_length=3, blank=True, null=True)
    str_mail_owner_zip_code_4 = models.CharField(max_length=4, blank=True, null=True)
    str_mail_owner_addr_state = models.CharField(max_length=20, blank=True, null=True)
    str_mail_owner_addr_city = models.CharField(max_length=50, blank=True, null=True)
    str_mail_owner_addr_block = models.CharField(max_length=100, blank=True, null=True)
    str_mail_owner_addr_no = models.CharField(max_length=100, blank=True, null=True)
    str_owner_comment = models.TextField(blank=True, null=True)
    int_person_id = models.IntegerField(blank=True, null=True)
    int_family_relationship_id_1 = models.IntegerField(blank=True, null=True)
    str_family_name_1 = models.CharField(max_length=100, blank=True, null=True)
    str_family_furigana_1 = models.CharField(max_length=100, blank=True, null=True)
    int_family_sex_1 = models.IntegerField(blank=True, null=True)
    dat_family_birthday_1 = models.DateField(blank=True, null=True)
    str_family_memo_1 = models.TextField(blank=True, null=True)
    int_family_relationship_id_2 = models.IntegerField(blank=True, null=True)
    str_family_name_2 = models.CharField(max_length=100, blank=True, null=True)
    str_family_furigana_2 = models.CharField(max_length=100, blank=True, null=True)
    int_family_sex_2 = models.IntegerField(blank=True, null=True)
    dat_family_birthday_2 = models.DateField(blank=True, null=True)
    str_family_memo_2 = models.TextField(blank=True, null=True)
    int_family_relationship_id_3 = models.IntegerField(blank=True, null=True)
    str_family_name_3 = models.CharField(max_length=100, blank=True, null=True)
    str_family_furigana_3 = models.CharField(max_length=100, blank=True, null=True)
    int_family_sex_3 = models.IntegerField(blank=True, null=True)
    dat_family_birthday_3 = models.DateField(blank=True, null=True)
    str_family_memo_3 = models.TextField(blank=True, null=True)
    int_family_relationship_id_4 = models.IntegerField(blank=True, null=True)
    str_family_name_4 = models.CharField(max_length=100, blank=True, null=True)
    str_family_furigana_4 = models.CharField(max_length=100, blank=True, null=True)
    int_family_sex_4 = models.IntegerField(blank=True, null=True)
    dat_family_birthday_4 = models.DateField(blank=True, null=True)
    str_family_memo_4 = models.TextField(blank=True, null=True)
    str_print_owner_tel = models.CharField(max_length=50, blank=True, null=True)
    str_mail_owner_tel = models.CharField(max_length=50, blank=True, null=True)
    bol_chief_flg = models.BooleanField(blank=True, null=True)
    str_license_governor = models.CharField(max_length=50, blank=True, null=True)
    str_license_no = models.CharField(max_length=50, blank=True, null=True)
    int_area_id = models.IntegerField(blank=True, null=True)
    int_intro_fee_type = models.IntegerField(blank=True, null=True)
    int_intro_fee_tax_type = models.IntegerField(blank=True, null=True)
    flt_intro_fee = models.FloatField(blank=True, null=True)
    str_license_person = models.CharField(max_length=50, blank=True, null=True)
    int_print_owner_type_id = models.IntegerField(blank=True, null=True)
    int_mail_owner_type_id = models.IntegerField(blank=True, null=True)
    str_print_owner_memo = models.TextField(blank=True, null=True)
    str_mail_owner_memo = models.TextField(blank=True, null=True)
    str_trader_code = models.CharField(max_length=20, blank=True, null=True)
    int_print_part_id = models.IntegerField(blank=True, null=True)
    int_mail_part_id = models.IntegerField(blank=True, null=True)
    str_print_owner_name1 = models.CharField(max_length=100, blank=True, null=True)
    str_mail_owner_name1 = models.CharField(max_length=100, blank=True, null=True)
    str_mc_license_governor = models.CharField(max_length=50, blank=True, null=True)
    str_mc_license_no = models.CharField(max_length=50, blank=True, null=True)
    str_staff_code = models.CharField(max_length=50, blank=True, null=True)
    str_owner_code = models.CharField(max_length=50, blank=True, null=True)
    int_confirm_type_id = models.IntegerField()
    int_vat_calc_round_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = u'"public\".\"t_dealer"'


class TUser(models.Model):
    int_user_id = models.AutoField(primary_key=True)
    int_branch_id = models.IntegerField()
    int_section_id = models.IntegerField()
    str_login_name = models.CharField(max_length=100)
    str_public_key = models.TextField(blank=True, null=True)
    int_user_level = models.IntegerField()
    str_password = models.CharField(max_length=100)
    int_dealer = models.ForeignKey(TDealer, on_delete=models.SET_DEFAULT, default=0)
    str_license_person = models.CharField(max_length=50, blank=True, null=True)
    str_license_governor = models.CharField(max_length=100, blank=True, null=True)
    str_license_no = models.CharField(max_length=100, blank=True, null=True)
    str_license_person_post = models.CharField(max_length=50, blank=True, null=True)
    dat_regist_date_license = models.DateField(blank=True, null=True)
    bol_del_flg = models.BooleanField(blank=True, null=True)
    bol_sales_menu = models.BooleanField(blank=True, null=True)
    bol_input_flg = models.BooleanField()

    class Meta:
        managed = False
        db_table = u'"public\".\"t_user"'


class TlPrefecture(models.Model):
    int_prefecture_id = models.AutoField(primary_key=True)
    str_prefecture = models.CharField(max_length=10)
    str_prefecture_kana = models.CharField(max_length=255, blank=True, null=True)
    str_code = models.CharField(max_length=4)
    flt_longitude = models.FloatField(blank=True, null=True)
    flt_latitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tl_prefecture'


class TlMainStructure(models.Model):
    int_main_structure_id = models.AutoField(primary_key=True)
    str_main_structure = models.CharField(max_length=100)
    str_export_1 = models.CharField(max_length=100, blank=True, null=True)
    str_export_2 = models.CharField(max_length=100, blank=True, null=True)
    str_export_3 = models.CharField(max_length=100, blank=True, null=True)
    str_export_4 = models.CharField(max_length=100, blank=True, null=True)
    str_export_5 = models.CharField(max_length=100, blank=True, null=True)
    str_export_6 = models.CharField(max_length=100, blank=True, null=True)
    str_export_7 = models.CharField(max_length=100, blank=True, null=True)
    str_export_8 = models.CharField(max_length=100, blank=True, null=True)
    str_export_9 = models.CharField(max_length=100, blank=True, null=True)
    str_export_10 = models.CharField(max_length=100, blank=True, null=True)
    str_export_11 = models.CharField(max_length=100, blank=True, null=True)
    str_export_12 = models.CharField(max_length=100, blank=True, null=True)
    str_export_13 = models.CharField(max_length=100, blank=True, null=True)
    str_export_14 = models.CharField(max_length=100, blank=True, null=True)
    str_export_15 = models.CharField(max_length=100, blank=True, null=True)
    str_export_16 = models.CharField(max_length=100, blank=True, null=True)
    str_export_17 = models.CharField(max_length=100, blank=True, null=True)
    str_export_18 = models.CharField(max_length=100, blank=True, null=True)
    str_export_19 = models.CharField(max_length=100, blank=True, null=True)
    str_export_20 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = u'"public\".\"tl_main_structure"'


class TlYubin(models.Model):
    int_yubin_id = models.AutoField(primary_key=True)
    int_public_code = models.IntegerField()
    str_old_number = models.CharField(max_length=7, blank=True, null=True)
    str_yubin_num = models.CharField(max_length=10, blank=True, null=True)
    str_prefecture_kana = models.CharField(max_length=255, blank=True, null=True)
    str_city_kana = models.CharField(max_length=255, blank=True, null=True)
    str_town_kana = models.CharField(max_length=255, blank=True, null=True)
    str_prefecture = models.CharField(max_length=255, blank=True, null=True)
    str_city = models.CharField(max_length=255, blank=True, null=True)
    str_town = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tl_yubin'


class TRentalFeeDetail(models.Model):
    int_rental_fee_detail_id = models.AutoField(primary_key=True)
    int_unit_id = models.IntegerField()
    int_detail_group_id = models.IntegerField()
    int_detail_type_id = models.IntegerField()
    int_detail_item_id = models.IntegerField()
    bol_taxable_flg = models.BooleanField(blank=True, null=True)
    flt_month_minute = models.FloatField(blank=True, null=True)
    int_amount = models.IntegerField(blank=True, null=True)
    int_tax = models.IntegerField(blank=True, null=True)
    int_amount_with_tax = models.IntegerField(blank=True, null=True)
    int_fee_cycle = models.IntegerField(blank=True, null=True)
    int_period_from = models.IntegerField(blank=True, null=True)
    int_period_to = models.IntegerField(blank=True, null=True)
    int_payee_account_id = models.IntegerField(blank=True, null=True)
    bol_bring_flg = models.BooleanField(blank=True, null=True)
    bol_management_consignment_obj_flg = models.BooleanField(blank=True, null=True)
    int_management_consignment_calc_type = models.IntegerField(blank=True, null=True)
    int_period_start_month = models.IntegerField(blank=True, null=True)
    bol_reward_flg = models.BooleanField(blank=True, null=True)
    bol_include_administrative_flg = models.BooleanField(blank=True, null=True)
    bol_include_parking_flg = models.BooleanField(blank=True, null=True)
    int_vat_type = models.IntegerField()
    bol_actual_cost = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = u'"public\".\"t_rental_fee_detail"'


class UlUnitEquipment(models.Model):
    int_unit_equipment_id = models.AutoField(primary_key=True)
    str_unit_equipment = models.CharField(max_length=100)
    str_meaning = models.CharField(max_length=100, blank=True, null=True)
    bol_show = models.BooleanField(blank=True, null=True)
    bol_fixed = models.BooleanField(blank=True, null=True)
    str_export_1 = models.CharField(max_length=100, blank=True, null=True)
    str_export_2 = models.CharField(max_length=100, blank=True, null=True)
    str_export_3 = models.CharField(max_length=100, blank=True, null=True)
    str_export_4 = models.CharField(max_length=100, blank=True, null=True)
    str_export_5 = models.CharField(max_length=100, blank=True, null=True)
    str_export_6 = models.CharField(max_length=100, blank=True, null=True)
    str_export_7 = models.CharField(max_length=100, blank=True, null=True)
    str_export_8 = models.CharField(max_length=100, blank=True, null=True)
    str_export_9 = models.CharField(max_length=100, blank=True, null=True)
    str_export_10 = models.CharField(max_length=100, blank=True, null=True)
    str_export_11 = models.CharField(max_length=100, blank=True, null=True)
    str_export_12 = models.CharField(max_length=100, blank=True, null=True)
    str_export_13 = models.CharField(max_length=100, blank=True, null=True)
    str_export_14 = models.CharField(max_length=100, blank=True, null=True)
    str_export_15 = models.CharField(max_length=100, blank=True, null=True)
    str_export_16 = models.CharField(max_length=100, blank=True, null=True)
    str_export_17 = models.CharField(max_length=100, blank=True, null=True)
    str_export_18 = models.CharField(max_length=100, blank=True, null=True)
    str_export_19 = models.CharField(max_length=100, blank=True, null=True)
    str_export_20 = models.CharField(max_length=100, blank=True, null=True)
    int_order_id = models.IntegerField(blank=True, null=True)
    bol_default_flg = models.BooleanField(blank=True, null=True)
    bol_print = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = u'"public\".\"ul_unit_equipment"'


class UlUnitEquipmentSelect(models.Model):
    int_unit_equipment_select_id = models.AutoField(primary_key=True)
    int_unit_equipment_id = models.IntegerField()
    int_equipment_id = models.IntegerField()
    str_equipment = models.CharField(max_length=100, blank=True, null=True)
    str_meaning = models.CharField(max_length=100, blank=True, null=True)
    bol_show = models.BooleanField(blank=True, null=True)
    bol_fixed = models.BooleanField(blank=True, null=True)
    str_export_1 = models.CharField(max_length=100, blank=True, null=True)
    str_export_2 = models.CharField(max_length=100, blank=True, null=True)
    str_export_3 = models.CharField(max_length=100, blank=True, null=True)
    str_export_4 = models.CharField(max_length=100, blank=True, null=True)
    str_export_5 = models.CharField(max_length=100, blank=True, null=True)
    str_export_6 = models.CharField(max_length=100, blank=True, null=True)
    str_export_7 = models.CharField(max_length=100, blank=True, null=True)
    str_export_8 = models.CharField(max_length=100, blank=True, null=True)
    str_export_9 = models.CharField(max_length=100, blank=True, null=True)
    str_export_10 = models.CharField(max_length=100, blank=True, null=True)
    str_export_11 = models.CharField(max_length=100, blank=True, null=True)
    str_export_12 = models.CharField(max_length=100, blank=True, null=True)
    str_export_13 = models.CharField(max_length=100, blank=True, null=True)
    str_export_14 = models.CharField(max_length=100, blank=True, null=True)
    str_export_15 = models.CharField(max_length=100, blank=True, null=True)
    str_export_16 = models.CharField(max_length=100, blank=True, null=True)
    str_export_17 = models.CharField(max_length=100, blank=True, null=True)
    str_export_18 = models.CharField(max_length=100, blank=True, null=True)
    str_export_19 = models.CharField(max_length=100, blank=True, null=True)
    str_export_20 = models.CharField(max_length=100, blank=True, null=True)
    int_order_id = models.IntegerField(blank=True, null=True)
    bol_default_flg = models.BooleanField(blank=True, null=True)
    bol_default_simple_flg = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = u'"public\".\"ul_unit_equipment_select"'
        unique_together = (('int_unit_equipment_id', 'int_equipment_id'),)


# tracking_schema
# ユーザ権限マスタ
class UlAuthority(models.Model):
    int_auth = models.IntegerField(default=0)
    str_auth = models.CharField(max_length=30)


# ユーザ権限
class Authority(models.Model):
    int_user = models.ForeignKey(TUser, on_delete=models.SET_DEFAULT, default='')
    int_auth = models.ForeignKey(UlAuthority, on_delete=models.SET_DEFAULT, default='')


# 反響元
class Responds(models.Model):
    str_respond = models.CharField(max_length=20)


# 媒体
class Media(models.Model):
    str_media = models.CharField(max_length=20)


# 契約形態
class ContractType(models.Model):
    str_contract_type = models.CharField(max_length=20)


# transaction
# 見込み客情報
class PotentialCustomers(models.Model):
    str_name = models.CharField(max_length=100)
    str_email = models.CharField(max_length=100, null=True)
    int_media = models.ForeignKey(Media, on_delete=models.SET_DEFAULT, default=99)
    int_respond = models.IntegerField(default=0)
    int_contract_type = models.IntegerField(default=0)
    str_reception_mail = models.CharField(max_length=100)
    str_tel = models.CharField(max_length=20, null=True)
    str_fax = models.CharField(max_length=20, null=True)
    str_mobile = models.CharField(max_length=20, null=True)
    str_zip_code_3 = models.CharField(max_length=3, null=True)
    str_zip_code_4 = models.CharField(max_length=4, null=True)
    str_addr_pref = models.CharField(max_length=20, null=True)
    str_addr_city = models.CharField(max_length=100, null=True)
    str_addr_block = models.CharField(max_length=100, null=True)
    int_prefecture = models.IntegerField(default=0, null=True)
    int_city = models.IntegerField(default=0, null=True)
    int_dealer = models.IntegerField(default=0, null=True)
    str_memo = models.TextField(null=True)
    tim_reception = models.DateTimeField('time reception', null=True)
    tim_send_mail = models.DateTimeField('time auto mail send', null=True)
    str_information_premise = models.CharField(max_length=100, null=True)
    int_information_premise = models.ForeignKey(TPremise, on_delete=models.SET_NULL, null=True)
    str_information_unit = models.CharField(max_length=100, null=True)
    int_information_unit = models.IntegerField(default=0)
    int_amount = models.IntegerField(default=0, null=True)
    int_train = models.IntegerField(default=0, null=True)
    int_station = models.IntegerField(default=0, null=True)
    bol_assigned = models.BooleanField(default=False)
    dat_created_at = models.DateTimeField('date created')
    dat_updated_at = models.DateTimeField('date updated')


class TempCustomers(models.Model):
    str_user_name = models.CharField(max_length=100)
    str_user_kana = models.CharField(max_length=100, null=True)
    str_user_mail = models.CharField(max_length=100, null=True, unique=True)
    str_user_tel = models.CharField(max_length=100, null=True)
    str_user_fax = models.CharField(max_length=100, null=True)
    str_user_contact = models.TextField(null=True)
    str_user_inquiry_detail = models.TextField(null=True)
    int_user_media = models.IntegerField(null=False)
    int_unit = models.ForeignKey(TUnit, on_delete=models.SET_DEFAULT, default='')

    dat_created_at = models.DateTimeField('date created')
    dat_updated_at = models.DateTimeField('date updated')


class TrackingUnitEquipment(models.Model):
    int_tracking_potential_customers_id = models.IntegerField()
    int_equipment_id = models.IntegerField()
    int_equipment_select = models.IntegerField()
    str_premise_name = models.CharField(max_length=100, blank=True, null=True)
    str_premise_address = models.CharField(max_length=100, blank=True, null=True)


class CustomerRequirement(models.Model):
    int_tracking_potential_customers_id = models.IntegerField(null=False, unique=True, blank=True)
    int_min_rental_fee = models.IntegerField(null=True, blank=True)  # 賃料下限
    int_max_rental_fee = models.IntegerField(null=True, blank=True)  # 賃料上限
    bol_construction_iron = models.BooleanField(default=False, null=True, blank=True)  # 構造 鉄筋系
    bol_construction_steel = models.BooleanField(default=False, null=True, blank=True)  # 構造 鉄骨系
    bol_construction_wooden = models.BooleanField(default=False, null=True, blank=True)  # 構造 木造
    bol_construction_other = models.BooleanField(default=False, null=True, blank=True)  # 構造 その他
    bol_layout_one_room = models.BooleanField(default=False, null=True, blank=True)  # 間取 ワンルーム
    bol_layout_1k = models.BooleanField(default=False, null=True, blank=True)  # 間取 1k
    bol_layout_1dk = models.BooleanField(default=False, null=True, blank=True)  # 間取 1dk
    bol_layout_1ldk = models.BooleanField(default=False, null=True, blank=True)  # 間取 1ldk
    bol_layout_2k = models.BooleanField(default=False, null=True, blank=True)  # 間取 2k
    bol_layout_2dk = models.BooleanField(default=False, null=True, blank=True)  # 間取 2dk
    bol_layout_2ldk = models.BooleanField(default=False, null=True, blank=True)  # 間取 2ldk
    bol_layout_3k = models.BooleanField(default=False, null=True, blank=True)  # 間取 3k
    bol_layout_3dk = models.BooleanField(default=False, null=True, blank=True)  # 間取 3dk
    bol_layout_3ldk = models.BooleanField(default=False, null=True, blank=True)  # 間取 3ldk
    bol_layout_4k = models.BooleanField(default=False, null=True, blank=True)  # 間取 4k
    bol_layout_4dk = models.BooleanField(default=False, null=True, blank=True)  # 間取 4dk
    bol_layout_4ldk = models.BooleanField(default=False, null=True, blank=True)  # 間取 4ldk以上
    int_line1 = models.IntegerField(null=True, blank=True)  # 路線ID1
    int_station1 = models.IntegerField(null=True, blank=True)  # 駅ID1
    int_line2 = models.IntegerField(null=True, blank=True)  # 路線ID2
    int_station2 = models.IntegerField(null=True, blank=True)  # 駅ID2
    int_line3 = models.IntegerField(null=True, blank=True)  # 路線ID3
    int_station3 = models.IntegerField(null=True, blank=True)  # 駅ID3
    bol_area1 = models.BooleanField(default=False, null=True, blank=True)  # エリア1
    bol_area2 = models.BooleanField(default=False, null=True, blank=True)  # エリア2
    bol_area3 = models.BooleanField(default=False, null=True, blank=True)  # エリア3
    bol_area4 = models.BooleanField(default=False, null=True, blank=True)  # エリア4
    int_school_area1 = models.IntegerField(null=True, blank=True)  # 学区1
    int_school_area2 = models.IntegerField(null=True, blank=True)  # 学区2
    int_school_area3 = models.IntegerField(null=True, blank=True)  # 学区3
    int_school_area4 = models.IntegerField(null=True, blank=True)  # 学区4
    bol_other_conditions_pet = models.BooleanField(default=False, null=True, blank=True)
    bol_other_conditions_city_gas = models.BooleanField(default=False, null=True, blank=True)
    bol_other_conditions_second_floor = models.BooleanField(default=False, null=True, blank=True)
    bol_other_conditions_bath_toilet = models.BooleanField(default=False, null=True, blank=True)


# 構造カテゴリ
class UlMainStructureCategory(models.Model):

    str_main_structure = models.CharField(max_length=100)
    int_category = models.IntegerField(null=True, blank=True)


# 間取カテゴリ
class UlLayoutCategory(models.Model):
    str_layout = models.CharField(max_length=100)
    int_category = models.IntegerField(null=True, blank=True)


# 沿線
class TlLine(models.Model):
    int_line_id = models.IntegerField(blank=True)
    str_line = models.CharField(max_length=100)


# 駅
class TlStation(models.Model):
    int_line_id = models.IntegerField(blank=True)
    int_station_id = models.IntegerField(blank=True)
    str_station = models.CharField(max_length=100)


# エリア
class TlArea(models.Model):
    int_area_id = models.IntegerField(blank=True)
    str_area = models.CharField(max_length=100)


# 学区
class TlSchoolArea(models.Model):
    int_school_area_id = models.IntegerField(blank=True)
    str_school_area = models.CharField(max_length=100)


# その他
class TlOtherCondition(models.Model):
    int_other_condition_id = models.IntegerField(blank=True)
    str_other_condition = models.CharField(max_length=100)