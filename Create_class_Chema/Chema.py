from time import sleep
class Chema() :
    def __init__(self,heigt,width,length,windows_col,electronics:list):
        self.__heigt=heigt
        self.__width=width
        self.__length=length
        self.__windows_col=windows_col
        self.__electronics=electronics



class Electronics() :
    def __init__(self,brand,manufacturer_country,heigt,width,length,power,volume,material,color) :
        self.__brand=brand
        self.__manufacturer_country=manufacturer_country
        self.__heigt=heigt
        self.__width=width
        self.__length=length
        self.__power=power
        self.__volume=volume
        self.__material=material
        self.__color=color
    def _get_info(self) :
        print(f'Brand :{self.__brand}\nManufacturer country :{self.__manufacturer_country}\nHeigt :{self.__heigt}\nWidth : {self.__width}\n\
            Length : {self.__length}\nPower :{power}\nVolume :{self.volume}\nMaterial :{self.__material}\nColor :{self.color}')


class Teapot(Electronics) :
    __water_level=0
    def __init__(self,brand,manufacturer_country,heigt,width,length,power,volume,material,color,
    heating_element_type,smart_control:bool,functional_features:list,equipment:list) :
        Electronics.__init__(self, brand, manufacturer_country, heigt, width, length, power, volume, material, color)
        self.__heating_element_type=heating_element_type
        self.__smart_control=smart_control
        self.__functional_features
        self.__equipment
        def get_info(self) :
            super()._get_info()
            print(f'Heating element type :{self.heating_element_type}\nSmart control :{self.__smart_control}\n\
                Functional features :{self.__functional_features}\nEquipment :{self.__equipment}')
    @property
    def water_level(self):
        return self.__water_level
    @water_level.setter
    def water_level(self,level) :
        if 0<=level<=100 :
            self.__water_level=level
        else :
            print('Value must be between 0 and 100')
    def boil_water(self) :
        if __water_level==0 :
            print('Fill the kettle with water!')
        else :
            print("Please wait...")
            sleep(self.__water_level+20)#for example
            print('The water boiled')
class Refrigerator(Electronics):
    def __init__(self,brand,manufacturer_country,heigt,width,length,power,volume,material,color,
    refr_type,energy_class,noise_level,climate_class,total_usable_volume,proprietary_technologies):
        Electronics.__init__(self, brand, manufacturer_country, heigt, width, length, power, volume, material, color)
        self.__refr_type=refr_type
        self.__energy_class=energy_class
        self.__noise_level=noise_level
        self.__climate_class=climate_class
        self.__total_usable_volume=total_usable_volume
        self.__proprietary_technologies=proprietary_technologies
    
    def get_info(self) :
        super()._get_info()
        print(f'Refrigerator type :{self.__refr_type}\nEnergy class :{self.__energy_class}\nNoise level :{self.noise_level}\n\
            Climate class :{self.__climate_class}\nTotal usable volume :{self.__total_usable_volume}\nProprietary technologies :{self.__proprietary_technologies}')