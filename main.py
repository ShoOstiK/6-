import argparse
from collections import defaultdict,Counter
from train import fit_model
from generate import text_generation




class model:
    def __init__(self):
        self.dict_of_tokens = defaultdict(Counter)

    def fit(self,text=None):
        self.encoded_dict=fit_model(input_dir=text,model=self.dict_of_tokens)


    def generate(self,length,prefix=None):
        return text_generation(self.encoded_dict,length,prefix)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Генерация текста')
    parser.add_argument('text', type=str, help='ссылка на корпус текста для обучения')
    parser.add_argument('length', type=int, help='количество слов для генериеруемой последовательности')
    args = parser.parse_args()

    m=model()
    m.fit(args.text)
    print(m.generate(args.length))


