---
UID: NF.wdfcompanion.WdfCompanionCreateTaskQueue
title: WdfCompanionCreateTaskQueue
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdfcompanioncreatetaskqueue.htm
ms.assetid: 05298ffe-75e5-444e-9843-54dd063f59f5
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfcompanion.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.23
req.alt-api: WdfCompanionCreateTaskQueue
req.alt-loc: wdfcompanion.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: WdfCompanionCreateTaskQueue
req.iface: 
req.product: Windows 10 or later.
---

# WdfCompanionCreateTaskQueue function



## -description
<p>
			For internal use only.</p>


## -syntax

````
NTSTATUS WdfCompanionCreateTaskQueue(
  _In_      WDFCOMPANION           Companion,
  _In_      PWDF_TASK_QUEUE_CONFIG Config,
  _In_opt_  PWDF_OBJECT_ATTRIBUTES QueueAttributes,
  _Out_opt_ WDFTASKQUEUE           *Queue
);
````


## -parameters
<dl>

### -param <i>Companion</i> [in]

<dd></dd>

### -param <i>Config</i> [in]

<dd></dd>

### -param <i>QueueAttributes</i> [in, optional]

<dd></dd>

### -param <i>Queue</i> [out, optional]

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.23</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfcompanion.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>