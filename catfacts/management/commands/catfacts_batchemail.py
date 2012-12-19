from django.core.management.base import NoArgsCommand
from django.core.mail import send_mail, EmailMultiAlternatives
from random import choice
from catfacts.models import Email_User, Fact
import catfactssite.settings

class Command(NoArgsCommand):

    help = "Randomly selects a Fact from catfacts.models.Fact." \
           " Sends a batch email containing this fact to every validated email in Email_User."

    option_list = NoArgsCommand.option_list

    # Choose random fact, create list of valid emails, send batch email to all
    def handle_noargs(self, **options):
        # Generate random CatFact
        facts = Fact.objects.all()
        todays_fact = choice(facts)
        self.stdout.write("Today's Fact: %s\n" % todays_fact)

        # Create a list of all valid email addresses
        user_list = Email_User.objects.filter(valid=True)
        self.stdout.write("All valid email users: %s\n" % str(user_list))

        # Send an email to each user
        for user in user_list:
            text_message = """Hey %s,
Here's your personal CatFact for the day:

    %s

Sent with love from CatFacts Galore!

Kevin""" % (user.name, todays_fact)

            html_message = '''<html>
	<body>
		<p>
			<span style="font-size:18px;"><span style="font-family: trebuchet ms,helvetica,sans-serif;">Hey %s, <br> Welcome to CatFacts!</span></span></p>
		<blockquote>
			<p>
				<span style="font-size:16px;">%s</span></p>
		</blockquote>
		<p>
			<span style="font-size:14px;">Sent with love!</span></p>
		<p>
			<em><span style="font-size:8px;"><span style="font-size:10px;">If you wish to unsubscribe for some reason, please <a href="%s/unsubscribe?email=%s">click this link</a>. I'll miss you though. :(</em></span></span></p>
	</body>
</html>''' % (user.name, todays_fact, catfactssite.settings.HOSTNAME, user.email)

            msg = EmailMultiAlternatives("Here's today's CatFact!",
                      text_message,
                      "CatFacts Galore <catfacts@thekevincrane.com>",
                      [user.email]
                      )
            msg.attach_alternative(html_message, "text/html")
            msg.send()
            self.stdout.write("Sent email to %s\n" % user.email)
