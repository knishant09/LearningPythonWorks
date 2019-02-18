

def solutions(S):

    output = ""
    file_dict = {"music": 0, "images": 0, "movies": 0, "other": 0}

    string_list = S.split('\n')
    for s in string_list:
        file_details = s.split(" ")
        file_detail_token = file_details[0].split(".")
        file_type = getFileType(file_detail_token[-1])

        current_size = file_dict.get(file_type)

        current_size += int(file_details[1][:-1])

        file_dict.update({file_type: current_size})

    first = True
    for key, value in file_dict.items():

        value = str(value)
        value = value + 'b'

        if first:
            output += key + ' ' + value
            first = False
        else:
            output += '\n' + key + ' ' + value

    return output




def getFileType(ext):
    if ext == "mp3" or ext == "aac" or ext =="flac":
        return "music"
    elif ext == "jpg" or ext == "bmp" or ext =="gif":
        return "images"
    elif ext == "mp4" or ext == "avi" or ext =="mkv":
        return "movies"
    else:
        return "other"




S = "my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b"

print(solutions(S))

