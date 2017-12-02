---
UID: NS.d3dumddi._D3DDDI_FRAMELATENCYESCAPE
title: D3DDDI_FRAMELATENCYESCAPE
author: windows-driver-content
description: Specifies an app's maximum frame latency.
old-location: display\d3dddi_framelatencyescape.htm
old-project: display
ms.assetid: 19395349-375E-46AF-BCCF-FF5C92B374C4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDI_FRAMELATENCYESCAPE, D3DDDI_FRAMELATENCYESCAPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDI_FRAMELATENCYESCAPE
req.alt-loc: D3dumddi.h
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
---

# D3DDDI_FRAMELATENCYESCAPE structure



## -description
<p>Specifies an app's maximum frame latency.</p>


## -syntax

````
typedef struct _D3DDDI_FRAMELATENCYESCAPE {
  UINT RequestedLatency;
} D3DDDI_FRAMELATENCYESCAPE;
````


## -struct-fields
<dl>

### -field RequestedLatency

<dd>
<p>[in] The frame latency requested by the driver, specified as the number of frames that are allowed to be stored in a queue, before submission for rendering.</p>
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
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>