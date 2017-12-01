---
UID: NS.dot11wdi._WDI_TXRX_PARAMETERS
title: WDI_TXRX_PARAMETERS
author: windows-driver-content
description: The WDI_TXRX_PARAMETERS structure defines the parameters that are passed down to the TXRX component.
old-location: netvista\wdi_txrx_parameters.htm
old-project: netvista
ms.assetid: 839a1c3d-ac9f-4723-a0f1-6610b763c32a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TXRX_PARAMETERS, WDI_TXRX_PARAMETERS, *PWDI_TXRX_PARAMETERS
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
req.alt-api: WDI_TXRX_PARAMETERS
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

# WDI_TXRX_PARAMETERS structure



## -description
<p>The 
  WDI_TXRX_PARAMETERS structure defines the parameters that are passed down to the TXRX component.</p>


## -syntax

````
typedef struct _WDI_TXRX_PARAMETERS {
  WDI_TXRX_CAPABILITIES TxRxCapabilities;
} WDI_TXRX_PARAMETERS, *PWDI_TXRX_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>TxRxCapabilities</b>

<dd>
<p>Specifies the TXRX capabilities.</p>
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