from have_a_nice_day import app
from freezegun import freeze_time
import unittest
import datetime


class TestGoodDay(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    @freeze_time("2022-03-15")  # Tuesday
    def test_can_get_correct_day_of_week(self):
        assert self.check_weekday_correctness('вторника') == True

    @freeze_time("2022-03-16")  # Wednesday
    def test_can_get_correct_day_of_week(self):
        assert self.check_weekday_correctness('среды') == True

    # and so on for all the days of the week

    def check_weekday_correctness(self, day_str):
        days_strs = [
            'понедельника',
            'вторника',
            'среды',
            'четверга',
            'пятницы',
            'субботы',
            'воскресенья'
        ]
        return day_str == days_strs[datetime.datetime.weekday(datetime.datetime.now())]

    def get_weekday_from_response(self):
        response = self.app.get('/hello-world/John')
        response_text = response.data.decode()
        response_text_splitted = ''.join(x for x in response_text if x.isalpha() or x == ' ').split()
        return response_text_splitted[-1]
