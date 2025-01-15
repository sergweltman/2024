def longest_common_prefix(words):
    if not words:
        return ""

    # Начнем с предположения, что префикс — это первое слово
    prefix = words[0]

    for word in words[1:]:
        # Пока префикс не является началом текущего слова, сокращаем его
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

# Пример использования
words = ["flower", "flow", "flight"]
result = longest_common_prefix(words)
print(result)  # Вывод: "fl"