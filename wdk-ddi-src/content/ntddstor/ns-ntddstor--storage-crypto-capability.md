---
UID: NS.ntddstor._STORAGE_CRYPTO_CAPABILITY
title: STORAGE_CRYPTO_CAPABILITY
author: windows-driver-content
description: Reserved for system use.
old-location: storage\storage_crypto_capability.htm
ms.assetid: 9DFAB3C6-F833-487D-87FC-292B3AFAD767
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddstor.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_CRYPTO_CAPABILITY
req.alt-loc: Ntddstor.h
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
ms.keywords: STORAGE_CRYPTO_CAPABILITY, STORAGE_CRYPTO_CAPABILITY, *PSTORAGE_CRYPTO_CAPABILITY
req.iface: 
---

# STORAGE_CRYPTO_CAPABILITY structure



## -description
<p>Reserved for system use.</p>


## -syntax

````
typedef struct _STORAGE_CRYPTO_CAPABILITY {
  ULONG                       Version;
  ULONG                       Size;
  ULONG                       CryptoCapabilityIndex;
  STORAGE_CRYPTO_ALGORITHM_ID AlgorithmId;
  STORAGE_CRYPTO_KEY_SIZE     KeySize;
  ULONG                       DataUnitSizeBitmask;
} STORAGE_CRYPTO_CAPABILITY, *PSTORAGE_CRYPTO_CAPABILITY;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>CryptoCapabilityIndex</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>AlgorithmId</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>KeySize</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>DataUnitSizeBitmask</b>

<dd>
<p>Reserved for system use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h</dt>
</dl>
</td>
</tr>
</table>