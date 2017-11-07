
def query_common_date(query_date,create_at_start):

    if int(query_date) == 2:
        if not create_at_start:
            form_create_at_start = datetime.now().strftime('%Y-%m')
            _year, _month = form_create_at_start.split('-')
        else:
            form_create_at_start = create_at_start
            _year, _month = create_at_start.split('-')[:2]
        query_create_at_start = datetime(int(_year), int(
            _month), 2, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')
        query_create_at_end = datetime(int(_year), int(
            _month) + 1, 1, 23, 59, 59).strftime('%Y-%m-%d %H:%M:%S')

    if int(query_date) == 1:

        if not create_at_start:
            query_date_def = form_create_at_start = (common.timestamp_now().replace(
                hour=0, minute=0, second=0) - timedelta(days=1)).date()
        else:
            query_date_def = common.parse_ymd(create_at_start)

        query_create_at_start = query_date_def + timedelta(days=1)
        query_create_at_end = query_date_def + timedelta(days=2)

    return [form_create_at_start,query_create_at_start,query_create_at_end]

def downloads_query_date(query_date,create_at_start,create_at_end):
    if int(query_date) == 1:
        # 模块下
        create_at_end_search = common.parse_ymd(
            create_at_end) + timedelta(1)
        create_at_start_search = common.parse_ymd(create_at_start) + \
            timedelta(1)
    else:
        # 模块下
        end_year, end_month = create_at_end.split('-')[:2]
        create_at_end_search = datetime(int(end_year), int(
            end_month) + 1, 1, 23, 59, 59).strftime('%Y-%m-%d %H:%M:%S')
        s_year, s_month = create_at_start.split('-')[:2]
        create_at_start_search = datetime(int(s_year), int(
            s_month), 2, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')
    return [create_at_start_search,create_at_end_search]