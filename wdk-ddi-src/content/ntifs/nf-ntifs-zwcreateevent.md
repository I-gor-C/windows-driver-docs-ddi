---
UID: NF.ntifs.ZwCreateEvent
title: ZwCreateEvent
author: windows-driver-content
description: The ZwCreateEvent routine creates an event object, sets the initial state of the event to the specified value, and opens a handle to the object with the specified desired access.
old-location: kernel\zwcreateevent.htm
old-project: kernel
ms.assetid: c11265fb-df9d-405e-ac9f-e868ab392e7b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ZwCreateEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwCreateEvent,NtCreateEvent
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
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
---

# ZwCreateEvent function



## -description
<p>The <b>ZwCreateEvent</b> routine creates an event object, sets the initial state of the event to the specified value, and opens a handle to the object with the specified desired access.</p>


## -syntax

````
NTSTATUS ZwCreateEvent(
  _Out_    PHANDLE            EventHandle,
  _In_     ACCESS_MASK        DesiredAccess,
  _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes,
  _In_     EVENT_TYPE         EventType,
  _In_     BOOLEAN            InitialState
);
````


## -parameters
<dl>

### -param <i>EventHandle</i> [out]

<dd>
<p>A pointer to a variable that will receive the event object handle. The handle includes bookkeeping information, such as a reference count and security context.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> value that represents the desired types of access for the event object. The following table contains the event-specific ACCESS_MASK values.</p>
<table>
<tr>
<th>Value</th>
<th>Desired access</th>
</tr>
<tr>
<td>EVENT_QUERY_STATE</td>
<td>Query the state of the event object.</td>
</tr>
<tr>
<td>EVENT_MODIFY_STATE</td>
<td>Modify the state of the event object.</td>
</tr>
<tr>
<td>EVENT_ALL_ACCESS</td>
<td>All possible access rights to the event object.</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>ObjectAttributes</i> [in, optional]

<dd>
<p>A pointer to the object attributes structure supplied by the caller to be used for the specified object. These attributes would include the <b>ObjectName</b> and the <a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a>, for example. This parameter is initialized by calling the <a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a> macro.</p>
</dd>

### -param <i>EventType</i> [in]

<dd>
<p>The type of the event, which can be <b>SynchronizationEvent</b> or a <b>NotificationEvent</b>. These values belong to the <b>EVENT_TYPE</b> enumeration, which is defined in the Ntdef.h header file.  The event type can be modified with the REALTIME_OBJECT_FLAG modifier to provide priority-ordered queuing of wait requests.</p>
</dd>

### -param <i>InitialState</i> [in]

<dd>
<p>The initial state of the event object. Set to <b>TRUE</b> to initialize the event object to the Signaled state. Set to <b>FALSE</b> to initialize the event object to the not-Signaled state.</p>
</dd>
</dl>

## -returns
<p><b>ZwCreateEvent</b> returns STATUS_SUCCESS or an appropriate error status. Possible error status codes include the following:</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Resources required by this function could not be allocated.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The supplied <i>ObjectAttributes</i> structure contained an invalid parameter value.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_4</b></dt>
</dl><p>The specified <i>EventType</i> parameter was invalid. The allowable <i>EventType</i> values are <b>NotificationEvent</b> or <b>SynchronizationEvent</b>. The REALTIME_OBJECT_FLAG can also be specified for these <i>EventType</i> parameters.</p><dl>
<dt><b>STATUS_OBJECT_NAME_INVALID</b></dt>
</dl><p>The <i>ObjectAttributes</i> parameter contained an <b>ObjectName</b> in the <a href="..\d3dkmthk\ns-d3dkmthk--object-attributes.md">OBJECT_ATTRIBUTES</a> structure that was invalid.</p><dl>
<dt><b>STATUS_OBJECT_PATH_SYNTAX_BAD</b></dt>
</dl><p>The <i>ObjectAttributes</i> parameter did not contain a <b>RootDirectory</b> member, but the <b>ObjectName</b> member in the <b>OBJECT_ATTRIBUTES</b> structure was an empty string or did not contain an OBJECT_NAME_PATH_SEPARATOR character. This indicates incorrect syntax for the object path.</p><dl>
<dt><b>STATUS_PRIVILEGE_NOT_HELD</b></dt>
</dl><p>The caller did not have the required privilege to create a handle with the access specified in the <i>DesiredAccess</i> parameter.</p>

