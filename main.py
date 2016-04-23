import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
import time
import sys
import webbrowser
import pychromecast
import pychromecast.controllers.youtube as youtube

def playSound():

    webbrowser.open("https://www.youtube.com/watch?v=Lr-OgG1A74c")

    cast = pychromecast.get_chromecast()
    yt = youtube.YouTubeController()
    cast.register_handler(yt)


    if '--show-status-only' in sys.argv:
        sys.exit()

    if not cast.is_idle:
        print("Killing current running app")
        cast.quit_app()
        time.sleep(5)

    print("Playing media")
    cast.play_media('http://r6---sn-q4fl6n7y.googlevideo.com/videoplayback?mime=video%2Fmp4&initcwndbps=298750&mn=sn-q4fl6n7y&signature=7A89B609313E18A3D799262D2D8D6B4726C6A977.04D80F787565AA1CC3864D109E173DC7FC46629D&mm=31&ip=2a03%3A8180%3A1001%3A16a%3A%3A8ee1&key=yt6&sver=3&dur=221.100&pl=40&source=youtube&ms=au&id=o-AIw_azGH9lHhJlCm_HeXT-pqttw2RzX73JhH4Db5M1Sq&mv=m&mt=1461376097&lmt=1429689317363014&fexp=9407610%2C9408210%2C9416126%2C9416891%2C9419451%2C9422342%2C9422596%2C9426926%2C9428398%2C9429149%2C9429165%2C9429585%2C9431012%2C9432363%2C9433045%2C9433097%2C9433301%2C9433424%2C9433858%2C9433947%2C9433999%2C9435058&upn=x7ANUCJiIvM&itag=18&ipbits=0&ratebypass=yes&sparams=dur%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cnh%2Cpl%2Cratebypass%2Csource%2Cupn%2Cexpire&nh=IgpwcjA1LmRmdzA2KgkxMjcuMC4wLjE&expire=1461397882&title=Love+Can%27t+Turn+Around+-+Farley+Jackmaster+Funk%2C+featuring+Darryl+Pandy', 'video/mp4')

def arp_display(pkt):
    if pkt[ARP].op == 1:  # who-has (request)
        if pkt[ARP].psrc == '0.0.0.0':  # ARP Probe
            if pkt[ARP].hwsrc == 'f0:27:2d:f6:d2:98':  #
                print "hijackin' ur arps"
                playSound()


while (1):
    print sniff(prn=arp_display, filter="arp", store=0, count=10)
