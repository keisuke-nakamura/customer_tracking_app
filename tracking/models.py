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
        db_table = 't_unit'


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


# master
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
    dat_created_at = models.DateTimeField('date created')
    dat_updated_at = models.DateTimeField('date updated')
