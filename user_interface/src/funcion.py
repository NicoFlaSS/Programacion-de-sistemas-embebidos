def create_dict(first_name, last_name, age, height, weight, birth_place, birthday, blood_type, curp, rfc):

    user_info = {
    "firstname": first_name,
    "lastname": last_name,
    "age": age,
    "height": height,
    "weight": weight,
    "birth_place": birth_place,
    "birthday": birthday,
    "blood_type": blood_type,
    "curp": curp,
    "rfc": rfc
    }

    return user_info

diccionario_nico = create_dict('jesus','fuentes', 20, 172, 63, 'Ciudad Victoria', '30 de noviembre', 'o+', 'FURJ041130HTSNZSA9' ,'kusk')
print (diccionario_nico)