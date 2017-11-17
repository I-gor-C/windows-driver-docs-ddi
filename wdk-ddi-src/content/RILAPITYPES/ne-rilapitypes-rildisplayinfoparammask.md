---
UID: NE.rilapitypes.RILDISPLAYINFOPARAMMASK
title: RILDISPLAYINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildisplayinfoparammask_2.htm
ms.assetid: d8bd093d-ad95-488e-a057-b96fecf58bbb
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
req.alt-api: RILDISPLAYINFOPARAMMASK
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

# RILDISPLAYINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILDISPLAYINFOPARAMMASK { 
  RIL_PARAM_DISPLAY_TYPE,
  RIL_PARAM_DISPLAY_TAG,
  RIL_PARAM_DISPLAY_MESSAGESIZE,
  RIL_PARAM_DISPLAY_MESSAGE,
  RIL_PARAM_DISPLAY_ALL
} RILDISPLAYINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_DISPLAY_TYPE"></a><a id="ril_param_display_type"></a><b>RIL_PARAM_DISPLAY_TYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_DISPLAY_TAG"></a><a id="ril_param_display_tag"></a><b>RIL_PARAM_DISPLAY_TAG</b>

<dd></dd>

### -field <a id="RIL_PARAM_DISPLAY_MESSAGESIZE"></a><a id="ril_param_display_messagesize"></a><b>RIL_PARAM_DISPLAY_MESSAGESIZE</b>

<dd></dd>

### -field <a id="RIL_PARAM_DISPLAY_MESSAGE"></a><a id="ril_param_display_message"></a><b>RIL_PARAM_DISPLAY_MESSAGE</b>

<dd></dd>

### -field <a id="RIL_PARAM_DISPLAY_ALL"></a><a id="ril_param_display_all"></a><b>RIL_PARAM_DISPLAY_ALL</b>

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