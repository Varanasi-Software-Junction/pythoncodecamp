import matplotlib.pyplot as plt


class RegressionPredict:
    def __init__(self, x, y, projecttitle, xlabel="X", ylabel="Y"):
        self.x = x
        self.y = y
        self.projecttitle = projecttitle
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.x2= [i*i for i in x]

    def plotdata(self, x, y, xlabel, ylabel, plotlabel, projecttitle):
        plt.title(projecttitle)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.plot(x, y, color="red", label=plotlabel)
        plt.scatter(x, y, color="blue", label=plotlabel)
        plt.legend()
        plt.show()

    def plotXY(self):
        self.plotdata(self.x, self.y, self.xlabel, self.ylabel,
                      "Runs per innings", self.projecttitle)
    def plotXX2(self):
        self.plotdata(self.x, self.x2, self.xlabel, "Innings2",
                      "Runs per innings", self.projecttitle + "\nInnings="+str(self.x) + "\nInnings2=" + str(self.x2))


rgp = RegressionPredict([1, 2, 3, 4, 5], [44, 32, 57, 90, 16],
                        "Virat's Runs in IPL", "Innings", "Runs")
rgp.plotXY()
rgp.plotXX2()
0