import gdown
import datetime

print("start",datetime.datetime.now())

x = "https://drive.google.com/file/d/14S0n5NAEAZMoyWIGeDaUAzUhhHTfj4pH/view?usp=sharing"
y = "https://drive.google.com/file/d/12xxJbZ_EUOsUt6n75JwOB5rXFUxoneLH/view?usp=sharing"
trained_knn_model = "https://drive.google.com/file/d/1AESNJcw69dmIL6ya8eXsVSSpWj5zQbMr/view?usp=sharing"

gdown.download(x, "X.sav", quiet=False)
gdown.download(y, "Y.sav", quiet=False)
gdown.download(trained_knn_model, "trained_knn_model.clf", quiet=False)
print("end",datetime.datetime.now())

# 19:42:55.857939
# 19:42:58.455556