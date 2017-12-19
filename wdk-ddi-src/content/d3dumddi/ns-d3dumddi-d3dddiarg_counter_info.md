---
UID: NS.D3DUMDDI.D3DDDIARG_COUNTER_INFO
title: D3DDDIARG_COUNTER_INFO
author: windows-driver-content
description: Describes info to manipulate counters.
old-location: display\d3dddiarg_counter_info.htm
old-project: display
ms.assetid: FB2B8FBF-908D-4668-8C5B-263903BA1EF5
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
---

# D3DDDIARG_COUNTER_INFO structure



## -description
Describes info to manipulate counters.



## -syntax

````
typedef struct D3DDDIARG_COUNTER_INFO {
  D3DDDIQUERYTYPE LastDeviceDependentCounter;
  UINT            NumSimultaneousCounters;
} D3DDDIARG_COUNTER_INFO;
````


## -struct-fields

### -field LastDeviceDependentCounter

A value of type <a href="display.d3dddiarg_createquery">D3DDDIQUERYTYPE</a> that identifies the largest device-dependent counter identifier that the device supports. If none are supported, the user-mode display driver must set the value to 0; otherwise, the driver sets the value to greater than or equal to  <b>D3DDDIQUERYTYPE_COUNTER_DEVICE_DEPENDENT</b>.


### -field NumSimultaneousCounters

The number of simultaneously active counters that the driver supports.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 8.1

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2012 R2

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>