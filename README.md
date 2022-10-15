## I created whl file of my code name as 
```
excelDataManipulation-0.0.1-py3-none-any.whl
```

## we can directly install this whl file and run the main.py file which will create a required output file at ".//sampleInOutFiles//OptFile.xlsx" location

```
pip install excelDataManipulation-0.0.1-py3-none-any.whl
py main.py
```

## If you want to install from the scratch then please follow this below commands.
### NOTE: below commands are valid for Windows OS only
```
git init
git clone https://github.com/amitsahuit/ExcepDatamanipulationProject.git
py -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
cd src\excelDataManipulation\
py main.py
```

