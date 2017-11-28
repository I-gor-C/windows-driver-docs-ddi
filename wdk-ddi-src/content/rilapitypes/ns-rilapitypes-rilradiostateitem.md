---
UID: NS.rilapitypes.RILRADIOSTATEITEM
title: RILRADIOSTATEITEM
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilradiostateitem_2.htm
old-project: netvista
ms.assetid: 1cfc3e62-3398-435a-b603-fb7638ed8ce9
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILRADIOSTATEITEM, RILRADIOSTATEITEM
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
req.alt-api: RILRADIOSTATEITEM
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

# RILRADIOSTATEITEM structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILRADIOSTATEITEM {
  DWORD                                        dwItemId;
  RILRADIOSTATEITEMFLAG                        dwItemFlag;
  DWORD                                        dwItemAttributes;
  NULL                                         RILITEMVALUEUNION;
  RILITEMVALUEUNION                            itemValueUnion;
  NULL                                         switch_is;
  NULL                                         dwItemFlag;
  int                                          intVal;
  NULL                                         case;
  NULL                                         RIL_RADIOSTATE_ITEMFLAG_USE_INTVAL;
  unsigned int                                 uintVal;
  NULL                                         case;
  NULL                                         RIL_RADIOSTATE_ITEMFLAG_USE_UINTVAL;
  WCHAR [MAXLENGTH_RADIOITEMVALUE_WCHAR]       wszVal;
  NULL                                         case;
  NULL                                         RIL_RADIOSTATE_ITEMFLAG_USE_WSZVAL;
  int [MAXLENGTH_RADIOITEMVALUE_INT]           intArray;
  NULL                                         case;
  NULL                                         RIL_RADIOSTATE_ITEMFLAG_USE_INTARRAY;
  unsigned int [MAXLENGTH_RADIOITEMVALUE_UINT] uintArray;
  NULL                                         case;
  NULL                                         RIL_RADIOSTATE_ITEMFLAG_USE_UINTARRAY;
  BYTE [MAXLENGTH_RADIOITEMVALUE_BYTE]         byteArray;
  NULL                                         case;
  NULL                                         RIL_RADIOSTATE_ITEMFLAG_USE_BYTEARRAY;
  WCHAR [MAXLENGTH_RADIOITEMNAME]              wszFriendlyName;
  WCHAR [MAXLENGTH_RADIOITEM_OPTIONS]          wszItemValueOptions;
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

### -field <b>switch_is</b>

<dd></dd>

### -field <b>dwItemFlag</b>

<dd></dd>

### -field <b>intVal</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_RADIOSTATE_ITEMFLAG_USE_INTVAL</b>

<dd></dd>

### -field <b>uintVal</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_RADIOSTATE_ITEMFLAG_USE_UINTVAL</b>

<dd></dd>

### -field <b>wszVal</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_RADIOSTATE_ITEMFLAG_USE_WSZVAL</b>

<dd></dd>

### -field <b>intArray</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_RADIOSTATE_ITEMFLAG_USE_INTARRAY</b>

<dd></dd>

### -field <b>uintArray</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_RADIOSTATE_ITEMFLAG_USE_UINTARRAY</b>

<dd></dd>

### -field <b>byteArray</b>

<dd></dd>

### -field <b>case</b>

<dd></dd>

### -field <b>RIL_RADIOSTATE_ITEMFLAG_USE_BYTEARRAY</b>

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>