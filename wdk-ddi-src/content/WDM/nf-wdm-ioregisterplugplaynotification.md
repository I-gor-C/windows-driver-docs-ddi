---
UID: NF.wdm.IoRegisterPlugPlayNotification
title: IoRegisterPlugPlayNotification
author: windows-driver-content
description: The IoRegisterPlugPlayNotification routine registers a Plug and Play (PnP) notification callback routine to be called when a PnP event of the specified category occurs.
old-location: kernel\ioregisterplugplaynotification.htm
ms.assetid: 06fd10ab-3478-4b01-b678-24944f17fa9d
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoRegisterPlugPlayNotification
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: MarkPower, MarkPowerDown, MarkQueryRelations, MarkStartDevice, PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
ms.keywords: IoRegisterPlugPlayNotification
req.iface: 
req.product: Windows 10 or later.
---

# IoRegisterPlugPlayNotification function



## -description
<p>The <b>IoRegisterPlugPlayNotification</b> routine registers a Plug and Play (PnP) notification callback routine to be called when a PnP event of the specified category occurs.</p>


## -syntax

````
NTSTATUS IoRegisterPlugPlayNotification(
  _In_     IO_NOTIFICATION_EVENT_CATEGORY        EventCategory,
  _In_     ULONG                                 EventCategoryFlags,
  _In_opt_ PVOID                                 EventCategoryData,
  _In_     PDRIVER_OBJECT                        DriverObject,
  _In_     PDRIVER_NOTIFICATION_CALLBACK_ROUTINE CallbackRoutine,
  _In_opt_ PVOID                                 Context,
  _Out_    PVOID                                 *NotificationEntry
);
````


## -parameters
<dl>

### -param <i>EventCategory</i> [in]

<dd>
<p>The category of PnP event for which the callback routine is being registered. <i>EventCategory</i> must be one of the following: </p>
<p></p>
<dl>

### -param <a id="EventCategoryDeviceInterfaceChange"></a><a id="eventcategorydeviceinterfacechange"></a><a id="EVENTCATEGORYDEVICEINTERFACECHANGE"></a><b>EventCategoryDeviceInterfaceChange</b>

<dd>
<p>PnP events in this category include the arrival (enabling) of a new instance of a <a href="https://msdn.microsoft.com/C989D2D3-E8DE-4D64-86EE-3D3B3906390D">device interface class</a> (GUID_DEVICE_INTERFACE_ARRIVAL), or the removal (disabling) of an existing device interface instance (GUID_DEVICE_INTERFACE_REMOVAL).</p>
</dd>

### -param <a id="EventCategoryHardwareProfileChange"></a><a id="eventcategoryhardwareprofilechange"></a><a id="EVENTCATEGORYHARDWAREPROFILECHANGE"></a><b>EventCategoryHardwareProfileChange</b>

<dd>
<p>PnP events in this category include query-change (GUID_HWPROFILE_QUERY_CHANGE), change-complete (GUID_HWPROFILE_CHANGE_COMPLETE), and change-cancel (GUID_HWPROFILE_CHANGE_CANCELLED) of a hardware profile.</p>
</dd>

### -param <a id="EventCategoryTargetDeviceChange"></a><a id="eventcategorytargetdevicechange"></a><a id="EVENTCATEGORYTARGETDEVICECHANGE"></a><b>EventCategoryTargetDeviceChange</b>

<dd>
<p>PnP events in this category include events related to removing a device: the device's drivers received a query-remove IRP (GUID_TARGET_DEVICE_QUERY_REMOVE), the drivers completed a remove IRP (GUID_TARGET_DEVICE_REMOVE_COMPLETE), or the drivers received a cancel-remove IRP (GUID_TARGET_DEVICE_REMOVE_CANCELLED). This category is also used for custom notification events.</p>
</dd>
</dl>
</dd>

### -param <i>EventCategoryFlags</i> [in]

<dd>
<p>Flag bits that modify the registration operation. Possible values include:</p>
<p></p>
<dl>

### -param <a id="PNPNOTIFY_DEVICE_INTERFACE_INCLUDE_EXISTING_INTERFACES"></a><a id="pnpnotify_device_interface_include_existing_interfaces"></a>PNPNOTIFY_DEVICE_INTERFACE_INCLUDE_EXISTING_INTERFACES

<dd>
<p>Only valid with an <i>EventCategory</i> of <b>EventCategoryDeviceInterfaceChange</b>. If set, the PnP manager calls the driver callback routine for each device interface instance that is currently registered and active and registers the callback routine for future arrivals or removals of device interface instances.</p>
</dd>
</dl>
</dd>

### -param <i>EventCategoryData</i> [in, optional]

