---
UID: NS.printoem._PDEV_ADJUST_PHYSICAL_PAPER_SIZE
title: PDEV_ADJUST_PHYSICAL_PAPER_SIZE
author: windows-driver-content
description: The PDEV_ADJUST_PAPER_PHYSICAL_SIZE structure specifies a paper size value.
old-location: print\pdev_adjust_paper_physical_size.htm
old-project: print
ms.assetid: 27f6bc52-6973-4370-87cb-07d6f9399e20
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PDEV_ADJUST_PHYSICAL_PAPER_SIZE, PDEV_ADJUST_PHYSICAL_PAPER_SIZE, *PPDEV_ADJUST_PHYSICAL_PAPER_SIZE
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
req.alt-api: PDEV_ADJUST_PHYSICAL_PAPER_SIZE
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

# PDEV_ADJUST_PHYSICAL_PAPER_SIZE structure



## -description
<p>The PDEV_ADJUST_PAPER_PHYSICAL_SIZE structure specifies a paper size value.</p>


## -syntax

````
typedef struct _PDEV_ADJUST_PHYSICAL_PAPER_SIZE {
  SIZEL szlPhysicalPaperSize;
} PDEV_ADJUST_PHYSICAL_PAPER_SIZE, *PPDEV_ADJUST_PHYSICAL_PAPER_SIZE;
````


## -struct-fields
<dl>

### -field <b>szlPhysicalPaperSize</b>

<dd>
<p>A SIZEL structure that specifies the physical paper size, in graphics device units (pixels).</p>
</dd>
</dl>

## -remarks
<p>The PDEV_ADJUST_PAPER_PHYSICAL_SIZE structure is available in Windows Vista and later operating systems. </p>

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