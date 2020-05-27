# A FUD Malware

This is a malware  C&C malware in CPP and Python. This is for educational purposes only.

## Development Enviroment

Install:

* C/C++ (Malware/Bot)
* Python 3 (Server)
* WINAPI (Windows Sockets)
* Mingw-g++ compiler flags/options (to reduce the size of the binary)
* Debian or Windows

On Debian, install Windows compiler:

```bash
sudo apt-get install mingw-w64-common mingw-w64-i686-dev mingw-w64-tools mingw-w64-x86-64-dev
```

## Compiling the C++ Client

```bash
For Linux:
$ i686-w64-mingw32-g++ -std=c++11 maldev.cpp -o maldev.exe -s -lws2_32 -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc

For Windows:

> g++ -std=c++11 maldev.cpp -o maldev.exe -s -lws2_32 -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc


```