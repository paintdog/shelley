Shelley
=======

Letztlich handelt es sich um eine Fingerübung, bei der eine Website mit Horoskopen gescrapt und die Horoskope in der Konsole ausgegeben werden können. 

Es gibt 4 Modi ("*daily*", "*weekly*", "*monthly*", "*yearly*") und 12 Sternzeichen ("*Capricorn*", "*Aquarius*", "*Pisces*", "*Aries*", "*Taurus*", "*Gemini*", "*Cancer*", "*Leo*", "*Virgo*", "*Libra*", "*Scorpio*", "*Sagittarius*").

Standardmäßig wird das Tageshoroskop geliefert (Modus: "*daily*"):

    >>> from shelley import get_horoscope
    >>> get_horoscope("aries")
    'The [...] changes.'

Ein anderer Modus kann als Parameter übergeben werden:

    >>> from shelley import get_horoscope
    >>> get_horoscope("aries", "monthly")
    'Usually [...] developments.'

Es handelt sich um eine Fingerübung. Die Urheberrechte an den Texten auf der Website sind zu beachten.
