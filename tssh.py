import argparse
from tsshclass import Tssh
from tsshclass import Output
import sys


parser = argparse.ArgumentParser()
parser.add_argument('-u','--username', nargs="?", help='SSH username.')
parser.add_argument('--host', nargs="?", help='Single host target, you can use it for password bruteforce.')
parser.add_argument('-pwd','--password', nargs="?", help='Constant password, you can use it for host bruteforce.')
parser.add_argument('-hw','--hostwl', nargs="?", help='Host wordlist.')
parser.add_argument('-pw','--passwordwl', nargs="?",help='Password wordlist.')
parser.add_argument('-p','--port',nargs="?",type=int ,default=22,help='Port to connect to on the remote host (default 22).')
parser.add_argument('-r','--retries',nargs="?", default=1,type=int,help='Specify the connection retries (default 1).')
parser.add_argument('-t','--timeout',nargs="?",default=30,type=int, help='Connection timeout (default 30s).')
parser.add_argument('-c','--thread',nargs="?",default=40,type=int, help='Connection thread count (default 40).')
parser.add_argument('-s','--silent',nargs="?",default=False,type=bool, help='Silent mode (default False).')
parser.add_argument('-o','--output', help='Output file for successful connections')
args = parser.parse_args()

logo="""
  ________________ __  __
 /_  __/ ___/ ___// / / /
  / /  \__ \\__ \/ /_/ / 
 / /  ___/ /__/ / __  /  
/_/  /____/____/_/ /_/   
                         
"""
print(logo)


if args.host and args.passwordwl:
    Output.info("Mode: Password brute force")
    ts=Tssh(
        username=args.username,
        host=args.host,
        passwordwl=args.passwordwl,
        port=args.port,
        retries=args.retries,
        timeout=args.timeout,
        outfile=args.output,
        thread=args.thread,
        silent=args.silent
    )
elif args.password and args.hostwl:
    Output.info("Mode: Host brute force")
    ts=Tssh(
        username=args.username,
        hostwl=args.hostwl,
        password=args.password,
        port=args.port,
        retries=args.retries,
        timeout=args.timeout,
        outfile=args.output,
        thread=args.thread,
        silent=args.silent
    )
elif args.hostwl and args.passwordwl:
    Output.info("Mode: Host and password brute force")
    ts=Tssh(
        username=args.username,
        hostwl=args.hostwl,
        passwordwl=args.passwordwl,
        port=args.port,
        retries=args.retries,
        timeout=args.timeout,
        outfile=args.output,
        thread=args.thread,
        silent=args.silent
    )
else:
    Output.info("Mode: Unknown")
    sys.exit(1)


ts.brute()

