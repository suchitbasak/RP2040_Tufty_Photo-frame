# RP2040 Tufty to Display Images

Bought a [Tufty 2040](https://shop.pimoroni.com/products/tufty-2040?variant=40036912595027) because it looked cute.

Used micropython to display images and attached it to our Christmas tree ✨

## How to use the code
1. Follow [this Pimoroni tutorial to setup the board](https://learn.pimoroni.com/article/getting-started-with-tufty-2040)
2. Transfer `.py` the files from this repository onto the device. I use Thonny- its simple to use.
3. Create a folder called `photos_dir`
4. Add photos to the folder. The photos need to be 240x360 in size so that they fit the screen.


## Troubleshooting:
1. Once the Tufty is plugged in to your computer, don't forget to press the on-board power button to switch it on!
3. If Thonny gives a `Permission denied: Cannot access /dev/ttyACM0...` error, run `sudo usermod -a -G dialout username` and reboot your computer.
