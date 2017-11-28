---
UID: NS.wiamicro._RANGEVALUE
title: RANGEVALUE
author: windows-driver-content
description: The RANGEVALUE structure is used by a microdriver to communicate to the WIA Flatbed driver the legal values for a microdriver function parameter.
old-location: image\rangevalue.htm
old-project: image
ms.assetid: 18322d1f-9fc9-43f0-925e-616731845792
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RANGEVALUE, RANGEVALUE, *PRANGEVALUE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wiamicro.h
req.include-header: Wiamicro.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RANGEVALUE
req.alt-loc: wiamicro.h
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

# RANGEVALUE structure



## -description
<p>The RANGEVALUE structure is used by a microdriver to communicate to the WIA Flatbed driver the legal values for a microdriver function parameter.</p>


## -syntax

````
typedef struct _RANGEVALUE {
  LONG lMin;
  LONG lMax;
  LONG lStep;
} RANGEVALUE, *PRANGEVALUE;
````


## -struct-fields
<dl>

### -field <b>lMin</b>

<dd>
<p>Specifies the minimum value for a parameter.</p>
</dd>

### -field <b>lMax</b>

<dd>
<p>Specifies the maximum value for a parameter.</p>
</dd>

### -field <b>lStep</b>

<dd>
<p>Specifies the step value for a parameter.</p>
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
<p>Available in Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamicro.h (include Wiamicro.h)</dt>
</dl>
</td>
</tr>
</table>