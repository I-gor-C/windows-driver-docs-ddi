---
UID: NE:ntddstor._STORAGE_CRYPTO_ALGORITHM_ID
title: "_STORAGE_CRYPTO_ALGORITHM_ID"
author: windows-driver-content
description: The STORAGE_CRYPTO_ALGORITHM_ID enum provides an output buffer for StorageAdapterCryptoProperty and PropertyStandardQuery.
old-location: storage\storage_crypto_algorithm_id.htm
old-project: storage
ms.assetid: 5D1CCF3D-D677-47B0-9C7B-7E35C649A7D5
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PSTORAGE_CRYPTO_ALGORITHM_ID, STORAGE_CRYPTO_ALGORITHM_ID, STORAGE_CRYPTO_ALGORITHM_ID enumeration [Storage Devices], STORAGE_CRYPTO_ALGORITHM_ID, *PSTORAGE_CRYPTO_ALGORITHM_ID, STORAGE_CRYPTO_ALGORITHM_ID, *PSTORAGE_CRYPTO_ALGORITHM_ID enumeration [Storage Devices], StorageCryptoAlgorithmAESECB, StorageCryptoAlgorithmBitlockerAESCBC, StorageCryptoAlgorithmESSIVAESCBC, StorageCryptoAlgorithmMax, StorageCryptoAlgorithmUnknown, StorageCryptoAlgorithmXTSAES, _STORAGE_CRYPTO_ALGORITHM_ID, ntddstor/STORAGE_CRYPTO_ALGORITHM_ID, ntddstor/StorageCryptoAlgorithmAESECB, ntddstor/StorageCryptoAlgorithmBitlockerAESCBC, ntddstor/StorageCryptoAlgorithmESSIVAESCBC, ntddstor/StorageCryptoAlgorithmMax, ntddstor/StorageCryptoAlgorithmUnknown, ntddstor/StorageCryptoAlgorithmXTSAES, storage.storage_crypto_algorithm_id"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddstor.h
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ntddstor.h
api_name:
-	STORAGE_CRYPTO_ALGORITHM_ID, *PSTORAGE_CRYPTO_ALGORITHM_ID
product: Windows
targetos: Windows
req.typenames: STORAGE_CRYPTO_ALGORITHM_ID, *PSTORAGE_CRYPTO_ALGORITHM_ID
---

# _STORAGE_CRYPTO_ALGORITHM_ID Enumeration
The <b>STORAGE_CRYPTO_ALGORITHM_ID</b> enum provides an output buffer for <b>StorageAdapterCryptoProperty</b> and <b>PropertyStandardQuery</b>.

## Syntax
```
typedef enum _STORAGE_CRYPTO_ALGORITHM_ID {
  StorageCryptoAlgorithmUnknown          ,
  StorageCryptoAlgorithmXTSAES           ,
  StorageCryptoAlgorithmBitlockerAESCBC  ,
  StorageCryptoAlgorithmAESECB           ,
  StorageCryptoAlgorithmESSIVAESCBC      ,
  StorageCryptoAlgorithmMax
} *PSTORAGE_CRYPTO_ALGORITHM_ID, STORAGE_CRYPTO_ALGORITHM_ID;
```

## Constants

<table>
            
                <tr>
                    <td>StorageCryptoAlgorithmUnknown</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>StorageCryptoAlgorithmXTSAES</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>StorageCryptoAlgorithmBitlockerAESCBC</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>StorageCryptoAlgorithmAESECB</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>StorageCryptoAlgorithmESSIVAESCBC</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>StorageCryptoAlgorithmMax</td>
                    <td>Reserved for system use.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddstor.h |