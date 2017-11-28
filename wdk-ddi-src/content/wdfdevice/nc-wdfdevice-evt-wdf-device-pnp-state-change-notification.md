---
UID: NC.wdfdevice.EVT_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION
title: EVT_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION
author: windows-driver-content
description: A driver's EvtDevicePnpStateChange event callback function informs the driver that a device's Plug and Play (PnP) state machine is moving from one state to another.
old-location: wdf\evtdevicepnpstatechange.htm
old-project: wdf
ms.assetid: 5f08d331-0e58-45a3-93a3-b5e9a40b5af3
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
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: EvtDevicePnpStateChange
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

# EVT_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION callback



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>A driver's <i>EvtDevicePnpStateChange</i> event callback function informs the driver that a device's Plug and Play (PnP) state machine is moving from one state to another.</p>


## -prototype

````
EVT_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION EvtDevicePnpStateChange;

VOID EvtDevicePnpStateChange(
  _In_ WDFDEVICE                          Device,
  _In_ PCWDF_DEVICE_PNP_NOTIFICATION_DATA NotificationData
)
{ ... }
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>NotificationData</i> [in]

<dd>
<p>A pointer to a framework-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff551260">WDF_DEVICE_PNP_NOTIFICATION_DATA</a> structure that identifies the state machine's old and new states.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>To register an <i>EvtDevicePnpStateChange</i> callback function, a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546057">WdfDeviceInitRegisterPnpStateChangeCallback</a>.</p>

<p>Most drivers do not need to be notified when the framework's PnP state machine changes state. For more information about the framework's PnP state machine, see <a href="wdf.state_machines_in_the_framework">State Machines in the Framework</a>.</p>

<p>To define an <i>EvtDevicePnpStateChange</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDevicePnpStateChange</i> callback function that is named <i>MyDevicePnpStateChange</i>, use the <b>EVT_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION</b> function type is defined in the Wdfdevice.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

<p>To register an <i>EvtDevicePnpStateChange</i> callback function, a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546057">WdfDeviceInitRegisterPnpStateChangeCallback</a>.</p>

<p>Most drivers do not need to be notified when the framework's PnP state machine changes state. For more information about the framework's PnP state machine, see <a href="wdf.state_machines_in_the_framework">State Machines in the Framework</a>.</p>

<p>To define an <i>EvtDevicePnpStateChange</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDevicePnpStateChange</i> callback function that is named <i>MyDevicePnpStateChange</i>, use the <b>EVT_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION</b> function type is defined in the Wdfdevice.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<p>1.0</p>
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

## -see-also
<dl>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-power-policy-state-change-notification.md">EvtDevicePowerPolicyStateChange</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-power-state-change-notification.md">EvtDevicePowerStateChange</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
