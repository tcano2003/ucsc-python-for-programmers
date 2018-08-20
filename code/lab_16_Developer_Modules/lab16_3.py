#!/usr/bin/env python
"""Provides a FileLogger(file_name) context manager class, that logs the opening and closing of the file_name.
"""     

#!/usr/bin/env python
"""Provides FileLogger(file_name) context manager class.
"""
import context, time

class FileLogger(context.OpenClose):
    log_file_name = "file.log"
    
    def __enter__(self):
        self.logger_object = open(FileLogger.log_file_name, 'a')
        self.logger_object.write("Opening '%s' as '%s' at %s\n"
                                  % (self.file_name, self.mode,
                                     time.ctime(time.time())))
        return context.OpenClose.__enter__(self)

    def __exit__(self,*args):
        self.logger_object.write("Closing '%s' at %s\n\n" % (
            self.file_name, time.ctime(time.time())))
        self.logger_object.close()
        context.OpenClose.__exit__(self, *args)    

def main():
    for loop in range(3):
        with FileLogger("words.txt", "a") as file_obj:
            file_obj.write("%d time\n" % loop)
    print "words.text:"
    print open("words.txt").read()
    print FileLogger.log_file_name + ":"
    print open(FileLogger.log_file_name).read()

main()                            
