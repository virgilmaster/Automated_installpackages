import time
class timebar:

    def __init__(self,start,end):
        self.start = start 
        self.end = end


    def counter_process(self):
        start_time = self.start
        end_time = self.end
        runtime = start_time - end_time
        scale = 100
        print('{:=^89}'.format("Line"))
        print("Start downloading the python packages".center(scale // 2, "-"))
        for i in range(scale + 1):
            conuter1 = ">" * i
            counter2 = "-" * (scale - i)
            counter3 = (i / scale) * 100
            print("\r{:^3.0f}%[{}>{}]{:.2f}s".format(counter3, conuter1, counter2, runtime), end="")
            time.sleep(0.1)
        print("\n" + "All the job is done,God bless me,lucky so much".center(scale // 2, "-"))



