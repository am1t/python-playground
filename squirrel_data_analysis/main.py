import pandas

data = pandas.read_csv("squirrel_data.csv")
output_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [],
}

for color in output_dict["Fur Color"]:
    output_dict["Count"].append(len(data[data["Primary Fur Color"] == color]["Primary Fur Color"]))

squirrel_result_dataframe = pandas.DataFrame(output_dict)
squirrel_result_dataframe.to_csv("squirrel_count.csv")