class Node:
    def __init__(self, dur = {'video_dur' : 0, 'video_id' : -1}, videos_dur=None, lim=0):
        self.dur = dur
        self.lim = lim
        self.references = [None] * len(videos_dur)
        for i in range(len(videos_dur)):
            next_lim = lim - videos_dur[i]['video_dur']
            if next_lim < 0:
                break
            if videos_dur[i]['video_dur'] >= dur['video_dur']:
                self.references[i] = Node(videos_dur[i], videos_dur, lim - videos_dur[i]['video_dur'])
        for ref in self.references:
            if ref is not None:
                self.lim = min(self.lim, ref.lim)

    def get_req_sublist(self):
        list = [self.dur['video_id']]
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