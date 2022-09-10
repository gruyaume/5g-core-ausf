# 5g-core-ausf

> **Warning**: This project is under construction!

The Network Function (NF) Authentication Server Function (AUSF) is the network entity in the 5G Core Network
(5GC) supporting the following functionalities:
- Authenticate the UE for the requester NF,
- Provide keying material to the requester NF,
- Protect the Steering Information List for the requester NF.


## Usage

Run AUSF using docker:

```bash
docker pull ghcr.io/gruyaume/5g-core-ausf:main
docker run -p 8082:80 ghcr.io/gruyaume/5g-core-ausf:main
```

## Reference

### API Framework

This project leverages [FastAPI](https://github.com/tiangolo/full-stack-fastapi-postgresql) web
  framework. 

### 5G Specification

This service has been created following the 
[ETSI specification for the AUSF](https://www.etsi.org/deliver/etsi_ts/129500_129599/129509/16.04.00_60/ts_129509v160400p.pdf).
Some common data models are also taken from this [specification sheet](https://www.etsi.org/deliver/etsi_ts/129500_129599/129571/15.03.00_60/ts_129571v150300p.pdf) from ETSI.
