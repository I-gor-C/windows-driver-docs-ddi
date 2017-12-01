---
UID: NS.nfcsedev._SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD
title: SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD
author: windows-driver-content
description: .
old-location: nfpdrivers\secure_element_hce_activation_payload.htm
old-project: nfpdrivers
ms.assetid: 2FFEB2DB-7506-4CDB-BD5F-41D2E4212017
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD, SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD, *PSECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: nfcsedev.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD
req.alt-loc: nfcsedev.h
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

# SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD structure



## -description
<p></p>


## -syntax

````
typedef struct _SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD {
  USHORT bConnectionId;
  BYTE   eRfTechType;
  BYTE   eRfProtocolType;
} SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD, *PSECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD;
````


## -struct-fields
<dl>

### -field <b>bConnectionId</b>

<dd>
<p>Unique identifer for current connection.</p>
</dd>

### -field <b>eRfTechType</b>

<dd>
<p>NFC Forum RF technology type.
</p>
</dd>

### -field <b>eRfProtocolType</b>

<dd>
<p>NFC Forum RF protocol
type.</p>
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
<dt>Nfcsedev.h</dt>
</dl>
</td>
</tr>
</table>