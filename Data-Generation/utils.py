from datetime import datetime
import pytz

def non_zero_yuyupos(array):
    """
    Find positions of non-zero elements in an array.
    
    Parameters:
    array (array-like): Input array.
    
    Returns:
    list: Positions of non-zero elements.
    """
    return [i for i in range(len(array)) if array[i] != 0]

def time_hour(timestamps):
    """
    Convert timestamps to a specific timezone and format.
    
    Parameters:
    timestamps (array-like): Input timestamps.
    
    Returns:
    list: Formatted timestamps.
    """
    time_vct = []
    for timestamp in timestamps:
        dt_obj = datetime.fromtimestamp(timestamp[0])
        utc_timezone = pytz.timezone('UTC')
        utc_aware_datetime = utc_timezone.localize(dt_obj)
        quebec_timezone = pytz.timezone('America/Montreal')
        quebec_aware_datetime = utc_aware_datetime.astimezone(quebec_timezone)
        formatted_date = quebec_aware_datetime.strftime("%Y-%m-%d %H:%M:%S")
        time_vct.append(formatted_date)
    return time_vct

def find_first(time_vct, time_p):
    """
    Find the first occurrence of each timestamp in a list.
    
    Parameters:
    time_vct (list): List of formatted timestamps.
    time_p (list): List of search timestamps.
    
    Returns:
    list: Indices of the first occurrences.
    """
    first_occ = []
    for search_string in time_p:
        for index, string in enumerate(time_vct):
            if string == search_string:
                first_occ.append(index)
                break
    return first_occ