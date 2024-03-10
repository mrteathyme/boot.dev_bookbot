from pathlib import Path

def word_instances(word_list: list[str]) -> dict[str, int]:
    map = {}
    for word in word_list:
        if word in map:
            map[word] += 1
        else:
            map[word] = 1
    return map

def count_letters(word_list: list[str]) -> dict[str, int]:
    map = {}
    for word in word_list:
        for letter in word:
            if letter in map:
                map[letter] += 1
            else:
                map[letter] = 1
    return map

def generate_report(path_string: str, word_list: list[str], letter_count = True, word_count = True, word_instance_count = False) -> str:
    report = ""
    word_map = word_instances(word_list)
    letter_map = count_letters(word_list)
    report += f"--- Begin Report of {path_string} ---\n"
    if word_count:
        report += f"{len(word_list)} words found in document \n\n"
    if letter_count:
        report += "\nLetter Count:\n"
        for (letter, count) in sort_count_dict(letter_map): 
            if letter.isalpha():
                report += f"The '{letter}' character was found {count} times\n"
    if word_instance_count:
        report += "\nWord Count:\n"
        for (word, count) in sort_count_dict(word_map):
            if word.isalpha():
                report += f"The word '{word}' was found {count} times\n"
    report += f"\n--- End Report of {path_string} ---"
    return report

def sort_count_dict(map: dict[str, int]) -> list[dict[str, int]]:
    return sorted(map.items(), key=lambda x: x[1], reverse=True)

def main():
    path_string = "books/frankenstein.txt"
    book_name = path_string.split("/")[1].split(".")[0]
    with open(path_string, "r") as file:
        contents = file.read()
        words = contents.split()
        lower_words = contents.lower().split()
        print(generate_report(path_string, lower_words))
        if Path("reports").exists == False:
            Path.mkdir("reports", exist_ok=True)
        with open(f"reports/{book_name}.txt", "w") as report_file:
            report_file.write(generate_report(path_string, lower_words, letter_count=True, word_count=True, word_instance_count=True))
main()
