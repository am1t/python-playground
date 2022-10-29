languages = ["Python", "golang", "javascript"]
def print_str(str):
    print(str)
    return str

map(print_str, languages)

language = ", ".join(map(print_str, languages))
print(f"I love {language}")