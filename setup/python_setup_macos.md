### Introduction
To get started with our computational social science projects, we need to set up a few tools on our computers. This guide is designed for macOS users and will walk you through installing Homebrew (a package manager for macOS), wget (a utility for downloading files from the web), Miniconda (a minimal installer for Conda), and finally, how to set up your project environment using an environment file. Let's dive in!

### Step 1: Install Homebrew
Homebrew is a package manager that simplifies the installation of software on macOS.

1. **Open Terminal:** You can find Terminal in `/Applications/Utilities/`, or you can search for it using Spotlight (Cmd + Space).
2. **Install Homebrew:** Copy and paste the following command into Terminal, then press Enter. This command downloads and runs the Homebrew installation script.
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. **Follow On-screen Instructions:** The script will explain what it plans to do and then pause for your confirmation. You may need to enter your password to proceed with the installation.

### Step 2: Install wget
`wget` is a utility for downloading files from the internet. It's handy for fetching files from the command line.

1. **Install wget:** In the Terminal, type the following command and press Enter:
   ```
   brew install wget
   ```

### Step 3: Download and Install Miniconda
Miniconda is a minimal version of Conda, a package and environment manager. It includes only Conda, Python, and a few other packages.

1. **Download Miniconda Installer:** Depending on your Mac's chip (Intel or Apple Silicon), download the appropriate version of Miniconda. You can check your chip type by clicking on the Apple logo in the top left corner, selecting "About This Mac," and looking at the "Chip" information.
   - For Intel Macs:
     ```
     cd ~/Downloads
     wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
     ```
   - For Apple Silicon Macs:
     ```
     cd ~/Downloads
     wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
     ```
2. **Install Miniconda:** After downloading, run the installer by replacing `<CHIP>` with either `x86_64` for Intel Macs or `arm64` for Apple Silicon Macs.
   ```
   bash Miniconda3-latest-MacOSX-<CHIP>.sh
   ```
   Follow the prompts on the screen to complete the installation.

### Step 4: Install Mamba
Mamba is a fast and flexible alternative to Conda for managing packages and environments.

1. **Install Mamba:** Execute the following command in Terminal:
   ```
   conda install mamba -n base -c conda-forge
   ```

### Step 5: Create and Activate Your Conda Environment
Using the provided environment file, you will set up a Conda environment specific to our course requirements.

1. **Locate the Environment File:** Your instructor should provide you with an `environment_envpycss.yml` file. Place this file in a known directory on your Mac.
2. **Navigate to the File's Directory:** In Terminal, change your directory to where you've placed the `environment_envpycss.yml` file. Replace `PATH_TO_ENVIRONMENT_FILE` with the actual path.
   ```
   cd ~/PATH_TO_ENVIRONMENT_FILE
   ```
3. **Create the Environment:** Use the following command to create your Conda environment from the `environment_envpycss.yml` file.
   ```
   mamba env create -f environment_envpycss.yml
   ```
4. **Activate the Environment:** To start using this environment, activate it by typing:
   ```
   conda activate envpyc
   ```

### Optional: Automate Environment Activation
To automatically activate this environment when you open a new Terminal window, you can add the activation command to your `.zshrc` file.
```
echo "conda activate envpyc" >> ~/.zshrc
```

### Troubleshooting
If you encounter any issues during installation, check your internet connection, ensure you have enough disk space, and confirm you have the necessary permissions to install software on your Mac.