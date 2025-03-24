text_file = open("file.txt","w")
text_file.write("siemka\n")
lines = ["siemka 2\n","siemka 3\n","siemka 4\n"]
text_file.writelines(lines)
text_file.close()