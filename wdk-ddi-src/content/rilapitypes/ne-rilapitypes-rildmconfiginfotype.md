---
UID: NE.rilapitypes.RILDMCONFIGINFOTYPE
title: RILDMCONFIGINFOTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildmconfiginfotype_2.htm
old-project: netvista
ms.assetid: 86f09204-5f4a-412d-a10b-4692e159ca1b
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
req.alt-api: RILDMCONFIGINFOTYPE
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

# RILDMCONFIGINFOTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILDMCONFIGINFOTYPE { 
  RIL_DMCV_TYPE_BOOLEAN,
  RIL_DMCV_TYPE_DWORD,
  RIL_DMCV_TYPE_STRING,
  RIL_DMCV_TYPE_MAX
} RILDMCONFIGINFOTYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_DMCV_TYPE_BOOLEAN"></a><a id="ril_dmcv_type_boolean"></a><b>RIL_DMCV_TYPE_BOOLEAN</b>

<dd></dd>

### -field <a id="RIL_DMCV_TYPE_DWORD"></a><a id="ril_dmcv_type_dword"></a><b>RIL_DMCV_TYPE_DWORD</b>

<dd></dd>

### -field <a id="RIL_DMCV_TYPE_STRING"></a><a id="ril_dmcv_type_string"></a><b>RIL_DMCV_TYPE_STRING</b>

<dd></dd>

### -field <a id="RIL_DMCV_TYPE_MAX"></a><a id="ril_dmcv_type_max"></a><b>RIL_DMCV_TYPE_MAX</b>

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