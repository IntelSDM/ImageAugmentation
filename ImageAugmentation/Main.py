from DataManager import LoadInputs
from DataManager import Files
from AugmentationManager import MutateImages
LoadInputs()
MutateImages(Files)
print("Finished")