<dd>
<p>A pointer to further information about the events for which <i>CallbackRoutine</i> is being registered. The information varies for different <i>EventCategory</i> values:</p>
<ul>
<li>
<p>When <i>EventCategory</i> is <b>EventCategoryDeviceInterfaceChange</b>, <i>EventCategoryData</i> must point to a GUID specifying a device interface class. <i>CallbackRoutine</i> will be called when an interface of that class is enabled or removed.</p>
</li>
<li>
<p>When <i>EventCategory</i> is <b>EventCategoryHardwareProfileChange</b>, <i>EventCategoryData</i> must be <b>NULL</b>.</p>
</li>
<li>
<p>When <i>EventCategory</i> is <b>EventCategoryTargetDeviceChange</b>, <i>EventCategoryData</i> must point to the file object for which PnP notification is requested.</p>
</li>
</ul>
</dd>

### -param <i>DriverObject</i> [in]

<dd>
<p>A pointer to the caller's driver object.</p>
<p>To ensure that the driver remains loaded while it is registered for PnP notification, this call increments the reference count on <i>DriverObject</i>. The PnP manager decrements the reference count when this registration is removed.</p>
</dd>

### -param <i>CallbackRoutine</i> [in]

<dd>
<p>A pointer to the PnP notification callback routine to be called when the specified PnP event occurs.</p>
<p>The function prototype for this callback routine is defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef NTSTATUS 
  DRIVER_NOTIFICATION_CALLBACK_ROUTINE(
    _In_ PVOID NotificationStructure,
    _Inout_opt_ PVOID Context
    );</pre>
</td>
</tr>
</table></span></div>
<p>The callback routine's <i>NotificationStructure</i> is specific to the <i>EventCategory</i> value, as shown in the following table.</p>
<table>
<tr>
<th>Event category</th>
<th>Notification structure</th>
</tr>
<tr>
<td>
<p><b>EventCategoryDeviceInterfaceChange</b></p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543134">DEVICE_INTERFACE_CHANGE_NOTIFICATION</a>
</p>
</td>
</tr>
<tr>
<td>
<p><b>EventCategoryHardwareProfileChange</b></p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547073">HWPROFILE_CHANGE_NOTIFICATION</a>
</p>
</td>
</tr>
<tr>
<td>
<p><b>EventCategoryTargetDeviceChange</b></p>
</td>
<td>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564601">TARGET_DEVICE_REMOVAL_NOTIFICATION</a>
</p>
</td>
</tr>
</table>
<p> </p>
<p>The callback routine's <i>Context</i> parameter contains the context data the driver supplied during registration.</p>
<p>For information about including a function declaration for the callback routine  that meets the requirements of <a href="NULL">Static Driver Verifier</a> (SDV), see Examples.</p>
<p>The PnP manager calls driver callback routines at IRQL = PASSIVE_LEVEL.</p>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated buffer containing context that the PnP manager passes to the callback routine.</p>
</dd>

### -param <i>NotificationEntry</i> [out]

<dd>
<p>A pointer to an opaque value returned by this call that identifies the registration. Pass this value to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550404">IoUnregisterPlugPlayNotificationEx</a> routine to remove the registration. (In versions of Windows before Windows 7, call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550398">IoUnregisterPlugPlayNotification</a> routine instead of <b>IoUnregisterPlugPlayNotificationEx</b>.)</p>
</dd>
</dl>

## -returns
<p><b>IoRegisterPlugPlayNotification</b> returns STATUS_SUCCESS or an appropriate error status.</p>

## -remarks
<p>A driver registers for an event category. Each category includes one or more types of PnP events.</p>

<p>A driver can register different callback routines for different event categories or can register a single callback routine. A single callback routine can cast the <i>NotificationStructure</i> to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff558805">PLUGPLAY_NOTIFICATION_HEADER</a> and use the <b>Event</b> field to determine the exact type of the notification structure.</p>

<p>PnP notification callback routines should complete their tasks as quickly as possible and return control to the PnP manager, to prevent delays in notifying other drivers and applications that have registered for the event.</p>

<p>The PnP manager does not take out a reference on the file object when a driver registers for notification of an <b>EventCategoryTargetDeviceChange</b> event. If the driver's PnP notification callback routine requires access to the file object, the driver should take out an extra reference on the file object before calling <b>IoRegisterPlugPlayNotification</b>.</p>

