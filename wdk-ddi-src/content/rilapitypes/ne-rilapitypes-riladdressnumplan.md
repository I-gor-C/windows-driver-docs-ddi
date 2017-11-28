---
UID: NE.rilapitypes.RILADDRESSNUMPLAN
title: RILADDRESSNUMPLAN
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riladdressnumplan_2.htm
old-project: netvista
ms.assetid: 14c0f786-4616-49f1-aa9c-0e5c8d4f0197
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
req.alt-api: RILADDRESSNUMPLAN
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

# RILADDRESSNUMPLAN enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILADDRESSNUMPLAN { 
  RIL_NUMPLAN_TELEPHONE,
  RIL_NUMPLAN_DATA,
  RIL_NUMPLAN_TELEX,
  RIL_NUMPLAN_NATIONAL,
  RIL_NUMPLAN_PRIVATE,
  RIL_NUMPLAN_ERMES,
  RIL_NUMPLAN_MAX
} RILADDRESSNUMPLAN;
````


## -enum-fields
<dl>

### -field <a id="RIL_NUMPLAN_TELEPHONE"></a><a id="ril_numplan_telephone"></a><b>RIL_NUMPLAN_TELEPHONE</b>

<dd></dd>

### -field <a id="RIL_NUMPLAN_DATA"></a><a id="ril_numplan_data"></a><b>RIL_NUMPLAN_DATA</b>

<dd></dd>

### -field <a id="RIL_NUMPLAN_TELEX"></a><a id="ril_numplan_telex"></a><b>RIL_NUMPLAN_TELEX</b>

<dd></dd>

### -field <a id="RIL_NUMPLAN_NATIONAL"></a><a id="ril_numplan_national"></a><b>RIL_NUMPLAN_NATIONAL</b>

<dd></dd>

### -field <a id="RIL_NUMPLAN_PRIVATE"></a><a id="ril_numplan_private"></a><b>RIL_NUMPLAN_PRIVATE</b>

<dd></dd>

### -field <a id="RIL_NUMPLAN_ERMES"></a><a id="ril_numplan_ermes"></a><b>RIL_NUMPLAN_ERMES</b>

<dd></dd>

### -field <a id="RIL_NUMPLAN_MAX"></a><a id="ril_numplan_max"></a><b>RIL_NUMPLAN_MAX</b>

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