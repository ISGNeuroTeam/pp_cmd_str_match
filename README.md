# pp_cmd_str_match
Postprocessing command `str_match`

## Description
`str_match` finds strings or regular expression in columns. If several columns are passed then result dataframe include all matches for all columns

### Arguments
- vals - infinite keyword argument, where key is column name and value is string (character sequence or regular expression)

### Usage example
Input dataframe:  
```
        a          b           c
0   ab11c       dfag  bbbl33asdd
1     zdf  fffa22fff     znowaty
2  zd111f  fffa22fff   zno33waty
```
Row at index `2` has `c` value that starts with `zno33`:  
```
query: readFile test.csv | str_match  c="zno33"
        a          b          c
2  zd111f  fffa22fff  zno33waty
```
Rows at index `0` and `2` has values matched by regular expression:  
```
query: readFile test.csv | str_match a=".*11.*"
        a          b           c
0   ab11c       dfag  bbbl33asdd
2  zd111f  fffa22fff   zno33waty
```
Row at index 0 matched by first regular expression and row at index 2 matched by second:  
```

query: readFile test.csv | str_match a=".*c", c="^zno3"
        a          b           c
0   ab11c       dfag  bbbl33asdd
2  zd111f  fffa22fff   zno33waty
```


## Getting started
### Installing
1. Create virtual environment with post-processing sdk 
```bash
    make dev
```
That command  
- downloads [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- creates python virtual environment with [postprocessing_sdk](https://github.com/ISGNeuroTeam/postprocessing_sdk)
- creates link to current command in postprocessing `pp_cmd` directory 

2. Configure `otl_v1` command. Example:  
```bash
    vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/otl_v1/config.ini
```
Config example:  
```ini
[spark]
base_address = http://localhost
username = admin
password = 12345678

[caching]
# 24 hours in seconds
login_cache_ttl = 86400
# Command syntax defaults
default_request_cache_ttl = 100
default_job_timeout = 100
```

3. Configure storages for `readFile` and `writeFile` commands:  
```bash
   vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/readFile/config.ini
   
```
Config example:  
```ini
[storages]
lookups = /opt/otp/lookups
pp_shared = /opt/otp/shared_storage/persistent
```

### Run str_match
Use `pp` to run str_match command:  
```bash
pp
Storage directory is /tmp/pp_cmd_test/storage
Commmands directory is /tmp/pp_cmd_test/pp_cmd
query: | otl_v1 <# makeresults count=100 #> |  str_match 
```
## Deploy
Unpack archive `pp_cmd_str_match` to postprocessing commands directory

