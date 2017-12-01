---
UID: NS.ntddrilapitypes.RILRADIOSTATEITEM
title: RILRADIOSTATEITEM
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilradiostateitem.htm
old-project: netvista
ms.assetid: 152e3b52-44e4-4ed7-bfc3-38d0c65725fd
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILRADIOSTATEITEM, RILRADIOSTATEITEM, *LPRILRADIOSTATEITEM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILRADIOSTATEITEM
req.alt-loc: ntddrilapitypes.h
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

# RILRADIOSTATEITEM structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILRADIOSTATEITEM {
  DWORD                  dwItemId;
  RILRADIOSTATEITEMFLAG  dwItemFlag;
  DWORD                  dwItemAttributes;
  NULL                   RILITEMVALUEUNION;
  RILITEMVALUEUNION      itemValueUnion;
  int                    intVal;
  unsigned int           uintVal;
  WCHAR [32]             wszVal;
  int [16]               intArray;
  unsigned int [16]      uintArray;
  BYTE [64]              byteArray;
  WCHAR [32]             wszFriendlyName;
  WCHAR [256]            wszItemValueOptions;
} RILRADIOSTATEITEM, RILRADIOSTATEITEM;
````


## -struct-fields
<dl>

### -field <b>dwItemId</b>

<dd></dd>

### -field <b>dwItemFlag</b>

<dd></dd>

### -field <b>dwItemAttributes</b>

<dd></dd>

### -field <b>RILITEMVALUEUNION</b>

<dd></dd>

### -field <b>itemValueUnion</b>

<dd></dd>

### -field <b>intVal</b>

<dd></dd>

### -field <b>uintVal</b>

<dd></dd>

### -field <b>wszVal</b>

<dd></dd>

### -field <b>intArray</b>

<dd></dd>

### -field <b>uintArray</b>

<dd></dd>

### -field <b>byteArray</b>

<dd></dd>

### -field <b>wszFriendlyName</b>

<dd></dd>

### -field <b>wszItemValueOptions</b>

<dd></dd>
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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>