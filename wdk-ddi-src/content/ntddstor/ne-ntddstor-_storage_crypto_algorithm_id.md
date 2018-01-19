---
UID : NE:ntddstor._STORAGE_CRYPTO_ALGORITHM_ID
title : _STORAGE_CRYPTO_ALGORITHM_ID
author : windows-driver-content
description : The STORAGE_CRYPTO_ALGORITHM_ID enum provides an output buffer for StorageAdapterCryptoProperty and PropertyStandardQuery.
old-location : storage\storage_crypto_algorithm_id.htm
old-project : storage
ms.assetid : 5D1CCF3D-D677-47B0-9C7B-7E35C649A7D5
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _STORAGE_CRYPTO_ALGORITHM_ID, STORAGE_CRYPTO_ALGORITHM_ID, *PSTORAGE_CRYPTO_ALGORITHM_ID
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntddstor.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : STORAGE_CRYPTO_ALGORITHM_ID, *PSTORAGE_CRYPTO_ALGORITHM_ID
req.alt-loc : Ntddstor.h
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
req.typenames : STORAGE_CRYPTO_ALGORITHM_ID, *PSTORAGE_CRYPTO_ALGORITHM_ID
---

# _STORAGE_CRYPTO_ALGORITHM_ID Enumeration
The <b>STORAGE_CRYPTO_ALGORITHM_ID</b> enum provides an output buffer for <b>StorageAdapterCryptoProperty</b> and <b>PropertyStandardQuery</b>.

## Syntax
````
typedef enum _STORAGE_CRYPTO_ALGORITHM_ID { 
  StorageCryptoAlgorithmUnknown          = 0,
  StorageCryptoAlgorithmXTSAES           = 1,
  StorageCryptoAlgorithmBitlockerAESCBC,
  StorageCryptoAlgorithmAESECB,
  StorageCryptoAlgorithmESSIVAESCBC,
  StorageCryptoAlgorithmMax
} STORAGE_CRYPTO_ALGORITHM_ID, *PSTORAGE_CRYPTO_ALGORITHM_ID;
````

## Constants

<table>

<tr>
<td>StorageCryptoAlgorithmAESECB</td>
<td>Reserved for system use.</td>
</tr>

<tr>
<td>StorageCryptoAlgorithmBitlockerAESCBC</td>
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

<tr>
<td>StorageCryptoAlgorithmUnknown</td>
<td>Reserved for system use.</td>
</tr>

<tr>
<td>StorageCryptoAlgorithmXTSAES</td>
<td>Reserved for system use.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddstor.h |