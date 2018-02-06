---
UID: NE:storport._STOR_CRYPTO_KEY_SIZE
title: "_STOR_CRYPTO_KEY_SIZE"
author: windows-driver-content
description: Reserved for system use.
old-location: storage\stor_crypto_key_size.htm
old-project: storage
ms.assetid: 5CBE8A2B-E2E1-4B76-A76F-51DA9F301DAA
ms.author: windowsdriverdev
ms.date: 1/10/2018
ms.keywords: storport/PSTOR_CRYPTO_KEY_SIZE, *PSTOR_CRYPTO_KEY_SIZE, PSTOR_CRYPTO_KEY_SIZE enumeration pointer [Storage Devices], PSTOR_CRYPTO_KEY_SIZE, storage.stor_crypto_key_size, STOR_CRYPTO_KEY_SIZE, storport/STOR_CRYPTO_KEY_SIZE, _STOR_CRYPTO_KEY_SIZE, STOR_CRYPTO_KEY_SIZE enumeration [Storage Devices], storport/
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: storport.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Storport.h
apiname:
-	STOR_CRYPTO_KEY_SIZE
product: Windows
targetos: Windows
req.typenames: STOR_CRYPTO_KEY_SIZE, *PSTOR_CRYPTO_KEY_SIZE
req.product: Windows 10 or later.
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
| **Header** | storport.h |