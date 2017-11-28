---
UID: NE.ntddstor._STORAGE_CRYPTO_ALGORITHM_ID
title: STORAGE_CRYPTO_ALGORITHM_ID
author: windows-driver-content
description: The STORAGE_CRYPTO_ALGORITHM_ID enum provides an output buffer for StorageAdapterCryptoProperty and PropertyStandardQuery.
old-location: storage\storage_crypto_algorithm_id.htm
old-project: storage
ms.assetid: 5D1CCF3D-D677-47B0-9C7B-7E35C649A7D5
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
req.alt-api: STORAGE_CRYPTO_ALGORITHM_ID, *PSTORAGE_CRYPTO_ALGORITHM_ID
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

# STORAGE_CRYPTO_ALGORITHM_ID enumeration



## -description
<p>The <b>STORAGE_CRYPTO_ALGORITHM_ID</b> enum provides an output buffer for <b>StorageAdapterCryptoProperty</b> and <b>PropertyStandardQuery</b>.</p>


## -syntax

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


## -enum-fields
<dl>

### -field <a id="StorageCryptoAlgorithmUnknown"></a><a id="storagecryptoalgorithmunknown"></a><a id="STORAGECRYPTOALGORITHMUNKNOWN"></a><b>StorageCryptoAlgorithmUnknown</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="StorageCryptoAlgorithmXTSAES"></a><a id="storagecryptoalgorithmxtsaes"></a><a id="STORAGECRYPTOALGORITHMXTSAES"></a><b>StorageCryptoAlgorithmXTSAES</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="StorageCryptoAlgorithmBitlockerAESCBC"></a><a id="storagecryptoalgorithmbitlockeraescbc"></a><a id="STORAGECRYPTOALGORITHMBITLOCKERAESCBC"></a><b>StorageCryptoAlgorithmBitlockerAESCBC</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="StorageCryptoAlgorithmAESECB"></a><a id="storagecryptoalgorithmaesecb"></a><a id="STORAGECRYPTOALGORITHMAESECB"></a><b>StorageCryptoAlgorithmAESECB</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="StorageCryptoAlgorithmESSIVAESCBC"></a><a id="storagecryptoalgorithmessivaescbc"></a><a id="STORAGECRYPTOALGORITHMESSIVAESCBC"></a><b>StorageCryptoAlgorithmESSIVAESCBC</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="StorageCryptoAlgorithmMax"></a><a id="storagecryptoalgorithmmax"></a><a id="STORAGECRYPTOALGORITHMMAX"></a><b>StorageCryptoAlgorithmMax</b>

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