
import requests
import random
import threading

url = 'http://karresults.nic.in/resPUC_2020.asp'

invalid_reg = 'Please check the registration number and try again'
start_roll_no = 100000
end_roll_no =   1000000

def fetch_results(start_roll_no, end_roll_no):
    for roll_no in range(start_roll_no,end_roll_no):
        token = random.random()
        r = requests.post(url, data={'frmpuc_tockens': token, 'reg':roll_no}) #, headers={'accept':'application/json'})
        if invalid_reg not in r.text:
            print(roll_no, '-> VALID')
            with open('revresults/'+str(roll_no),'w') as fh:
                fh.write(r.text)
        else:
            print(roll_no, '-> NOT VALID')


if __name__ == "__main__":
    step = 1000
    threads = list()
    for start in range(start_roll_no, end_roll_no, step):
        try:
            thread_start = start
            thread_end = start + step
            x = threading.Thread(target=fetch_results, args=(thread_start,thread_end))
            threads.append(x)
            x.start()
        except Exception as e:
            print(str(e))
            continue

    for thread in threads:
        try:
            thread.join()
        except Exception as e:
            print("Exception while JOINing")
            print(str(e))
            continue
