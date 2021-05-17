import csv

def write_to_csv(experiment_list):
    with open("simulation/experiments/log.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(experiment_list)

def get_list(self, count, avg_health, avg_energy):
    experiment_list = list()
    experiment_list.append(self.day)
    experiment_list.append(self.hour)
    experiment_list.append(self.minute)

    experiment_list.append(count)
    experiment_list.append(avg_health)
    experiment_list.append(avg_energy)

    experiment_list.append(len(self.food.mushrooms))
    experiment_list.append(self.transit)
    experiment_list.append(self.storage)

    experiment_list.append(len(self.enemies))

    write_to_csv(experiment_list)
