---
UID: NS.iddcx.IDARG_OUT_MONITORCREATE~r1
title: IDARG_OUT_MONITORCREATE
author: windows-driver-content
description: Gives information about the newly created monitor object.
old-location: display\idarg_out_monitorcreate.htm
old-project: display
ms.assetid: 713cd675-56a8-42d8-ac75-4af227c55dec
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDARG_OUT_MONITORCREATE,
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
req.alt-api: IDARG_OUT_MONITORCREATE
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

# IDARG_OUT_MONITORCREATE structure



## -description
<p>Gives information about the newly created monitor object.</p>


## -syntax

````
typedef struct IDARG_OUT_MONITORCREATE {
  IDDCX_MONITOR MonitorObject;
} IDARG_OUT_MONITORCREATE, *IDARG_OUT_MONITORCREATE;
````


## -struct-fields
<dl>

### -field <b>MonitorObject</b>

<dd>
<p>
                     [out] Handle the driver can use to identify this monitor when calling OS functions.
                 </p>
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