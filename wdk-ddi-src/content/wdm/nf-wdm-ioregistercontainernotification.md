---
UID: NF.wdm.IoRegisterContainerNotification
title: IoRegisterContainerNotification
author: windows-driver-content
description: The IoRegisterContainerNotification routine registers a kernel-mode driver to receive notifications about a specified class of events.
old-location: kernel\ioregistercontainernotification.htm
old-project: kernel
ms.assetid: 5cfef8cc-b6b8-4b97-b8da-bf579e26f64d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoRegisterContainerNotification
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h, Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoRegisterContainerNotification
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
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoRegisterContainerNotification function



## -description
<p>The <b>IoRegisterContainerNotification</b> routine registers a kernel-mode driver to receive notifications about a specified class of events. </p>


## -syntax

````
NTSTATUS IoRegisterContainerNotification(
  _In_     IO_CONTAINER_NOTIFICATION_CLASS     NotificationClass,
  _In_     PIO_CONTAINER_NOTIFICATION_FUNCTION CallbackFunction,
  _In_opt_ PVOID                               NotificationInformation,
  _In_     ULONG                               NotificationInformationLength,
  _Out_    PVOID                               CallbackRegistration
);
````


## -parameters
<dl>

### -param NotificationClass [in]

<dd>
<p>Specifies the class of events for which the caller (driver) requests notifications. Set this parameter to the following <a href="..\wdm\ne-wdm--io-container-notification-class.md">IO_CONTAINER_NOTIFICATION_CLASS</a> enumeration value:</p>
<ul>
<li>
<p><b>IoSessionStateNotification</b></p>
</li>
</ul>
<p>For more information, see the following Remarks section. </p>
</dd>

### -param CallbackFunction [in]

<dd>
<p>A pointer to a callback function that is implemented by the caller (driver). The I/O manager calls this function to notify the caller when an event of the class indicated by <i>NotificationClass</i> occurs. For <i>NotificationClass</i> = <b>IoSessionStateNotification</b>, this parameter is a pointer to a caller-supplied <a href="..\wdm\nc-wdm-io-session-notification-function.md">IO_SESSION_NOTIFICATION_FUNCTION</a> function. However, the caller should cast this function pointer to type PIO_CONTAINER_NOTIFICATION_FUNCTION to match the parameter type. For more information, see the following Remarks section.</p>
</dd>

### -param NotificationInformation [in, optional]

<dd>
<p>A pointer to a caller-allocated buffer that contains the notification information structure for an event of the class specified by <i>NotificationClass</i>. For <i>NotificationClass</i> = <b>IoSessionStateNotification</b>, <i>NotificationInformation</i> points to an <a href="..\wdm\ns-wdm--io-session-state-notification.md">IO_SESSION_STATE_NOTIFICATION</a> structure. The caller must fill out this structure before it calls <b>IoRegisterContainerNotification</b>. During this call, <b>IoRegisterContainerNotification</b> copies the data from this structure, and the I/O manager does not access the driver's copy of the structure after the call returns.</p>
</dd>

### -param NotificationInformationLength [in]

<dd>
<p>The size, in bytes, of the notification information structure contained in the buffer that is pointed to by <i>NotificationInformation</i>. For <i>NotificationClass</i> = <b>IoSessionStateNotification</b>, set this parameter to <b>sizeof</b>(<b>IO_SESSION_STATE_NOTIFICATION</b>).</p>
</dd>

### -param CallbackRegistration [out]

<dd>
<p>A pointer to a location into which this routine writes the address of a container notification registration object. This object is an opaque, system object in which the I/O manager stores information about the caller's container notification registration. When notifications are no longer required, the caller cancels the registration by passing this object pointer to the <a href="..\wdm\nf-wdm-iounregistercontainernotification.md">IoUnregisterContainerNotification</a> routine.</p>
</dd>
</dl>

## -returns
<p><b>IoRegisterContainerNotification</b> returns STATUS_SUCCESS if the call is successful. Possible error return values include the following:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_1</b></dt>
</dl><p>Parameter <i>NotificationClass</i> is not a valid <b>IO_CONTAINER_NOTIFICATION_CLASS</b> enumeration constant. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER_3</b></dt>
</dl><p>The information in the structure that is pointed to by <i>NotificationInformation</i> is incorrect.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_4</b></dt>
</dl><p>Parameter <i>NotificationInformationLength</i> does not equal the size of the notification information structure that is required for use with the specified <i>NotificationClass</i> parameter value.</p><dl>
<dt><b>STATUS_ALREADY_COMMITTED</b></dt>
</dl><p>The driver is already registered to receive <i>NotificationClass</i> notifications of events that are associated with the specified I/O object. </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The operating system has insufficient resources to create the requested registration.</p>

<p> </p>

## -remarks
<p>This routine can potentially support notifications of events in a variety of event classes. In Windows 7, this routine supports only <b>IoSessionStateNotification</b> notifications, which notify a kernel-mode driver of changes in the status of user sessions that the driver is interested in. For user-mode applications, the <a href="http://go.microsoft.com/fwlink/p/?linkid=155043">WTSRegisterSessionNotification</a> function fills a similar role.</p>

<p>The function pointer type for the <i>CallbackFunction</i> parameter is defined as follows:</p>

<p>The caller should cast the callback function pointer to this type to match the <i>CallbackFunction</i> parameter type. <b>IoRegisterContainerNotification</b> determines the actual type of the callback function pointer from the <i>NotificationClass</i> parameter. For <i>NotificationClass</i> = <b>IoSessionStateNotification</b>, <i>CallbackFunction</i> points to an <a href="..\wdm\nc-wdm-io-session-notification-function.md">IO_SESSION_NOTIFICATION_FUNCTION</a> function.</p>

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
<p>Available in Windows 7 and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, Ntifs.h, or Fltkernel.h)</dt>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ne-wdm--io-container-notification-class.md">IO_CONTAINER_NOTIFICATION_CLASS</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-io-session-notification-function.md">IO_SESSION_NOTIFICATION_FUNCTION</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--io-session-state-notification.md">IO_SESSION_STATE_NOTIFICATION</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iounregistercontainernotification.md">IoUnregisterContainerNotification</a>
</dt>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=155043">WTSRegisterSessionNotification</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoRegisterContainerNotification routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
