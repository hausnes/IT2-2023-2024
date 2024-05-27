import json
from datetime import datetime

class Collectible:
    def __init__(self, price, purchase_date, current_value, category, franchise):
        self.price = price
        self.purchase_date = purchase_date
        self.current_value = current_value
        self.category = category
        self.franchise = franchise

    def potential_profit(self):
        return self.current_value - self.price
    
class Movie(Collectible):
    def __init__(self, price, purchase_date, current_value, category, franchise, runtime, release_year):
        super().__init__(price, purchase_date, current_value, category, franchise)
        self.runtime = runtime
        self.release_year = release_year

class Collector:
    def __init__(self):
        self.collection = []

    def add_collectible(self, collectible):
        self.collection.append(collectible)

    def remove_collectible(self, collectible):
        self.collection.remove(collectible)

    def filter_by_category(self, category):
        return [c for c in self.collection if c.category == category]

    def filter_by_franchise(self, franchise):
        return [c for c in self.collection if c.franchise == franchise]

def save_to_file(collector, filename):
    with open(filename, 'w') as f:
        json.dump([{'class': type(c).__name__, 'attributes': {**c.__dict__, 'purchase_date': c.purchase_date.isoformat()}} for c in collector.collection], f)

def load_from_file(filename):
    collector = Collector()
    with open(filename, 'r') as f:
        for c in json.load(f):
            c['attributes']['purchase_date'] = datetime.fromisoformat(c['attributes']['purchase_date'])
            if c['class'] == 'Collectible':
                collector.collection.append(Collectible(**c['attributes']))
            elif c['class'] == 'Movie':
                collector.collection.append(Movie(**c['attributes']))
    return collector

# For testing av oppretting
# collector = Collector()
# collector.add_collectible(Collectible(100, datetime.now(), 200, 'Book', 'Harry Potter'))
# collector.add_collectible(Movie(200, datetime.now(), 400, 'Movie', 'Harry Potter', 120, 2001))
# save_to_file(collector, 'collectibles.json')

# For testing av lasting
collector = load_from_file('collectibles.json')

for i, collectible in enumerate(collector.collection):
    print(f"Collectible {i+1}:")
    for key, value in collectible.__dict__.items():
        print(f"  {key}: {value}")
    print()

# Unittesting
import unittest

class TestCollector(unittest.TestCase):
    def setUp(self):
        self.collector = Collector()
        self.collectible = Collectible(100, datetime.now(), 200, 'Book', 'Harry Potter')
        self.movie = Movie(200, datetime.now(), 400, 'Movie', 'Harry Potter', 120, 2001)

    def test_add_collectible(self):
        self.collector.add_collectible(self.collectible)
        self.assertIn(self.collectible, self.collector.collection)

    def test_remove_collectible(self):
        self.collector.add_collectible(self.collectible)
        self.collector.remove_collectible(self.collectible)
        self.assertNotIn(self.collectible, self.collector.collection)

    def test_filter_by_category(self):
        self.collector.add_collectible(self.collectible)
        self.collector.add_collectible(self.movie)
        result = self.collector.filter_by_category('Book')
        self.assertEqual(result, [self.collectible])

    def test_filter_by_franchise(self):
        self.collector.add_collectible(self.collectible)
        self.collector.add_collectible(self.movie)
        result = self.collector.filter_by_franchise('Harry Potter')
        self.assertEqual(result, [self.collectible, self.movie])

    def test_save_and_load(self):
        self.collector.add_collectible(self.collectible)
        self.collector.add_collectible(self.movie)
        save_to_file(self.collector, 'collectibles.json')
        loaded_collector = load_from_file('collectibles.json')
        for original, loaded in zip(self.collector.collection, loaded_collector.collection):
            self.assertEqual(original.__dict__, loaded.__dict__)

if __name__ == '__main__':
    unittest.main()