<p>Typically, Kernel-Mode Driver Framework (KMDF) drivers should call <b>IoRegisterPlugPlayNotification</b> from their <a href="https://msdn.microsoft.com/9dbc66db-ea94-4e6a-9618-00999a9dd641">EvtDeviceSelfManagedIoInit</a> callback function, and should call <b>IoUnregisterPlugPlayNotification</b> from their <a href="https://msdn.microsoft.com/639ff3fd-ce38-417e-8fc4-a03ad259a5c8">EvtDeviceSelfManagedIoCleanup</a> callback function. These drivers should <u>not</u> call <b>IoRegisterPlugPlayNotification</b> from their <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> callback function; otherwise, the PnP notification callback routine might be called before the driver stack is started by PnP, in which case the driver will not be prepared to handle the notification.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565480">Using PnP Notification</a>.</p>

<p>To define a PnP notification callback routine, you must first provide a function declaration that identifies the type of callback routine you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a PnP notification callback routine that is named <code>MyCallbackRoutine</code>, use the DRIVER_NOTIFICATION_CALLBACK_ROUTINE type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The DRIVER_NOTIFICATION_CALLBACK_ROUTINE function type is defined in the Wdm.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the DRIVER_NOTIFICATION_CALLBACK_ROUTINE function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/3260b53e-82be-4dbc-8ac5-d0e52de77f9d">Declaring Functions by Using Function Role Types for WDM Drivers</a>. For information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

<p>A driver registers for an event category. Each category includes one or more types of PnP events.</p>

<p>A driver can register different callback routines for different event categories or can register a single callback routine. A single callback routine can cast the <i>NotificationStructure</i> to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff558805">PLUGPLAY_NOTIFICATION_HEADER</a> and use the <b>Event</b> field to determine the exact type of the notification structure.</p>

<p>PnP notification callback routines should complete their tasks as quickly as possible and return control to the PnP manager, to prevent delays in notifying other drivers and applications that have registered for the event.</p>

<p>The PnP manager does not take out a reference on the file object when a driver registers for notification of an <b>EventCategoryTargetDeviceChange</b> event. If the driver's PnP notification callback routine requires access to the file object, the driver should take out an extra reference on the file object before calling <b>IoRegisterPlugPlayNotification</b>.</p>

<p>Typically, Kernel-Mode Driver Framework (KMDF) drivers should call <b>IoRegisterPlugPlayNotification</b> from their <a href="https://msdn.microsoft.com/9dbc66db-ea94-4e6a-9618-00999a9dd641">EvtDeviceSelfManagedIoInit</a> callback function, and should call <b>IoUnregisterPlugPlayNotification</b> from their <a href="https://msdn.microsoft.com/639ff3fd-ce38-417e-8fc4-a03ad259a5c8">EvtDeviceSelfManagedIoCleanup</a> callback function. These drivers should <u>not</u> call <b>IoRegisterPlugPlayNotification</b> from their <a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a> callback function; otherwise, the PnP notification callback routine might be called before the driver stack is started by PnP, in which case the driver will not be prepared to handle the notification.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565480">Using PnP Notification</a>.</p>

<p>To define a PnP notification callback routine, you must first provide a function declaration that identifies the type of callback routine you're defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it's a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define a PnP notification callback routine that is named <code>MyCallbackRoutine</code>, use the DRIVER_NOTIFICATION_CALLBACK_ROUTINE type as shown in this code example:</p>

<p>Then, implement your callback routine as follows:</p>

<p>The DRIVER_NOTIFICATION_CALLBACK_ROUTINE function type is defined in the Wdm.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the DRIVER_NOTIFICATION_CALLBACK_ROUTINE function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/3260b53e-82be-4dbc-8ac5-d0e52de77f9d">Declaring Functions by Using Function Role Types for WDM Drivers</a>. For information about _Use_decl_annotations_, see <a href="http://go.microsoft.com/fwlink/p/?linkid=286697">Annotating Function Behavior</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh975188">MarkPower</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975189">MarkPowerDown</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975190">MarkQueryRelations</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975191">MarkStartDevice</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543134">DEVICE_INTERFACE_CHANGE_NOTIFICATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/639ff3fd-ce38-417e-8fc4-a03ad259a5c8">EvtDeviceSelfManagedIoCleanup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/9dbc66db-ea94-4e6a-9618-00999a9dd641">EvtDeviceSelfManagedIoInit</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b20db029-ee2c-4fb1-bd69-ccd2e37fdc9a">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547073">HWPROFILE_CHANGE_NOTIFICATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550398">IoUnregisterPlugPlayNotification</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550404">IoUnregisterPlugPlayNotificationEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558805">PLUGPLAY_NOTIFICATION_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564596">TARGET_DEVICE_CUSTOM_NOTIFICATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564601">TARGET_DEVICE_REMOVAL_NOTIFICATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoRegisterPlugPlayNotification routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
