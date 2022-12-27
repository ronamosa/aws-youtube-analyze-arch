# Layers

## Overview

For various import dependencies, you need to create a "layer" in AWS Lambda for your function to pull these libraries in.

## scrapetube & youtube_transcript_api

This project needs `scrapetube` and `youtube_transcript_api`, so do the following to package up a layer to upload to AWS:

```bash
# create the folder for your layer
mkdir -p layers/python

# change into, and install libraries to the folder
cd layers/python
pip install --target . <libraries>

# change up a directory, create a zip file of the `python/` folder
cd ..
zip -r <layername>.zip python
```

The zip contents should have the `python/` directory as root.

Your layer file is ready for upload to AWS.
