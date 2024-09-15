import argparse
from json import load, dump
from wallMan import render
from cv2 import VideoCapture, CAP_PROP_FRAME_COUNT, CAP_PROP_FPS

if __name__ == "__main__":
    prs = argparse.ArgumentParser(description="Live Wallpaper Manual")
    prs.add_argument("--set_wallpaper", default=None, type=str, help="Sets a wallpaper")
    prs.add_argument("--set_fps", default=None, type=int, help="Sets fps of the wallpaper")

    args = prs.parse_args()

    with open("wallpaper\\info.json", "r") as f:
        jsonFile = load(f)
        f.close()

    if not args.set_wallpaper == None:
        video = VideoCapture(args.set_wallpaper)
        
        jsonFile["path"] = args.set_wallpaper
        jsonFile["frames"] = video.get(CAP_PROP_FRAME_COUNT)
        jsonFile["FPS"] = float(args.set_fps) if not args.set_fps is None else video.get(CAP_PROP_FPS)
        
        video.release()
        with open("wallpaper\\info.json", "w") as f:
            dump(jsonFile, f)
            f.close()
    else:
        print("Path : {}\nFrames : {}\nFPS : {}\nWallpaper is active now.".format(jsonFile["path"], jsonFile["frames"], jsonFile["FPS"]))
        render(VideoCapture(jsonFile["path"]), jsonFile["FPS"])