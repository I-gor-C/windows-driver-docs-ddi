---
UID: NE.oemrilapitypes.RILGETTOKENPARAMMASK
title: RILGETTOKENPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilgettokenparammask.htm
old-project: netvista
ms.assetid: d791b497-3ef3-42f1-a6e6-980992c97f45
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RtlUnicodeStringVPrintfEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: oemrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILDEVSPECIFICPARAMMASK
req.alt-loc: oemrilapitypes.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntstrsafe.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# RILGETTOKENPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILDEVSPECIFICPARAMMASK { 
  RIL_PARAM_GETTOKEN_TIMEOUT,
  RIL_PARAM_GETTOKEN_HEADER,
  RIL_PARAM_GETTOKEN_PROTOCOL_ID,
  RIL_PARAM_GETTOKEN_ALL
} RILDEVSPECIFICPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_GETTOKEN_TIMEOUT"></a><a id="ril_param_gettoken_timeout"></a><b>RIL_PARAM_GETTOKEN_TIMEOUT</b>

<dd></dd>

### -field <a id="RIL_PARAM_GETTOKEN_HEADER"></a><a id="ril_param_gettoken_header"></a><b>RIL_PARAM_GETTOKEN_HEADER</b>

<dd></dd>

### -field <a id="RIL_PARAM_GETTOKEN_PROTOCOL_ID"></a><a id="ril_param_gettoken_protocol_id"></a><b>RIL_PARAM_GETTOKEN_PROTOCOL_ID</b>

<dd></dd>

### -field <a id="RIL_PARAM_GETTOKEN_ALL"></a><a id="ril_param_gettoken_all"></a><b>RIL_PARAM_GETTOKEN_ALL</b>

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
<dt>Oemrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>