# s3-mfa-delete

Enable MFA delete on S3 buckets

## Requirements
(1) Root access to the AWS account containing the S3 bucket(with hardware MFA token)  
(2) Python 3  
(3) Python Virtualenvwrapper, for building the executable or running the script directly  


## Usage
```
(1) Log into AWS account as root (requires the hardware )

(2) Create a temporary access key id and secret access key for the root account

(3) Run CLI tool

export AWS_ACCESS_KEY_ID=<access key id>
export AWS_SECRET_ACCESS_KEY=<secret access key>
s3-mfa-delete

(4) Step through wizard

$ s3-mfa-delete
Bucket name: <S3 bucket name>
MFA delete(enable/disable)? [enable]: enable
MFA serial number: <serial number of hardware MFA token in the AWS console>
MFA token: <MFA token from the hardware MFA token

(5) Delete temporary access key id and secret access key for the root account

```


## Build executable
```
(1) Setup Python virtualenv
make setup

(2) Activate Python virtualenv
workon s3-mfa-delete

(3) Build executable
make executable

s3-mfa-delete CLI tool executable is created in the '/dist' directory. The executable runs on the OS which compiled it

```

## MFA Delete status using CLI
```

aws s3api get-bucket-versioning \
    --bucket <S3 bucket name>
```



## Authors
* [Brian Macauley](https://github.com/bmacauley) &lt;brian.macauley@gmail.com&gt;

## License
[MIT](/LICENSE)
