---
UID: NS.iddcx.IDARG_IN_MONITORCREATE~r1
title: IDARG_IN_MONITORCREATE
author: windows-driver-content
description: Gives information about the monitor object that will be created.
old-location: display\idarg_in_monitorcreate.htm
old-project: display
ms.assetid: 0de9686f-69e6-4aac-8f58-9e61bcfe3827
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDARG_IN_MONITORCREATE,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDARG_IN_MONITORCREATE
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _Must_inspect_result_
req.iface: 
---

# IDARG_IN_MONITORCREATE structure



## -description
<p>
                 Gives information about the monitor object that will be created.
             </p>


## -syntax

````
typedef struct IDARG_IN_MONITORCREATE {
  PWDF_OBJECT_ATTRIBUTES ObjectAttributes;
  IDDCX_MONITOR_INFO*    pMonitorInfo;
} IDARG_IN_MONITORCREATE, *IDARG_IN_MONITORCREATE;
````


## -struct-fields
<dl>

### -field ObjectAttributes

<dd>
<p>
                     
                 Indicates object attributes for the monitor.</p>
</dd>

### -field pMonitorInfo

<dd>
<p>[in] Pointer to the information about this monitor.</p>
</dd>
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
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>