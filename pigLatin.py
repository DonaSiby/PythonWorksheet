def translate(text):
    vowels = "AEIOUaeiou"
    start = ["xr", "yt"]
    if text[0] in vowels or text[:2] in start:
        return text + "ay"
    for index, letter in enumerate(text):
        if letter in vowels:
            return text[index:] + text[:index] + "ay"
    if "qu" in text:
        qu_index = text.find("qu")
        return text[qu_index + 1 :] + "qu" + "ay"
    y_index = text.find("y")
    if y_index > 0:
        return text[y_index:] + text[:y_index] + "ay"


print(translate("apple"))