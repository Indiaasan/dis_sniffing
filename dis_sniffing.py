#!/usr/bin/python3
from glob import glob
import os
if os.path.exists("/etc/v2ray-agent/xray/conf"):
    config_list = glob("/etc/v2ray-agent/xray/conf/*.json")
    if config_list:
        for file in config_list:
            try:
                os.system(f"cp {file} {file}-副本")
                with open(file, "r") as r_text:
                    read_conf = r_text.read()

                with open(file, "w") as w_text:
                    new_conf = read_conf.replace('"enabled": true,', '"enabled": false,')
                    w_text.write(new_conf)
                os.system(f"rm {file}-副本")
            except:
                print(f"修改【{file}】这个配置文件时发生错误，请手动修改。")
        else:
            try:
                os.system('/etc/v2ray-agent/xray/xray -confdir /etc/v2ray-agent/xray/conf')
                os.system('systemctl status xray')
            except:
                print('重启xray失败，请手动启动mack-a脚本以添加账户的方式重启xray')
            print("修改结束...")
            
    else:
        print("错误：配置文件路中没有配置文件")
else:
    print("错误：未发现mack-a的xray配置文件路径")
