---
UID: NS.dot11wdi._WDI_MAC_ADDRESS~r1
title: WDI_MAC_ADDRESS
author: windows-driver-content
description: The WDI_MAC_ADDRESS structure defines an IEEE media access control (MAC) address.
old-location: netvista\wdi_mac_address.htm
old-project: netvista
ms.assetid: e170b797-f8bb-4d3c-a3ee-5fd1a817a500
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDI_MAC_ADDRESS,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dot11wdi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_MAC_ADDRESS
req.alt-loc: dot11wdi.h
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

# WDI_MAC_ADDRESS structure



## -description
<p>The 
  WDI_MAC_ADDRESS structure defines an IEEE media access control (MAC) address.</p>


## -syntax

````
typedef struct _WDI_MAC_ADDRESS {
  UINT8 Address[6];
} WDI_MAC_ADDRESS, *PWDI_MAC_ADDRESS;
````


## -struct-fields
<dl>

### -field <b>Address</b>

<dd>
<p>A Wi-Fi MAC address.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>