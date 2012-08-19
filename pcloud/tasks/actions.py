from celery import task


@task
def get_photos(receipt, instagram=None, facebook=None):
    print(instagram)
    print(facebook)
    # twitter.s(show_schedule.show).apply_async()
    # facebook.s(show_schedule.show).apply_async()
    # get_glue.s(show_schedule.show).apply_async()

    # now = make_naive(datetime.utcnow().replace(tzinfo=utc), pytz.utc)
    # stop_time = make_naive(show_schedule.start_date + timedelta(minutes=show_schedule.run_for),pytz.utc)
    # if now < stop_time:
    #     again = now + timedelta(seconds=60)
    #     start_show_polling.apply_async([show_schedule],eta=again)