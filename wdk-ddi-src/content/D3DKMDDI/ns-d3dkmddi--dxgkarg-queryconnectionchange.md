---
UID: NS.d3dkmddi._DXGKARG_QUERYCONNECTIONCHANGE
title: DXGKARG_QUERYCONNECTIONCHANGE
author: windows-driver-content
description: Used to hold the arguments for DXGKDDI_QUERYCONNECTIONCHANGE.
old-location: display\dxgkarg_queryconnectionchange.htm
ms.assetid: 6B91F3F0-B02D-46F3-9086-EA32F043FC16
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_QUERYCONNECTIONCHANGE
req.alt-loc: d3dkmddi.h
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
ms.keywords: DXGKARG_QUERYCONNECTIONCHANGE, DXGKARG_QUERYCONNECTIONCHANGE
req.iface: 
---

# DXGKARG_QUERYCONNECTIONCHANGE structure



## -description
<p>Used to hold the arguments for <a href="https://msdn.microsoft.com/8C09B692-3439-4ACD-942D-F7A107E2B4DA">DXGKDDI_QUERYCONNECTIONCHANGE</a>.</p>


## -syntax

````
typedef struct _DXGKARG_QUERYCONNECTIONCHANGE {
  DXGK_CONNECTION_CHANGE ConnectionChange;
} DXGKARG_QUERYCONNECTIONCHANGE;
````


## -struct-fields
<dl>

### -field <b>ConnectionChange</b>

<dd>
<p>[out] Buffer into which the oldest available change is copied by driver.</p>
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
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>