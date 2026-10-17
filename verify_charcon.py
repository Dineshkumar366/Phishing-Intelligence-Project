def CharConRate(url):
    rate = 0
    ln = len(url)
    chC, nmC, spC = 0, 0, 0
    maxCh, maxNm, MaxSp = 0, 0, 0

    for i in range(0, ln):
        ch = url[i]

        if ch.isalpha():
            chC = chC + 1

            if nmC > 0:
                if maxNm < nmC:
                    maxNm = nmC
                    nmC = 0
            elif spC > 0:
                if MaxSp < spC:
                    MaxSp = spC
                    spC = 0

            nmC, spC = 0, 0

        elif ch.isdigit():
            nmC = nmC + 1

            if chC > 0:
                if maxCh < chC:
                    maxCh = chC
                    chC = 0
            elif spC > 0:
                if MaxSp < spC:
                    MaxSp = spC
                    spC = 0

            chC, spC = 0, 0

        else:
            spC = spC + 1

            if nmC > 0:
                if maxNm < nmC:
                    maxNm = nmC
                    nmC = 0
            elif chC > 0:
                if maxCh < chC:
                    maxCh = chC
                    chC = 0

            nmC, chC = 0, 0

    if maxCh < chC:
        maxCh = chC

    if maxNm < nmC:
        maxNm = nmC

    if MaxSp < spC:
        MaxSp = spC

    return (maxCh + maxNm + MaxSp) / ln


domain = "paypa1-login-security"

result = CharConRate(domain)

print("Domain:", domain)
print("CharContinuationRate:", result)