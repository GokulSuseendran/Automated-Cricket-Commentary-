#!pip install pillow
#import Pillow
from PIL import ImageTk, Image
#!pip install ImageHash
import  imagehash
from PIL import Image
import imagehash
import os
import numpy as np


class DuplicateRemover:
    def __init__(self,dirname,hash_size = 8):
        self.dirname = dirname
        self.hash_size = hash_size
        
    def find_duplicates(self):
        """
        Find and Delete Duplicates
        """
        
        fnames = os.listdir(self.dirname)
        hashes = {}
        duplicates = []
        print("Finding Duplicates Now!\n")
        for image in fnames:
            with Image.open(os.path.join(self.dirname,image)) as img:
                temp_hash = imagehash.average_hash(img, self.hash_size)
                if temp_hash in hashes:
                    print("Duplicate {} \nfound for Image {}!\n".format(image,hashes[temp_hash]))
                    duplicates.append(image)
                else:
                    hashes[temp_hash] = image
                   
        if len(duplicates) != 0:
            a = input("Do you want to delete these {} Images? Press Y or N:  ".format(len(duplicates)))
            space_saved = 0
            if(a.strip().lower() == "y"):
                for duplicate in duplicates:
                    space_saved += os.path.getsize(os.path.join(self.dirname,duplicate))
                    
                    os.remove(os.path.join(self.dirname,duplicate))
                    print("{} Deleted Succesfully!".format(duplicate))
    
                print("\n\nYou saved {} mb of Space!".format(round(space_saved/1000000),2))
            else:
                print("Thank you for Using Duplicate Remover")
        else:
            print("No Duplicates Found :(")
        return duplicates
        
            
            
    def find_similar(self,name,directory,similarity=70):
        fnames = os.listdir(self.dirname)
        threshold = 1 - similarity/100
        diff_limit = int(threshold*(self.hash_size**2))
        location = directory + "//" + name 
        
        with Image.open(location) as img:
            hash1 = imagehash.average_hash(img, self.hash_size).hash
        
        print("Finding Similar Images to {} Now!\n".format(location))
        for image in fnames:
            with Image.open(os.path.join(self.dirname,image)) as img:
                hash2 = imagehash.average_hash(img, self.hash_size).hash
                
                if np.count_nonzero(hash1 != hash2) <= diff_limit:
                    print("{} image found {}% similar to {}".format(image,similarity,location))
                    if image != name:
                        return name
                    	#name1 = directory + "//" + image
                    	#os.remove(name1)

    def similarity_between(self,directory,img1,img2,similarity = 90):
        fnames = os.listdir(self.dirname)
        threshold = 1 - similarity/100
        diff_limit = int(threshold*(self.hash_size**2))
        location1 = directory + "//" + img1
        location2 = directory + "//" + img2
        
        with Image.open(location1) as img:
            hash1 = imagehash.average_hash(img, self.hash_size).hash
        with Image.open(location2) as img:
            hash2 = imagehash.average_hash(img, self.hash_size).hash
        if np.count_nonzero(hash1 != hash2) <= diff_limit:
                    #print("{} image found {}% similar to {}".format(img2,similarity,img1))
                    return 1
        else:
          #print("Images Not similar")
                    return 0
                    
        
        
        #print("Finding Similar Images to {} Now!\n".format(location))
        #for image in fnames:
         #   with Image.open(os.path.join(self.dirname,image)) as img:
          #      hash2 = imagehash.average_hash(img, self.hash_size).hash
           #     
            #    if np.count_nonzero(hash1 != hash2) <= diff_limit:
             #       print("{} image found {}% similar to {}".format(image,similarity,location))
              #      if image != name:
               #         return name

#from DuplicateRemover import DuplicateRemover

#dirname = "/content/drive/MyDrive/For Video captioning/Data"

# Remove Duplicates
#dr = DuplicateRemover(dirname)
#dr.find_duplicates()

# Find Similar Images
#dr.find_similar("104.jpg","/content/drive/MyDrive/For Video captioning/data")
#Check similarity between two images
#directory = "/content/drive/MyDrive/For Video captioning/Data"
#img1 = '20.jpg'
#img2 = '21.jpg'
#dr.similarity_between(directory,img1,img2)