---
UID: NE.rilapitypes.RILCALLRTTACTION
title: RILCALLRTTACTION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallrttaction_2.htm
old-project: netvista
ms.assetid: e4a28382-25f9-427d-ba7a-3b35c01f50fd
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
req.alt-api: RILCALLRTTACTION
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

# RILCALLRTTACTION enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILCALLRTTACTION { 
  RIL_CALLRTTACTION_REJECT,
  RIL_CALLRTTACTION_ASK,
  RIL_CALLRTTACTION_ACCEPT,
  RIL_CALLRTTACTION_MAX
} RILCALLRTTACTION;
````


## -enum-fields
<dl>

### -field <a id="RIL_CALLRTTACTION_REJECT"></a><a id="ril_callrttaction_reject"></a><b>RIL_CALLRTTACTION_REJECT</b>

<dd></dd>

### -field <a id="RIL_CALLRTTACTION_ASK"></a><a id="ril_callrttaction_ask"></a><b>RIL_CALLRTTACTION_ASK</b>

<dd></dd>

### -field <a id="RIL_CALLRTTACTION_ACCEPT"></a><a id="ril_callrttaction_accept"></a><b>RIL_CALLRTTACTION_ACCEPT</b>

<dd></dd>

### -field <a id="RIL_CALLRTTACTION_MAX"></a><a id="ril_callrttaction_max"></a><b>RIL_CALLRTTACTION_MAX</b>

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