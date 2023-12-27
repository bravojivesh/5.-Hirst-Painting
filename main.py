###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    rgb_color1= color.rgb.r #red
    rgb_color2= color.rgb.g #green
    rgb_color3= color.rgb.b #blue
    rgb_colors.append((rgb_color1,rgb_color2, rgb_color3)) #note: this will first create a tuple. And then a list of
    #tuples.
    # rgb_colors.append(color.rgb)

print(rgb_colors)
print (type((rgb_colors)[0])) #to check I created the tuple properly

