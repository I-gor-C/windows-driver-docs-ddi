---
UID: NF.wdm.IoWMIWriteEvent
title: IoWMIWriteEvent
author: windows-driver-content
description: The IoWMIWriteEvent routine delivers a given event to the user-mode WMI components for notification.
old-location: kernel\iowmiwriteevent.htm
old-project: kernel
ms.assetid: 6b98861c-b108-4b07-b494-e3647d03de4c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoWMIWriteEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoWMIWriteEvent
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# IoWMIWriteEvent function



## -description
<p>The <b>IoWMIWriteEvent</b> routine delivers a given event to the user-mode WMI components for notification.</p>


## -syntax

````
NTSTATUS IoWMIWriteEvent(
  _Inout_ PVOID WnodeEventItem
);
````


## -parameters
<dl>

### -param <i>WnodeEventItem</i> [in, out]

<dd>
<p>Pointer to a <a href="kernel.wnode_event_item">WNODE_EVENT_ITEM</a> structure to be delivered to the user-mode WMI components that requested notification of the event. </p>
</dd>
</dl>

## -returns
<p><b>IoWMIWriteEvent</b> returns a status code from the following list:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>Indicates that WMI has successfully queued the event for delivery to the user-mode WMI components.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>Indicates that WMI services are unavailable. </p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>Indicates that the event item specified exceeds the maximum allowed size.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Indicates that insufficient resources were available for WMI to queue the event for delivery.</p>

<p> </p>

## -remarks
<p>The WNODE_EVENT_ITEM structure that is allocated by the caller and passed in <i>WnodeEventItem</i> must be allocated from nonpaged pool. If <b>IoWMIWriteEvent</b> returns STATUS_SUCCESS, the memory for the event item will automatically be freed by the system. If <b>IoWMIWriteEvent</b> returns anything other than STATUS_SUCCESS, it is the caller's responsibility to free the buffer.</p>

<p>Drivers should only call <b>IoWMIWriteEvent</b> for events that have been enabled for WMI. This ensures that there is an event consumer waiting for indication on that event.</p>

<p>Callers of this routine must be running at IRQL &lt;= APC_LEVEL, with one exception. When the <b>Flags</b> member of the <a href="..\wmistr\ns-wmistr--wnode-header.md">WNODE_HEADER</a> structure contains WNODE_FLAG_TRACED_GUID, <b>IoWMIWriteEvent</b> can be called at any IRQL. (The <b>WNODE_HEADER</b> structure is a member of the <a href="kernel.wnode_event_item">WNODE_EVENT_ITEM</a> structure that the <i>WnodeEventItem</i> parameter points to.)</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-iowmideviceobjecttoproviderid.md">IoWmiDeviceObjectToProviderId</a>
</dt>
<dt>
<a href="kernel.wnode_event_item">WNODE_EVENT_ITEM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoWMIWriteEvent routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
