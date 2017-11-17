---
UID: NS.bdatypes._BDA_ETHERNET_ADDRESS
title: BDA_ETHERNET_ADDRESS
author: windows-driver-content
description: TBD.
old-location: stream\bda_ethernet_address.htm
ms.assetid: F4B9A413-7FB5-4CA3-9731-A143CB0D7346
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: bdatypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_ETHERNET_ADDRESS
req.alt-loc: 
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
ms.keywords: BDA_ETHERNET_ADDRESS, BDA_ETHERNET_ADDRESS, *PBDA_ETHERNET_ADDRESS
req.iface: 
---

# BDA_ETHERNET_ADDRESS structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct _BDA_ETHERNET_ADDRESS {
  BYTE rgbAddress[6];
} BDA_ETHERNET_ADDRESS, *PBDA_ETHERNET_ADDRESS;
````


## -struct-fields
<dl>

### -field <b>rgbAddress</b>

<dd>
<p>TBD</p>
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
<dt>Bdatypes.h</dt>
</dl>
</td>
</tr>
</table>