---
UID: NE.iscsidef.PISCSI_DIGEST_TYPES
title: PISCSI_DIGEST_TYPES
author: windows-driver-content
description: The ISCSI_DIGEST_TYPES enumeration indicates the digest type.
old-location: storage\iscsi_digest_types.htm
ms.assetid: 0515dd76-ef1f-4f0f-a7d7-1b3b07e0523d
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
req.header: iscsidef.h
req.include-header: Iscsidef.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ISCSI_DIGEST_TYPES
req.alt-loc: iscsidef.h
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
ms.keywords: MSiSCSI_TCPIPConfig, MSiSCSI_TCPIPConfig, *PMSiSCSI_TCPIPConfig
req.iface: 
---

# PISCSI_DIGEST_TYPES enumeration



## -description
<p>The ISCSI_DIGEST_TYPES enumeration indicates the digest type.</p>


## -syntax

````
typedef enum  { 
  ISCSI_DIGEST_TYPE_NONE    = 0,
  ISCSI_DIGEST_TYPE_CRC32C  = 1
} ISCSI_DIGEST_TYPES, *PISCSI_DIGEST_TYPES;
````


## -enum-fields
<dl>

### -field <a id="ISCSI_DIGEST_TYPE_NONE"></a><a id="iscsi_digest_type_none"></a><b>ISCSI_DIGEST_TYPE_NONE</b>

<dd>
<p>There is no usable digest that guarantees data integrity. </p>
</dd>

### -field <a id="ISCSI_DIGEST_TYPE_CRC32C"></a><a id="iscsi_digest_type_crc32c"></a><b>ISCSI_DIGEST_TYPE_CRC32C</b>

<dd>
<p>The digest that guarantees data integrity uses a 32-bit cyclic redundancy check. </p>
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
<dt>Iscsidef.h (include Iscsidef.h)</dt>
</dl>
</td>
</tr>
</table>