---
UID: NS.dxva._DXVA_Frequency
title: DXVA_Frequency
author: windows-driver-content
description: The DXVA_Frequency structure is sent by the host decoder to the driver to specify the video frame rate, in Hz. For example, NTSC TV is 60000 over 1001.
old-location: display\dxva_frequency.htm
old-project: display
ms.assetid: 4e7d9746-7dae-4f53-9bf8-e0acc807306a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVA_Frequency, DXVA_Frequency
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_Frequency
req.alt-loc: dxva.h
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

# DXVA_Frequency structure



## -description
<p>The DXVA_Frequency structure is sent by the host decoder to the driver to specify the video frame rate, in Hz. For example, NTSC TV is 60000 over 1001.</p>


## -syntax

````
typedef struct _DXVA_Frequency {
  DWORD Numerator;
  DWORD Denominator;
} DXVA_Frequency;
````


## -struct-fields
<dl>

### -field Numerator

<dd>
<p>Specifies the numerator of the frequency fraction.</p>
</dd>

### -field Denominator

<dd>
<p>Specifies the denominator of the frequency fraction.</p>
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
<dt>Dxva.h (include Dxva.h)</dt>
</dl>
</td>
</tr>
</table>