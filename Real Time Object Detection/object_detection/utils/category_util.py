
import csv

import tensorflow as tf


def load_categories_from_csv_file(csv_path):
  """Loads categories from a csv file.

  The CSV file should have one comma delimited numeric category id and string
  category name pair per line. For example:

  0,"cat"
  1,"dog"
  2,"bird"
  ...

  Args:
    csv_path: Path to the csv file to be parsed into categories.
  Returns:
    categories: A list of dictionaries representing all possible categories.
                The categories will contain an integer 'id' field and a string
                'name' field.
  Raises:
    ValueError: If the csv file is incorrectly formatted.
  """
  categories = []

  with tf.gfile.Open(csv_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
      if not row:
        continue

      if len(row) != 2:
        raise ValueError('Expected 2 fields per row in csv: %s' % ','.join(row))

      category_id = int(row[0])
      category_name = row[1]
      categories.append({'id': category_id, 'name': category_name})

  return categories


def save_categories_to_csv_file(categories, csv_path):
  """Saves categories to a csv file.

  Args:
    categories: A list of dictionaries representing categories to save to file.
                Each category must contain an 'id' and 'name' field.
    csv_path: Path to the csv file to be parsed into categories.
  """
  categories.sort(key=lambda x: x['id'])
  with tf.gfile.Open(csv_path, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    for category in categories:
      writer.writerow([category['id'], category['name']])
