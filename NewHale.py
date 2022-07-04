# cluster = [[0 for x in range(n)] for y in range(n)]
# for c in range(n):
for k in range(n):
    cluster[k][c] = 0  # alle Werte werden mit 0 initialisiert
    if k in (2, 3) and c in (2, 3):
        cluster[k][c] = cluster[c][k] = -K
    elif k in (6, 7) and c in (6, 7):
        cluster[k][c] = cluster[c][k] = -K
    elif k in (7, 8) and c in (7, 8):
        cluster[k][c] = cluster[c][k] = -K
    elif k in (8, 9) and c in (8, 9):
        cluster[k][c] = cluster[c][k] = -K
    elif k in (9, 10) and c in (9, 10):
        cluster[k][c] = cluster[c][k] = -K
    elif k in (10, 11) and c in (10, 11):
        cluster[k][c] = cluster[c][k] = -K
    elif k in (11, 12) and c in (11, 12):
        cluster[k][c] = cluster[c][k] = -K
    elif k in (15, 16) and c in (15, 16):
        cluster[k][c] = cluster[c][k] = -K
    elif k in (17, 20) and c in (17, 20):
        cluster[k][c] = cluster[c][k] = -K
    elif k in (18, 19) and c in (18, 19):
        cluster[k][c] = cluster[c][k] = -K
    elif k in (21, 22) and c in (21, 22):
        cluster[k][c] = cluster[c][k] = -K
    elif k in (22, 23) and c in (22, 23):
        cluster[k][c] = cluster[c][k] = -K
    """
    elif k in (24, 25) and l in (24, 25):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (25, 26) and l in (25, 26):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (26, 27) and l in (26, 27):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (27, 28) and l in (27, 28):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (28, 29) and l in (28, 29):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (42, 43) and l in (42, 43):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (43, 44) and l in (43, 44):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (44, 45) and l in (44, 45):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (45, 46) and l in (45, 46):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (46, 47) and l in (46, 47):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (47, 48) and l in (47, 48):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (18, 19) and l in (18, 19):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (174, 175) and l in (174, 175):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (81, 82) and l in (81, 82):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (116, 119) and l in (116, 119):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (119, 121) and l in (119, 121):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (148, 176) and l in (148, 176):
        cluster[k][l] = cluster[l][k] = -K
    # elif k in (82, 83) and l in (82, 83):
    #   cluster[k][l] = cluster[l][k] = -K
    # elif k in (83, 171) and l in (83, 171):
    #   cluster[k][l] = cluster[l][k] = -K
    # elif k in (37, 133) and l in (37, 133):
    #   cluster[k][l] = cluster[l][k] = -K
    # elif k in (135, 136) and l in (135, 136):
    #   cluster[k][l] = cluster[l][k] = -K
    # elif k in (135, 24) and l in (135, 24):
    #   cluster[k][l] = cluster[l][k] = -K


    elif k in (117, 118) and l in (117, 118):
        cluster[k][l] = cluster[l][k] = -K

    elif k in (10, 142) and l in (10, 142):
        cluster[k][l] = cluster[l][k] = -K



    elif k in (49, 50) and l in (49, 50):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (50, 51) and l in (50, 51):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (51, 52) and l in (51, 52):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (52, 53) and l in (52, 53):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (53, 54) and l in (53, 54):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (54, 55) and l in (54, 55):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (55, 56) and l in (55, 56):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (56, 57) and l in (56, 57):
        cluster[k][l] = cluster[l][k] = -K

    elif k in (58, 59) and l in (58, 59):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (59, 60) and l in (59, 60):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (60, 61) and l in (60, 61):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (61, 62) and l in (61, 62):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (62, 63) and l in (62, 63):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (63, 64) and l in (63, 64):
        cluster[k][l] = cluster[l][k] = -K

    elif k in (65, 66) and l in (65, 66):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (66, 67) and l in (66, 67):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (67, 68) and l in (67, 68):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (68, 69) and l in (68, 69):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (69, 70) and l in (69, 70):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (70, 71) and l in (70, 71):
        cluster[k][l] = cluster[l][k] = -K

    elif k in (72, 73) and l in (72, 73):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (73, 74) and l in (73, 74):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (74, 75) and l in (74, 75):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (75, 76) and l in (75, 76):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (76, 77) and l in (76, 77):
        cluster[k][l] = cluster[l][k] = -K

    elif k in (78, 79) and l in (78, 79):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (79, 80) and l in (79, 80):
        cluster[k][l] = cluster[l][k] = -K

    elif k in (85, 86) and l in (85, 86):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (86, 87) and l in (86, 87):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (87, 88) and l in (87, 88):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (88, 89) and l in (88, 89):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (89, 90) and l in (89, 90):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (90, 91) and l in (90, 91):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (91, 92) and l in (91, 92):
        cluster[k][l] = cluster[l][k] = -K

    elif k in (93, 94) and l in (93, 94):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (94, 95) and l in (94, 95):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (95, 96) and l in (95, 96):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (96, 97) and l in (96, 97):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (97, 98) and l in (97, 98):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (98, 99) and l in (98, 99):
        cluster[k][l] = cluster[l][k] = -K

    elif k in (100, 101) and l in (100, 101):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (101, 102) and l in (101, 102):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (102, 103) and l in (102, 103):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (103, 104) and l in (103, 104):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (104, 105) and l in (104, 105):
        cluster[k][l] = cluster[l][k] = -K

    elif k in (106, 107) and l in (106, 107):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (107, 108) and l in (107, 108):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (108, 109) and l in (108, 109):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (109, 110) and l in (109, 110):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (110, 111) and l in (110, 111):
        cluster[k][l] = cluster[l][k] = -K

    elif k in (121, 122) and l in (121, 122):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (122, 123) and l in (122, 123):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (123, 124) and l in (123, 124):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (124, 125) and l in (124, 125):
        cluster[k][l] = cluster[l][k] = -K

    elif k in (127, 128) and l in (127, 128):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (132, 150) and l in (132, 150):
        cluster[k][l] = cluster[l][k] = -K

    elif k in (137, 138) and l in (137, 138):
        cluster[k][l] = cluster[l][k] = -K

    elif k in (139, 140) and l in (139, 140):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (140, 141) and l in (140, 141):
        cluster[k][l] = cluster[l][k] = -K

    elif k in (143, 169) and l in (143, 169):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (144, 145) and l in (144, 145):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (146, 147) and l in (146, 147):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (152, 153) and l in (152, 153):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (154, 155) and l in (154, 155):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (156, 157) and l in (156, 157):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (161, 162) and l in (161, 162):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (166, 167) and l in (166, 167):
        cluster[k][l] = cluster[l][k] = -K
    elif k in (172, 173) and l in (172, 173):
        cluster[k][l] = cluster[l][k] = -K
"""