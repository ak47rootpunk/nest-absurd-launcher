import pychromecast
import time

MUSIC_URL = 'https://raw.githubusercontent.com/ak47rootpunk/nest-absurd-launcher/main/sounds/suara_roket.mp3'

casts, _ = pychromecast.get_chromecasts()
cast = next(cc for cc in casts if 'Nest Mini' in cc.device.friendly_name)
cast.wait()

mc = cast.media_controller
mc.play_media(MUSIC_URL, 'audio/mp3')
mc.block_until_active()
time.sleep(5)
