# DrBitSky
Messing around with the BlueSky APIs using ATPROTO

Start here - https://docs.bsky.app/docs/get-started

## Quick Start (for macOS/unix)
### Install Homebrew
``` bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
### Install Python
``` bash
brew install python
```
### Navigate to root directory
``` bash
cd [path/to/repo]
```
### Create a local environment
``` bash
python3 -m venv myenv
source myenv/bin/activate
```
### Install dependencies
``` bash
python3 -m pip install -r requirements.txt
```
### Run
Via your editor of choice. VSCode recommended

## Environment Variables
Make sure to add `.env` file and provide values for the following environment variables
``` bash
export BSKY_USERNAME="[Your_BlueSky_Handle]"
export BSKY_PASSWORD="[Your_BlueSky_App_Password]" # Can be found or created here - https://bsky.app/settings/app-passwords

export STEAM_WEB_API_KEY="Your_Steam_API_Key" # Can be found or created here - https://steamcommunity.com/dev/apikey

# Use your personal account key for testing, but to get stats for other players, you'll need their account keys
# AKA Steam ID
export STEAM_ACCOUNT_KEY="[Your_Steam_Account_Key]" # Can be found or created here - https://store.steampowered.com/account/
```
