---
UID: NS.rilapitypes.RILOPERATORNAMES
title: RILOPERATORNAMES
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riloperatornames_2.htm
old-project: netvista
ms.assetid: 5a066e35-1e8c-431e-897f-9d864991b15f
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILOPERATORNAMES, RILOPERATORNAMES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILOPERATORNAMES
req.alt-loc: rilapitypes.h
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

# RILOPERATORNAMES structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILOPERATORNAMES {
  DWORD                                   cbSize;
  DWORD                                   dwParams;
  DWORD                                   dwSystemType;
  WCHAR [MAXLENGTH_OPERATOR_LONG]         wszLongName;
  WCHAR [MAXLENGTH_OPERATOR_SHORT]        wszShortName;
  WCHAR [MAXLENGTH_OPERATOR_NUMERIC]      wszNumName;
  WCHAR [MAXLENGTH_OPERATOR_COUNTRY_CODE] wszCountryCode;
} RILOPERATORNAMES, RILOPERATORNAMES;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwSystemType</b>

<dd></dd>

### -field <b>wszLongName</b>

<dd></dd>

### -field <b>wszShortName</b>

<dd></dd>

### -field <b>wszNumName</b>

<dd></dd>

### -field <b>wszCountryCode</b>

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>