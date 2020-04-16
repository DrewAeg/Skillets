import click
from pythonping import ping
@click.command()
@click.option("-url", "--url", help="url list to ping", type=str,
              default="use text file")
def cli(url):
    """
    process a list of URLs and get ping results
    """
    # creating the jinja context from the skillet vars
    url_list = url.split(',')
    for item in url_list:
        print(f'\n{item}')
        response_list = ping(item)
        print(f'  min rtt is: {response_list.rtt_min_ms} ms')
        print(f'  avg rtt is: {response_list.rtt_avg_ms} ms')
        print(f'  max rtt is: {response_list.rtt_max_ms} ms\n')


if __name__ == '__main__':
    cli()

