---
UID: NS.rilapitypes.RILRESETMODEMCONFIGVALUE
title: RILRESETMODEMCONFIGVALUE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilresetmodemconfigvalue_2.htm
old-project: netvista
ms.assetid: 8749345c-a1a6-43f6-8cb7-f69a6734839f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILRESETMODEMCONFIGVALUE, RILRESETMODEMCONFIGVALUE
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

### -field cbSize

<dd></dd>

### -field dwType

<dd></dd>

### -field RILRESETMODEMCONFIGVALUEUNION

<dd></dd>

### -field configValueUnion

<dd></dd>

### -field switch_is

<dd></dd>

### -field dwType

<dd></dd>

### -field fValue

<dd></dd>

### -field case

<dd></dd>

### -field RIL_RMCV_TYPE_BOOLEAN

<dd></dd>

### -field dwValue

<dd></dd>

### -field case

<dd></dd>

### -field RIL_RMCV_TYPE_DWORD

<dd></dd>

### -field wszValue

<dd></dd>

### -field case

<dd></dd>

### -field RIL_RMCV_TYPE_STRING

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