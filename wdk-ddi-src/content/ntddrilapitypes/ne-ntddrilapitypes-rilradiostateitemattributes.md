---
UID: NE.ntddrilapitypes.RILRADIOSTATEITEMATTRIBUTES
title: RILRADIOSTATEITEMATTRIBUTES
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilradiostateitemattributes.htm
old-project: netvista
ms.assetid: 320ad6e2-0d11-4902-bfdb-8df201d4d5b7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILRADIOSTATEITEMATTRIBUTES
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

# RILRADIOSTATEITEMATTRIBUTES enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILRADIOSTATEITEMATTRIBUTES { 
  RIL_RADIOSTATE_ITEM_ATTRIBUTE_ISDIRTY,
  RIL_RADIOSTATE_ITEM_ATTRIBUTE_ISWRITABLE,
  RIL_RADIOSTATE_ITEM_ATTRIBUTE_HAVEOPTIONS,
  RIL_RADIOSTATE_ITEM_ATTRIBUTE_ALL
} RILRADIOSTATEITEMATTRIBUTES;
````


## -enum-fields
<dl>

### -field <a id="RIL_RADIOSTATE_ITEM_ATTRIBUTE_ISDIRTY"></a><a id="ril_radiostate_item_attribute_isdirty"></a><b>RIL_RADIOSTATE_ITEM_ATTRIBUTE_ISDIRTY</b>

<dd></dd>

### -field <a id="RIL_RADIOSTATE_ITEM_ATTRIBUTE_ISWRITABLE"></a><a id="ril_radiostate_item_attribute_iswritable"></a><b>RIL_RADIOSTATE_ITEM_ATTRIBUTE_ISWRITABLE</b>

<dd></dd>

### -field <a id="RIL_RADIOSTATE_ITEM_ATTRIBUTE_HAVEOPTIONS"></a><a id="ril_radiostate_item_attribute_haveoptions"></a><b>RIL_RADIOSTATE_ITEM_ATTRIBUTE_HAVEOPTIONS</b>

<dd></dd>

### -field <a id="RIL_RADIOSTATE_ITEM_ATTRIBUTE_ALL"></a><a id="ril_radiostate_item_attribute_all"></a><b>RIL_RADIOSTATE_ITEM_ATTRIBUTE_ALL</b>

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