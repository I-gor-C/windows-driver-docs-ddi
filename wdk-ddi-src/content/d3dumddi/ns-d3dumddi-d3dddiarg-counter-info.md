---
UID: NS.d3dumddi.D3DDDIARG_COUNTER_INFO
title: D3DDDIARG_COUNTER_INFO
author: windows-driver-content
description: Describes info to manipulate counters.
old-location: display\d3dddiarg_counter_info.htm
old-project: display
ms.assetid: FB2B8FBF-908D-4668-8C5B-263903BA1EF5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_COUNTER_INFO, D3DDDIARG_COUNTER_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_COUNTER_INFO
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

# D3DDDIARG_COUNTER_INFO structure



## -description
<p>Describes info to manipulate counters.</p>


## -syntax

````
typedef struct D3DDDIARG_COUNTER_INFO {
  D3DDDIQUERYTYPE LastDeviceDependentCounter;
  UINT            NumSimultaneousCounters;
} D3DDDIARG_COUNTER_INFO;
````


## -struct-fields
<dl>

### -field LastDeviceDependentCounter

<dd>
<p>A value of type <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-createquery.md">D3DDDIQUERYTYPE</a> that identifies the largest device-dependent counter identifier that the device supports. If none are supported, the user-mode display driver must set the value to 0; otherwise, the driver sets the value to greater than or equal to  <b>D3DDDIQUERYTYPE_COUNTER_DEVICE_DEPENDENT</b>.</p>
</dd>

### -field NumSimultaneousCounters

<dd>
<p>The number of simultaneously active counters that the driver supports.</p>
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
<dt>D3dumddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>