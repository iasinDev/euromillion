import collections
import heapq
import itertools
import psycopg2
import smtplib

from operator import itemgetter


class Euromillion(object):
    # Available numbers from 1-50
    available_number = range(1, 51)
    # Avalable lucky stars 1-11
    lucky_stars = range(1, 12)

    def __init__(self):
        # Initialize connection to db
        self.conn_string = """
        host='localhost'
        dbname='euromillion'
        user='zatan'
        password='sidabras007'
        """
        self.conn = psycopg2.connect(self.conn_string)
        self.cursor = self.conn.cursor()

    def send_email(self, least_common_numbers, least_common_lucky_numbers):
        gmail_user = "ikonitas@gmail.com"
        gmail_pwd = "sidabras0915"
        FROM = 'euroMillion@gmail.com'
        TO = ['ikonitas@gmail.com', "doviletaraskute@gmail.com"]
        TEXT = """Numbers: {0} \n Lucky: {1}""".format(
            least_common_numbers,
            least_common_lucky_numbers
        )
        SUBJECT = "Lucky numbers"
        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

        try:
            #server = smtplib.SMTP(SERVER)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            #server.quit()
            server.close()
            print 'successfully sent the mail'
        except:
            print "failed to send mail"

    def get_least_common_values(self, array, to_find=None):
        counter = collections.Counter(array)
        if to_find is None:
            return sorted(counter.items(), key=itemgetter(1), reverse=False)
        return heapq.nsmallest(to_find, counter.items(), key=itemgetter(1))

    def insert_data(self, date, five_numbers, lucky_numbers):
        """ Insert data to db """
        try:
            self.cursor.execute(
                """INSERT INTO results VALUES (
                '{0}', ARRAY[{1}], ARRAY[{2}]
            )""".format(date, five_numbers, lucky_numbers)
            )
        except psycopg2.IntegrityError:
            pass

    def get_lucky_numbers(self):
        """ Get data from db """

        numbers = list()
        lucky_numbers = list()

        self.cursor.execute(
            """SELECT * FROM results"""
        )
        for row in self.cursor:
            numbers.append(row[1])
            lucky_numbers.append(row[2])

        merged_numbers = list(itertools.chain(*numbers))
        merged_lucky_numbers = list(itertools.chain(*lucky_numbers))

        least_common_numbers = self.get_least_common_values(merged_numbers, 10)
        least_common_lucky_numbers = self.get_least_common_values(
            merged_lucky_numbers, 5
        )
        self.send_email(least_common_numbers, least_common_lucky_numbers)

    def choices(self):
        numbers, lucky = self.get_data()

    def close_connection(self):
        """ Close connection """
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    euro = Euromillion()
    #euro.choices()
    euro.insert_data()
    euro.close_connection()



