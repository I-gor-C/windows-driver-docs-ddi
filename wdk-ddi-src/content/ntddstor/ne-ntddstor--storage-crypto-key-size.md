---
UID: NE.ntddstor._STORAGE_CRYPTO_KEY_SIZE
title: STORAGE_CRYPTO_KEY_SIZE
author: windows-driver-content
description: The STORAGE_CRYPTO_KEY_SIZE enum returns the Size of the key in bits.
old-location: storage\storage_crypto_key_size.htm
old-project: storage
ms.assetid: C3E5CEC6-34A2-48DF-B963-677C69A97E0B
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
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
req.alt-api: STORAGE_CRYPTO_KEY_SIZE, *PSTORAGE_CRYPTO_KEY_SIZE
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
req.iface: 
---

# STORAGE_CRYPTO_KEY_SIZE enumeration



## -description
<p>The <b>STORAGE_CRYPTO_KEY_SIZE</b> enum returns the Size of the key in bits.</p>


## -syntax

````
typedef enum _STORAGE_CRYPTO_KEY_SIZE { 
  StorageCryptoKeySizeUnknown  = 0,
  StorageCryptoKeySize128Bits  = 1,
  StorageCryptoKeySize192Bits,
  StorageCryptoKeySize256Bits,
  StorageCryptoKeySize512Bits
} STORAGE_CRYPTO_KEY_SIZE, *PSTORAGE_CRYPTO_KEY_SIZE;
````


## -enum-fields
<dl>

### -field StorageCryptoKeySizeUnknown

<dd>
<p>Reserved for system use.</p>
</dd>

### -field StorageCryptoKeySize128Bits

<dd>
<p>Reserved for system use.</p>
</dd>

### -field StorageCryptoKeySize192Bits

<dd>
<p>Reserved for system use.</p>
</dd>

### -field StorageCryptoKeySize256Bits

<dd>
<p>Reserved for system use.</p>
</dd>

### -field StorageCryptoKeySize512Bits

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