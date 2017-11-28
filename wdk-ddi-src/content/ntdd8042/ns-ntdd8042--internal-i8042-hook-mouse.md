---
UID: NS.ntdd8042._INTERNAL_I8042_HOOK_MOUSE
title: INTERNAL_I8042_HOOK_MOUSE
author: windows-driver-content
description: INTERNAL_I8042_HOOK_MOUSE is used by I8042prt to connect an optional callback routine that supplements the operation of the mouse ISR. The callback can be supplied by an optional, vendor-supplied, upper-level filter driver.
old-location: hid\internal_i8042_hook_mouse.htm
old-project: hid
ms.assetid: 7ac9fc14-9e94-412b-811a-6013d46020a0
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: INTERNAL_I8042_HOOK_MOUSE, INTERNAL_I8042_HOOK_MOUSE, *PINTERNAL_I8042_HOOK_MOUSE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntdd8042.h
req.include-header: Ntdd8042.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: INTERNAL_I8042_HOOK_MOUSE
req.alt-loc: ntdd8042.h
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
---

# INTERNAL_I8042_HOOK_MOUSE structure



## -description
<p>INTERNAL_I8042_HOOK_MOUSE is used by I8042prt to connect an optional callback routine that supplements the operation of the mouse ISR. The callback can be supplied by an optional, vendor-supplied, upper-level filter driver.</p>


## -syntax

````
typedef struct _INTERNAL_I8042_HOOK_MOUSE {
  PVOID                 Context;
  PI8042_MOUSE_ISR      IsrRoutine;
  PI8042_ISR_WRITE_PORT IsrWritePort;
  PI8042_QUEUE_PACKET   QueueMousePacket;
  PVOID                 CallContext;
} INTERNAL_I8042_HOOK_MOUSE, *PINTERNAL_I8042_HOOK_MOUSE;
````


## -struct-fields
<dl>

### -field <b>Context</b>

<dd>
<p>Pointer, if non-<b>NULL</b>, to the context that must be used with the <b>IsrRoutine</b> routine. Otherwise, <b>Context</b> is <b>NULL</b>. </p>
</dd>

### -field <b>IsrRoutine</b>

<dd>
<p>Pointer, if non-<b>NULL</b>, to an optional <a href="https://msdn.microsoft.com/library/windows/hardware/ff543252">PI8042_MOUSE_ISR</a> callback that customizes the operation of the I8042prt mouse ISR. Otherwise, <b>IsrRoutine </b>is <b>NULL</b>. </p>
</dd>

### -field <b>IsrWritePort</b>

<dd>
<p>Pointer to the system-supplied mouse <a href="https://msdn.microsoft.com/library/windows/hardware/ff543231">PI8042_ISR_WRITE_PORT</a> callback, which writes data to a mouse.</p>
</dd>

### -field <b>QueueMousePacket</b>

<dd>
<p>Pointer to the system-supplied mouse <a href="https://msdn.microsoft.com/library/windows/hardware/ff543263">PI8042_QUEUE_PACKET</a> callback, which queues a mouse input data packet for processing by the mouse's ISR deferred procedure call. </p>
</dd>

### -field <b>CallContext</b>

<dd>
<p>Pointer to the context that must be used with the <b>IsrWritePort</b> and <b>QueueMousePacket</b> routines. </p>
</dd>
</dl>

## -remarks
<p>This structure is only used with an <a href="https://msdn.microsoft.com/library/windows/hardware/ff541242">IOCTL_INTERNAL_I8042_HOOK_MOUSE</a> request. </p>

<p><b>Context</b>, <b>InitializationRoutine</b>, and <b>IsrRoutine</b> can be supplied by an optional, vendor-supplied, upper-level filter driver. </p>

<p><b>IsrWritePort</b>, <b>QueueMousePacket</b>, and <b>CallContext</b> are supplied by I8042prt.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntdd8042.h (include Ntdd8042.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541242">IOCTL_INTERNAL_I8042_HOOK_MOUSE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/34d0a7e9-4a1e-43ba-a643-800ebaadc360">MouFilter_IsrHook</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543231">PI8042_ISR_WRITE_PORT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543252">PI8042_MOUSE_ISR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543263">PI8042_QUEUE_PACKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20INTERNAL_I8042_HOOK_MOUSE structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
