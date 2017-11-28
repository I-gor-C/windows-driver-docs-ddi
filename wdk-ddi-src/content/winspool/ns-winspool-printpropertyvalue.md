---
UID: NS.winspool.PrintPropertyValue
title: PrintPropertyValue
author: windows-driver-content
description: .
old-location: print\printpropertyvalue.htm
old-project: print
ms.assetid: B442AE8E-A4CE-481A-A69C-496CBF3E4722
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: PrintPropertyValue, PrintPropertyValue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: winspool.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PrintPropertyValue
req.alt-loc: Winspool.h
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

# PrintPropertyValue structure



## -description
<p></p>


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

<dd></dd>

### -field <b>value</b>

<dd>
<dl>

### -field <b>propertyBlob</b>

<dd>
<dl>

### -field <b>pBuf</b>

<dd>
<p>TD</p>
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