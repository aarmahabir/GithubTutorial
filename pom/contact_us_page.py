class ContactUsPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://symonstorozhenko.wixsite.com/website-1/contact")
        self.page.get_by_role("textbox", name="Name *").click()
        self.page.get_by_role("textbox", name="Name *").fill("Arun")
        self.page.get_by_role("textbox", name="Address").click()
        self.page.get_by_role("textbox", name="Address").fill("Fahrenheitstraat")
        self.page.get_by_role("textbox", name="Email *").click()
        self.page.get_by_role("textbox", name="Email *").fill("aarmahabir@gmail.com")
        self.page.get_by_role("textbox", name="Phone").click()
        self.page.get_by_role("textbox", name="Phone").fill("0621324040")
        self.page.get_by_role("textbox", name="Subject").click()
        self.page.get_by_role("textbox", name="Subject").fill("Vakantie")
        self.page.get_by_role("textbox", name="Message").click()
        self.page.get_by_role("textbox", name="Message").fill("Vakantie")

    def submit_form(self, name, address, email, phone, subject, message):
        self.page.fill("[placeholder=\"Enter your name\"]", name)
        self.page.fill("[placeholder=\"Enter your address\"]", address)
        self.page.fill("[placeholder=\"Enter your email\"]", email)
        self.page.fill("[placeholder=\"Enter your phone number\"]", phone)
        self.page.fill("[placeholder=\"Type the subject\"]", subject)
        self.page.fill("textarea", message)

        # self.page.fill("[aria-label=\"Enter your search term\"]", message)
