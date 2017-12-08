---
UID: NS.dbgeng._DEBUG_LAST_EVENT_INFO_EXIT_THREAD
title: DEBUG_LAST_EVENT_INFO_EXIT_THREAD
author: windows-driver-content
description: Describes the exit thread of the last event.
old-location: debugger\debug_last_event_info_exit_thread.htm
old-project: debugger
ms.assetid: 1C7E79F2-120A-424B-B4E3-EF202FA90C2A
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: DEBUG_LAST_EVENT_INFO_EXIT_THREAD, DEBUG_LAST_EVENT_INFO_EXIT_THREAD, *PDEBUG_LAST_EVENT_INFO_EXIT_THREAD
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
req.alt-api: DEBUG_LAST_EVENT_INFO_EXIT_THREAD
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

# DEBUG_LAST_EVENT_INFO_EXIT_THREAD structure



## -description
<p>Describes the exit thread of the last event.</p>


## -syntax

````
typedef struct _DEBUG_LAST_EVENT_INFO_EXIT_THREAD {
  ULONG ExitCode;
} DEBUG_LAST_EVENT_INFO_EXIT_THREAD, *PDEBUG_LAST_EVENT_INFO_EXIT_THREAD;
````


## -struct-fields
<dl>

### -field ExitCode

<dd>
<p>The exit code of the thread.</p>
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