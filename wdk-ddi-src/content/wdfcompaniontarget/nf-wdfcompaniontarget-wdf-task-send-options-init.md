---
UID: NF.wdfcompaniontarget.WDF_TASK_SEND_OPTIONS_INIT
title: WDF_TASK_SEND_OPTIONS_INIT
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdf_task_send_options_init.htm
old-project: wdf
ms.assetid: ba10c012-f64c-42cd-bedc-72f620818aa5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_TASK_SEND_OPTIONS_INIT
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
req.alt-api: WDF_TASK_SEND_OPTIONS_INIT
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
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# WDF_TASK_SEND_OPTIONS_INIT function



## -description
<p>
			For internal use only.</p>


## -syntax

````
FORCEINLINE VOID WDF_TASK_SEND_OPTIONS_INIT(
  _Out_ PWDF_TASK_SEND_OPTIONS Options,
  _In_  ULONG                  Flags
);
````


## -parameters
<dl>

### -param <i>Options</i> [out]

<dd></dd>

### -param <i>Flags</i> [in]

<dd></dd>
</dl>

## -returns
<p>This method does not return a value.</p>

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