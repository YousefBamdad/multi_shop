from django import forms


def validate_phone(value):
    if value[0] != "0":
        raise forms.ValidationError("Phone Should Be Starts With 0", code="phone_validate")


# d = "fff"
# d.isdigit()

def validate_number(value):
    if not value.isnumeric():
        raise forms.ValidationError("Phone Should Be Only Numeric!", code="validate_number")
