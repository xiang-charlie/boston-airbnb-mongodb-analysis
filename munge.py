
import csv

def get_csv_data(filepath):
    csv_file = open(filepath, 'r')
    reader = csv.DictReader(csv_file)

    data_list = list(reader)
    
    return data_list


def remove_unnecessary_fields(data):
    new_data_list = []

    necessary_keys = ['id', 'name', 'price', 'neighborhood', 'host_name', 'host_is_superhost', 'beds', 'neighbourhood_group_cleansed', 'neighbourhood', 'neighbourhood_cleansed','city', 'review_scores_rating']

    for row in data:
        transfer_dict = {}
        for key, value in row.items():
            if key not in necessary_keys:
                pass
            else:
                transfer_dict[key] = value
        
        new_data_list.append(transfer_dict)
    
    return new_data_list


def save_csv_data(data, filepath):

    key_list = list(data[0].keys())

    with open(filepath, 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, key_list)
        dict_writer.writeheader()
        dict_writer.writerows(data)


def main():
    data = get_csv_data('data/listings.csv')
    data = remove_unnecessary_fields(data)
    save_csv_data(data, 'data/listings_clean.csv')


main()