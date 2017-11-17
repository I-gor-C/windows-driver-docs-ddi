---
UID: NE.rilapitypes.RILMSGACKSTATUS
title: RILMSGACKSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgackstatus_2.htm
ms.assetid: 412d9a0b-429b-4ce5-bf74-f602533174d7
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
req.alt-api: RILMSGACKSTATUS
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

# RILMSGACKSTATUS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>