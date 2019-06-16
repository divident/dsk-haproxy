import eventlet

eventlet.monkey_patch()
import sys
import requests
import csv
from statistics import mean
from timeit import default_timer as timer

PROBE_NUM = 10


def test_performance(queries_number):
    url = "http://localhost:12001"
    pool = eventlet.GreenPool()
    time_probes = []
    for i in range(PROBE_NUM):
        start = timer()
        for _ in range(queries_number):
            pool.spawn(requests.get, url)
        pool.waitall()
        end = timer()
        time_probes.append(end - start)
    result = mean(time_probes)
    print(f"Mean time equals {result} seconds for {queries_number} queries")
    return result


def save_csv(data, file_name):
    with open(file_name, "w+", newline='\n') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for d in data:
            csv_writer.writerow(["{:2.3f}".format(d)])


def main():
    if len(sys.argv) <= 1:
        print("You must provide number of queries to perform!")
        exit(-1)
    try:
        results = []
        for n in sys.argv[1:]:
            n = int(n)
            results.append(test_performance(n))
        save_csv(results, f"results.csv")
    except ValueError:
        print("Queries number must be an integer!")


if __name__ == "__main__":
    main()
