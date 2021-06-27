class NameNotFound(Exception):
    pass


class MustContainAtSymbol(Exception):
    pass


class TooManyAtSymbols(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


domains = ['.com', '.bg', '.net', '.org']


def validate_email(email):
    if '@' not in email:
        raise MustContainAtSymbol('Email must contain @')
    username, domain, *rest = email.split('@')
    if len(rest) > 0:
        raise TooManyAtSymbols('The mail must contain only one "@" symbol')
    if len(username) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')
    if '.' + domain.split('.')[-1] not in domains:
        raise InvalidDomainError('Domain must be on of the following: .com, .bg, .org, .net')


def main():
    while True:
        email = input()
        if email == 'End':
            break
        try:
            validate_email(email)
        except (NameTooShortError, InvalidDomainError, TooManyAtSymbols, MustContainAtSymbol) as exception:
            print(exception)


if __name__ == "__main__":
    main()
