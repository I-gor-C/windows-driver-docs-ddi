---
UID: NE.wditypes._WDI_DATA_RATE_FLAGS
title: WDI_DATA_RATE_FLAGS
author: windows-driver-content
description: The WDI_DATA_RATE_FLAGS enumeration defines the data rate flags.
old-location: netvista\wdi_data_rate_flags.htm
old-project: netvista
ms.assetid: 937D1C48-AC5A-4D55-8722-BDC1192613A9
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_DATA_RATE_FLAGS
req.alt-loc: wditypes.hpp
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDI_DATA_RATE_FLAGS enumeration



## -description
<p>The WDI_DATA_RATE_FLAGS enumeration defines the data rate flags.</p>


## -syntax

````
typedef enum _WDI_DATA_RATE_FLAGS { 
  WDI_DATA_RATE_NON_STANDARD  = 0x01,
  WDI_DATA_RATE_RX_RATE       = 0x02,
  WDI_DATA_RATE_TX_RATE       = 0x04
} WDI_DATA_RATE_FLAGS;
````


## -enum-fields
<dl>

### -field WDI_DATA_RATE_NON_STANDARD

<dd>
<p>The data rate is not a standard data rate defined in the IEEE 802.11 standards.</p>
</dd>

### -field WDI_DATA_RATE_RX_RATE

<dd>
<p>The data rate can be used for RX.</p>
</dd>

### -field WDI_DATA_RATE_TX_RATE

<dd>
<p>The data rate can be used for TX.</p>
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
<dt>Wditypes.hpp</dt>
</dl>
</td>
</tr>
</table>