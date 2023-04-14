# def my_country(Country="Rwanda"):
#     print(f"Hello from {Country}")
#A function named concatenate_args that takes any number of string arguments in positional arguments format and concatenates them into a single string
def concatenate_args(*fruits, both="/"):
    return both.join(fruits)
#A function named concatenate_kwargs that takes any number of string arguments in keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    answer = ""
    for key,value in kwargs.items():
        answer+=value

    return answer




