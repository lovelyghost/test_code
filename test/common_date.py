
def common_date_deal(query_date,create_at_start,create_at_end):

    if int(query_date) == 1:
        # 模块下
        if create_at_end:
            create_at_end_search = parse_ymd(
                create_at_end) + timedelta(1)
        else:
            create_at_end = (
                datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
            create_at_end_search = (
                datetime.now() + timedelta(1)).strftime("%Y-%m-%d")

        create_at_end = str(parse_ymd(
            create_at_end).strftime("%Y-%m-%d"))

        if create_at_start:
            create_at_start_search = parse_ymd(create_at_start) + \
                                          timedelta(1)
        else:
            create_at_start = (datetime.strptime(create_at_end, "%Y-%m-%d") - timedelta(days=6)).strftime(
                "%Y-%m-%d")
            create_at_start_search = (
                datetime.strptime(create_at_end, "%Y-%m-%d") - timedelta(days=5)).strftime(
                "%Y-%m-%d")

    if int(query_date) == 2:
        # 模块下
        if create_at_end:
            _year, _month =create_at_end.split('-')[:2]
        else:
            create_at_end = datetime.now().strftime('%Y-%m')
            _year, _month = create_at_end.split('-')
        create_at_end_search = datetime(int(_year), int(
            _month) + 1, 1, 23, 59, 59).strftime('%Y-%m-%d %H:%M:%S')

        create_at_end = str(create_at_end)

        if create_at_start:
            _year, _month = create_at_start.split('-')[:2]
        else:
            now_date = datetime.now().strftime("%Y-%m-%d")
            create_at_start = (datetime.strptime(
                str(now_date), "%Y-%m-%d") - timedelta(days=150)).strftime('%Y-%m')
            _year, _month = create_at_start.split('-')
        create_at_start_search = datetime(int(_year), int(
            _month), 2, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')
    return [create_at_start,create_at_end,create_at_start_search,create_at_end_search]