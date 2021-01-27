message = input(">Convert: ")
words = message.split()
emojis = {
    ":)" : "😀",
    ":(" : "☹",
    "B)" : "😎",
    ":D" : "😃",
    ">:(" : "😡",
    ">:c" : "😡",
    ">:C" : "😡",
    "<3" : "❤"
}
output = ''
for word in words:
    output += emojis.get(word, word) + " "
print(output)
