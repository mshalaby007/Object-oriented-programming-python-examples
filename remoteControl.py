#!/usr/bin/env python3
import random
import time

class Remote_Controller():
    def __init__(self, tv_status = "off", tv_volume = 0,channel_list = ["BBC"],channel_name = "BBC"):
        print("creating a remote controller")
        self.tv_status = tv_status
        self.tv_volume = tv_volume
        self.channel_list = channel_list
        self.channel_name = channel_name

    def tv_on(self):
        if self.tv_status == 'on':
            print("tv is already on")
        else:
            print("tv is turnning on...")
            self.tv_status = "on"

    def tv_off(self):
        if self.tv_status == 'off':
            print("tv is already off")
        else:
            print("tv turning off...")
            self.tv_status = 'off'

    def volume_adjustment(self):
        while True:
            answer = input("volume Down: - \nvolume up: '+' \nExit: 'exit'")
            if answer == '-':
                if self.tv_volume != 0:
                    self.tv_volume -= 1
                    print("volume: - ", self.tv_volume)
            elif answer == '+':
                if self.tv_volume != 50:
                    self.tv_volume += 1
                    print("volume: - ", self.tv_volume)
            else:
                print("The sound level has updated.")
                break

    def add_channel(self,channel_name):
        print("adding channel")
        time.sleep(1)
        self.channel_list.append()(channel_name)
        print("channel added...")

    def random_channel(self):
        random_var = random.randint(0,len(self.channel_list)-1)
        self.channel_name = self.channel_list[random_var]
        print("you are now watching ",self.channel_name)

    def __len__(self):
        return len(self.channel_list)

    def __str__(self):
        return "tv status: {} \ntv volume: {} \nchannel list{} \nwatching channel: {}".format(self.tv_status,self.tv_volume,self.channel_list,self.channel_name)

rc = Remote_Controller()

print("""

1. Turn on Tv
2. Turn off tv
3. volume adjustment
4. add channel
5. number of channels
6. open random channel
7. tv inf0

for exit press q


""")

while True:
    operation = input("enter an operation").lower()
    if operation == "q":
        print("program is closing")
    elif operation == '1':
        rc.tv_on()
    elif operation == '2':
        rc.tv_off()
    elif operation == '3':
        rc.volume_adjustment()
    elif operation == '4':
        channel_names = input("enter channel name followed by ,").split(',')
        for channel in channel_names:
            rc.add_channel(channel_name)
    elif operation == '5':
        print("number of channels:",len(rc))
    elif operation == '6':
        rc.random_channel()
    elif operation == '7':
        print(rc)
    else:
        print('bad operation')