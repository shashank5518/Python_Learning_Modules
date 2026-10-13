class Sentence:
    def __init__(self, sentence):
        self.message = sentence
        self.index = 0
        self.words = self.message.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]


def sentence(sentence):
    for word in sentence.split():
        yield word


def main():
    my_sentence = Sentence("this is a test madar chod")

    print(next(my_sentence))
    print(next(my_sentence))
    print(next(my_sentence))
    print(next(my_sentence))
    print(next(my_sentence))
    print(next(my_sentence))

    new_sentence = sentence("hello guys ! welcome to my vlog")
    print(next(new_sentence))
    print(next(new_sentence))
    print(next(new_sentence))
    print(next(new_sentence))
    print(next(new_sentence))
    print(next(new_sentence))
    print(next(new_sentence))
    print(next(new_sentence))


if __name__ == "__main__":
    main()
