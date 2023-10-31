#! /usr/bin/python3

intList = list[int]


def calculate_mean(temp_list: intList, num_temps: int) -> int:
    return (int(sum(temp_list) / num_temps))


def main():
    num_temps = int(input())
    str_temp_list = input().split()
    temp_list = [int(temp) for temp in str_temp_list]
    print(calculate_mean(temp_list, num_temps))


if __name__ == "__main__":
    main()
