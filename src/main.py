from prettytable import PrettyTable


# Functions
def letter_lookup(letter):
    """
    Look up and print information from a dictionary based on the given letter.

    This function searches for a specific letter in a predefined dictionary.
    If the letter is found, it prints out each category and its corresponding
    name in a tabular format using PrettyTable. If the letter is not found,
    it prints an appropriate message.

    Parameters:
        letter (str): The letter to look up in the dictionary.

    Returns:
        None: This function prints the results directly.
    """
    # Dictionary containing data for each letter of the alphabet
    letters_dict = {
        "A": {
            "Prénom": "Albert",
            "Ville": "Annecy",
            "Sport": "Athlétisme",
            "Célébrité": "Adèle",
            "Animal": "Aigle",
            "Couleur": "Ambre",
            "Légume": "Asperge",
            "Fruit": "Abricot"
        },
        "B": {
            "Prénom": "Brigitte",
            "Ville": "Bordeaux",
            "Sport": "Badminton",
            "Célébrité": "Bardot",
            "Animal": "Baleine",
            "Couleur": "Bleu",
            "Légume": "Brocoli",
            "Fruit": "Banane"
        },
        "C": {
            "Prénom": "Charles",
            "Ville": "Cannes",
            "Sport": "Cyclisme",
            "Célébrité": "Chaplin",
            "Animal": "Chat",
            "Couleur": "Cyan",
            "Légume": "Carotte",
            "Fruit": "Cerise"
        },
        "D": {
            "Prénom": "Daniel",
            "Ville": "Dijon",
            "Sport": "Danse",
            "Célébrité": "Depardieu",
            "Animal": "Dauphin",
            "Couleur": "Doré",
            "Légume": "Dolique",
            "Fruit": "Datte"
        },
        "E": {
            "Prénom": "Emma",
            "Ville": "Évian",
            "Sport": "Escalade",
            "Célébrité": "Einstein",
            "Animal": "Éléphant",
            "Couleur": "Émeraude",
            "Légume": "Épinard",
            "Fruit": "Églantine"
        },
        "F": {
            "Prénom": "François",
            "Ville": "Fontainebleau",
            "Sport": "Football",
            "Célébrité": "Fonda",
            "Animal": "Faucon",
            "Couleur": "Fuchsia",
            "Légume": "Fenouil",
            "Fruit": "Figue"
        },
        "G": {
            "Prénom": "Gabrielle",
            "Ville": "Grenoble",
            "Sport": "Gymnastique",
            "Célébrité": "Gainsbourg",
            "Animal": "Girafe",
            "Couleur": "Gris",
            "Légume": "Gombo",
            "Fruit": "Groseille"
        },
        "H": {
            "Prénom": "Hugo",
            "Ville": "Havre",
            "Sport": "Handball",
            "Célébrité": "Hepburn",
            "Animal": "Hibou",
            "Couleur": "Havane",
            "Légume": "Haricot",
            "Fruit": "Hélène"
        },
        "I": {
            "Prénom": "Isabelle",
            "Ville": "Istanbul",
            "Sport": "Iaido",
            "Célébrité": "Iglesias",
            "Animal": "Ibis",
            "Couleur": "Indigo",
            "Légume": "Igname",
            "Fruit": "Icaque"
        },
        "J": {
            "Prénom": "Julien",
            "Ville": "Jérusalem",
            "Sport": "Judo",
            "Célébrité": "Jobs",
            "Animal": "Jaguar",
            "Couleur": "Jade",
            "Légume": "Jicama",
            "Fruit": "Jujube"
        },
        "K": {
            "Prénom": "Karine",
            "Ville": "Kyoto",
            "Sport": "Karaté",
            "Célébrité": "Kidman",
            "Animal": "Kangourou",
            "Couleur": "Kaki",
            "Légume": "Kale",
            "Fruit": "Kiwi"
        },
        "L": {
            "Prénom": "Lucas",
            "Ville": "Lyon",
            "Sport": "Lutte",
            "Célébrité": "Lennon",
            "Animal": "Lion",
            "Couleur": "Lavande",
            "Légume": "Lentille",
            "Fruit": "Litchi"
        },
        "M": {
            "Prénom": "Marie",
            "Ville": "Marseille",
            "Sport": "Marathon",
            "Célébrité": "Monroe",
            "Animal": "Morse",
            "Couleur": "Mauve",
            "Légume": "Maïs",
            "Fruit": "Mangue"
        },
        "N": {
            "Prénom": "Nicolas",
            "Ville": "Nantes",
            "Sport": "Natation",
            "Célébrité": "Newton",
            "Animal": "Narval",
            "Couleur": "Navy",
            "Légume": "Navet",
            "Fruit": "Nectarine"
        },
        "O": {
            "Prénom": "Olivier",
            "Ville": "Oslo",
            "Sport": "Omnisport",
            "Célébrité": "Oprah",
            "Animal": "Otarie",
            "Couleur": "Ocre",
            "Légume": "Oignon",
            "Fruit": "Orange"
        },
        "P": {
            "Prénom": "Paul",
            "Ville": "Paris",
            "Sport": "Polo",
            "Célébrité": "Pitt",
            "Animal": "Panda",
            "Couleur": "Pourpre",
            "Légume": "Poivron",
            "Fruit": "Poire"
        },
        "Q": {
            "Prénom": "Quentin",
            "Ville": "Québec",
            "Sport": "Quidditch",
            "Célébrité": "Quincy",
            "Animal": "Quokka",
            "Couleur": "Quartz",
            "Légume": "Quinoa",
            "Fruit": "Quetsche"
        },
        "R": {
            "Prénom": "Raphaël",
            "Ville": "Rome",
            "Sport": "Rugby",
            "Célébrité": "Rihanna",
            "Animal": "Renard",
            "Couleur": "Rouge",
            "Légume": "Radis",
            "Fruit": "Raisin"
        },
        "S": {
            "Prénom": "Sophie",
            "Ville": "Strasbourg",
            "Sport": "Ski",
            "Célébrité": "Streep",
            "Animal": "Serpent",
            "Couleur": "Saumon",
            "Légume": "Salade",
            "Fruit": "Strawberry"
        },
        "T": {
            "Prénom": "Thomas",
            "Ville": "Toulouse",
            "Sport": "Tennis",
            "Célébrité": "Turner",
            "Animal": "Tigre",
            "Couleur": "Turquoise",
            "Légume": "Tomate",
            "Fruit": "Tangerine"
        },
        "U": {
            "Prénom": "Ulysse",
            "Ville": "Utrecht",
            "Sport": "Ultimate Frisbee",
            "Célébrité": "Usher",
            "Animal": "Urubu",
            "Couleur": "Ultramarine",
            "Légume": "Ulluco",
            "Fruit": "Ugli fruit"
        },
        "V": {
            "Prénom": "Valérie",
            "Ville": "Venise",
            "Sport": "Volleyball",
            "Célébrité": "Vega",
            "Animal": "Vipère",
            "Couleur": "Vert",
            "Légume": "Verveine",
            "Fruit": "Vanille"
        },
        "W": {
            "Prénom": "William",
            "Ville": "Washington",
            "Sport": "Water-polo",
            "Célébrité": "Winslet",
            "Animal": "Wallaby",
            "Couleur": "Wengé",
            "Légume": "Wasabi",
            "Fruit": "Watermelon"
        },
        "X": {
            "Prénom": "Xavier",
            "Ville": "Xian",
            "Sport": "Xingyi quan",
            "Célébrité": "Xzibit",
            "Animal": "Xénarthre",
            "Couleur": "Xanadu",
            "Légume": "Xérès",
            "Fruit": "Ximenia"
        },
        "Y": {
            "Prénom": "Yasmine",
            "Ville": "Yokohama",
            "Sport": "Yoga",
            "Célébrité": "Yeoh",
            "Animal": "Yak",
            "Couleur": "Yellow",
            "Légume": "Yucca",
            "Fruit": "Yuzu"
        },
        "Z": {
            "Prénom": "Zoé",
            "Ville": "Zurich",
            "Sport": "Zumba",
            "Célébrité": "Zeta-Jones",
            "Animal": "Zèbre",
            "Couleur": "Zinzolin",
            "Légume": "Zucchini",
            "Fruit": "Ziziphus"
        }
    }

    # Display data in a table format if the letter is found
    if letter in letters_dict:
        table = PrettyTable()
        table.field_names = letters_dict[letter].keys()
        table.add_row(letters_dict[letter].values())

        print(table)
    else:
        print(f"Aucune donnée disponible pour la lettre '{letter}'.")

def main():
    """
    Main function to drive the program.

    Asks the user to input a letter, then calls `letter_lookup` with
    the uppercase version of that letter.
    """
    letter = input(str("Lettre : "))
    letter_lookup(letter.upper())

# Main
if __name__ == "__main__":
    main()
