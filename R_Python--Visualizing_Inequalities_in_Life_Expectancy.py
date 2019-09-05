### Cell 1: UN life expectancy data ###
# Import packages
import pandas as pd
import matplotlib.pyplot as plt

# Load the UN data set "UNdata.csv"
dataset = "Datacamp_Projects/UNdata.csv"

UN_df = pd.read_csv(dataset)
#print(UN_df.head(), UN_df.columns)


### Cell 2: Life expectancy of men vs. women by country ###
# Subset the dataframe to only include the average life expectancy data of men and women across countries
# for the period from 2000 to 2005.
sub_df = UN_df[UN_df["Year"] == "2000-2005"][["Country or Area", "Subgroup", "Value"]]
#print(sub_df.head(15))

pivoted_df = sub_df.pivot_table(index="Country or Area", values="Value", columns="Subgroup")
#print(pivoted_df.head())


### Cells 3, 4, 5: Visualize I, Reference lines I, add plot titles, axes labels and captions ###
# Name titles, subtitles and captions
title_str = "Life expectancy at birth by country"
subtitle_str = "(Average. Period: 2000-2005)"
caption_str = "Source: U.N. Statistics Division"

# Create figure and axes objects and label figure
fig, ax = plt.subplots(figsize=(5.5,5.5))

# Add background grid
ax.grid(b=True, which="major", axis="both", linestyle="-", linewidth=0.25)
ax.set_axisbelow(True)

# x and y positions determined by trial-and-error
ax.set_title(subtitle_str, fontsize=10, ha="center")
fig.suptitle(title_str, fontsize=18, y=0.965, ha="center")    
ax.set_xlabel("Males")
ax.set_ylabel("Females")
fig.text(x=0.65, y=0.015, s=caption_str, fontsize=8, ha="left")

# Create a scatterplot of life expectancy data and add reference line
ax.scatter(pivoted_df.Male, pivoted_df.Female, alpha = 0.55, color="yellowgreen")
ax.plot([35, 85], [35, 85], dashes=[2,2])

# Display the plot
#plt.show()


### Cell #6: Highlighting remarkable countries ###
# Subset the data to obtain countries with top 3 male and female life expectancies
top_male = (pivoted_df.Male - pivoted_df.Female).nlargest(3)
top_female = (pivoted_df.Female - pivoted_df.Male).nlargest(3)

top_male_columns = top_male.index.tolist()
top_female_columns = top_female.index.tolist()
# print(pivoted_df.loc[top_male_columns], pivoted_df.loc[top_female_columns])

# Annotate the data
for country in top_female_columns:
    y, x = pivoted_df.loc[country]
    ax.text(x, y, country, ha="right", va="top", color="midnightblue")

for cntry in top_male_columns:
    y, x = pivoted_df.loc[cntry]
    ax.text(x, y, cntry, ha="left", va="bottom", color="maroon")
    

# Display the annotated plot
#plt.show()


### Cell #7: How has life expectancy by gender evolved?
# Subset the dataframe to only include the average life expectancy data of men and women across countries
# for the periods from 1985 to 1990 and from 2000 to 2005.
sub2_df = UN_df[(UN_df["Year"] == "1985-1990") | (UN_df["Year"] == "2000-2005")]

pivoted2_df = sub2_df.pivot_table(index="Country or Area", values="Value", columns=["Subgroup", "Year"])
#print(pivoted2_df.head(10))

# Determine the difference in life expectancy in these two periods
female_diff = pivoted2_df["Female"]["2000-2005"] - pivoted2_df["Female"]["1985-1990"]
male_diff = pivoted2_df["Male"]["2000-2005"] - pivoted2_df["Male"]["1985-1990"]
#print(female_diff.head(), male_diff.head())


### Cell #8, #9: Visualize I, Reference lines I, add plot titles, axes labels and captions ###
# Name titles, subtitles and captions 
title_string = "Life expectancy at birth by country"
subtitle_string = "(Average. Difference between periods: 1985-1990 and 2000-2005)"
caption_string = "Source: U.N. Statistics Division"

# Create figure and axes objects and label figure
fig2, ax2 = plt.subplots(figsize=(5.75,5.75))

ax2.set_title(subtitle_string, fontsize=10, ha="center")
fig2.suptitle(title_string, fontsize=18, y=0.965, ha="center")    
ax2.set_xlabel("Males")
ax2.set_ylabel("Females")
fig2.text(x=0.65, y=0.015, s=caption_string, fontsize=8, ha="left")

# Add background grid
ax2.grid(b=True, which="major", axis="both", linestyle="-", linewidth=0.25)
ax2.set_axisbelow(True)

# Create a scatterplot of life expectancy data and add reference lines
ax2.scatter(male_diff, female_diff, alpha = 0.55, color="darkmagenta")
ax2.plot([-25, 25], [-25, 25], dashes=[2,2], color="darkslategray")

#hx1, hx2, hy1, hy2 = -25, 25, 0, 0
#ax2.plot((hx1, hx2), (hy1, hy2), dashes=[2,2], color="darkslategray")
#vx1, vx2, vy1, vy2 = 0, 0, -25, 25
#ax2.plot((vx1, vx2), (vy1, vy2), dashes=[2,2], color="darkslategray")

# Simpler to use below to add reference lines along the origin
ax2.axhline(y=0, dashes=[2,2], color="darkslategray")
ax2.axvline(x=0, dashes=[2,2], color="darkslategray")

# Display the plot
# plt.show()


### Cell #10: Highlighting remarkable countries II ###
# Subset the data to obtain countries with top 3 male and female life expectancy changes between periods
top_3 = (male_diff + female_diff).nlargest(3).index.tolist()
bottom_3 = (male_diff + female_diff).nsmallest(3).index.tolist()
#print(top_3, bottom_3)

# Annotate the second dataset
for country in top_3:
    x, y = male_diff[country], female_diff[country]
    ax2.text(x, y, country, ha="right", va="top", color="darkgoldenrod")

for country in bottom_3:
    x, y = male_diff[country], female_diff[country]
    ax2.text(x, y, country, ha="left", va="bottom", color="darkred")
    

# Display the annotated plot
plt.show()
