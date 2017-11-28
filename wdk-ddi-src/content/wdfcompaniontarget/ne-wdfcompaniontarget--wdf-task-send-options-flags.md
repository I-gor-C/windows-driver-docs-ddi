---
UID: NE.wdfcompaniontarget._WDF_TASK_SEND_OPTIONS_FLAGS
title: WDF_TASK_SEND_OPTIONS_FLAGS
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdf_task_send_options_flags.htm
old-project: wdf
ms.assetid: 8ff13908-57f2-404f-a8ea-70c798ee3d7d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_TASK_QUEUE_CONFIG, WDF_TASK_QUEUE_CONFIG, *PWDF_TASK_QUEUE_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfcompaniontarget.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.23
req.umdf-ver: 
req.alt-api: WDF_TASK_SEND_OPTIONS_FLAGS
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

# WDF_TASK_SEND_OPTIONS_FLAGS enumeration



## -description
<p>For internal use only.</p>


## -syntax

````
typedef enum _WDF_TASK_SEND_OPTIONS_FLAGS { 
  WDF_TASK_SEND_OPTION_TIMEOUT      = 1,
  WDF_TASK_SEND_OPTION_SYNCHRONOUS  = 2
} WDF_TASK_SEND_OPTIONS_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="WDF_TASK_SEND_OPTION_TIMEOUT"></a><a id="wdf_task_send_option_timeout"></a><b>WDF_TASK_SEND_OPTION_TIMEOUT</b>

<dd></dd>

### -field <a id="WDF_TASK_SEND_OPTION_SYNCHRONOUS"></a><a id="wdf_task_send_option_synchronous"></a><b>WDF_TASK_SEND_OPTION_SYNCHRONOUS</b>

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
</table>