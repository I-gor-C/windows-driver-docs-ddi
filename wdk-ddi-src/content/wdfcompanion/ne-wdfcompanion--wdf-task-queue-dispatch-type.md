---
UID: NE.wdfcompanion._WDF_TASK_QUEUE_DISPATCH_TYPE
title: WDF_TASK_QUEUE_DISPATCH_TYPE
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdf_task_queue_dispatch_type.htm
old-project: wdf
ms.assetid: 27cc4067-33de-4f2d-abad-05c73c875458
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_COMMON_BUFFER_CONFIG, WDF_COMMON_BUFFER_CONFIG, *PWDF_COMMON_BUFFER_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfcompanion.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.23
req.alt-api: WDF_TASK_QUEUE_DISPATCH_TYPE
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

# WDF_TASK_QUEUE_DISPATCH_TYPE enumeration



## -description
<p>For internal use only.</p>


## -syntax

````
typedef enum _WDF_TASK_QUEUE_DISPATCH_TYPE { 
  WdfTaskQueueDispatchInvalid     = 0,
  WdfTaskQueueDispatchSequential,
  WdfTaskQueueDispatchParallel,
  WdfTaskQueueDispatchMax
} WDF_TASK_QUEUE_DISPATCH_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WdfTaskQueueDispatchInvalid"></a><a id="wdftaskqueuedispatchinvalid"></a><a id="WDFTASKQUEUEDISPATCHINVALID"></a><b>WdfTaskQueueDispatchInvalid</b>

<dd></dd>

### -field <a id="WdfTaskQueueDispatchSequential"></a><a id="wdftaskqueuedispatchsequential"></a><a id="WDFTASKQUEUEDISPATCHSEQUENTIAL"></a><b>WdfTaskQueueDispatchSequential</b>

<dd></dd>

### -field <a id="WdfTaskQueueDispatchParallel"></a><a id="wdftaskqueuedispatchparallel"></a><a id="WDFTASKQUEUEDISPATCHPARALLEL"></a><b>WdfTaskQueueDispatchParallel</b>

<dd></dd>

### -field <a id="WdfTaskQueueDispatchMax"></a><a id="wdftaskqueuedispatchmax"></a><a id="WDFTASKQUEUEDISPATCHMAX"></a><b>WdfTaskQueueDispatchMax</b>

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