<p> </p>

## -remarks
<p><b>ZwCreateEvent</b> creates an event object, sets it initial state to the specified value, and opens a handle to the object with the specified desired access. </p>

<p><b>ZwCreateEvent</b> can create either notification or synchronization events.</p>

<p>Events are used to coordinate execution. Events can be used by file system drivers to allow a caller to wait for completion of the requested operation until the given event is set to the Signaled state. </p>

<p>Notification events can be used to notify one or more threads of execution that an event has occurred. Synchonization events can be used in the serialization of access to hardware between two otherwise unrelated drivers. </p>

<p>A synchonization event is auto-resetting. When a synchronization event is set to the Signaled state, a single thread of execution that was waiting for the event to be signaled is released, and the event is automatically reset to the Not-Signaled state.</p>

<p>Unlike a synchronization event, a notification event is not auto-resetting. Once a notification event is in the Signaled state, it remains in that state until it is explicitly reset.</p>

<p>To synchronize on a notification event:</p>

<p>Create the notification event with <b>ZwCreateEvent</b> with the <i>EventType</i> parameter set to <b>NotificationEvent</b>.</p>

<p>Wait for the event to be signaled by calling <a href="..\ntifs\nf-ntifs-zwwaitforsingleobject.md">ZwWaitForSingleObject</a> with the <i>EventHandle</i> returned by <b>ZwCreateEvent</b>. More than one thread of execution can wait for a given notification event to be signaled. To poll instead of stall, specify a <i>Timeout</i> of zero to <b>ZwWaitForSingleObject</b>.</p>

<p>Close the handle to the notification event with <a href="..\wdm\nf-wdm-zwclose.md">ZwClose</a> when access to the event is no longer needed.</p>

<p>The <b>ZwCreateEvent</b> function is called after the <b>InitializeObjectAttributes</b> macro is used to set attributes in the <b>OBJECT_ATTRIBUTES</b> structure for the object. </p>

<p>There are two alternate ways to specify the name of the object passed to <b>ZwCreateEvent</b>:</p>

<p>As a fully qualified pathname, supplied in the <b>ObjectName</b> member of the input <i>ObjectAttributes</i>.</p>

<p>As pathname relative to the directory represented by the handle in the <b>RootDirectory</b> member of the input <i>ObjectAttributes</i>.</p>

<p>To release the event, a driver calls <a href="..\wdm\nf-wdm-zwclose.md">ZwClose</a> with the event handle.</p>

<p>For more information about events, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff544323">Event Objects</a>.</p>

<p>For calls from kernel-mode drivers, the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <b>Nt<i>Xxx</i></b> and <b>Zw<i>Xxx</i></b> versions of a routine, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>

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
<p>Available starting with Windows XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="..\wudfwdm\nf-wudfwdm-initializeobjectattributes.md">InitializeObjectAttributes</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iocreatenotificationevent.md">IoCreateNotificationEvent</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iocreatesynchronizationevent.md">IoCreateSynchronizationEvent</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keclearevent.md">KeClearEvent</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keresetevent.md">KeResetEvent</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kesetevent.md">KeSetEvent</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-kewaitforsingleobject.md">KeWaitForSingleObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565438">Using Nt and Zw Versions of the Native System Services Routines</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwclose.md">ZwClose</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwsetevent.md">ZwSetEvent</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwwaitforsingleobject.md">ZwWaitForSingleObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwCreateEvent routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
