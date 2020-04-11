# I use an old version of hugo that doesnt have a supported cask version anymore :(
# This code will set you up.
# This code is lifted from the build script
# Customized for mac
curl -Ls https://github.com/gohugoio/hugo/releases/download/v0.38/hugo_0.38_macOS-64bit.tar.gz -o ./hugo.tar.gz
mkdir ./hugo-temp
tar xf ./hugo.tar.gz -C ./hugo-temp
mv ./hugo-temp/hugo ./hugo
rm -rf ./hugo-temp
rm -f ./hugo.tar.gz