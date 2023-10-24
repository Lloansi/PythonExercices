class Stars_Wars_Character:
    def __init__(self, edited, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year) -> None:
        self.edited = edited
        self.name = name
        self.created = created
        self.gender = gender
        self.skin_color = skin_color
        self.hair_color = hair_color
        self.height = height
        self.eye_color = eye_color
        self.mass = mass
        self.homeworld = homeworld
        self.birth_year = birth_year

    def __str__(self):
        return("\nThe Star Wars character is called " + str(self.name) + 
               "\nDATA:" + 
               "\n Gender:" + str(self.gender) + 
               "\n Height:" + str(self.height) + 
               "\n Mass:" + str(self.mass) + 
               "\n Eye Color:" + str(self.eye_color) +
               "\n Skin color:" + str(self.skin_color) + 
               "\n Hair color:" + str(self.hair_color) +
               "\n Home World:" + str(self.homeworld) + 
               "\n Birthday:" + str(self.birth_year) +
               "\n Created:" + str(self.created) + 
               "\n Edited:" + str(self.edited) 
            )
    
    def __json__(self):
        return {
            "edited": self.edited,
            "name": self.name,
            "created": self.created,
            "gender": self.gender,
            "skin_color": self.skin_color,
            "hair_color": self.hair_color,
            "height": self.height,
            "eye_color": self.eye_color,
            "mass": self.mass,
            "homeworld": self.homeworld,
            "birth_year": self.birth_year
        }
    
    def to_dict(self):
        return {
            "edited": self.edited,
            "name": self.name,
            "created": self.created,
            "gender": self.gender,
            "skin_color": self.skin_color,
            "hair_color": self.hair_color,
            "height": self.height,
            "eye_color": self.eye_color,
            "mass": self.mass,
            "homeworld": self.homeworld,
            "birth_year": self.birth_year
        }
    
class Character_Films(Stars_Wars_Character):
    def __init__(self, edited, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year, num_of_films, first_film, alive_at_the_end) -> None:
        super().__init__(edited, name, created, gender, skin_color, hair_color, height, eye_color, mass, homeworld, birth_year)
        self.num_of_films = num_of_films
        self.first_film = first_film
        self.alive_at_the_end = alive_at_the_end 

    def __str__(self):
        return("\nThe Star Wars new data character is called " + str(self.name) + 
               "\nDATA:" + 
               "\n Gender:" + str(self.gender) + 
               "\n Height:" + str(self.height) + 
               "\n Mass:" + str(self.mass) + 
               "\n Eye Color:" + str(self.eye_color) +
               "\n Skin color:" + str(self.skin_color) + 
               "\n Hair color:" + str(self.hair_color) +
               "\n Home World:" + str(self.homeworld) + 
               "\n Birthday:" + str(self.birth_year) +
               "\n Created:" + str(self.created) + 
               "\n Edited:" + str(self.edited) +
               "\n" +
               "\nEXTRA DATA:"+
               "\n Num of films:" + str(self.num_of_films) +
               "\n First film:" + str(self.first_film) +
               "\n Dead at:" + str(self.alive_at_the_end)
            )
    
    def __json__(self):
        data = super().__json__()
        data.update({
            "num_of_films": self.num_of_films,
            "first_film": self.first_film,
            "alive_at_the_end": self.alive_at_the_end
        })
        return data

    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "num_of_films": self.num_of_films,
            "first_film": self.first_film,
            "alive_at_the_end": self.alive_at_the_end
        })
        return data

    @property
    def num_of_films(self):
        return self._num_of_films

    @num_of_films.setter
    def num_of_films(self, value):
        self._num_of_films = value

    @property
    def first_film(self):
        return self._first_film

    @first_film.setter
    def first_film(self, value):
        self._first_film = value

    @property
    def alive_at_the_end(self):
        return self._alive_at_the_end

    @alive_at_the_end.setter
    def alive_at_the_end(self, value):
        self._alive_at_the_end = value