---
UID: NS.wdfcompanion._WDF_TASK_QUEUE_CONFIG
title: WDF_TASK_QUEUE_CONFIG
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdf_task_queue_config.htm
old-project: wdf
ms.assetid: a58dd106-dec8-4444-9783-eb16e969ea42
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_TASK_QUEUE_CONFIG, WDF_TASK_QUEUE_CONFIG, *PWDF_TASK_QUEUE_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfcompanion.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.23
req.alt-api: WDF_TASK_QUEUE_CONFIG
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
req.iface: 
req.product: Windows 10 or later.
---

# WDF_TASK_QUEUE_CONFIG structure



## -description
<p>For internal use only.</p>


## -syntax

````
typedef struct _WDF_TASK_QUEUE_CONFIG {
  ULONG                                Size;
  USHORT                               TaskQueueId;
  WDF_TASK_QUEUE_DISPATCH_TYPE         DispatchType;
  PFN_WDF_TASK_QUEUE_TASK_EXECUTE_SYNC EvtTaskExecuteSync;
} WDF_TASK_QUEUE_CONFIG, *PWDF_TASK_QUEUE_CONFIG;
````


## -struct-fields
<dl>

### -field Size

<dd></dd>

### -field TaskQueueId

<dd></dd>

### -field DispatchType

<dd></dd>

### -field EvtTaskExecuteSync

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
</table>