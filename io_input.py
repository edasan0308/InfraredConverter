import difflib
import os


def cnv_func():
    # ファイルをオープンする
    test_data = open("./input", "r")
    in_data = open("./tmp", "r")

    inline = in_data.readline()
    sin_Data = inline.split(":")
    sin_Data[1] = sin_Data[1].lstrip(" [")
    sin_Data[1] = sin_Data[1].rstrip("\n")
    sin_Data[1] = sin_Data[1].rstrip("}")
    sin_Data[1] = sin_Data[1].rstrip(",")
    sin_Data[1] = sin_Data[1].rstrip("]")

    input = sin_Data[1]
    SplitData2 = []

    for b in range(112):
        SplitData2.append(input.split(",")[b])

    print("input")
    print(input)

    # 行ごとにすべて読み込んでリストデータにする
    lines = test_data.readlines()

    Datalist = [[]]
    s = []
    SplitData = []
    # 一行ずつ表示する
    for i,line in enumerate(lines):
        s_Data = line.split(":")
        #Datalist = [x for x in Datalist if x]
        Datalist.append([s_Data[0],s_Data[1]]);
        Datalist = [x for x in Datalist if x]

        Datalist[i][0] = Datalist[i][0].strip("{")
        Datalist[i][0] = Datalist[i][0].strip(" \"")
        Datalist[i][1] = Datalist[i][1].lstrip(" [")
        Datalist[i][1] = Datalist[i][1].rstrip("\n")
        Datalist[i][1] = Datalist[i][1].rstrip("}")
        Datalist[i][1] = Datalist[i][1].rstrip(",")
        Datalist[i][1] = Datalist[i][1].rstrip("]")

        SplitData.append(Datalist[i][1].split(",",112))

        print(Datalist[i][0])
        print(Datalist[i][1])

    print()

    Dis = []
    for i,data in enumerate(Datalist):
        Dis.append(0)
        #0クリア

        for b in range(111):
            Dis[i] += abs(int(SplitData[i][b]) - int(SplitData2[b]) )
        #s.append(difflib.SequenceMatcher(None, input, Datalist[i][1]).ratio())
        #それぞれの信号のシンクロ率の算出

        print(Datalist[i][0]+"    "+str(Dis[i]))

    print()
    print(Datalist[Dis.index(min(Dis))][0]+"    "+str(min(Dis)))

    # ファイルをクローズする
    test_data.close()
    in_data.close()
    os.remove("./tmp")

    return "p1"
