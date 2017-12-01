---
UID: NF.wdfcompanion.WDF_TASK_QUEUE_CONFIG_INIT
title: WDF_TASK_QUEUE_CONFIG_INIT
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdf_task_queue_config_init.htm
old-project: wdf
ms.assetid: 51c43509-074c-4118-afe5-2e568d733751
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_TASK_QUEUE_CONFIG_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfcompanion.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.23
req.alt-api: WDF_TASK_QUEUE_CONFIG_INIT
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
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# WDF_TASK_QUEUE_CONFIG_INIT function



## -description
<p>
			For internal use only.</p>


## -syntax

````
FORCEINLINE VOID WDF_TASK_QUEUE_CONFIG_INIT(
  _Out_ PWDF_TASK_QUEUE_CONFIG       Config,
  _In_  USHORT                       TaskQueueId,
  _In_  WDF_TASK_QUEUE_DISPATCH_TYPE DispatchType
);
````


## -parameters
<dl>

### -param <i>Config</i> [out]

<dd></dd>

### -param <i>TaskQueueId</i> [in]

<dd></dd>

### -param <i>DispatchType</i> [in]

<dd></dd>
</dl>

## -returns
<p>This method does not return a value.</p>

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