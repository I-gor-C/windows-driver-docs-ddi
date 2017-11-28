---
UID: NF.wdfcompaniontarget.WdfCompanionTargetSendTaskSynchronously
title: WdfCompanionTargetSendTaskSynchronously
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdfcompaniontargetsendtasksynchronously.htm
old-project: wdf
ms.assetid: d58a275a-aaaa-4159-ba00-6998b7a63434
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfCompanionTargetSendTaskSynchronously
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfcompaniontarget.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.23
req.umdf-ver: 
req.alt-api: WdfCompanionTargetSendTaskSynchronously
req.alt-loc: wdfcompaniontarget.h
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

# WdfCompanionTargetSendTaskSynchronously function



## -description
<p>
			For internal use only.</p>


## -syntax

````
NTSTATUS WdfCompanionTargetSendTaskSynchronously(
  _In_     WDFCOMPANIONTARGET     CompanionTarget,
  _In_     USHORT                 TaskQueueIdentifier,
  _In_     ULONG                  TaskOperationCode,
  _In_opt_ PWDF_MEMORY_DESCRIPTOR InputBuffer,
  _In_opt_ PWDF_MEMORY_DESCRIPTOR OutputBuffer,
  _In_opt_ PWDF_TASK_SEND_OPTIONS TaskOptions,
  _Out_    PULONG_PTR             BytesReturned
);
````


## -parameters
<dl>

### -param <i>CompanionTarget</i> [in]

<dd></dd>

### -param <i>TaskQueueIdentifier</i> [in]

<dd></dd>

### -param <i>TaskOperationCode</i> [in]

<dd></dd>

### -param <i>InputBuffer</i> [in, optional]

<dd></dd>

### -param <i>OutputBuffer</i> [in, optional]

<dd></dd>

### -param <i>TaskOptions</i> [in, optional]

<dd></dd>

### -param <i>BytesReturned</i> [out]

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.23</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfcompaniontarget.h</dt>
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