import math
import node

class Profiler:

    @staticmethod
    def get_int_vid_amount(vid_dur, perc, lim):
        amount_of_videos = []
        for i in range(len(vid_dur)):
            amount_of_videos.append(math.floor(lim*perc[i]/vid_dur[i]))
        return amount_of_videos

    @staticmethod
    def get_perc_int_vid(vid_dur, perc, lim):
        amount_of_videos = Profiler.get_int_vid_amount(vid_dur, perc, lim)
        new_perc = []
        for i in range(len(amount_of_videos)):
            new_perc.append(vid_dur[i]*amount_of_videos[i]/lim)
        return new_perc

    @staticmethod
    def interleave(am_of_vid):
        minEl = max(am_of_vid)
        sch = []
        j = 0
        idv = 0
        while minEl != 0:
            j = 0
            for am in am_of_vid:
                if am != 0:
                    minEl = min(minEl, am)
                    j += 1
            if j == 1:
                idv = am_of_vid.index(minEl)
                break
            sub_sch = []
            for i in range(len(am_of_vid)):
                if am_of_vid[i] != 0:
                    am_of_vid[i] -= minEl
                    sub_sch.append(i)
            sch += sub_sch*minEl
            minEl = max(am_of_vid)
        start = 0
        if j == 1:
            for i in range(am_of_vid[idv]):
                br = False
                while sch.index(idv, start) - start == 0:
                    start = sch.index(idv, start) + 2
                    if start >= len(sch):
                        br = True
                        break
                if br:
                    break
                sch.insert(start, idv)
                am_of_vid[idv] -= 1
            sch += [idv]*am_of_vid[idv]
        return sch

    @staticmethod
    def get_schedule(vid_dur, perc, lim):
        amount_of_videos = Profiler.get_int_vid_amount(vid_dur, perc, lim)
        rest = lim
        for i in range(len(vid_dur)):
            rest -= amount_of_videos[i]*vid_dur[i]
        if rest != 0:
            nod = node.Node(0,vid_dur,rest)
            rest_list = nod.get_req_list()
            for r in rest_list:
                amount_of_videos[vid_dur.index(r)] += 1
        return Profiler.interleave(amount_of_videos)


vide_dur = [1000, 3000, 4235, 5000]
per = [0.25, 0.35, 0.2, 0.2]
lims = 30000
print(Profiler.get_schedule(vide_dur,per,lims))

lz = Profiler.interleave(z)
print(lz)