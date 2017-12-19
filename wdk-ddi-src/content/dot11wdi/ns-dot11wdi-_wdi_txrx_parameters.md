---
UID: NS.DOT11WDI._WDI_TXRX_PARAMETERS
title: _WDI_TXRX_PARAMETERS
author: windows-driver-content
description: The WDI_TXRX_PARAMETERS structure defines the parameters that are passed down to the TXRX component.
old-location: netvista\wdi_txrx_parameters.htm
old-project: NetVista
ms.assetid: 839a1c3d-ac9f-4723-a0f1-6610b763c32a
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: _WDI_TXRX_PARAMETERS, PWDI_TXRX_PARAMETERS, *PWDI_TXRX_PARAMETERS, WDI_TXRX_PARAMETERS
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
---

# _WDI_TXRX_PARAMETERS structure



## -description
The 
  WDI_TXRX_PARAMETERS structure defines the parameters that are passed down to the TXRX component.



## -syntax

````
typedef struct _WDI_TXRX_PARAMETERS {
  WDI_TXRX_CAPABILITIES TxRxCapabilities;
} WDI_TXRX_PARAMETERS, *PWDI_TXRX_PARAMETERS;
````


## -struct-fields

### -field TxRxCapabilities

Specifies the TXRX capabilities.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 10

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2016

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Dot11wdi.h</dt>
</dl>
</td>
</tr>
</table>