# Project Name
**Edible Mushroom Classifier**

# Team members
- Alexis Erne
- Muhammad Azeem Arshad
- Maxime Kilian Pasquier


# Table of Contents

[Short summary](#short-summary)
[Introduction](#introduction)
[Methodology](#methodology)
[Results](#results)
[Summary and outlook](#summary-and-outlook)
[Conclusion](#conclusion)


## 1. Short summary

The goal of our project is to classify different varieties of edible / none-edible mushrooms from their deceptive look-alikes. The task of classifying mushroom can be very challenging due to the fungal diversity as there are millions of mushroom species. Therefore, our goal is to focus on the most cultivated mushrooms by people in Switzerland. In fact, we gathered in total 7 species of mushroom and their corresponding fake friend (non-edible), to help people, find edible mushrooms and not misidentify edible mushroom from toxic ones. 


## 2. Introduction

In Switzerland, there are about 5’000 different species of mushrooms which can be picked from summer until the first autumn frost [0]. Out of those thousand species, three species are the most popular and the most liked by people, which are: the dead trumpet, the boletus, and the morel. As most people look for specific species, we have decided to create a Machine Learning algorithm which could help people pick 7 of the most liked mushroom types in Switzerland. Mushroom classification using Machine Learning is a well-known problem. Machine Learning models around mushroom classification has developed recently with the availability of public datasets of mushroom pictures. In fact, mobile applications such as Picture mushroom [1] uses machine learning models to classify edible mushrooms. However, these machine learning models remain a challenge. In fact, the diversity of species is extremely large and misidentifying a mushroom could have severe consequences. This is why we have chosen to work on a smaller set of 7 specific species, which would enable us to have more relevant and precise results. This project is driven by the need to address the significant risks associated with misidentifying mushrooms, as consuming toxic varieties can lead to severe illness or even be fatal. By accurately classifying mushrooms, the model aims to help mushroom enthusiast and individuals to have access to an informed decision-making algorithm regarding mushroom consumption and safety.


## 3. Methodology

To do so, we have decided to use the citizen science website, which is scientific research conducted with the participation of the public. We have created a project on Project Builder which allows to see a picture, in our case the picture a mushroom, and choose if the mushroom is edible or not. In fact, this crowdsourcing platform would enable us to collect the necessary data to train the machine learning models we are going to build. More precisely, to make the data collection more accessible to the largest range of user, we have decided to create a tutorial in order learn how to detect nonedible mushrooms. With this clear information, participants would be able to classify mushrooms and label our dataset. The individuals will simply have to answer a 3-choice question: “is this mushroom classified as edible or non-edible” with the response options: 1. Edible, 2. Non-edible and 3. I don’t know. 
In this project, crowdsourcing can be utilized to gather the necessary data to train our machine learning models. By using the collective knowledge and contribution of a crowd, which can be mushroom enthusiasts, culinary professionals or even individuals, the project can benefit from the expertise and experience of individuals. Using the citizen-science website and more precisely the project builder to create the platform for data collection is a direct link to crowdsourcing. The use of crowdsourcing allows for a larger and more diverse dataset to be created, covering the most images to be classified between edible or not. This will directly influence the training of the model and as a result, the overall performance of the model. The active involvement of the crowd will also help awareness about mushroom safety. In fact, it encourages people to participate and collaborate in identifying edible mushrooms and avoiding potential health risks.  

<img width="928" alt="Screenshot 2023-05-23 at 13 03 48" src="https://github.com/azeemarshad97/CSAI-project/assets/43532600/497a817a-cc24-46a4-9b2d-5005b2ad0f31">
<img width="924" alt="Screenshot 2023-05-23 at 13 04 06" src="https://github.com/azeemarshad97/CSAI-project/assets/43532600/bea08e58-3a77-4e7d-8ffc-b2d6cfae2c44">


## 4. Results

To replicate the AICrowd website, we decided to create a mockup, where we could insert all the necessary information concerning our project. The website can be found under this link: https://azeemarshad97.github.io/CSAI-project/.  More precisely, we introduced our project, explained all the information concerning our dataset (each feature and labels), we also precises the different tasks that can be performed for our project, we mentioned the prices and the contacts to the administrators of the project. We also added how the data we collected and all the information concerning how to differentiate edible from non-edible mushrooms. 


## 5. Summary and outlook

This project could be further developed with more data. In fact, collecting could enable to train the model even more and test the model. This model could then be deployed on a mobile application and people collecting mushroom could use it in real-life to see if their mushrooms are edible or not. 

<img width="919" alt="Screenshot 2023-05-23 at 13 05 07" src="https://github.com/azeemarshad97/CSAI-project/assets/43532600/b33d5975-b896-4519-b9ae-63ff9e14f71c">

## 6. Conclusion 

The goal of this project was to involve the crowd in the data collection for the creation of a machine learning model to predict if mushrooms are edible or not. We focused on a subset of specific species from the 5’000 species of mushrooms that could be found in Switzerland. In fact, we filtered the most liked and eaten mushrooms that were collected by individuals and mushroom enthusiasts. Involving the crowd and collecting the data enabled us to have a large number images classified. In future steps this will allow us to create a classification model and to export it to be used in a mobile application to allow individuals to use it. Finally, with the use of the different tools: citizen-science / project builder (data collection), AIShwrooms (replicated AICrowd website) and SdgInnProgress (documentation), this allowed us to have an overview of how a machine learning project could be done. In fact, this allowed us to collect data, understand how to publish a machine learning project to involve the crowd and document the entire process (explaining wins and challenges along the way). 


Literature References
[0] https://hausinfo.ch/fr/jardin-balcon/verdir-balcon-jardin/legumes-fruits/cueillette-champignons.html#:~:text=En%20Suisse%2C%20la%20cueillette%20des,par%20personne%20et%20par%20jour. 
[1] https://play.google.com/store/apps/details?id=com.glority.picturemushroom&hl=en_US


