#  受信箱に送信されてきたメールを取得
#  物件に関する問い合わせメールの場合見込客として登録する
import datetime

from django.http import Http404

from tracking.models import TempCustomers, TUnit, TPremise, PotentialCustomers
import logging
import poplib
import re
import email
import pytz
from email.header import decode_header, make_header

logging.basicConfig(level=logging.DEBUG)

# settings(別ファイル保管するか未定)
host = 'serita.wp-x.jp'
port = '110'
user = 'yoshizawa@serita-f.jp'
password = 'serita0004'
suumo_subject = '[リクルートＪＤＳ]反響お知らせメール'
suumo_tour_subject = '[リクルートＪＤＳ]反響（見学予約）お知らせメール'
homes_subject = '【LIFULL HOME\'S】お客様からの問合せ'
mypage_subject = '芹田不動産HPからのお問い合わせ'


def run():
    # similar_unit(3000)
    try:
        connection = connect()
        mails = receive_mail(connection)
        datas = classification_mail(mails)
    #     import_mail(datas)
    #     connection.quit()
    except poplib.error_proto as POP3_Exception:
        print('POP3_EXCEPTION : ')
        print(POP3_Exception)
    except Exception as e:
        print('ERROR : ')
        print(e)


# メールサーバ接続
def connect():
    cli = poplib.POP3(host)
    cli.user(user)
    cli.pass_(password)

    return cli


# メール取得
def receive_mail(con):
    num_mails = len(con.list()[1])
    mail_list = dict()
    print(num_mails)
    for i in range(num_mails):
        msg_bytes = b""
        for line in con.retr(i + 1)[1]:
            msg_bytes += line + b"\n"

        mail_list[i] = email.message_from_bytes(msg_bytes)

    return mail_list


# メール仕訳
def classification_mail(mails):
    mail_lists = []
    for i in mails:
        subject = str(make_header(decode_header(mails[i]['Subject'])))
        # ポータル・件名ごとに分類　ループで処理しようかと思ったが、今後多様化するかもしれないのでべた書きにする
        if suumo_subject in subject:  # SUUMO 物件問い合わせ
            mail_lists.insert(i, parse_suumo_mail(mails[i]))
        elif suumo_tour_subject in subject:  # SUUMO 内見依頼
            mail_lists.insert(i, parse_suumo_mail(mails[i]))
        elif homes_subject in subject:  # HOME'S 物件問い合わせ
            mail_lists.insert(i, parse_homes_mail(mails[i]))
        elif mypage_subject in subject:  # 自社ホームページ 物件問い合わせ
            mail_lists.insert(i, parse_my_page_mail(mails[i]))
        else:
            print('not much')

    return mail_lists


# パース処理
def parse_suumo_mail(mail):
    mail_data = dict()
    payload = mail.get_payload(decode=True)
    charset = mail.get_content_charset()
    if charset is not None:
        payload = payload.decode(charset, "ignore")

    mail_data['subject'] = str(make_header(decode_header(mail['Subject'])))  # 件名
    mail_data['from'] = str(make_header(decode_header(mail['From'])))  # 送信者
    mail_data['int_user_media'] = 1  # 1:SUUMO

    mail_data['inquiry_date'] = payload.split('お問合せ日時：')[-1].split('\n')[0]  # 問い合わせ日時
    mail_data['unit_id'] = payload.split('貴社物件コード：')[-1].split('\n')[0]  # 部屋ID
    # mail_data['unit_type'] = payload.split('物件種別：')[-1].split('\n')[0]  #
    # mail_data['premise_name'] = payload.split('物件名：')[-1].split('\n')[0]  #
    # mail_data['premise_station'] = payload.split('最寄り駅：')[-1].split('\n')[0]  #
    # mail_data['premise_bus'] = payload.split('バス／歩：')[-1].split('\n')[0]  #
    # mail_data['premise_address'] = payload.split('所在地：')[-1].split('\n')[0]  #
    # mail_data['unit_rent'] = payload.split('賃料：')[-1].split('\n')[0]  #
    # mail_data['unit_arrangement'] = payload.split('間取り：')[-1].split('\n')[0]  #
    # mail_data['unit_area'] = payload.split('専有面積：')[-1].split('\n')[0]  #

    mail_data['user_name'] = payload.split('名前（漢字）：')[-1].split('\n')[0]  # ユーザ名
    mail_data['user_mail'] = payload.split('メールアドレス：')[-1].split('\n')[0]  # メールアドレス
    mail_data['user_tel'] = payload.split('ＴＥＬ：')[-1].split('\n')[0]  # 電話番号
    mail_data['user_fax'] = payload.split('FAX：')[-1].split('\n')[0]  # FAX
    mail_data['user_contact'] = payload.split('連絡方法：')[-1].split('\n')[0]  # 連絡方法
    mail_data['user_inquiry_detail'] = payload.split('お問合せ内容：')[-1].split('\n')[0]  # 問い合わせ内容

    return mail_data


