---
UID: NS.dot11wdi._TAL_TXRX_PARAMETERS
title: TAL_TXRX_PARAMETERS
author: windows-driver-content
description: The TAL_TXRX_PARAMETERS structure defines the TAL TXRX parameters.
old-location: netvista\tal_txrx_parameters.htm
old-project: netvista
ms.assetid: 44f5c907-7368-43ea-b581-3b9ecf25c611
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: TAL_TXRX_PARAMETERS, TAL_TXRX_PARAMETERS, *PTAL_TXRX_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dot11wdi.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TAL_TXRX_PARAMETERS
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

# TAL_TXRX_PARAMETERS structure



## -description
<p>The 
  TAL_TXRX_PARAMETERS structure defines the TAL TXRX parameters.</p>


## -syntax

````
typedef struct _TAL_TXRX_PARAMETERS {
  UINT16 MaxOutstandingTransfers;
} TAL_TXRX_PARAMETERS, *PTAL_TXRX_PARAMETERS;
````


## -struct-fields
<dl>

### -field MaxOutstandingTransfers

<dd>
<p>Specifies the maximum number of outstanding  frame transfers to the target. No further frames are transferred until a transfer complete indication is received from the target/TAL.</p>
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
<dt>Dot11wdi.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>