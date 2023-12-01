#include <fstream>
#include <iostream>
#include <string>
// permet de parser un fichier texte
namespace AOC
{

    // Fonction pour parser le fichier
    void parseFile(const std::string &filePath)
    {
        std::ifstream file(filePath);

        if (!file.is_open())
        {
            std::cerr << "Erreur : Impossible d'ouvrir le fichier " << filePath << std::endl;
            return;
        }

        std::string line;
        while (getline(file, line))
        {
            // Effectuez ici votre parsing
            
            std::cout << line << std::endl; // affiche simplement chaque ligne
        }

        file.close();
    }

    int main()
    {
        std::string filePath = "nom_du_fichier.txt"; // Remplacez par le chemin de votre fichier
        parseFile(filePath);

        return 0;
    }

}