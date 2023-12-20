# Ransomware Educational Project

This project is a simple educational demonstration of file encryption using Python. It uses the cryptography library to implement the Fernet symmetric key encryption algorithm.

## Disclaimer

**This project is created for educational purposes only. The development and distribution of malicious software, including ransomware, are illegal and unethical. The author does not endorse or encourage any form of illegal or harmful activities.**

## Description

The ransomware project demonstrates a basic file encryption process. It recursively traverses files and directories within the specified path, encrypting each file with a randomly generated key using Fernet encryption.

## Requirements

- Python 3.x
- cryptography library

Install the required library using the following:

```bash
pip install cryptography
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/ransomware-educational.git](https://github.com/SathiraSriSathsara/Ransomware.git)
cd Ransomware
```

2. Run the ransomware:

```bash
python app.py
```

## Configuration

Exclude certain files from encryption by adding their names to the `exclude_files` list in the `if __name__ == "__main__":` block.

## Warning

**Use this code responsibly and only for educational purposes. Do not deploy or distribute any form of ransomware in real-world scenarios. Unauthorized access and encryption of files without explicit consent are illegal.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
