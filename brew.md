# Brew

run
> xcode-select --installation

>curl -fsSL -o install.sh https://raw.githubusercontent.com/Homebrew/install/master/install.sh

>less install.sh

>/bin/bash install.sh

>nano ~/.bash_profile

add
export PATH=/usr/local/bin:$PATH
save

> source ~/.bash_profile

>brew doctor
you system is ready to brew

## to install a program
> brew install tree

> brew --version

> brew upgrade tree

> brew uninstall tree

## uninstall brew

>curl -fsSL -o uninstall.sh https://raw.githubusercontent.com/Homebrew/install/master/uninstall.sh

>less uninstall.sh

>bash uninstall.sh --help

>bash uninstall.sh -d

without any flag
>bash uninstall.sh




### Installing Desktop Applications

> brew cask install visual-studio-code

> brew cask uninstall visual-studio-code
