---
UID: NS.d3dkmthk._DXGK_GRAPHICSPOWER_REGISTER_INPUT_V_1_1
title: DXGK_GRAPHICSPOWER_REGISTER_INPUT_V_1_1
author: windows-driver-content
description: Used to register the power state of a new input.
old-location: display\dxgk-graphicspower-register-input-v-1-1.htm
old-project: display
ms.assetid: 5b120f3c-43d2-447a-9959-0788d7decf50
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_GRAPHICSPOWER_REGISTER_INPUT_V_1_1, DXGK_GRAPHICSPOWER_REGISTER_INPUT_V_1_1, *PDXGK_GRAPHICSPOWER_REGISTER_INPUT_V_1_1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_GRAPHICSPOWER_REGISTER_INPUT_V_1_1
req.alt-loc: d3dkmthk.h
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
---

# DXGK_GRAPHICSPOWER_REGISTER_INPUT_V_1_1 structure



## -description
<p>Used to register the power state of a new input.</p>


## -syntax

````
typedef struct _DXGK_GRAPHICSPOWER_REGISTER_INPUT_V_1_1 {
  ULONG                      Version;
  PVOID                      PrivateHandle;
  PDXGK_POWER_NOTIFICATION   PowerNotificationCb;
  PDXGK_REMOVAL_NOTIFICATION RemovalNotificationCb;
  PDXGK_FSTATE_NOTIFICATION  FStateNotificationCb;
} DXGK_GRAPHICSPOWER_REGISTER_INPUT_V_1_1, *PDXGK_GRAPHICSPOWER_REGISTER_INPUT_V_1_1;
````


## -struct-fields
<dl>

### -field Version

<dd>
<p>The current version being used.</p>
</dd>

### -field PrivateHandle

<dd>
<p>A private handle to the device.</p>
</dd>

### -field PowerNotificationCb

<dd>
<p>Issues a power notification.</p>
</dd>

### -field RemovalNotificationCb

<dd>
<p>Issues a removal notification.</p>
</dd>

### -field FStateNotificationCb

<dd>
<p>Issues a state notification.</p>
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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>