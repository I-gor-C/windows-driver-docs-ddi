---
UID: NS.printoem._PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA
title: PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA
author: windows-driver-content
description: The PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA structure specifies the imageable origin area.
old-location: print\pdev_adjust_imageable_origin_area.htm
old-project: print
ms.assetid: 7b66ed24-64c2-49bc-a417-05fe11178b9f
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA, PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA, *PPDEV_ADJUST_IMAGEABLE_ORIGIN_AREA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: printoem.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA
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
req.irql: 
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA structure



## -description
<p>The PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA structure specifies the imageable origin area.</p>


## -syntax

````
typedef struct _PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA {
  POINT ptImageOrigin;
  SIZEL szlImageableArea;
} PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA, *PPDEV_ADJUST_IMAGEABLE_ORIGIN_AREA;
````


## -struct-fields
<dl>

### -field ptImageOrigin

<dd>
<p>A POINT structure that specifies the origin of the imageable area, in graphics device units (pixels).</p>
</dd>

### -field szlImageableArea

<dd>
<p>A SIZEL structure that specifies the size of the image area, in graphics device units (pixels).</p>
</dd>
</dl>

## -remarks
<p>The PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA structure is available in Windows Vista and later operating systems. </p>

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