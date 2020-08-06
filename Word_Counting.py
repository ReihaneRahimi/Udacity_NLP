"""Count words."""
import re
import string

def count_words(text):
    """Count how many times each unique word occurs in text."""
    counts = dict()  # dictionary of { <word>: <count> } pairs to return

    # TODO: Convert to lowercase
    text_lower = text.lower()

    # TODO: Split text into tokens (words), leaving out punctuation
    a = text_lower.translate(str.maketrans('', '', string.punctuation))
    x = re.split('[^a-z]', a)

    # TODO: Aggregate word counts using a dictionary
    counts = dict([(i, x.count(i)) for i in set(x)])

    return counts


def test_run():
    with open("input.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))

        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()
