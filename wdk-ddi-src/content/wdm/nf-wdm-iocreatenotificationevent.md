---
UID: NF.wdm.IoCreateNotificationEvent
title: IoCreateNotificationEvent
author: windows-driver-content
description: The IoCreateNotificationEvent routine creates or opens a named notification event used to notify one or more threads of execution that an event has occurred.
old-location: kernel\iocreatenotificationevent.htm
old-project: kernel
ms.assetid: 44be034e-0c82-4980-a246-132d1b50dee1
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoCreateNotificationEvent
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
req.alt-api: IoCreateNotificationEvent
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlIoPassive4, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoCreateNotificationEvent function



## -description
<p>The <b>IoCreateNotificationEvent</b> routine creates or opens a named notification event used to notify one or more threads of execution that an event has occurred. </p>


## -syntax

````
PKEVENT IoCreateNotificationEvent(
  _In_  PUNICODE_STRING EventName,
  _Out_ PHANDLE         EventHandle
);
````


## -parameters
<dl>

### -param <i>EventName</i> [in]

<dd>
<p>Pointer to a buffer containing a null-terminated Unicode string that names the event.</p>
</dd>

### -param <i>EventHandle</i> [out]

<dd>
<p>Pointer to a location in which to return a handle for the event object. In Windows Server 2003 and later versions of Windows, the returned handle is a <a href="wdkgloss.k#wdkgloss.kernel_handle#wdkgloss.kernel_handle"><i>kernel handle</i></a>. </p>
</dd>
</dl>

## -returns
<p><b>IoCreateNotificationEvent</b> returns a pointer to the created or opened event object or <b>NULL</b> if the event object could not be created or opened. </p>

## -remarks
<p><b>IoCreateNotificationEvent</b> creates and opens the event object if it does not already exist. <b>IoCreateNotificationEvent</b> sets the state of a new notification event to Signaled. If the event object already exists, <b>IoCreateNotificationEvent</b> just opens the event object.</p>

<p>When a notification event is set to the Signaled state it remains in that state until it is explicitly cleared.</p>

<p>Notification events, like synchronization events, are used to coordinate execution. Unlike a synchronization event, a notification event is not auto-resetting. Once a notification event is in the Signaled state, it remains in that state until it is explicitly reset (with a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551980">KeClearEvent</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff553176">KeResetEvent</a>).</p>

<p>To synchronize on a notification event:</p>

<p>Open the notification event with <b>IoCreateNotificationEvent</b>. Identify the event with the <i>EventName</i> string.</p>

<p>Wait for the event to be signaled by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a> with the PKEVENT returned by <b>IoCreateNotificationEvent</b>. More than one thread of execution can wait for a given notification event. To poll instead of stall, specify a <i>Timeout</i> of zero to <b>KeWaitForSingleObject</b>.</p>

<p>Close the handle to the notification event with <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a> when access to the event is no longer needed. </p>

<p>Sharing event objects between user mode and kernel mode requires care. There are two main methods for sharing event objects: </p>

<p>The user-mode application creates the event object and passes a handle to the object to the driver by sending an IOCTL to the driver. The driver must handle the IOCTL in the context of the process that created the event object and must validate the handle by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff558679">ObReferenceObjectByHandle</a>. This method is the recommended method for sharing event objects between user and kernel modes.</p>

<p>The driver creates a named event object in the \\BaseNamedObjects object directory. You can open a kernel-mode event named \\BaseNamedObjects\<i>Xxx</i> in user mode under the name <i>Xxx</i>. Note that security settings can prevent an application from opening the event. For more information, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=70044">OpenEvent Fails in a Non-Administrator Account</a> KB article. The \\BaseNamedObjects object directory is not created until the Microsoft Win32 subsystem initializes, so drivers that are loaded at boot time cannot create event objects in the \\BaseNamedObjects directory in their <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routines.</p>

<p>For more information about events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544323">Event Objects</a>. </p>

<p><b>IoCreateNotificationEvent</b> creates and opens the event object if it does not already exist. <b>IoCreateNotificationEvent</b> sets the state of a new notification event to Signaled. If the event object already exists, <b>IoCreateNotificationEvent</b> just opens the event object.</p>

<p>When a notification event is set to the Signaled state it remains in that state until it is explicitly cleared.</p>

<p>Notification events, like synchronization events, are used to coordinate execution. Unlike a synchronization event, a notification event is not auto-resetting. Once a notification event is in the Signaled state, it remains in that state until it is explicitly reset (with a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551980">KeClearEvent</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff553176">KeResetEvent</a>).</p>

<p>To synchronize on a notification event:</p>

<p>Open the notification event with <b>IoCreateNotificationEvent</b>. Identify the event with the <i>EventName</i> string.</p>

<p>Wait for the event to be signaled by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a> with the PKEVENT returned by <b>IoCreateNotificationEvent</b>. More than one thread of execution can wait for a given notification event. To poll instead of stall, specify a <i>Timeout</i> of zero to <b>KeWaitForSingleObject</b>.</p>

<p>Close the handle to the notification event with <a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a> when access to the event is no longer needed. </p>

<p>Sharing event objects between user mode and kernel mode requires care. There are two main methods for sharing event objects: </p>

<p>The user-mode application creates the event object and passes a handle to the object to the driver by sending an IOCTL to the driver. The driver must handle the IOCTL in the context of the process that created the event object and must validate the handle by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff558679">ObReferenceObjectByHandle</a>. This method is the recommended method for sharing event objects between user and kernel modes.</p>

<p>The driver creates a named event object in the \\BaseNamedObjects object directory. You can open a kernel-mode event named \\BaseNamedObjects\<i>Xxx</i> in user mode under the name <i>Xxx</i>. Note that security settings can prevent an application from opening the event. For more information, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=70044">OpenEvent Fails in a Non-Administrator Account</a> KB article. The \\BaseNamedObjects object directory is not created until the Microsoft Win32 subsystem initializes, so drivers that are loaded at boot time cannot create event objects in the \\BaseNamedObjects directory in their <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routines.</p>

<p>For more information about events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544323">Event Objects</a>. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547787">IrqlIoPassive4</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549045">IoCreateSynchronizationEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551980">KeClearEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553176">KeResetEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553253">KeSetEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561934">RtlInitUnicodeString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566417">ZwClose</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoCreateNotificationEvent routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
