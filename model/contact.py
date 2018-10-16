from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, photo=None, title=None, company=None,
                 address=None, thome=None, tmobile=None, twork=None, fax=None, email=None, email2=None, email3=None,
                 homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, secaddress=None,
                 sechome=None, secnote=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.thome = thome
        self.tmobile = tmobile
        self.twork = twork
        self.tfax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.secaddress = secaddress
        self.sechome = sechome
        self.secnote = secnote
        self.id = id

    def __repr__(self):
        return ("%s,%s,%s") % (self.firstname, self.lastname, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
