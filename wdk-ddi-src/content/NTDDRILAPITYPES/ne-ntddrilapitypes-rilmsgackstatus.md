---
UID: NE.ntddrilapitypes.RILMSGACKSTATUS
title: RILMSGACKSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgackstatus.htm
ms.assetid: 551193d0-596c-40bf-9a31-f8b6eb330e25
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
req.alt-api: RILMSGACKSTATUS
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

# RILMSGACKSTATUS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGACKSTATUS { 
  RIL_MSGACKSTATUS_FAIL_MEM_FULL,
  RIL_MSGACKSTATUS_ERROR,
  RIL_MSGACKSTATUS_MAX
} RILMSGACKSTATUS;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGACKSTATUS_FAIL_MEM_FULL"></a><a id="ril_msgackstatus_fail_mem_full"></a><b>RIL_MSGACKSTATUS_FAIL_MEM_FULL</b>

<dd></dd>

### -field <a id="RIL_MSGACKSTATUS_ERROR"></a><a id="ril_msgackstatus_error"></a><b>RIL_MSGACKSTATUS_ERROR</b>

<dd></dd>

### -field <a id="RIL_MSGACKSTATUS_MAX"></a><a id="ril_msgackstatus_max"></a><b>RIL_MSGACKSTATUS_MAX</b>

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