---
UID: NE.rilapitypes.RILGEOSCOPE
title: RILGEOSCOPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilgeoscope_2.htm
old-project: netvista
ms.assetid: 821f05f8-cc2c-4567-a1a0-aaa7b535d568
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILGEOSCOPE
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

# RILGEOSCOPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILGEOSCOPE { 
  RIL_GEOSCOPE_CELL_IMMEDIATE,
  RIL_GEOSCOPE_LOCATIONAREA,
  RIL_GEOSCOPE_PLMN,
  RIL_GEOSCOPE_CELL,
  RIL_GEOSCOPE_MAX
} RILGEOSCOPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_GEOSCOPE_CELL_IMMEDIATE"></a><a id="ril_geoscope_cell_immediate"></a><b>RIL_GEOSCOPE_CELL_IMMEDIATE</b>

<dd></dd>

### -field <a id="RIL_GEOSCOPE_LOCATIONAREA"></a><a id="ril_geoscope_locationarea"></a><b>RIL_GEOSCOPE_LOCATIONAREA</b>

<dd></dd>

### -field <a id="RIL_GEOSCOPE_PLMN"></a><a id="ril_geoscope_plmn"></a><b>RIL_GEOSCOPE_PLMN</b>

<dd></dd>

### -field <a id="RIL_GEOSCOPE_CELL"></a><a id="ril_geoscope_cell"></a><b>RIL_GEOSCOPE_CELL</b>

<dd></dd>

### -field <a id="RIL_GEOSCOPE_MAX"></a><a id="ril_geoscope_max"></a><b>RIL_GEOSCOPE_MAX</b>

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