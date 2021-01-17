filename = "video_summary.csv"
f = open(filename, "a")

def output(line_str):
    f.write(line_str + '\n')
