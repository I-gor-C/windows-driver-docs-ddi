---
UID: NS.dbgeng._STACK_SRC_INFO
title: STACK_SRC_INFO
author: windows-driver-content
description: Defines stack source information.
old-location: debugger\stack_src_info.htm
ms.assetid: F19D5A5C-D9CF-40CC-B344-8F2D862FBF04
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STACK_SRC_INFO
req.alt-loc: dbgeng.h
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
ms.keywords: STACK_SRC_INFO, STACK_SRC_INFO, *PSTACK_SRC_INFO
req.iface: IDebugSystemObjects4
---

# STACK_SRC_INFO structure



## -description
<p>Defines stack source information. </p>


## -syntax

````
typedef struct _STACK_SRC_INFO {
  PCWSTR ImagePath;
  PCWSTR ModuleName;
  PCWSTR Function;
  ULONG  Displacement;
  ULONG  Row;
  ULONG  Column;
} STACK_SRC_INFO, *PSTACK_SRC_INFO;
````


## -struct-fields
<dl>

### -field <b>ImagePath</b>

<dd>
<p>An image path.</p>
</dd>

### -field <b>ModuleName</b>

<dd>
<p>A module name.</p>
</dd>

### -field <b>Function</b>

<dd>
<p>A function.</p>
</dd>

### -field <b>Displacement</b>

<dd>
<p>A displacement value. </p>
</dd>

### -field <b>Row</b>

<dd>
<p>A row number.</p>
</dd>

### -field <b>Column</b>

<dd>
<p>A column number.</p>
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
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>