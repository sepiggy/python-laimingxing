import configparser


cf = configparser.ConfigParser(allow_no_value=True)
cf.read('my.cnf')
print(cf.sections())
print(cf.has_section('client'))
print(cf.options('client'))
print(cf.has_option('client', 'user'))
print(cf.get('client', 'host'))
