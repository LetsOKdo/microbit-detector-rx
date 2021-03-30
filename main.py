def on_received_string(receivedString):
    global signal
    signal = Math.map(radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH),
        -75,
        -47,
        0,
        9)
    led.plot_bar_graph(signal, 9)
radio.on_received_string(on_received_string)

signal = 0
radio.set_group(1)

def on_forever():
    if signal < 2:
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.WHOLE))
    elif 2 >= signal > 1:
        music.play_tone(392, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.SIXTEENTH))
basic.forever(on_forever)
