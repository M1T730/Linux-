# PCI passthrough(GPU) and USB passthough (took a long time)

**step 1:**
PCI Passthough, pretty much followed: https://pve.proxmox.com/wiki/PCI_Passthrough

**step 2:** 
USB Passthough, done via Proxmox cli, and using lsusb to identify ports.

**result** 
USB Passthough was pretty straight foward and simple, PCI Passthough worked for audio.
GPU Passthough **failed**, attemped many times and in different ways, from what I understood, my gaming laptop, Lenovo Legion 5, has 2 types of GPU, integrated GPU on the CPU, that is direcly connected to the laptop display, and a seperate High performance GPU, NVIDIA RTX 3060 Mobile, tried passing both GPU seperately in different attempts, both failed: 
BIOS settings: Discrete GPU (using only the NVIDIA GPU), trying to passthough the NVIDIA GPU caused the error 43 in the VM, the VM could not have the connection to the laptop display, thus not loading the NVIDIA GPU even though it had the drivers installed and the GPU; with this setting I tried to pass only the iGPU(AMD) as well, big mistake, it completely locked me out from the computer, since the iGPU is the primary controller of the display, removing it caused the console to not initialize properly, causing the system failing to start, (had to boot into recovery mode and remove its bound to the VFIO).
BIOS settings: hybrid mode (using both iGPU and NVIDIA GPU), tried to passthough the NVIDIA GPU, thinking to split the iGPU for the Proxmox console and the NVIDIA GPU for the VM, but same as before, error 43, same problem, the VM recieves the GPU but cannot load it because the laptop display is not passed and because the system cannot seperate completely the NVIDIA GPU, architecture of the gaming laptop doens't let me. 

