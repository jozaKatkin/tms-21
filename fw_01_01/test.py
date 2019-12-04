from json_tools import (
    write_json,
    read_json,
    create_user,
    filter_users,
    print_dicts,
    make_correction,
)

filename = "users.json"
write_json(filename, [
    {
        "First Name": "Petr",
        "LastName": "Pchyolkin",
        "Birthday": "01.01.1960",
        "Profession": "Security",
        "id": "0010",
    },
    {
        "First Name": "Masha",
        "LastName": "Kot",
        "Birthday": "02.02.2006",
        "Profession": "School",
        "id": "0020",
    },
    {
        "First Name": "Doomer",
        "LastName": "Wojak",
        "Birthday": "03.03.1992",
        "Profession": "Freelancer",
        "id": "0030",
    },
    {
        "First Name": "Mariya",
        "LastName": "Fapka",
        "Birthday": "04.04.1996",
        "Profession": "HR",
        "id": "0040",
    },
    {
        "First Name": "David",
        "LastName": "Firth",
        "Birthday": "05.05.1980",
        "Profession": "Multiplicator",
        "id": "0050",
    },
    {
        "First Name": "Daniil",
        "LastName": "Sibirsky",
        "Birthday": "06.06.1994",
        "Profession": "Blogger",
        "id": "0060",
    },
    {
        "First Name": "Suri",
        "LastName": "Noel",
        "Birthday": "06.06.1994",
        "Profession": "Blogger",
        "id": "0070",
    },
    {
        "First Name": "Ruslan",
        "LastName": "Koshchey",
        "Birthday": "08.08.1992",
        "Profession": "Freelancer",
        "id": "0080",
    },
    {
        "First Name": "Daniil",
        "LastName": "Ostapov",
        "Birthday": "09.09.1992",
        "Profession": "Teacher",
        "id": "0090",
    },
    {
        "First Name": "Joza",
        "LastName": "Katkin",
        "Birthday": "08.08.1996",
        "Profession": "Anime critic",
        "id": "0100",
    },

])

