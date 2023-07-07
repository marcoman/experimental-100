# Introduction

In this exercise, we use contemporary technologies to log our workouts.


#  Resources

## Google Sheet

I have a copy of this Spreadsheet : https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit?usp=sharing

## Nutritionix API website:

https://developer.nutritionix.com/signup


Test the experience with this API:
https://www.nutritionix.com/natural-demo/


For reference, this is what the response for a nutrition inquiry looks like:

```json
{
   "foods":[
      {
         "food_name":"kohlrabi",
         "brand_name":null,
         "serving_qty":1,
         "serving_unit":"cup",
         "serving_weight_grams":135,
         "nf_calories":36.45,
         "nf_total_fat":0.14,
         "nf_saturated_fat":0.02,
         "nf_cholesterol":0,
         "nf_sodium":27,
         "nf_total_carbohydrate":8.37,
         "nf_dietary_fiber":4.86,
         "nf_sugars":3.51,
         "nf_protein":2.3,
         "nf_potassium":472.5,
         "nf_p":62.1,
         "full_nutrients":[
            {
               "attr_id":203,
               "value":2.295
            },
            {
               "attr_id":"MANY ARE TRUNCATED",
               "value":0.135
            },
         ],
         "nix_brand_name":null,
         "nix_brand_id":null,
         "nix_item_name":null,
         "nix_item_id":null,
         "upc":null,
         "consumed_at":"2023-07-06T19:43:57+00:00",
         "metadata":{
            "is_raw_food":false
         },
         "source":1,
         "ndb_no":11241,
         "tags":{
            "item":"kohlrabi",
            "measure":null,
            "quantity":"1.0",
            "food_group":null,
            "tag_id":4333
         },
         "alt_measures":[
            {
               "serving_weight":16,
               "measure":"slice",
               "seq":2,
               "qty":1
            },
         ],
         "lat":null,
         "lng":null,
         "meal_type":3,
         "photo":{
            "thumb":"https://nix-tag-images.s3.amazonaws.com/4333_thumb.jpg",
            "highres":"https://nix-tag-images.s3.amazonaws.com/4333_highres.jpg",
            "is_user_uploaded":false
         },
         "sub_recipe":null,
         "class_code":null,
         "brick_code":null,
         "tag_id":null
      }
   ]
}
```


The response for exercises is:

```json
{
   "exercises":[
      {
         "tag_id":317,
         "user_input":"running",
         "duration_min":30,
         "met":9.8,
         "nf_calories":421.4,
         "photo":{
            "highres":"https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg",
            "thumb":"https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg",
            "is_user_uploaded":false
         },
         "compendium_code":12050,
         "name":"running",
         "description":"None",
         "benefits":"None"
      }
   ]
}
```


## Sheetly

I signed up with Sheetly at this URL:

https://sheety.co/

