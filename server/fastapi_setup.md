### Installation
#### Create virtual python environment(.venv) running python 3.12
##### On Mac
1. Open Terminal
2. Navigate to the directory where you want to create the virtual env
3. Create venv: `python3 -m venv env`
4. Activate: `source env/bin/activate`
5. Install Libraries with pip(possibly pip3)
6. When you're done, deactivate: `deactivate'
*you will need to activate venv in each terminal you want to use it*

#### Setup
Install FastAPI
'pip install fastapi`

Create a file named `main.py`
within file:
1. Import FastAPI
`from fastapi import FastAPI`

2. Import CORS
`from fastapi.middleware.cors import CORSMiddleware`

3. Decare app variable
`app = FastAPI()`

4. Add CORS middleware
```app.add_middleware(
    CORSMiddleware,
    # allow_origins val should be string array of allowed crossorigin requests
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

5. Define Routes
```@app.HTTPMETHOD("PATH/{PARAMS}")
       async def FUNCTION_TO_RUN(param, param_w_default_val = 0, optional_param = None):
          return {}

