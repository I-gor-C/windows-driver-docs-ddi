---
UID : NE:storport._STOR_CRYPTO_KEY_SIZE
title : _STOR_CRYPTO_KEY_SIZE
author : windows-driver-content
description : Reserved for system use.
old-location : storage\stor_crypto_key_size.htm
old-project : storage
ms.assetid : 5CBE8A2B-E2E1-4B76-A76F-51DA9F301DAA
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : STOR_CRYPTO_KEY_SIZE, PSTOR_CRYPTO_KEY_SIZE, *PSTOR_CRYPTO_KEY_SIZE, STOR_CRYPTO_KEY_SIZE enumeration [Storage Devices], storage.stor_crypto_key_size, storport/PSTOR_CRYPTO_KEY_SIZE, PSTOR_CRYPTO_KEY_SIZE enumeration pointer [Storage Devices], _STOR_CRYPTO_KEY_SIZE, storport/, storport/STOR_CRYPTO_KEY_SIZE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : storport.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PSTOR_CRYPTO_KEY_SIZE, STOR_CRYPTO_KEY_SIZE"
req.product : Windows 10 or later.
---

# _STOR_CRYPTO_KEY_SIZE Enumeration
Reserved for system use.

## Syntax
````
typedef enum _STOR_CRYPTO_KEY_SIZE { 
    = 
} STOR_CRYPTO_KEY_SIZE, *PSTOR_CRYPTO_KEY_SIZE;
````

## Constants

<table>

<tr>
<td>StorCryptoKeySize128Bits</td>
<td></td>
</tr>

<tr>
<td>StorCryptoKeySize192Bits</td>
<td></td>
</tr>

<tr>
<td>StorCryptoKeySize256Bits</td>
<td></td>
</tr>

<tr>
<td>StorCryptoKeySize512Bits</td>
<td></td>
</tr>

<tr>
<td>StorCryptoKeySizeMax</td>
<td></td>
</tr>

<tr>
<td>StorCryptoKeySizeUnknown</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | storport.h |