from requests_html import HTML
import time

"""
result = [
    {
    subjects: {
        kannada: (36,None,36,True),
        english: (36,None,36,True)
    },
    total: 237,
    remark: True
}
]
with open('scresult.html') as fr:
    source = fr.read()
    html = HTML(html=source)
"""

#print(html.text)

# print(html.find('title')[0].text)

#print(html.find('#footer'))

def extract_marks(filename):
    with open('results/'+filename) as fr:
        source = fr.read()
        html = HTML(html=source)
    with open('zipresults/'+filename,'w') as fz:
        print(filename)
        panels = html.find('div.panel')
        for panel in panels:
            tables = panel.find('table')
            for table in tables:
                table_rows = table.find('tr')
                for tr in table_rows:
                    # fz.(str(tr.text.split()))
                    print(tr.text.split(), file=fz)
                    # time.sleep(2)
        remarks = html.find('#result')
        for rem in remarks:
            indrems = rem.find('tr')
            for ir in indrems:
                print(ir.text.split(), file=fz)


if __name__ == "__main__":
    import os
    for file in os.listdir('results'):
        print(file)
        if os.path.isfile('results/'+file):
            extract_marks(file)
