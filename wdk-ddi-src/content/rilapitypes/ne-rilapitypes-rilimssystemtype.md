---
UID: NE.rilapitypes.RILIMSSYSTEMTYPE
title: RILIMSSYSTEMTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimssystemtype_2.htm
old-project: netvista
ms.assetid: 94c37721-372f-448f-8cd9-d4c64dd285cb
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: RILIMSSYSTEMTYPE
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

# RILIMSSYSTEMTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILIMSSYSTEMTYPE { 
  RIL_IMSSYSTEMTYPE_WIFI,
  RIL_IMSSYSTEMTYPE_LTE,
  RIL_IMSSYSTEMTYPE_MAX
} RILIMSSYSTEMTYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_IMSSYSTEMTYPE_WIFI"></a><a id="ril_imssystemtype_wifi"></a><b>RIL_IMSSYSTEMTYPE_WIFI</b>

<dd></dd>

### -field <a id="RIL_IMSSYSTEMTYPE_LTE"></a><a id="ril_imssystemtype_lte"></a><b>RIL_IMSSYSTEMTYPE_LTE</b>

<dd></dd>

### -field <a id="RIL_IMSSYSTEMTYPE_MAX"></a><a id="ril_imssystemtype_max"></a><b>RIL_IMSSYSTEMTYPE_MAX</b>

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