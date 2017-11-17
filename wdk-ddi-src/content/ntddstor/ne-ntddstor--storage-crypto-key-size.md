---
UID: NE.ntddstor._STORAGE_CRYPTO_KEY_SIZE
title: STORAGE_CRYPTO_KEY_SIZE
author: windows-driver-content
description: The STORAGE_CRYPTO_KEY_SIZE enum returns the Size of the key in bits.
old-location: storage\storage_crypto_key_size.htm
ms.assetid: C3E5CEC6-34A2-48DF-B963-677C69A97E0B
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
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
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
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

### -field <a id="StorageCryptoKeySizeUnknown"></a><a id="storagecryptokeysizeunknown"></a><a id="STORAGECRYPTOKEYSIZEUNKNOWN"></a><b>StorageCryptoKeySizeUnknown</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="StorageCryptoKeySize128Bits"></a><a id="storagecryptokeysize128bits"></a><a id="STORAGECRYPTOKEYSIZE128BITS"></a><b>StorageCryptoKeySize128Bits</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="StorageCryptoKeySize192Bits"></a><a id="storagecryptokeysize192bits"></a><a id="STORAGECRYPTOKEYSIZE192BITS"></a><b>StorageCryptoKeySize192Bits</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="StorageCryptoKeySize256Bits"></a><a id="storagecryptokeysize256bits"></a><a id="STORAGECRYPTOKEYSIZE256BITS"></a><b>StorageCryptoKeySize256Bits</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="StorageCryptoKeySize512Bits"></a><a id="storagecryptokeysize512bits"></a><a id="STORAGECRYPTOKEYSIZE512BITS"></a><b>StorageCryptoKeySize512Bits</b>

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