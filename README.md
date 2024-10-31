## Note
This Python project implements Tencent-RTC's UserSig authentication, providing a secure server-side method for generating signatures to protect the keys from leakage.

![](https://cloudcache.intl.tencent-cloud.com/cms/backend-cms/12569f72920411ef810152540055f650.png)

## Integration
It can be integrated using pip or source code.

#### pip
```shell
pip install tls-sig-api-v2
```

#### source code
Just download the file `TLSSigAPIv2.py` to the local.

## Usage

``` python
import TLSSigAPIv2

api = TLSSigAPIv2.TLSSigAPIv2(1400000000, '5bd2850fff3ecb11d7c805251c51ee463a25727bddc2385f3fa8bfee1bb93b5e')
sig = api.gen_sig("xiaojun")
print(sig)
```
