---
UID: NS.bdatypes._BDA_IPv4_ADDRESS
title: BDA_IPv4_ADDRESS
author: windows-driver-content
description: .
old-location: stream\bda_ipv4_address.htm
old-project: stream
ms.assetid: 5206CEEB-C1EF-4AE0-B4BC-52E8D85AD706
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: BDA_IPv4_ADDRESS, BDA_IPv4_ADDRESS, *PBDA_IPv4_ADDRESS
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
req.alt-api: BDA_IPv4_ADDRESS
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

# BDA_IPv4_ADDRESS structure



## -description
<p></p>


## -syntax

````
typedef struct _BDA_IPv4_ADDRESS {
  BYTE rgbAddress[4];
} BDA_IPv4_ADDRESS, *PBDA_IPv4_ADDRESS;
````


## -struct-fields
<dl>

### -field <b>rgbAddress</b>

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