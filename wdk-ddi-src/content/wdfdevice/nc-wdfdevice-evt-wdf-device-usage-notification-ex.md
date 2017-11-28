---
UID: NC.wdfdevice.EVT_WDF_DEVICE_USAGE_NOTIFICATION_EX
title: EVT_WDF_DEVICE_USAGE_NOTIFICATION_EX
author: windows-driver-content
description: A driver's EvtDeviceUsageNotificationEx event callback function determines whether a device can support a special file type.
old-location: wdf\evtdeviceusagenotificationex.htm
old-project: wdf
ms.assetid: A5C3E247-4883-4BFE-B36A-45AA989F36C9
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_REL_TIMEOUT_IN_US
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 2.0
req.alt-api: EvtDeviceUsageNotificationEx
req.alt-loc: Wdfdevice.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDF_DEVICE_USAGE_NOTIFICATION_EX callback



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>A driver's <i>EvtDeviceUsageNotificationEx</i> event callback function determines whether a device can support a special file type.</p>


## -prototype

````
EVT_WDF_DEVICE_USAGE_NOTIFICATION_EX EvtDeviceUsageNotificationEx;

NTSTATUS EvtDeviceUsageNotificationEx(
  _In_ WDFDEVICE             Device,
  _In_ WDF_SPECIAL_FILE_TYPE NotificationType,
  _In_ BOOLEAN               IsInNotificationPath
)
{ ... }
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>NotificationType</i> [in]

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff552509">WDF_SPECIAL_FILE_TYPE</a>-typed value that identifies the type of special file that the system is storing on the specified device.</p>
</dd>

### -param <i>IsInNotificationPath</i> [in]

<dd>
<p>A Boolean value which, if <b>TRUE</b>, indicates that the system has starting using the special file and, if <b>FALSE</b>, indicates that the system has finished using the special file.</p>
</dd>
</dl>

## -returns
<p>If the driver determines that the device can support the special file, the <i>EvtDeviceUsageNotificationEx</i> callback function must return STATUS_SUCCESS or another status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>(<i>status</i>) equals <b>TRUE</b>. Otherwise it must return a status value for which NT_SUCCESS(<i>status</i>) equals <b>FALSE</b>.</p>

## -remarks
<p>If your driver must provide driver-specific handling of special files, you must provide either an <i>EvtDeviceUsageNotificationEx</i> or an <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-usage-notification.md">EvtDeviceUsageNotification</a> event callback function. Do not provide both callback functions.</p>

<p>To register an <i>EvtDeviceUsageNotificationEx</i> callback function, a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546135">WdfDeviceInitSetPnpPowerEventCallbacks</a>. </p>

<p>If the driver's <i>EvtDeviceUsageNotificationEx</i> callback function returns a failure status, the framework propagates failure to other stacks that it may have notified earlier.</p>

<p>For more information about special files, see <a href="wdf.supporting_special_files">Supporting Special Files</a>.</p>

<p>To define an <i>EvtDeviceUsageNotificationEx</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDeviceUsageNotificationEx</i> callback function that is named <i>MyDeviceUsageNotificationEx</i>, use the <b>EVT_WDF_DEVICE_USAGE_NOTIFICATION_EX</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows.</p>

<p>The <b>EVT_WDF_DEVICE_USAGE_NOTIFICATION_EX</b> function type is defined in the Wdfdevice.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DEVICE_USAGE_NOTIFICATION_EX</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

<p>If your driver must provide driver-specific handling of special files, you must provide either an <i>EvtDeviceUsageNotificationEx</i> or an <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-usage-notification.md">EvtDeviceUsageNotification</a> event callback function. Do not provide both callback functions.</p>

<p>To register an <i>EvtDeviceUsageNotificationEx</i> callback function, a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546135">WdfDeviceInitSetPnpPowerEventCallbacks</a>. </p>

<p>If the driver's <i>EvtDeviceUsageNotificationEx</i> callback function returns a failure status, the framework propagates failure to other stacks that it may have notified earlier.</p>

<p>For more information about special files, see <a href="wdf.supporting_special_files">Supporting Special Files</a>.</p>

<p>To define an <i>EvtDeviceUsageNotificationEx</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDeviceUsageNotificationEx</i> callback function that is named <i>MyDeviceUsageNotificationEx</i>, use the <b>EVT_WDF_DEVICE_USAGE_NOTIFICATION_EX</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows.</p>

<p>The <b>EVT_WDF_DEVICE_USAGE_NOTIFICATION_EX</b> function type is defined in the Wdfdevice.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DEVICE_USAGE_NOTIFICATION_EX</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
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
</table>