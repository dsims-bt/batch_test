from pydaisi import Daisi

if __name__ == '__main__':
    daisi = Daisi('Batch Process', base_url='https://dev3.daisi.io')
    result = daisi.give_color(repeat=5)
    for res in result.value:
        print(res.value)