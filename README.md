# TSSH

SSH bruteforcer

# Usage

```bash
python3 tssh.py -u life --host 192.168.1.198  -pw password.txt
python3 tssh.py -u life -hw hosts.txt --password admin123
python3 tssh.py -u life -hw hosts.txt -pw password.txt -o output.txt
```

# Setup
```bash	
git clone https://github.com/mvlttt/tssh.git
cd tssh
pip install -r requirements.txt
```

# Options

```
  -u [USERNAME], --username [USERNAME]
                        SSH username.
  --host [HOST]         Single host target, you can use it for password bruteforce.
  -pwd [PASSWORD], --password [PASSWORD]
                        Constant password, you can use it for host bruteforce.
  -hw [HOSTWL], --hostwl [HOSTWL]
                        Host wordlist.
  -pw [PASSWORDWL], --passwordwl [PASSWORDWL]
                        Password wordlist.
  -p [PORT], --port [PORT]
                        Port to connect to on the remote host (default 22).
  -r [RETRIES], --retries [RETRIES]
                        Specify the connection retries (default 1).
  -t [TIMEOUT], --timeout [TIMEOUT]
                        Connection timeout (default 30s).
  -c [THREAD], --thread [THREAD]
                        Connection thread count (default 40).
  -s [SILENT], --silent [SILENT]
                        Silent mode (default False).
  -o OUTPUT, --output OUTPUT
                        Output file for successful connections
```