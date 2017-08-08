"""
For KIT103/KMA115 Practical 2: Working with sets
Revised: 2015-07-14

This is not a 'real' database, but a script to provide you with some
working data (fictitious students spread across fictitious units).

The 'database' is a dictionary of student IDs mapped to dictionaries,
which map field names (sid, given [name], family [name], and age) to
the values for that student.

The three unit enrolment sets are tik301, ikt130 and kti310. Rather
than typing these out each time, either create aliases for them, as in
i = ikt130
or type the first two letters and press Tab to get Spyder to complete it
for you.
"""

from matplotlib_venn import venn3
from pylab import show


def visualise_overlaps():
    """Displays a Venn diagram of the number of students in each unit
    and the intersections between them."""
    venn3([ikt130,kti310,tik301], set_labels=('IKT130', 'KTI310', 'TIK301'))
    show()


def display_student(student):
    """Prints one student (dict structure) in fixed width columns.

    If you don't mind columns not lining up then it can be done more simply
    than this.
    """
    print('{0:d}  {1:<12}  {2:<12}  {3:d}'.format(student['sid'], student['family'], student['given'], student['age']))


def display_subset(sidset):
    """Very basic printing of the subset of students."""
    print('ID    Family name   Given name    Age')
    print('----  ------------  ------------  ---')
    for sid in sidset:
        display_student(db[sid])


def display_all():
    """Displays all student details."""
    display_subset( list(db) ) #by default this takes the keys from the dict
        

"""The 'database' of students and enrolments."""

db = {
    2167:{'sid':2167,'given':'Carlo','family':'Aponte','age':19},
    6331:{'sid':6331,'given':'Missy','family':'Battin','age':19},
    8860:{'sid':8860,'given':'Rhonda','family':'Billingsley','age':21},
    3775:{'sid':3775,'given':'Reita','family':'Blaze','age':43},
    5160:{'sid':5160,'given':'Truman','family':'Cooke','age':25},
    9853:{'sid':9853,'given':'Reiko','family':'Coon','age':26},
    4678:{'sid':4678,'given':'Evangelina','family':'Croley','age':24},
    7419:{'sid':7419,'given':'Myrtice','family':'Cuevas','age':32},
    6962:{'sid':6962,'given':'Leonie','family':'Dessert','age':23},
    5031:{'sid':5031,'given':'Ardath','family':'Docherty','age':24},
    1712:{'sid':1712,'given':'Micah','family':'Dockstader','age':41},
    9494:{'sid':9494,'given':'Carletta','family':'Dolezal','age':36},
    8268:{'sid':8268,'given':'Jeff','family':'Garceau','age':22},
    5735:{'sid':5735,'given':'Ji','family':'Garris','age':20},
    1866:{'sid':1866,'given':'Williams','family':'Gillie','age':24},
    1625:{'sid':1625,'given':'Abigail','family':'Grignon','age':19},
    3542:{'sid':3542,'given':'Raleigh','family':'Guitierrez','age':28},
    6717:{'sid':6717,'given':'Gene','family':'Hamblin','age':56},
    8139:{'sid':8139,'given':'Cesar','family':'Hougen','age':30},
    8084:{'sid':8084,'given':'Michel','family':'Jablonski','age':24},
    6401:{'sid':6401,'given':'Tandra','family':'Joines','age':19},
    1760:{'sid':1760,'given':'Karena','family':'Killeen','age':19},
    9024:{'sid':9024,'given':'German','family':'Klass','age':22},
    5131:{'sid':5131,'given':'Millard','family':'Kluth','age':20},
    8254:{'sid':8254,'given':'Nga','family':'Kriebel','age':25},
    7144:{'sid':7144,'given':'Siobhan','family':'Kuo','age':32},
    5034:{'sid':5034,'given':'Otha','family':'Lang','age':23},
    4580:{'sid':4580,'given':'Kelsey','family':'Lares','age':21},
    6528:{'sid':6528,'given':'Buck','family':'Lenig','age':24},
    9072:{'sid':9072,'given':'Corey','family':'Liberatore','age':33},
    2302:{'sid':2302,'given':'Kecia','family':'Lindemann','age':31},
    1165:{'sid':1165,'given':'Santa','family':'Masden','age':31},
    6849:{'sid':6849,'given':'Glennis','family':'Mcandrews','age':20},
    6090:{'sid':6090,'given':'Pandora','family':'Mceachern','age':27},
    3566:{'sid':3566,'given':'Brigida','family':'Meng','age':31},
    2680:{'sid':2680,'given':'Chung','family':'Milstead','age':24},
    4221:{'sid':4221,'given':'Noelia','family':'Mullet','age':46},
    9603:{'sid':9603,'given':'Garret','family':'Nakasone','age':21},
    3769:{'sid':3769,'given':'Garth','family':'Nanez','age':20},
    8320:{'sid':8320,'given':'Lavada','family':'Neace','age':35},
    9104:{'sid':9104,'given':'August','family':'Neilsen','age':28},
    8741:{'sid':8741,'given':'Ward','family':'Ney','age':25},
    7735:{'sid':7735,'given':'Emil','family':'Oland','age':18},
    1043:{'sid':1043,'given':'Julio','family':'Overland','age':21},
    6028:{'sid':6028,'given':'Zaida','family':'Pablo','age':21},
    5290:{'sid':5290,'given':'Ardella','family':'Pendarvis','age':21},
    4223:{'sid':4223,'given':'Yun','family':'Perl','age':31},
    2409:{'sid':2409,'given':'Emile','family':'Reis','age':25},
    8602:{'sid':8602,'given':'Lucia','family':'Richter','age':19},
    9077:{'sid':9077,'given':'Mohammed','family':'Sakamoto','age':36},
    6887:{'sid':6887,'given':'Delora','family':'Sayegh','age':19},
    9143:{'sid':9143,'given':'Gayle','family':'Schiro','age':35},
    6650:{'sid':6650,'given':'Fermin','family':'Schutz','age':19},
    7907:{'sid':7907,'given':'Del','family':'Shellman','age':36},
    5814:{'sid':5814,'given':'Stacy','family':'Sorrentino','age':20},
    4013:{'sid':4013,'given':'Gladys','family':'Stringham','age':19},
    2701:{'sid':2701,'given':'Gilberto','family':'Tidsworth','age':20},
    1096:{'sid':1096,'given':'Josefa','family':'Tinker','age':24},
    5160:{'sid':5160,'given':'Ervin','family':'Voight','age':34},
    2009:{'sid':2009,'given':'Porfirio','family':'Weible','age':39},
}

# Unit enrolments

tik301 = {1043,1165,1625,1866,2009,2167,2701,3566,5034,5131,6331,6650,6717,6849,8084,9024,9072,9143,9494,9853}
ikt130 = {1165,1625,1760,1866,2302,2680,4223,5031,5034,5131,5814,6650,6887,7907,8084,8320,8860,9024,9143,9494}
kti310 = {1043,1165,1625,2009,3542,3566,4013,4221,4580,8320}
