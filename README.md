# Pixel-Bamboo
Generates minimum vertical bamboo tubes' length and position inside an N * N * N array, so that they makes up the two different images specified when seen from different sides. Used in a installation project on Lianhua Island in Lake Yangcheng, at Suzhou, Jiangsu, China. Pictures are to be updated soon. 

### Dependencies
* Python Libraries
  * **numpy** and **matplotlib** for generating 3d previews.
  * **svgwrite** and **cairosvg** for generating layout images.
* Software
  * **Autodesk Maya** for generating obj model file. (Note that a Maya with Python support is needed to do this)

### Usage
1. Set shebang in *calc_data.py* to a working python intepreter with **matplotlib** and **numpy** installed. 
2. Set shebang in *gen_blueprint.py* to a working python intepreter with **svgwrite** and **cairosvg** installed. 
3. In *calc_data.py*, set desired array size (MODELSIZE) to be the size of your pixel images, and path to write the maya script (PATH_TO_MAYA_SCRIPT) you'll be running to generate 3d model.
4. Create your two images in the format seen in *graphs.py*, and substitute those in file. Import your graphs in *calc_data.py*
5. Run "1 Calculate Data". This will update content in modeldata.py and generate maya script.
6. Run "2 Generate Blueprint". You will find svg version files in blueprint/svg and png files in blueprint/png.
