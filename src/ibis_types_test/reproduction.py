import ibis

t = ibis.table(dict(a="int"), name="t")
t.filter(t.a == 0)
t.filter(t.a.equals(0))
