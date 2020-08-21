import requests
import random
import threading
from requests_html import HTML

url = 'http://karresults.nic.in/resPUC_2020.asp'

invalid_reg = 'Please check the registration number and try again'
# A valid roll number is 6 digit one
start_roll_no = 1_00_000
end_roll_no = 10_00_000

def extract_marks(docstream, filename):
    html = HTML(html=docstream)
    with open('student_results/'+str(filename), 'w') as fz:
        panels = html.find('div.panel')
        for panel in panels:
            tables = panel.find('table')
            for table in tables:
                table_rows = table.find('tr')
                for tr in table_rows:
                    print(tr.text.split(), file=fz)
        remarks = html.find('#result')
        for rem in remarks:
            indrems = rem.find('tr')
            for ir in indrems:
                print(ir.text.split(), file=fz)


def fetch_results(start_roll_no, end_roll_no, thread_id):
    for index, roll_no in enumerate(range(start_roll_no, end_roll_no)):
        token = random.random()
        # , headers={'Accept':'application/json'})
        r = requests.post(url, data={'frmpuc_tockens': token, 'reg': roll_no})
        if invalid_reg not in r.text:
            print(roll_no, '-> VALID')
            extract_marks(r.text, f'{thread_id}_{index}')
        else:  # Invalid Roll number
            print(roll_no, '-> NOT VALID')


if __name__ == "__main__":
    number_of_threads = 1000
    step = (end_roll_no - start_roll_no)//number_of_threads
    if step <= 0: # When number of threads >= number of total roll_numbers
        step = 1
    threads = list()
    for thread_id, start in enumerate(range(start_roll_no, end_roll_no, step)):
        try:
            thread_start = start
            thread_end = start + step
            print(thread_start, thread_end)
            x = threading.Thread(target=fetch_results,
                                 args=(thread_start, thread_end, thread_id))
            threads.append(x)
            x.start()
        except Exception as e:
            print(str(e))
            continue # Though explicit `continue` is not required

    for thread in threads:
        try:
            thread.join()
        except Exception as e:
            print("Exception while JOINing")
            print(str(e))
            continue # Though explicit `continue` is not required
