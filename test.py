import lds_org

lds = lds_org.LDSOrg()
lds.signin(username, password)
rv = lds.get('current-user-id')
print(rv.json())

with lds_org.session() as lds:
    rv = lds.get(some_context_of_interest)

# TODO