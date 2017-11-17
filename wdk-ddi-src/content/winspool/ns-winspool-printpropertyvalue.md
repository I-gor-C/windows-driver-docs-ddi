---
UID: NS.winspool.PrintPropertyValue
title: PrintPropertyValue
author: windows-driver-content
description: TBD.
old-location: print\printpropertyvalue.htm
ms.assetid: B442AE8E-A4CE-481A-A69C-496CBF3E4722
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
req.alt-api: PrintPropertyValue
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
ms.keywords: PrintPropertyValue, PrintPropertyValue
req.iface: 
req.product: Windows 10 or later.
---

# PrintPropertyValue structure



## -description
<p>TBD</p>


## -syntax

````
typedef struct {
  EPrintPropertyType ePropertyType;
  union {
    BYTE     propertyByte;
    PWSTR    propertyString;
    LONG     propertyInt32;
    LONGLONG propertyInt64;
    struct {
      DWORD  cbBuf;
      LPVOID pBuf;
    } propertyBlob;
  } value;
} PrintPropertyValue;
````


## -struct-fields
<dl>

### -field <b>ePropertyType</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>value</b>

<dd>
<dl>

### -field <b>propertyByte</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>propertyString</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>propertyInt32</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>propertyInt64</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>propertyBlob</b>

<dd>
<dl>

### -field <b>cbBuf</b>

<dd>
<p>TBD</p>
</dd>

### -field <b>pBuf</b>

<dd>
<p>TBD</p>
</dd>
</dl>
</dd>
</dl>
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