---
UID: NS.winspool.PrintPropertiesCollection
title: PrintPropertiesCollection
author: windows-driver-content
description: TBD.
old-location: print\printpropertiescollection.htm
ms.assetid: 824E8A5C-7530-4C7B-B093-386DD3D45A6B
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
req.alt-api: PrintPropertiesCollection
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
ms.keywords: PrintPropertiesCollection, PrintPropertiesCollection
req.iface: 
req.product: Windows 10 or later.
---

# PrintPropertiesCollection structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct {
  ULONG                    numberOfProperties;
  PrintNamedProperty       *propertiesCollection;
} PrintPropertiesCollection;
````


## -struct-fields
<dl>

### -field <b>numberOfProperties</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>propertiesCollection</b>

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