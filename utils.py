import glob


def menu():
    lof = glob.glob("*.mp4")

    for f in lof:
        print(lof.index(f) + 1, f)

    nof = int(input("Number of file to select: "))

    name = lof[nof - 1]
    print(name)
    print("\n")

    return name


def resolution_menu():
    resolutions = ["720p", "480p", "360x240", "160x120"]

    for resolution in resolutions:
        print(resolutions.index(resolution) + 1, resolution)

    n = int(input("Resolution desired: "))
    print(resolutions[n-1])
    print("\n")

    if n == 1:
        return "scale=1280:720", "720p_resolution"
    elif n == 2:
        return "scale=854:420", "360p_resolution"
    elif n == 3:
        return "scale=360:240", "360x240_resolution"
    elif n == 4:
        return "scale=160:120", "160x120_resolution"
    else:
        return n


def audio_option_menu():
    audios = ["mono", "stereo"]

    for audio in audios:
        print(audios.index(audio) + 1, audio)

    n = int(input("Audio option desired: "))
    print(audios[n-1])
    print("\n")

    return n, audios[n-1]
