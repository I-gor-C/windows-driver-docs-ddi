---
UID: NS.printoem._PDEV_ADJUST_GRAPHICS_RESOLUTION
title: PDEV_ADJUST_GRAPHICS_RESOLUTION
author: windows-driver-content
description: The PDEV_ADJUST_GRAPHICS_RESOLUTION structure specifies a graphics resolution value.
old-location: print\pdev_adjust_graphics_resolution.htm
ms.assetid: d6cebb0d-87ca-4e40-8a87-9579a1026567
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
req.header: printoem.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PDEV_ADJUST_GRAPHICS_RESOLUTION
req.alt-loc: printoem.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
ms.keywords: PDEV_ADJUST_GRAPHICS_RESOLUTION, PDEV_ADJUST_GRAPHICS_RESOLUTION, *PPDEV_ADJUST_GRAPHICS_RESOLUTION
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# PDEV_ADJUST_GRAPHICS_RESOLUTION structure



## -description
<p>The PDEV_ADJUST_GRAPHICS_RESOLUTION structure specifies a graphics resolution value.</p>


## -syntax

````
typedef struct _PDEV_ADJUST_GRAPHICS_RESOLUTION {
  POINT ptGraphicsResolution;
} PDEV_ADJUST_GRAPHICS_RESOLUTION, *PPDEV_ADJUST_GRAPHICS_RESOLUTION;
````


## -struct-fields
<dl>

### -field <b>ptGraphicsResolution</b>

<dd>
<p>A POINT structure that specifies the resolution of the graphics area, in dots per inch (DPI).</p>
</dd>
</dl>

## -remarks
<p>The PDEV_ADJUST_GRAPHICS_RESOLUTION structure is available in Windows Vista and later operating systems. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Printoem.h</dt>
</dl>
</td>
</tr>
</table>