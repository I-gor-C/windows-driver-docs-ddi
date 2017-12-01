---
UID: NS.dbgeng._DEBUG_LAST_EVENT_INFO_EXCEPTION
title: DEBUG_LAST_EVENT_INFO_EXCEPTION
author: windows-driver-content
description: Describes the exception of the last event.
old-location: debugger\debug_last_event_info_exception.htm
old-project: debugger
ms.assetid: FB4EBA71-5144-440A-AFD1-7460903C9189
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: DEBUG_LAST_EVENT_INFO_EXCEPTION, DEBUG_LAST_EVENT_INFO_EXCEPTION, *PDEBUG_LAST_EVENT_INFO_EXCEPTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dbgeng.h
req.include-header: DbgEng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEBUG_LAST_EVENT_INFO_EXCEPTION
req.alt-loc: DbgEng.h
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
req.iface: IDebugSystemObjects4
---

# DEBUG_LAST_EVENT_INFO_EXCEPTION structure



## -description
<p>Describes the exception of the last event.</p>


## -syntax

````
typedef struct _DEBUG_LAST_EVENT_INFO_EXCEPTION {
  EXCEPTION_RECORD64 ExceptionRecord;
  ULONG              FirstChance;
} DEBUG_LAST_EVENT_INFO_EXCEPTION, *PDEBUG_LAST_EVENT_INFO_EXCEPTION;
````


## -struct-fields
<dl>

### -field <b>ExceptionRecord</b>

<dd>
<p>An exception record.</p>
</dd>

### -field <b>FirstChance</b>

<dd>
<p>A first chance value.</p>
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
<dt>DbgEng.h (include DbgEng.h)</dt>
</dl>
</td>
</tr>
</table>