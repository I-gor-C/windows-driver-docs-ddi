---
UID: NE.rilapitypes.RILCALLMEDIAOFFERACTION
title: RILCALLMEDIAOFFERACTION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmediaofferaction_2.htm
old-project: netvista
ms.assetid: 2acfaeab-c196-46a9-87a4-c44306b46ad1
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
req.alt-api: RILCALLMEDIAOFFERACTION
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

# RILCALLMEDIAOFFERACTION enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILCALLMEDIAOFFERACTION { 
  RIL_CALLMEDIAOFFERACTION_ERROR,
  RIL_CALLMEDIAOFFERACTION_REJECT,
  RIL_CALLMEDIAOFFERACTION_ASK,
  RIL_CALLMEDIAOFFERACTION_ACCEPT,
  RIL_CALLMEDIAOFFERACTION_CANCEL,
  RIL_CALLMEDIAOFFERACTION_MAX
} RILCALLMEDIAOFFERACTION;
````


## -enum-fields
<dl>

### -field <a id="RIL_CALLMEDIAOFFERACTION_ERROR"></a><a id="ril_callmediaofferaction_error"></a><b>RIL_CALLMEDIAOFFERACTION_ERROR</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIAOFFERACTION_REJECT"></a><a id="ril_callmediaofferaction_reject"></a><b>RIL_CALLMEDIAOFFERACTION_REJECT</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIAOFFERACTION_ASK"></a><a id="ril_callmediaofferaction_ask"></a><b>RIL_CALLMEDIAOFFERACTION_ASK</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIAOFFERACTION_ACCEPT"></a><a id="ril_callmediaofferaction_accept"></a><b>RIL_CALLMEDIAOFFERACTION_ACCEPT</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIAOFFERACTION_CANCEL"></a><a id="ril_callmediaofferaction_cancel"></a><b>RIL_CALLMEDIAOFFERACTION_CANCEL</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIAOFFERACTION_MAX"></a><a id="ril_callmediaofferaction_max"></a><b>RIL_CALLMEDIAOFFERACTION_MAX</b>

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