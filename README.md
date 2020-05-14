# ChecksumVerify
Basic MD5/SHA1 comparison application

## Table of Contents
1. About
2. Getting Started
    1. Prerequisites
    2. Installing
3. How to Use
4. How It Works
5. Built With
6. Acknowledgements

## About
ChecksumVerify is a simple checksum comparison program written in Python using the Tkinter Graphical User Interface framework and Microsoft's File Checksum Integrity Verifier application, developed for use with Windows 10.

## Getting Started
### Prerequisites
- Python 3.6+
- Microsoft File Checksum Integrity Verifier (FCIV) - [link](https://www.microsoft.com/en-us/download/details.aspx?id=11533)

## How It Works
- ChecksumVerify uses Python's Tkinter module to create a minimal graphical user interface for easy use
- Microsoft's File Checksum Integrity Verifier (FCIV) is used to generate the MD5 and SHA1 hashes for the entered file
- The checksums are then compared against given MD5 and SHA1 hashes, and the results are displayed to the user through the GUI