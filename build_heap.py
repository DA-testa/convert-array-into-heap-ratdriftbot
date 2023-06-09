def build_heap(data):
    swaps = []
    n=len(data)

    for i in range(n // 2-1, -1, -1):
        maks_indeks =i
        kreisais_berns=2*i+1
        labais_berns = 2*i+2

        if kreisais_berns < n and data[kreisais_berns] < data[maks_indeks]:
            maks_indeks = kreisais_berns
        if labais_berns < n and data[labais_berns] < data[maks_indeks]:
            maks_indeks=labais_berns

        if i!=maks_indeks:
            swaps.append((i, maks_indeks))
            data[i], data[maks_indeks]=data[maks_indeks], data[i]

            while maks_indeks * 2+1 < n:
                i=maks_indeks
                maks_indeks= 2*i+1
                if maks_indeks+1 < n and data [maks_indeks+1] < data[maks_indeks]:
                    maks_indeks = maks_indeks+1

                if data[i]> data[maks_indeks]:
                    swaps.append((i, maks_indeks))
                    data[i], data[maks_indeks]=data[maks_indeks], data[i]
        else:
            j=maks_indeks
            while j*2 +1 < n:
                i=j
                j=2*i+1
                if j+1< n and data [j+1]<data[j]:
                    j=j+1

                if data[i] > data[j]:
                    swaps.append((i,j))
                    data[i], data[j] = data[j], data[i]
                    i=j
                else:
                    break

    return swaps


def main():
    text= input ("F or I:")
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in text:
        name=input()
        path='./tests/'
        file=path+name 
        if "a" not in name:
            try:
                with open(file) as f:
                    n=int(f.readline())
                    data =list(map(int, f.readline().split()))
            except Exception as e:
                print("Error", str(e))
                return

    assert len(data) == n

    swaps = build_heap(data)

    assert len(swaps)<5 * len(data)
    print(len(swaps))
    
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
