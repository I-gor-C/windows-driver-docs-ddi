---
UID: NS.BDATYPES._BDA_IPV6_ADDRESS
title: _BDA_IPv6_ADDRESS
author: windows-driver-content
description: .
old-location: stream\bda_ipv6_address.htm
old-project: stream
ms.assetid: 50D52380-1FBE-4046-A7DC-8415501D7FA6
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _BDA_IPv6_ADDRESS, BDA_IPv6_ADDRESS, *PBDA_IPv6_ADDRESS
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
---

# _BDA_IPv6_ADDRESS structure



## -description




## -syntax

````
typedef struct _BDA_IPv6_ADDRESS {
  BYTE rgbAddress[6];
} BDA_IPv6_ADDRESS, *PBDA_IPv6_ADDRESS;
````


## -struct-fields

### -field rgbAddress


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Bdatypes.h</dt>
</dl>
</td>
</tr>
</table>