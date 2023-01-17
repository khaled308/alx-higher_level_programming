#!/usr/bin/python3
""" Find the peak in a list """


def find_peak(list_of_integers):
    """ Finding the peak """
    int_list = len(list_of_integers)
    if int_list is 0:
        return None
    peak = binary(list_of_integers, 0, int_list - 1)
    return list_of_integers[peak]


def binary(pivot, low, high):
    """ Searching for the peak using recursive binary search """
    if low >= high:
        return low
    middle = ((high - low) // 2) + low
    if pivot[middle] > pivot[middle + 1]:
        return binary(pivot, low, middle)
    else:
        return binary(pivot, middle + 1, high)
