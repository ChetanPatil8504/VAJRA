from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def get_volume_interface():
    devices = AudioUtilities.GetSpeakers()
    interface = devices._dev.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None
    )
    return cast(interface, POINTER(IAudioEndpointVolume))


def change_volume(action):
    volume = get_volume_interface()
    current = volume.GetMasterVolumeLevelScalar()

    if action == "up":
        volume.SetMasterVolumeLevelScalar(min(current + 0.1, 1.0), None)
        print("🔊 Volume increased")

    elif action == "down":
        volume.SetMasterVolumeLevelScalar(max(current - 0.1, 0.0), None)
        print("🔉 Volume decreased")

    elif action == "mute":
        volume.SetMute(1, None)
        print("🔇 Volume muted")

    elif action == "unmute":
        volume.SetMute(0, None)
        print("🔊 Volume unmuted")