def parse_homes_mail(mail):
    mail_data = dict()
    payload = mail.get_payload(decode=True)
    charset = mail.get_content_charset()
    if charset is not None:
        payload = payload.decode(charset, "ignore")

    mail_data['subject'] = str(make_header(decode_header(mail['Subject'])))  # 件名
    mail_data['from'] = str(make_header(decode_header(mail['From'])))  # 送信者
    mail_data['int_user_media'] = 2  # 2:HOME'S

    mail_data['inquiry_date'] = payload.split('ご確認の上、ご連絡をお願いいたします。')[-1].split('━━')[0].strip()  # 問い合わせ日時
    mail_data['unit_id'] = payload.split('自社管理番号：')[-1].split('\n')[0]  # 部屋ID
    mail_data['unit_type'] = payload.split('物件種別：')[-1].split('\n')[0]  #
    mail_data['premise_access'] = payload.split('交通：')[-1].split('\n')[0]  #
    mail_data['premise_address'] = payload.split('所在地：')[-1].split('\n')[0]  # 所在地
    mail_data['unit_rent'] = payload.split('賃料：')[-1].split('\n')[0]  # 賃料
    mail_data['unit_arrangement'] = payload.split('間取り：')[-1].split('\n')[0]  #
    mail_data['unit_area'] = payload.split('面積：')[-1].split('\n')[0]  #

    mail_data['user_name'] = payload.split('名前：')[-1].split('\n')[0]  # ユーザ名
    mail_data['user_mail'] = payload.split('メールアドレス：')[-1].split('\n')[0]  # メールアドレス
    mail_data['user_kana'] = ""  # payload.split('[ふりがな]')[-1].split('[')[0].strip()  #
    mail_data['user_address'] = ""  # payload.split('[住所]')[-1].split('[')[0].strip()  #
    mail_data['user_tel'] = payload.split('電話番号：')[-1].split('\n')[0]  #
    mail_data['user_fax'] = ''
    mail_data['user_contact'] = ''
    mail_data['user_inquiry_detail'] = payload.split('お問合せ内容：')[-1].split('\n')[0]  # 問い合わせ内容

    return mail_data


def parse_my_page_mail(mail):
    mail_data = dict()
    payload = mail.get_payload(decode=True)
    charset = mail.get_content_charset()

    if charset is not None:
        payload = payload.decode(charset, "ignore")

    mail_data['subject'] = str(make_header(decode_header(mail['Subject'])))  # 件名
    mail_data['from'] = str(make_header(decode_header(mail['From'])))  # 送信者
    mail_data['int_user_media'] = 3  # 3:自社HP

    unit_id = ''
    if '物件番号' in payload:
        unit_id = payload.split('物件番号：')[-1].split('）')[0].strip()  # 部屋ID

    if len(unit_id) > 0:
        mail_data['unit_id'] = unit_id
        mail_data['inquiry_type'] = payload.split('[お問い合わせ種別]')[-1].split('[')[0].strip()  # 問い合わせ種別
        mail_data['inquiry_unit'] = payload.split('[お問い合わせ物件]')[-1].split('(')[0].strip()  # 問い合わせ物件
        mail_data['preferred_day'] = payload.split('[希望面談日時]')[-1].split('[')[0].strip()  #

    else:
        mail_data['unit_id'] = None
        # mail_data['inquiry_type'] = payload.split('[お問い合わせ目的]')[-1].split('[')[0].strip()  # 問い合わせ種別

    mail_data['inquiry_date'] = datetime.datetime.today().strftime('%Y%m%d')
    mail_data['user_name'] = payload.split('[お名前]')[-1].split('[')[0].strip()  #
    mail_data['user_kana'] = payload.split('[ふりがな]')[-1].split('[')[0].strip()  #
    mail_data['user_address'] = payload.split('[住所]')[-1].split('[')[0].strip()  #
    mail_data['user_tel'] = payload.split('[電話番号]')[-1].split('[')[0].strip()  #
    mail_data['user_mail'] = payload.split('[メールアドレス]')[-1].split('[')[0].strip()  #
    mail_data['user_fax'] = ''
    mail_data['user_contact'] = ''
    mail_data['user_inquiry_detail'] = payload.split('[お問い合わせ内容]')[-1].split('□ユーザー情報')[0].strip().replace(
        '-------------------------------------------------------', '')  #

    return mail_data


