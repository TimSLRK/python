import re

def email_parse(email_address):
    """ Извлекает имя пользователя и почтовый домен из email адреса """

    compile_name = re.compile(r'(?P<username>[a-zA-Z0-9._-]+)[@](?P<domain>\w+[.]\w+)')
    parsed = re.match(compile_name, email_address)
    if not parsed:
        raise ValueError(f"wrong email: {email_address}")
    return parsed.groupdict()


print(email_parse('antonowtima@mail.ru'))
print(email_parse('anT.9o_no-wtima@mail.ru'))
print(email_parse('antonowtima@mailru'))
