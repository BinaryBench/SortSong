import os
import re
import shutil
import sys
import getopt
from mutagen.easyid3 import EasyID3

fileExtension = "mp3"


def main(argv):

    source_dir = os.getcwd()
    target_dir = os.path.join(os.getcwd(), "Output")


    try:
        opts, args = getopt.getopt(argv, "hs:t:", ["source=", "target="])
    except getopt.GetoptError:
        print(' --source- <src directory> --target <target directory>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(' --source <src directory> --target <target directory>')
            sys.exit()
        elif opt in ("-s", "--source"):
            source_dir = os.path.realpath(arg)
        elif opt in ("-t", "--target"):
            target_dir = os.path.realpath(arg)

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for subdir, dirs, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(fileExtension):

                # skip output file
                if subdir.startswith(target_dir):
                    continue

                file_name = os.path.splitext(file)[0]

                # Default meta
                song_name = file_name
                artist = "Unknown"
                genre = "Unknown"

                # Artist / Song Name
                name = re.sub("[\(\[].*?[\)\]]", "", file_name)  # Removes ()
                name = re.sub("[\{\[].*?[\}\]]", "", name)  # Removes {}
                name = re.sub("[\[].*?[\]]", "", name)  # Removes []
                split = name.split("-")
                if len(split) >= 2:
                    artist = split[1].strip()
                    song_name = split[2].strip()

                # Genre
                genre_match = re.match(r"[^[]*\[([^]]*)\]", file_name)
                if genre_match:
                    genre = genre_match.group(1)

                # Copy file
                artist_dir = os.path.join(target_dir, artist)
                if not os.path.exists(artist_dir):
                    os.makedirs(artist_dir)
                copy_from = os.path.join(subdir, file)
                copy_to = os.path.join(artist_dir, song_name + "." + fileExtension)
                if os.path.exists(copy_to):
                    print(copy_to + " already exists!")
                    continue
                shutil.copyfile(copy_from, copy_to)

                # Setting meta
                audio = EasyID3(copy_to)
                audio["title"] = song_name
                audio["artist"] = artist
                audio["genre"] = genre
                audio.save()

if __name__ == "__main__":
    main(sys.argv[1:])