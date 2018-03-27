import media
import website

toy_story = media.Movie("Toy Story",
                        "Toy Story is a computer animated film series and Disney media franchise that began with the 1995 film of the same name, produced by Pixar Animation Studios and released by Walt Disney Pictures. The franchise is based on the anthropomorphic concept that all toys, unknown to humans, are secretly alive, and the films ...",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
                        
avatar = media.Movie("Avatar",
                     "In 2154, humans have depleted Earth's natural resources, leading to a severe energy crisis. The Resources Development Administration (RDA for short) mines for a valuable mineral — unobtanium — on Pandora, a densely forested habitable moon orbiting the gas giant Polyphemus in the Alpha Centauri star system. Pandora, whose atmosphere is poisonous to humans, is inhabited by the Na'vi, a species of 10-foot tall (3.0 m), blue-skinned, sapient humanoids that live in harmony with nature and worship a mother goddess named Eywa.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
                     
avengers = media.Movie("Avengers",
                     "The Avengers, is a 2012 American superhero film based on the Marvel Comics superhero team of the same name, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.",
                     "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                     "https://www.youtube.com/watch?v=eOrNdBpGMv8")
                     
guardian2 = media.Movie("Guardians of the Galaxy Vol. 2",
                     "Guardians of the Galaxy Vol. 2 is a 2017 American superhero film based on the Marvel Comics superhero team Guardians of the Galaxy, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures. It is the sequel to 2014's Guardians of the Galaxy and the fifteenth film in the Marvel Cinematic Universe (MCU). Written and directed by James Gunn, the film stars an ensemble cast featuring Chris Pratt, Zoe Saldana, Dave Bautista, Vin Diesel, Bradley Cooper, Michael Rooker, Karen Gillan, Pom Klementieff, Elizabeth Debicki, Chris Sullivan, Sean Gunn, Sylvester Stallone, and Kurt Russell. In Guardians of the Galaxy Vol. 2, the Guardians travel throughout the cosmos as they help Peter Quill learn more about his mysterious parentage.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/a/ab/Guardians_of_the_Galaxy_Vol_2_poster.jpg/220px-Guardians_of_the_Galaxy_Vol_2_poster.jpg",
                     "https://www.youtube.com/watch?v=duGqrYw4usE")
                     
hunger2 = media.Movie("The Hunger Games: Mockingjay – Part 2",
                     "The Hunger Games: Mockingjay – Part 2 is a 2015 American dystopian science fiction adventure film directed by Francis Lawrence, with a screenplay by Peter Craig and Danny Strong. It is the fourth and final installment in The Hunger Games film series, and the second of two films based on the novel Mockingjay, the final book in The Hunger Games trilogy by Suzanne Collins.",
                     "https://upload.wikimedia.org/wikipedia/en/9/9d/Mockingjay_Part_2_Poster.jpg",
                     "https://www.youtube.com/watch?v=KmYNkasYthg")
                     
revenant = media.Movie("The Revenant",
                     "The Revenant is a 2015 American semi-biographical epic western film directed by Alejandro G. Iñárritu. The screenplay by Mark L. Smith and Iñárritu is based in part on Michael Punke's 2002 novel of the same name, describing frontiersman Hugh Glass's experiences in 1823. That novel is in turn based on the 1915 poem The Song of Hugh Glass. The film stars Leonardo DiCaprio, Tom Hardy, Domhnall Gleeson, and Will Poulter.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
                     "https://www.youtube.com/watch?v=QRfj1VCg16Y")
                     
movies = [toy_story, avatar, avengers, guardian2, hunger2, revenant];
#website.open_movies_page(movies);

print(media.Movie.__module__)