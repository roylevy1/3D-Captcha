
                            ____  _____          _____            _       _           
                           |___ \|  __ \        / ____|          | |     | |          
                             __) | |  | |______| |     __ _ _ __ | |_ ___| |__   __ _ 
                            |__ <| |  | |______| |    / _` | '_ \| __/ __| '_ \ / _` |
                            ___) | |__| |      | |___| (_| | |_) | || (__| | | | (_| |
                           |____/|_____/        \_____\__,_| .__/ \__\___|_| |_|\__,_|
                                                           | |                        
                                                           |_|                        
Generate a smart test with 3D for Captcha validation 

the project build in python 3.
the project use the library Vpython for create 3D shapes.

its easy for the user to use and write the captach's word, but it can be difficult for bots to use.
its suppose to be a "Checking page" that will refer u to the page u wanted, but it can be applied in other methods. 

Logic:
    the project create 3 shpaes randomly in canvas:
      it can be:
          3 same shapes
          2 same shapes + 1 diffrent shape
          all the shape diffrent
          
    threre are 5 diffrent shape's types
    the color of each shape will be DIFFRENT in any case. 
    there are 6 diffrent colors, so we got 6*5*4 option for colors = 120
    thefore we got 3^5 * 120 = 243*120 = 29160 option for shapes and colors for the user to choose

* to make it even harder to bots, i use textures
  there are 12 diffrent texture for the shapes = 3^12 = 531441
  now 531441*29160 = 15496819560 diffrent combination of shape's type, color and texture

* in each shape will be a diffrent word. the chance for them to be identical are convergent to 0 [see MATH for more info]

* also to make it even harder to bots, the project dont use "forms".
  instead i reconize the key press in the keyboard.



how to use:
* copy the file to your project
* make sure that Vpython library install in your python 3
* functinos:
    word_valid_do()
    word_invalid_do()
    need to be applied by u.
    
    
  MATH:                                                                  
    we use the chars(0-9, a-z, A-Z) = 10+26+26 = 62 diffrent option for 1 char                                                    
    word can be between 5-10 chars, therefor:                                                                                   
    62^5 = 916132832 differnt option in low number of chars                                                                     
    62^10 = 8.3929937*(10^17) differnt option in high number of chars                                                           
    the odd for two identical word is:                                                                                          
      1 / (62^5 * 62^5)   = 1 / (62^(5+5)) = 1 / (62^10) ~= 1.19147*(10^-18)     = 0.00000000000000000119147                      
      1 / (62^10 * 62^10) = 1 / (62^(10+10)) = 1 / (62^20) ~= 1.4196007*(10^-36) = 0.0000000000000000000000000000000000014196007 

    so as we can see the odd rly small, but u can even handle this by checking if the words are identical.         
      for 3 identical words its go even smaller.                                                                                
          1 / (62^5 * 62^5 * 62^5) = 1 / (62^15)    ~= 1.3005428*(10^-27)                                                         
          1 / (62^10 * 62^10 * 62^10) = 1 / (62^30) ~= 1.6914116*(10^-54)                                                         
 Good luck

                                    _____               _                      
                                   |  __ \             | |                     
                                   | |__) |___  _   _  | |     _____   ___   _ 
                                   |  _  // _ \| | | | | |    / _ \ \ / / | | |
                                   | | \ \ (_) | |_| | | |___|  __/\ V /| |_| |
                                   |_|  \_\___/ \__, | |______\___| \_/  \__, |
                                                 __/ |                    __/ |
                                                |___/                    |___/ 
