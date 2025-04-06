# assets
YOLO models for florr.io  

## Info

These are auto-generated

> ['./afk-det.pt', './afk-seg.pt', './desert.pt', './fire_ant.pt', './flower.pt', './hel.pt', './jf.pt', './sandstorm.pt']

* model: ./afk-det.pt  
  YOLO11n summary: 181 layers, 2,590,425 parameters, 0 gradients, 6.4 GFLOPs
  classes: {0: 'Window', 1: 'Start', 2: 'End'}  
* model: ./afk-seg.pt  
  YOLO11n-seg summary: 203 layers, 2,842,803 parameters, 0 gradients, 10.4 GFLOPs
  classes: {0: 'path'}  
* model: ./desert.pt  
  Model summary: 141 layers, 2,691,378 parameters, 0 gradients, 6.9 GFLOPs
  classes: {0: 'scorpion', 1: 'beetle', 2: 'cactus', 3: 'sandstorm', 4: 'sand_centipede', 5: 'soldier_fire_ant'}  
* model: ./fire_ant.pt  
  Model summary: 129 layers, 3,011,433 parameters, 0 gradients, 8.2 GFLOPs
  classes: {0: 'soldier_fire_ant', 1: 'queen_fire_ant', 2: 'fire_ant_mouth'}  
* model: ./flower.pt  
  Model summary: 129 layers, 3,011,043 parameters, 0 gradients, 8.2 GFLOPs
  classes: {0: 'flower'}  
* model: ./hel.pt  
  Model summary: 129 layers, 3,012,213 parameters, 0 gradients, 8.2 GFLOPs
  classes: {0: 'beetle', 1: 'beetle_head', 2: 'wasp', 3: 'spider', 4: 'centipede', 5: 'gambler', 6: 'spawn_mark'}  
* model: ./jf.pt  
  Model summary: 141 layers, 2,690,403 parameters, 0 gradients, 6.9 GFLOPs
  classes: {0: 'jellyfish'}  
* model: ./sandstorm.pt  
  Model summary: 129 layers, 3,011,043 parameters, 0 gradients, 8.2 GFLOPs
  classes: {0: 'sandstorm'} 

## Usage

* `afk_det.pt` & `afk_seg.pt` 

  Use for [florr-auto-afk](https://github.com/Shiny-Ladybug/florr-auto-afk)

  As detect model is for the detection of AFK Window, the segment model is for separating the path of the AFK

* `desert.pt`

  Use for specify desert mobs

* `flower.pt`

  Detect flowers (players)

* `hel.pt`

  Detect hel mobs

* `jf.pt`

  Detect only Jellyfish

* `sandstorm.pt`

  Use for [florr-auto-sszone](https://github.com/Shiny-Ladybug/florr-auto-sszone)
