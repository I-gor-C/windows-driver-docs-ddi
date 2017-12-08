---
UID: NS.windot11._DOT11_WFD_GO_INTENT
title: DOT11_WFD_GO_INTENT
author: windows-driver-content
description: The DOT11_WFD_GO_INTENT structure represents the Group Intent value used during Group Owner Negotiation
old-location: netvista\_dot11_wfd_go_intent.htm
old-project: netvista
ms.assetid: 8E4F88EF-04A9-4313-AE6A-2467DA08044A
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DOT11_WFD_GO_INTENT,
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
req.alt-api: DOT11_WFD_GO_INTENT
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

# DOT11_WFD_GO_INTENT structure



## -description

## -syntax

````
typedef struct _DOT11_WFD_GO_INTENT {
  UCHAR TieBreaker:1;
  UCHAR Intent:7;
} DOT11_WFD_GO_INTENT, *PDOT11_WFD_GO_INTENT;
````


## -struct-fields
<dl>

### -field TieBreaker:1

<dd>
<p>If set, indicates that group ownership is granted.</p>
</dd>

### -field Intent:7

<dd>
<p>Group ownership intent level. The value of the local device intent is compared to the remote device intent to negociate ownership.</p>
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