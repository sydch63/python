import re

def email_parse(email):
    try:
        dct_email = {}
        username, domain = email.split('@')
        with open('task_8_1_test_email.txt','r',encoding='utf-8') as f:
            str_file = f.readline()
            while str_file:
                parse_file = re.findall("(^\w+[\'\.\_\+\-]\w+)@(\w+[\.|\-]\w+\.\w+|\w+[\.|\-]\w+)", str_file)
                if parse_file != [] and (parse_file[0][0] == username and parse_file[0][1] == domain):
                    dct_email['username'] = parse_file[0][0]
                    dct_email['domain'] = parse_file[0][1]
                    return dct_email
                else:
                    str_file = f.readline()
    except ValueError as exc:
        raise ValueError((f"wrong email: {email}"))  from exc
    except IndexError as exc:
        raise ValueError((f"wrong email: {email}"))  from exc

print(email_parse("user14_name@domen-name.ru"))