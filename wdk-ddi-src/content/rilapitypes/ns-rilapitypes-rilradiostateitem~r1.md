---
UID: NS.rilapitypes.RILRADIOSTATEITEM~r1
title: RILRADIOSTATEITEM
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilradiostateitem_2.htm
old-project: netvista
ms.assetid: 1cfc3e62-3398-435a-b603-fb7638ed8ce9
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILRADIOSTATEITEM,
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

### -field dwItemId

<dd></dd>

### -field dwItemFlag

<dd></dd>

### -field dwItemAttributes

<dd></dd>

### -field RILITEMVALUEUNION

<dd></dd>

### -field itemValueUnion

<dd></dd>

### -field switch_is

<dd></dd>

### -field dwItemFlag

<dd></dd>

### -field intVal

<dd></dd>

### -field case

<dd></dd>

### -field RIL_RADIOSTATE_ITEMFLAG_USE_INTVAL

<dd></dd>

### -field uintVal

<dd></dd>

### -field case

<dd></dd>

### -field RIL_RADIOSTATE_ITEMFLAG_USE_UINTVAL

<dd></dd>

### -field wszVal

<dd></dd>

### -field case

<dd></dd>

### -field RIL_RADIOSTATE_ITEMFLAG_USE_WSZVAL

<dd></dd>

### -field intArray

<dd></dd>

### -field case

<dd></dd>

### -field RIL_RADIOSTATE_ITEMFLAG_USE_INTARRAY

<dd></dd>

### -field uintArray

<dd></dd>

### -field case

<dd></dd>

### -field RIL_RADIOSTATE_ITEMFLAG_USE_UINTARRAY

<dd></dd>

### -field byteArray

<dd></dd>

### -field case

<dd></dd>

### -field RIL_RADIOSTATE_ITEMFLAG_USE_BYTEARRAY

<dd></dd>

### -field wszFriendlyName

<dd></dd>

### -field wszItemValueOptions

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