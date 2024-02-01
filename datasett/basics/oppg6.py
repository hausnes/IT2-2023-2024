from matplotlib import pyplot as plt

aarstall = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
antall = [4478497, 4503436, 4524066, 4552252, 4577457, 4606363, 4640219, 4681134, 4737171, 4799252, 4858199, 4920305, 4985870, 5051275, 5109056, 5165802, 5213985, 5258317, 5295619, 5328212, 5367580, 5391369, 5425270]

plt.plot(aarstall, antall, label="Folkemengde i Norge")
plt.title("Folkemengde i Norge 2000-2022")
plt.xlabel("Årstall")
plt.ylabel("Folkemengde")

plt.legend()

plt.show()