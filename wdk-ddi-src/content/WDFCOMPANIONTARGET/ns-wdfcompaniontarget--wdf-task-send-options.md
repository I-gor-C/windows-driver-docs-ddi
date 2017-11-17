---
UID: NS.wdfcompaniontarget._WDF_TASK_SEND_OPTIONS
title: WDF_TASK_SEND_OPTIONS
author: windows-driver-content
description: For internal use only.
old-location: wdf\wdf_task_send_options.htm
ms.assetid: cb2fd11c-c6a5-4499-a340-f96ffcfbbe0f
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfcompaniontarget.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.23
req.umdf-ver: 
req.alt-api: WDF_TASK_SEND_OPTIONS
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: WDF_TASK_SEND_OPTIONS, WDF_TASK_SEND_OPTIONS, *PWDF_TASK_SEND_OPTIONS
req.iface: 
req.product: Windows 10 or later.
---

# WDF_TASK_SEND_OPTIONS structure



## -description
<p>For internal use only.</p>


## -syntax

````
typedef struct _WDF_TASK_SEND_OPTIONS {
  ULONG    Size;
  ULONG    Flags;
  LONGLONG Timeout;
} WDF_TASK_SEND_OPTIONS, *PWDF_TASK_SEND_OPTIONS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd></dd>

### -field <b>Flags</b>

<dd></dd>

### -field <b>Timeout</b>

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