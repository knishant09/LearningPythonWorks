import os


def grid_func(list_str, list_search):
    num_row = len(list_str)
    num_col = num_row
    for search_word in list_search:
        i = 0
        j = 0
        c = search_word[0]
        output = False
        #for c in search_word:
        while True:
            if (c == list_str[i][j]):
                output = remain_search(i, j, search_word[1:], num_row, num_col, list_str)
                if output:
                    search_new =''.join(search_word)
                    print(search_new,' ',i,' ',j)
                    break

            j += 1

            if j == num_col:
               i += 1
               j = 0

            if  i == num_row:
               break
        print(output)
        if not output:
            search_new = ''.join(search_word)
            print(search_new, ' ', -1, ' ', -1)


def remain_search(i, j, search_word, num_row, num_col, list_str):
    if len(search_word) == 0:
        return True
    c = search_word[0]
    if i == 0 and j == 0:  ## Top Left corner
        if list_str[i][j+1] == c:
            rem_len = len(search_word[1:])
            if rem_len == 0:
                return True
            if rem_len <= num_col - j + 1:

                if (search_word[1:] > list_str[i][j+1+rem_len]) - (search_word[1:] < list_str[i][j+1+rem_len]):
                    return True
                else:
                    return False
        else:

            if list_str[i+1][j] == c:
                rem_len = len(search_word[1:])
                row_index = i + 1 + 1
                w_index = 1
                while row_index < num_row and rem_len > 0:
                    if search_word[w_index] == list_str[row_index][0]:
                        w_index += 1
                        row_index += 1
                        rem_len -= 1

                    else:
                        return False

                if rem_len == 0:
                    return True

    else:
        return False





def main():

    list_str = []
    while True:
        str = input().strip()

        if len(str) != 0:
            list_str.append(list(str))

        else:
            break


    list_search = []
    while True:
        str = input().strip()

        if len(str) != 0:

            list_search.append(list(str))
        else:
            break

    grid_func(list_str, list_search)



if __name__ == "__main__":
   main()


