---
UID: NS.windot11.DOT11_CHANNEL_HINT
title: DOT11_CHANNEL_HINT
author: windows-driver-content
description: The DOT11_CHANNEL_HINT structure describes suggested channel numbers for an NLO operation.
old-location: netvista\dot11_channel_hint.htm
old-project: netvista
ms.assetid: B3E395C3-C642-4A5E-9005-88323A80F90E
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: DOT11_CHANNEL_HINT, DOT11_CHANNEL_HINT, *PDOT11_CHANNEL_HINT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Windot11.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_CHANNEL_HINT
req.alt-loc: Windot11.h
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
req.product: Windows 10 or later.
---

# DOT11_CHANNEL_HINT structure



## -description

## -syntax

````
typedef struct _DOT11_CHANNEL_HINT {
  DOT11_PHY_TYPE Dot11PhyType;
  ULONG          uChannelNumber;
} DOT11_CHANNEL_HINT, *PDOT11_CHANNEL_HINT;
````


## -struct-fields
<dl>

### -field <b>Dot11PhyType</b>

<dd>
<p>The 802.11 PHY and media type.</p>
</dd>

### -field <b>uChannelNumber</b>

<dd>
<p>Channel number.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported in Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Windot11.h)</dt>
</dl>
</td>
</tr>
</table>