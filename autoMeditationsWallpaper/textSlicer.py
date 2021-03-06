import os
from random import randrange

from autoMeditationsWallpaper.wallpaperMaker import textToImage


def find_lines(txt):
    excerpts = [[1, 1, 57], [1, 2, 67], [1, 3, 74], [1, 4, 85], [1, 5, 102], [1, 6, 113], [1, 7, 130], [1, 8, 137],
                [1, 9, 141], [1, 10, 147], [1, 11, 153], [1, 12, 166], [1, 13, 180], [1, 14, 245], [1, 15, 304],
                [1, 16, 323], [1, 17, 340, 359], [2, 1, 363], [2, 2, 379], [2, 3, 390], [2, 4, 402], [2, 5, 409],
                [2, 6, 420], [2, 7, 425], [2, 8, 431], [2, 9, 435], [2, 10, 441], [2, 11, 454], [2, 12, 473],
                [2, 13, 488], [2, 14, 501], [2, 15, 517], [2, 16, 521], [2, 17, 535, 554], [3, 1, 559], [3, 2, 572],
                [3, 3, 593], [3, 4, 608], [3, 5, 642], [3, 6, 652], [3, 7, 676], [3, 8, 689], [3, 9, 696], [3, 10, 702],
                [3, 11, 711], [3, 12, 734], [3, 13, 742], [3, 14, 749], [3, 15, 756], [3, 16, 760, 779], [4, 1, 784],
                [4, 2, 794], [4, 3, 797], [4, 4, 841], [4, 5, 854], [4, 6, 859], [4, 7, 864], [4, 8, 867], [4, 9, 870],
                [4, 10, 872], [4, 11, 879], [4, 12, 882], [4, 13, 889], [4, 14, 892], [4, 15, 896], [4, 16, 899],
                [4, 17, 903], [4, 18, 906], [4, 19, 911], [4, 20, 922], [4, 21, 932], [4, 22, 948], [4, 23, 951],
                [4, 24, 958], [4, 25, 969], [4, 26, 974], [4, 27, 981], [4, 28, 987], [4, 29, 992], [4, 30, 1004],
                [4, 31, 1009], [4, 32, 1014], [4, 33, 1032], [4, 34, 1046], [4, 35, 1049], [4, 36, 1052], [4, 37, 1059],
                [4, 38, 1064], [4, 39, 1067], [4, 40, 1078], [4, 41, 1084], [4, 42, 1086], [4, 43, 1089], [4, 44, 1093],
                [4, 45, 1097], [4, 46, 1105], [4, 47, 1115], [4, 48, 1122], [4, 49, 1140], [4, 50, 1158],
                [4, 51, 1172, 1177], [5, 1, 1182], [5, 2, 1207], [5, 3, 1210], [5, 4, 1218], [5, 5, 1225], [5, 6, 1241],
                [5, 7, 1261], [5, 8, 1265], [5, 9, 1300], [5, 10, 1317], [5, 11, 1335], [5, 12, 1341], [5, 13, 1358],
                [5, 14, 1368], [5, 15, 1374], [5, 16, 1386], [5, 17, 1400], [5, 18, 1403], [5, 19, 1409], [5, 20, 1414],
                [5, 21, 1425], [5, 22, 1431], [5, 23, 1437], [5, 24, 1447], [5, 25, 1452], [5, 26, 1457], [5, 27, 1466],
                [5, 28, 1472], [5, 29, 1480], [5, 30, 1487], [5, 31, 1493], [5, 32, 1506], [5, 33, 1512], [5, 34, 1531],
                [5, 35, 1538], [5, 36, 1542, 1559], [6, 1, 1563], [6, 2, 1568], [6, 3, 1575], [6, 4, 1578],
                [6, 5, 1581], [6, 6, 1584], [6, 7, 1586], [6, 8, 1589], [6, 9, 1593], [6, 10, 1598], [6, 11, 1606],
                [6, 12, 1611], [6, 13, 1618], [6, 14, 1631], [6, 15, 1647], [6, 16, 1660], [6, 17, 1688], [6, 18, 1693],
                [6, 19, 1699], [6, 20, 1704], [6, 21, 1714], [6, 22, 1719], [6, 23, 1723], [6, 24, 1730], [6, 25, 1734],
                [6, 26, 1740], [6, 27, 1749], [6, 28, 1756], [6, 29, 1760], [6, 30, 1763], [6, 31, 1789], [6, 32, 1793],
                [6, 33, 1800], [6, 34, 1806], [6, 35, 1809], [6, 36, 1816], [6, 37, 1825], [6, 38, 1829], [6, 39, 1835],
                [6, 40, 1839], [6, 41, 1846], [6, 42, 1854], [6, 43, 1867], [6, 44, 1871], [6, 45, 1890], [6, 46, 1896],
                [6, 47, 1901], [6, 48, 1917], [6, 49, 1925], [6, 50, 1931], [6, 51, 1941], [6, 52, 1945], [6, 53, 1949],
                [6, 54, 1952], [6, 55, 1954], [6, 56, 1958], [6, 57, 1960], [6, 58, 1965], [6, 59, 1969, 1973],
                [7, 1, 1977], [7, 2, 1984], [7, 3, 1992], [7, 4, 2000], [7, 5, 2005], [7, 6, 2015], [7, 7, 2019],
                [7, 8, 2024], [7, 9, 2027], [7, 10, 2036], [7, 11, 2040], [7, 12, 2043], [7, 13, 2045], [7, 14, 2055],
                [7, 15, 2060], [7, 16, 2065], [7, 17, 2080], [7, 18, 2085], [7, 19, 2092], [7, 20, 2099], [7, 21, 2103],
                [7, 22, 2106], [7, 23, 2113], [7, 24, 2120], [7, 25, 2126], [7, 26, 2131], [7, 27, 2139], [7, 28, 2146],
                [7, 29, 2150], [7, 30, 2156], [7, 31, 2159], [7, 32, 2165], [7, 33, 2169], [7, 34, 2175], [7, 35, 2181],
                [7, 36, 2186], [7, 37, 2189], [7, 38, 2193], [7, 39, 2196], [7, 40, 2198], [7, 41, 2201], [7, 42, 2204],
                [7, 43, 2206], [7, 44, 2208], [7, 45, 2214], [7, 46, 2220], [7, 47, 2229], [7, 48, 2234], [7, 49, 2242],
                [7, 50, 2248], [7, 51, 2254], [7, 52, 2260], [7, 53, 2264], [7, 54, 2269], [7, 55, 2274], [7, 56, 2293],
                [7, 57, 2297], [7, 58, 2300], [7, 59, 2310], [7, 60, 2313], [7, 61, 2319], [7, 62, 2323], [7, 63, 2329],
                [7, 64, 2334], [7, 65, 2344], [7, 66, 2347], [7, 67, 2362], [7, 68, 2370], [7, 69, 2385], [7, 70, 2389],
                [7, 71, 2395], [7, 72, 2399], [7, 73, 2402], [7, 74, 2406], [7, 75, 2410, 2417], [8, 1, 2421],
                [8, 2, 2441], [8, 3, 2447], [8, 4, 2453], [8, 5, 2455], [8, 6, 2462], [8, 7, 2468], [8, 8, 2484],
                [8, 9, 2489], [8, 10, 2492], [8, 11, 2498], [8, 12, 2502], [8, 13, 2508], [8, 14, 2511], [8, 15, 2518],
                [8, 16, 2524], [8, 17, 2529], [8, 18, 2536], [8, 19, 2541], [8, 20, 2546], [8, 21, 2554], [8, 22, 2561],
                [8, 23, 2565], [8, 24, 2570], [8, 25, 2574], [8, 26, 2588], [8, 27, 2593], [8, 28, 2598], [8, 29, 2604],
                [8, 30, 2610], [8, 31, 2613], [8, 32, 2623], [8, 33, 2632], [8, 34, 2635], [8, 35, 2649], [8, 36, 2657],
                [8, 37, 2667], [8, 38, 2677], [8, 39, 2680], [8, 40, 2684], [8, 41, 2690], [8, 42, 2703], [8, 43, 2706],
                [8, 44, 2711], [8, 45, 2717], [8, 46, 2726], [8, 47, 2732], [8, 48, 2744], [8, 49, 2753], [8, 50, 2761],
                [8, 51, 2775], [8, 52, 2789], [8, 53, 2797], [8, 54, 2802], [8, 55, 2808], [8, 56, 2813], [8, 57, 2820],
                [8, 58, 2833], [8, 59, 2838], [8, 60, 2841], [8, 61, 2846, 2849], [9, 1, 2853], [9, 2, 2892],
                [9, 3, 2901], [9, 4, 2925], [9, 5, 2928], [9, 6, 2930], [9, 7, 2934], [9, 8, 2937], [9, 9, 2943],
                [9, 10, 2971], [9, 11, 2976], [9, 12, 2982], [9, 13, 2986], [9, 14, 2990], [9, 15, 2994], [9, 16, 2998],
                [9, 17, 3002], [9, 18, 3004], [9, 19, 3007], [9, 20, 3011], [9, 21, 3013], [9, 22, 3023], [9, 23, 3030],
                [9, 24, 3038], [9, 25, 3042], [9, 26, 3046], [9, 27, 3050], [9, 28, 3058], [9, 29, 3073], [9, 30, 3091],
                [9, 31, 3102], [9, 32, 3107], [9, 33, 3116], [9, 34, 3120], [9, 35, 3125], [9, 36, 3133], [9, 37, 3139],
                [9, 38, 3148], [9, 39, 3151], [9, 40, 3158], [9, 41, 3175], [9, 42, 3191, 3229], [10, 1, 3233],
                [10, 2, 3249], [10, 3, 3257], [10, 4, 3265], [10, 5, 3268], [10, 6, 3272], [10, 7, 3290], [10, 8, 3316],
                [10, 9, 3344], [10, 10, 3355], [10, 11, 3361], [10, 12, 3375], [10, 13, 3385], [10, 14, 3394],
                [10, 15, 3399], [10, 16, 3406], [10, 17, 3408], [10, 18, 3412], [10, 19, 3416], [10, 20, 3422],
                [10, 21, 3426], [10, 22, 3431], [10, 23, 3436], [10, 24, 3442], [10, 25, 3447], [10, 26, 3455],
                [10, 27, 3465], [10, 28, 3473], [10, 29, 3480], [10, 30, 3483], [10, 31, 3491], [10, 32, 3509],
                [10, 33, 3517], [10, 34, 3546], [10, 35, 3563], [10, 36, 3573], [10, 37, 3594], [10, 38, 3598, 3608],
                [11, 1, 3612], [11, 2, 3633], [11, 3, 3642], [11, 4, 3649], [11, 5, 3652], [11, 6, 3656], [11, 7, 3686],
                [11, 8, 3689], [11, 9, 3705], [11, 10, 3713], [11, 11, 3722], [11, 12, 3727], [11, 13, 3732],
                [11, 14, 3744], [11, 15, 3747], [11, 16, 3760], [11, 17, 3775], [11, 18, 3779], [11, 19, 3855],
                [11, 20, 3865], [11, 21, 3883], [11, 22, 3893], [11, 23, 3896], [11, 24, 3899], [11, 25, 3902],
                [11, 26, 3906], [11, 27, 3909], [11, 28, 3914], [11, 29, 3919], [11, 30, 3922], [11, 31, 3924],
                [11, 32, 3926], [11, 33, 3928], [11, 34, 3931], [11, 35, 3936], [11, 36, 3939], [11, 37, 3942],
                [11, 38, 3949], [11, 39, 3952, 3957], [12, 1, 3961], [12, 2, 3979], [12, 3, 3987], [12, 4, 4008],
                [12, 5, 4016], [12, 6, 4031], [12, 7, 4035], [12, 8, 4039], [12, 9, 4045], [12, 10, 4050],
                [12, 11, 4053], [12, 12, 4057], [12, 13, 4062], [12, 14, 4065], [12, 15, 4075], [12, 16, 4079],
                [12, 17, 4090], [12, 18, 4092], [12, 19, 4097], [12, 20, 4103], [12, 21, 4107], [12, 22, 4113],
                [12, 23, 4118], [12, 24, 4134], [12, 25, 4147], [12, 26, 4150], [12, 27, 4162], [12, 28, 4175],
                [12, 29, 4182], [12, 30, 4188], [12, 31, 4201], [12, 32, 4208], [12, 33, 4216], [12, 34, 4220],
                [12, 35, 4224], [12, 36, 4230, 4241]]

    randomExcerpt = randrange(0, len(excerpts) - 1)

    start_line = excerpts[randomExcerpt][2]

    if len(excerpts[randomExcerpt]) == 4:
        end_line = excerpts[randomExcerpt][3]
    else:
        end_line = excerpts[randomExcerpt + 1][2]
    text = []

    with open(os.path.join(os.path.dirname(__file__), txt), 'rt') as myfile:

        for position, line in enumerate(myfile, 1):

            if start_line <= position < end_line:
                text.append(line)

    textToImage(text, excerpts[randomExcerpt][0])
