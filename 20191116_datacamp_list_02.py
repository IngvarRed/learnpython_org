# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

print(areas, "\n", areas_1, "\n", areas_2)

del(areas[10]); del(areas[11])
# del(areas[10:11])
# del(areas[-4:-2])
# del(areas[-3]); del(areas[-4])

print(areas, "\n", areas_1, "\n", areas_2)