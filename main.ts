radio.onReceivedString(function (receivedString) {
    signal = Math.map(radio.receivedPacket(RadioPacketProperty.SignalStrength), -75, -47, 0, 9)
    led.plotBarGraph(
    signal,
    9
    )
})
let signal = 0
radio.setGroup(1)
basic.forever(function () {
    if (signal < 4) {
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Whole))
    } else {
        music.playTone(392, music.beat(BeatFraction.Half))
        music.rest(music.beat(BeatFraction.Quarter))
    }
})
