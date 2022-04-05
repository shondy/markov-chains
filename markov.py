"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    with open(file_path) as f:
        contents = f.read()

    return contents


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for i in range(len(words) - n):
        key = tuple([words[i + x] for x in range(n)])
        value = words[i + n]
        if key in chains:
            chains[key].append(value)
        else:
            chains[key] = [value]
    # print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""
    if not chains:
        return ""

    link = choice(list(chains))
    words = list(link)
    next_word = ""

    while link in chains:
        next_word = choice(chains[link])
        words.append(next_word)
        list_link = list(link[1:])
        list_link.append(next_word)
        link = tuple(list_link)
        
    return ' '.join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 2)

# Produce random text
random_text = make_text(chains)

print(random_text)
