import re

def email_parse(email):
    try:
        dct_email = {}
        parse_email = re.findall("(^\w+[\'\.\_\+\-]\w+)@(\w+[\.|\-]\w+\.\w+|\w+[\.|\-]\w+)", email)
        if parse_email != []:
            dct_email['username'] = parse_email[0][0]
            dct_email['domain'] = parse_email[0][1]
            return dct_email
        else:
            raise ValueError
    except ValueError :
        raise ValueError((f"wrong email: {email}"))

print(email_parse("user12_name@domenna.me.ru"))