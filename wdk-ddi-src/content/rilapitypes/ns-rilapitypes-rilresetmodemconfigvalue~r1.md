---
UID: NS.rilapitypes.RILRESETMODEMCONFIGVALUE~r1
title: RILRESETMODEMCONFIGVALUE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilresetmodemconfigvalue_2.htm
old-project: netvista
ms.assetid: 8749345c-a1a6-43f6-8cb7-f69a6734839f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILRESETMODEMCONFIGVALUE,
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
req.alt-api: RILRESETMODEMCONFIGVALUE
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

# RILRESETMODEMCONFIGVALUE structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILRESETMODEMCONFIGVALUE {
  DWORD                                    cbSize;
  DWORD                                    dwType;
  NULL                                     RILRESETMODEMCONFIGVALUEUNION;
  RILRESETMODEMCONFIGVALUEUNION            configValueUnion;
  NULL                                     switch_is;
  NULL                                     dwType;
  BOOL                                     fValue;
  NULL                                     case;
  NULL                                     RIL_RMCV_TYPE_BOOLEAN;
  DWORD                                    dwValue;
  NULL                                     case;
  NULL                                     RIL_RMCV_TYPE_DWORD;
  WCHAR [MAXLENGTH_RESETMODEMCONFIGSTRING] wszValue;
  NULL                                     case;
  NULL                                     RIL_RMCV_TYPE_STRING;
} RILRESETMODEMCONFIGVALUE, RILRESETMODEMCONFIGVALUE;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwType</b>

<dd></dd>

### -field <b>RILRESETMODEMCONFIGVALUEUNION</b>

<dd></dd>

### -field <b>configValueUnion</b>

<dd></dd>

### -field <b>switch_is</b>

<dd></dd>

### -field <b>dwType</b>

<dd></dd>

### -field <b>fValue</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_RMCV_TYPE_BOOLEAN</b>

<dd></dd>

### -field <b>dwValue</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_RMCV_TYPE_DWORD</b>

<dd></dd>

### -field <b>wszValue</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_RMCV_TYPE_STRING</b>

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