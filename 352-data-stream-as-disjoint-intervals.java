/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
// import java.util.ArrayList;
// import java.util.Iterator;
// import java.util.List;
// import java.util.TreeSet;

public class SummaryRanges {

    /** Initialize your data structure here. */
    TreeMap<Integer, Integer> range;
    public SummaryRanges() {
        range = new TreeMap<Integer, Integer>();
    }

    public void addNum(int val) {
        Integer l = range.floorKey(val);
        if (l != null && range.get(l) >= val)
            return;
        Integer r = range.ceilingKey(val);
        if (l != null && r != null && val == range.get(l) + 1
                && val + 1 == r) {
            range.put(l, range.get(r));
            range.remove(r);
        } else if (l != null && val == range.get(l) + 1) {
            range.put(l, val);
        } else if (r != null && val + 1 == r) {
            range.put(val, range.get(r));
            range.remove(r);
        } else {
            range.put(val, val);
        }

    }

    public List<Interval> getIntervals() {
        List<Interval> list = new ArrayList<Interval>();
        for(int l:range.keySet())
        {
            Interval tmp = new Interval(l, range.get(l));
            list.add(tmp);
        }
        return list;
    }
}
/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * List<Interval> param_2 = obj.getIntervals();
 */