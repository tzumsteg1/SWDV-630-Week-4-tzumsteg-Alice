import sqlite

In [1]: import sqlite3

In [2]: con = sqlite3.connect('pcfb.sqlite')

In [3]: r = con.execute('select * from people')

In [4]: for i in r:
   ...:    print i

(0, u'Alice', u'Research Director', u'555-123-0001', u'4b')
(1, u'Bob', u'Research assistant', u'555-123-0002', u'17')
(2, u'Charles', u'Research assistant', u'555-123-0001', u'24')
(3, u'David', u'Research assistant', u'555-123-0001', u'8')
(4, u'Edward', u'Toadie', u'None', u'Basement')

In [5]: r = con.execute('select p.name, e.name from people as p join experiment as e where e.researcher == p.id')

In [6]: for i in r:
   ...:     print 'Name: %s\n\tExperiment: %s' % (i[0],i[1])
   ...:
Name: Alice
   Experiment: EPV Vaccine trial
Name: Charles
   Experiment: Flu antibody study

#the following line would update Alice's information to the new member
sqlite> update people set name='New Member' where id=0;

#the following line will delete Alice from the database
sqlite> delete from people where name='Alice';

#the following line will select all lines that have information for name and experiment.
sqlite> select p.name, e.name from people as p join experiment as e where e.researcher == p.id;

