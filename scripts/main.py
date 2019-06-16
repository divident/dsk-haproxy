import eventlet
eventlet.monkey_patch()
import sys
import requests
from statistics import mean
from timeit import default_timer as timer

PROBE_NUM = 10


def fetch(url):
    r = requests.get(url)
    # print(r.text)


def test_performance(queries_number):
    url = "http://localhost:12001"
    pool = eventlet.GreenPool()
    time_probes = []
    for i in range(PROBE_NUM):
        start = timer()
        for _ in range(queries_number):
            pool.spawn(fetch, url)
        pool.waitall()
        end = timer()
        time_probes.append(end - start)
    print(f"Mean time equals {mean(time_probes)} seconds for {queries_number} queries")


def main():
    if len(sys.argv) <= 1:
        print("You must provide number of queries to perform!")
        exit(-1)
    try:
        n = int(sys.argv[1])
        test_performance(n)
    except ValueError:
        print("Queries number must be an integer!")


if __name__ == "__main__":
    main()