# メール登録
def import_mail(mail_datas):
    for datas in mail_datas:
        if datas['unit_id'] is None:  # unitの指定が無いケース(未定)
            print('unit_id is None')
        else:  # unitの指定有　テーブルに登録
            try:
                tmp = TempCustomers(
                    str_user_name=datas['user_name'],
                    str_user_kana=datas['user_kana'],
                    str_user_mail=datas['user_mail'],
                    str_user_tel=datas['user_tel'],
                    str_user_fax=datas['user_fax'],
                    str_user_contact=datas['user_contact'],
                    str_user_inquiry_detail=datas['user_inquiry_detail'],
                    int_user_media=datas['int_user_media'],
                    int_unit=TUnit.objects.get(int_unit_id=datas['unit_id']),
                    dat_created_at=datetime.datetime.now(pytz.timezone('Asia/Tokyo')),
                    dat_updated_at=datetime.datetime.now(pytz.timezone('Asia/Tokyo')),
                )
                tmp.save()
                welcome_mail(datas['unit_id'])

            except Exception as e:
                print(e)


# 初回登録時メール送信　おすすめ物件をそえてプロモーションメールを送る
def welcome_mail(unit_id):
    print('welcome')
    similar_unit(unit_id)


# 物件IDから類似物件を検索
def similar_unit(unit_id):
    # 問い合わせ物件の物件名、部屋名、賃料、最寄り駅、路線
    try:
        inquiry = dict()
        for data_set in TUnit.objects.using('tsweb').raw(
                'SELECT u.int_unit_id, p.str_name, u.str_unit_name, rfd.int_amount_with_tax, p.int_station_id_1, p.int_train_id_1 '
                'FROM t_unit u '
                'LEFT JOIN t_premise p ON u.int_premise_id = p.int_premise_id '
                'LEFT JOIN t_rental_fee_detail rfd ON rfd.int_unit_id = u.int_unit_id '
                'AND rfd.int_detail_type_id = 11001 '
                'WHERE u.int_unit_id = ' + str(unit_id)):
            inquiry['PREMISE_NAME'] = data_set.str_name
            inquiry['UNIT_NAME'] = data_set.str_unit_name
            inquiry['UNIT_IDs'] = data_set.int_unit_id
            inquiry['AMOUNT'] = data_set.int_amount_with_tax
            inquiry['STATION'] = data_set.int_station_id_1
            inquiry['TRAIN'] = data_set.int_train_id_1

            # print(inquiry['AMOUNT'])  # 賃料未設定時の処理（検討中）

            sql = 'SELECT p.str_name AS premise_name '\
            ', u.str_unit_name AS unit_name '\
            ', u.int_unit_id AS unit_id '\
            ', rfd.int_amount_with_tax AS monthly_rental_fee '\
            ', ls.str_station AS station_name '\
            ', l.str_line AS line_name '\
            'FROM t_unit u '\
            'LEFT JOIN t_premise p ON p.int_premise_id = u.int_premise_id '\
            'LEFT JOIN t_unit_other uo ON uo.int_unit_id = u.int_unit_id '\
            'LEFT JOIN t_rental_fee_detail rfd ON rfd.int_unit_id = u.int_unit_id AND rfd.int_detail_type_id = 11001 '\
            'LEFT JOIN tl_line_station ls '\
            'ON ls.int_station_id = p.int_station_id_1 AND ls.int_line_id = p.int_train_id_1 '\
            'LEFT JOIN tl_line l '\
            'ON l.int_line_id = p.int_train_id_1 '\
            'WHERE p.bol_del_flg = false AND u.bol_del_flg = false AND u.int_usage_id != 10 '\
            'AND u.boL_rent_stop_flg = false AND u.int_contract_sts IN (1, 4, 7) '\
            'AND u.int_usage_id IN (1, 2) AND rfd.int_amount_with_tax > 0 '\
            'AND rfd.int_amount_with_tax BETWEEN ' + str(int(inquiry['AMOUNT']) - 5000) + ' AND ' + str(int(inquiry['AMOUNT']) + 5000)
            if inquiry['TRAIN']:
                sql += ' AND p.int_train_id_1 = ' + str(inquiry['TRAIN'])
            if inquiry['STATION']:
                sql += ' AND p.int_station_id_1 <= ' + str(inquiry['STATION'] + 10) + \
                       ' AND p.int_station_id_1 >= ' + str(inquiry['STATION'] - 10)

            print(sql)
            # for similar_data in TUnit.objects.using('tsweb').raw(sql):
            #     print(similar_data)

    # if (! empty($Inquiry['STATION'])) {
    #     $similar_sql .= " AND p.int_station_id_1 >= " . ((int) $Inquiry['STATION'] - 10)
    # }
    # if (! empty($Inquiry['STATION'])) {
    #     $similar_sql .= " AND p.int_station_id_1 <= " . ((int) $Inquiry['STATION'] + 10)
    # }
    # if (! empty($Inquiry['UNIT_IDs'])) {
    #     $similar_sql .= " AND u.int_unit_id != " . $Inquiry['UNIT_IDs']
    # }
    # $similar_sql .= " ORDER BY random() "
    # $similar_sql .= " LIMIT 4"

    except TUnit.DoesNotExist:
        print('UNIT NOT EXISTS')
        raise Http404('unit does not exists')


# 切断
def disconnect():
    print('disconnect')
