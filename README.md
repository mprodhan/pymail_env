Sending Email via Python

The reason why anyone would use a backend language such as Python, Java or C++ to send email, is for the use of the html file to customize an email. This makes the email look very professional. There are two valuable things about the use of this type of app, that can be quite similar to MailChimps email process.

Reason 1:

The first reason is that, this type of applicatiton can be used to customize the email according to a company's use of their logo and specifications. Thus, emails that one sees, as an active way to communicate events, or news from a news letter, often are able to use them for commercial purpose to reach out to their audiences or supporters.

Reason 2:

This is an easy way to send email in bulk and privately by the use of blind copying. In addition to this, a massive list of receivers can be maintained via a list, that can be extracted by a file or via a list, or even the use of a dictionary.

The need for securing private key information:

This is important for any dvelopers, as they will need a .env file, that is non-commital. The reason being, that what is required to keep a login and password secured, is to ensure that a .env is used but no commited to a git file. That way, the data is not leaked and used to hack into a developers or an indiviaual's email account. The use of python-decouple is important, as that app is used frequently and is highly regarded. A pip3 install is required to use it as a module:

    pip3 install python-decouple

Make sure that pip is up to date. If not, do the following:

    pip --upgrade install pip

The use of the decouple app, is to use the config variable as a way to hide the login and password for the user's email account, so that anyone, seeing a public git work, sees that the data is hidden and not in plain sight. Thus not commiting a .env to a git file is important and it will still carry the app forward.