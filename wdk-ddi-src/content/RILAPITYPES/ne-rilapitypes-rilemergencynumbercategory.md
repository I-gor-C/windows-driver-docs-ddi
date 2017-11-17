---
UID: NE.rilapitypes.RILEMERGENCYNUMBERCATEGORY
title: RILEMERGENCYNUMBERCATEGORY
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilemergencynumbercategory_2.htm
ms.assetid: 322e2622-1f9a-433a-8fe9-9d59c00ce8be
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILEMERGENCYNUMBERCATEGORY
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
ms.keywords: RIL_WritePhonebookEntry
req.iface: 
req.product: Windows 10 or later.
---

# RILEMERGENCYNUMBERCATEGORY enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILEMERGENCYNUMBERCATEGORY { 
  RIL_ENUM_AMBULANCE,
  RIL_ENUM_FIRE_BRIGADE,
  RIL_ENUM_MARINE_GUARD,
  RIL_ENUM_MOUNTAIN_RESCUE,
  RIL_ENUM_MANUAL_ECALL,
  RIL_ENUM_AUTO_ECALL,
  RIL_ENUM_ALL
} RILEMERGENCYNUMBERCATEGORY;
````


## -enum-fields
<dl>

### -field <a id="RIL_ENUM_AMBULANCE"></a><a id="ril_enum_ambulance"></a><b>RIL_ENUM_AMBULANCE</b>

<dd></dd>

### -field <a id="RIL_ENUM_FIRE_BRIGADE"></a><a id="ril_enum_fire_brigade"></a><b>RIL_ENUM_FIRE_BRIGADE</b>

<dd></dd>

### -field <a id="RIL_ENUM_MARINE_GUARD"></a><a id="ril_enum_marine_guard"></a><b>RIL_ENUM_MARINE_GUARD</b>

<dd></dd>

### -field <a id="RIL_ENUM_MOUNTAIN_RESCUE"></a><a id="ril_enum_mountain_rescue"></a><b>RIL_ENUM_MOUNTAIN_RESCUE</b>

<dd></dd>

### -field <a id="RIL_ENUM_MANUAL_ECALL"></a><a id="ril_enum_manual_ecall"></a><b>RIL_ENUM_MANUAL_ECALL</b>

<dd></dd>

### -field <a id="RIL_ENUM_AUTO_ECALL"></a><a id="ril_enum_auto_ecall"></a><b>RIL_ENUM_AUTO_ECALL</b>

<dd></dd>

### -field <a id="RIL_ENUM_ALL"></a><a id="ril_enum_all"></a><b>RIL_ENUM_ALL</b>

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