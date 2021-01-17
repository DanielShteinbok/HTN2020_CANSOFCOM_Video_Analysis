import file_manager

def csv_format(obj_list, frame):
    for item in obj_list:
        if item[1] > 0:
            for i in range(item[1]):
                file_manager.output(item[0] + ",entered," + frame)
        elif item[1] < 0:
             for i in range(-item[1]):
                file_manager.output(item[0] + ",exited," + frame)
