---
UID: NS.bdatypes._BDA_IPv6_ADDRESS
title: BDA_IPv6_ADDRESS
author: windows-driver-content
description: .
old-location: stream\bda_ipv6_address.htm
old-project: stream
ms.assetid: 50D52380-1FBE-4046-A7DC-8415501D7FA6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BDA_IPv6_ADDRESS, BDA_IPv6_ADDRESS, *PBDA_IPv6_ADDRESS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bdatypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_IPv6_ADDRESS
req.alt-loc: Bdatypes.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# BDA_IPv6_ADDRESS structure



## -description
<p></p>


## -syntax

````
typedef struct _BDA_IPv6_ADDRESS {
  BYTE rgbAddress[6];
} BDA_IPv6_ADDRESS, *PBDA_IPv6_ADDRESS;
````


## -struct-fields
<dl>

### -field rgbAddress

<dd></dd>
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
<dt>Bdatypes.h</dt>
</dl>
</td>
</tr>
</table>