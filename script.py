class ShowAttr:
    def __getattr__(self, char):
        print(char)

show = ShowAttr()

show.a
show.bulk
