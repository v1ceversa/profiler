class Node:
    def __init__(self, dur=0, videos_dur=None, lim=0):
        self.dur = dur
        self.lim = lim
        self.references = [None] * len(videos_dur)
        for i in range(len(videos_dur)):
            next_lim = lim - videos_dur[i]
            if next_lim < 0:
                break
            if videos_dur[i] >= dur:
                self.references[i] = Node(videos_dur[i], videos_dur, lim - videos_dur[i])
        for ref in self.references:
            if ref is not None:
                self.lim = min(self.lim, ref.lim)

    def max_level(self, level=0):
        max_lev = level
        for i in self.references:
            if i is not None:
                max_lev = max(max_lev, i.max_level(level + 1))
        return max_lev

    def print_level(self, req_lev, cur_lev=0):
        if req_lev == cur_lev:
            print(self.dur)
        else:
            for i in self.references:
                if i is not None:
                    i.print_level(req_lev, cur_lev + 1)
        if cur_lev == 0:
            print("req lev is: " + str(req_lev))

    def print_tree(self, level=0):
        n = self.max_level()
        for i in range(n):
            self.print_level(i)

    def get_req_sublist(self):
        list = [self.dur]
        for ref in self.references:
            if ref is not None and self.lim == ref.lim:
                list += ref.get_req_sublist()
                break
        return list

    def get_req_list(self):
        list = []
        for ref in self.references:
            if ref is not None and self.lim == ref.lim:
                list += ref.get_req_sublist()
                break
        return list