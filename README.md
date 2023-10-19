# Wichteln aka Secret Santa
The following scripts allow you to generate, retrieve and send secret santa requets without the creator even knowing.
## Configuration
Adapt the `settings.json` and set a budget, the list of participants and opionally your mail settings. For mailing STARTTLS is used keep that in mind when adding your settings. Also if you are using GMail check out: [https://support.google.com/accounts/answer/185833?visit_id=638333018254746748-3806559961&p=InvalidSecondFactor&rd=1] to create an app password for your account.
## Workflow
1. Run the `pair.py` which will generate match pairs.
2. Run the `get.py` which will allow the participants to retreive their partners on the fly or ...
3. Run the `mail.py` which will send a mail to the participants with their match.

Marry X-mas!