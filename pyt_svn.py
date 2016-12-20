#! /usr/bin/python
# -*- coding: utf-8 -*-

# FileName: pyt_svn.pyt
# Description: svn command used python language

import sys
import subprocess

repo_url_list = {"1":"https://svn.jetlive.net:8443/svn/rd/doc/芒果TV全志定制芯片",
                 "2":"https://svn.jetlive.net:8443/svn/rd/code/广西广电网络机顶盒中间件平台项目/trunk",
                 "3":"https://192.168.95.221:8443/svn/标准产品_Android_机顶盒_海思Hi106SA",
                 "4":"https://svn.jetlive.net:8443/svn/rd/code/广西广电网络机顶盒中间件平台项目/branches/dongliang.wang/trunk",
                 "5":"https://192.168.95.221:8443/svn/标准产品_android_机顶盒_HI3798CV200/trunk",
                 "6":"https://192.168.95.221:8443/svn/标准产品_android_机顶盒_晶晨S905_51/trunk",
                 "7":"https://svn.jetlive.net:8443/svn/rd/code/广西广电网络机顶盒中间件平台项目/branches/tao.yang/trunk"}

repo_url_list_index = ["1","2","3","4","5","6","7"]

class repo_list:
    def set_repo_list(self, list):
        self.repo_list = list

    def get_repo_list(self):
        return self.repo_list

    def show_repo_list(self):
        #for k, v in self.repo_list.items():
        #    print "repo url number[%s]:" %k
        #    print v
        #    print
        for k in repo_url_list_index:
             print "repo url number[%s]:" %k
             print repo_url_list[k]    
             print

def help():
    print "pyt_svn repo_url"

# main
if __name__ == "__main__":
    repo_lists = repo_list()
    repo_lists.set_repo_list(repo_url_list)
    
    if (len(sys.argv)==1):
        repo_lists.show_repo_list()
        url_num = int(raw_input("Enter url number:  "))
        url = repo_lists.get_repo_list()[str(url_num)]
        cmd = "svn co "+str(url)

    elif (len(sys.argv)==2):
        cmd = "svn co "+sys.argv[1]

    elif (len(sys.argv)==3):
        cmd = "svn co "+sys.argv[1]+sys.argv[2]

    # print cmd
    child = subprocess.Popen(cmd, shell=True)
    child.wait()
    print "Down OK!"

    
        

    
