---
UID: NS.winspool.PrintNamedProperty
title: PrintNamedProperty
author: windows-driver-content
description: TBD.
old-location: print\printnamedproperty.htm
ms.assetid: F7692594-DE13-4242-926C-F2706FF95E77
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: print
req.header: winspool.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PrintNamedProperty
req.alt-loc: 
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
ms.keywords: PrintNamedProperty, PrintNamedProperty
req.iface: 
req.product: Windows 10 or later.
---

# PrintNamedProperty structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct {
  WCHAR                    *propertyName;
  PrintPropertyValue       propertyValue;
} PrintNamedProperty;
````


## -struct-fields
<dl>

### -field <b>propertyName</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>propertyValue</b>

<dd>
<p>TBD</p>
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
<dt>Winspool.h</dt>
</dl>
</td>
</tr>
</table>