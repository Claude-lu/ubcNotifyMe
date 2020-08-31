import smtplib


class Notiifcations:

    def __init__(self):
        pass

    '''
    For the future
    1. Set up business email
    2. Set up two step authentication
    3. Add App Password
    '''

    def send_mail(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.echo()
        server.login('claudejlu@gmail.com', 'ysyxxddiobwkqyfe')

        subject = 'A Spot Opened Up in COMM 290'
        body = "Click the link: https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=COMM&course=290"

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail('claudejlu@gmail.com', 'jialonglu2017@gmail.com', msg)
        server.quit()

    def send_text(self):
        pass
