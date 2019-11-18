my_list = [
    {
        "Serial number": 1,
        "Year": 1995
    },
    {
        "Serial number": 2,
        "Year": 1996
    },
    {
        "Serial number": 3,
        "Year": 2005
    },
    {
        "Serial number": 4,
        "Year": 2000
    }
]

n = int(input())
new_list = [car for car in my_list if car["Year"] > n]
print(new_list)

