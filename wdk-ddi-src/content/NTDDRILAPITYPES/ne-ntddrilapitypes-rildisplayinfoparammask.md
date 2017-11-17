---
UID: NE.ntddrilapitypes.RILDISPLAYINFOPARAMMASK
title: RILDISPLAYINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildisplayinfoparammask.htm
ms.assetid: deb9da97-7a61-4642-bebd-ab0e4082b410
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILDISPLAYINFOPARAMMASK
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
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
req.iface: 
---

# RILDISPLAYINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>