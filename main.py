from MyBigInt import MyBigInt
import secrets


def monobit_test(sequence):
    one_count = 0
    for bit in sequence:
        if bit == "1":
            one_count += 1
    if 10346 >= one_count >= 9654:
        return True
    return False


def maxlength_series_test(sequence):
    series_bit = sequence[0]
    series_count = 0
    for bit in sequence:
        if bit == series_bit:
            series_count += 1
            if series_count > 36:
                return False
        else:
            series_bit = bit
            series_count = 1
    return True


def poker_test(sequence):
    m = 4
    k = len(sequence) // m
    n = [0] * 16
    for bit1, bit2, bit3, bit4 in zip(sequence[::4], sequence[1::4], sequence[2::4], sequence[3::4]):
        i = int(bit1) + int(bit2) * 2 + int(bit3) * 4 + int(bit4) * 8
        n[i] += 1
    n_square_sum = 0
    for n_i in n:
        n_square_sum += n_i * n_i
    x3 = 16 / k * n_square_sum - k
    return 1.03 <= x3 <= 57.4


def series_length_test(sequence):
    series_count = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    series_bit = sequence[0]
    series_length = 0
    for bit in sequence:
        if bit == series_bit:
            series_length += 1
        else:
            if series_length >= 6:
                series_count[int(series_bit)][5] += 1
            else:
                series_count[int(series_bit)][series_length-1] += 1
            series_bit = bit
            series_length = 1
    series_count[int(series_bit)][series_length-1] += 1
    if series_count[0][0] < 2267 or series_count[0][0] > 2733 or series_count[1][0] < 2267 or series_count[1][0] > 2733:
        return False
    if series_count[0][1] < 1079 or series_count[0][1] > 1421 or series_count[1][1] < 1079 or series_count[1][1] > 1421:
        return False
    if series_count[0][2] < 502 or series_count[0][2] > 748 or series_count[1][2] < 502 or series_count[1][2] > 748:
        return False
    if series_count[0][3] < 223 or series_count[0][3] > 402 or series_count[1][3] < 223 or series_count[1][3] > 402:
        return False
    if series_count[0][4] < 90 or series_count[0][4] > 223 or series_count[1][4] < 90 or series_count[1][4] > 223:
        return False
    if series_count[0][5] < 90 or series_count[0][5] > 223 or series_count[1][5] < 90 or series_count[1][5] > 223:
        return False
    return True


if __name__ == '__main__':
    random_hex = secrets.token_hex(2500)
    b = MyBigInt()
    b.setHex(random_hex)
    sequence = b.getBin()
    print(monobit_test(sequence))
    print(maxlength_series_test(sequence))
    print(poker_test(sequence))
    print(series_length_test(sequence))

