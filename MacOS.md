# picture save location

in the terminal
defaults write com.apple.screencapture location /Users/serdar/Documents/udel/courses/binf640/figures
killall SystemUIServer

## back to normal
defaults write com.apple.screencapture location ~/Desktop
killall SystemUIServer
