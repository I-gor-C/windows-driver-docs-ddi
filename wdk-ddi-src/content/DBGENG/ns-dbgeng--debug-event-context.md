---
UID: NS.dbgeng._DEBUG_EVENT_CONTEXT
title: DEBUG_EVENT_CONTEXT
author: windows-driver-content
description: Defines context information about an event.
old-location: debugger\debug_event_context.htm
ms.assetid: 3748675F-8187-4072-A0D0-3764B4D20288
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: DbgEng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEBUG_EVENT_CONTEXT
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
ms.keywords: DEBUG_EVENT_CONTEXT, DEBUG_EVENT_CONTEXT, *PDEBUG_EVENT_CONTEXT
req.iface: IDebugSystemObjects4
---

# DEBUG_EVENT_CONTEXT structure



## -description
<p>Defines context information about an event.</p>


## -syntax

````
typedef struct _DEBUG_EVENT_CONTEXT {
  ULONG Size;
  ULONG ProcessEngineId;
  ULONG ThreadEngineId;
  ULONG FrameEngineId;
} DEBUG_EVENT_CONTEXT, *PDEBUG_EVENT_CONTEXT;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size of the event.</p>
</dd>

### -field <b>ProcessEngineId</b>

<dd>
<p>The process engine ID of the event.</p>
</dd>

### -field <b>ThreadEngineId</b>

<dd>
<p>The process thread ID of the event.</p>
</dd>

### -field <b>FrameEngineId</b>

<dd>
<p>The frame engine ID of the event.</p>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541478">DEBUG_EVENT_XXX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20DEBUG_EVENT_CONTEXT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
