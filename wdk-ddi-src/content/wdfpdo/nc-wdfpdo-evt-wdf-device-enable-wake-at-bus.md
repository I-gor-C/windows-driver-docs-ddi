---
UID: NC.wdfpdo.EVT_WDF_DEVICE_ENABLE_WAKE_AT_BUS
title: EVT_WDF_DEVICE_ENABLE_WAKE_AT_BUS
author: windows-driver-content
description: A bus driver's EvtDeviceEnableWakeAtBus event callback function performs bus-level operations that enable one of the bus's devices to trigger a wake-up signal on the bus.
old-location: wdf\evtdeviceenablewakeatbus.htm
old-project: wdf
ms.assetid: 902c9bdc-d83a-4bc2-802c-1aaba43c9e2e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_OBJECT_CONTEXT_TYPE_INFO, WDF_OBJECT_CONTEXT_TYPE_INFO, *PWDF_OBJECT_CONTEXT_TYPE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdfpdo.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: EvtDeviceEnableWakeAtBus
req.alt-loc: Wdfpdo.h
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

# EVT_WDF_DEVICE_ENABLE_WAKE_AT_BUS callback



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>A bus driver's <i>EvtDeviceEnableWakeAtBus</i> event callback function performs bus-level operations that enable one of the bus's devices to trigger a wake-up signal on the bus.</p>


## -prototype

````
EVT_WDF_DEVICE_ENABLE_WAKE_AT_BUS EvtDeviceEnableWakeAtBus;

NTSTATUS EvtDeviceEnableWakeAtBus(
  _In_ WDFDEVICE          Device,
  _In_ SYSTEM_POWER_STATE PowerState
)
{ ... }
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>PowerState</i> [in]

<dd>
<p>A SYSTEM_POWER_STATE-typed enumerator that identifies the system power state that the system or device will wake from.</p>
</dd>
</dl>

## -returns
<p>If the <i>EvtDeviceEnableWakeAtBus</i> callback function encountered no errors, it must return STATUS_SUCCESS or another status value for which <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a>(<i>status</i>) equals <b>TRUE</b>. Otherwise it must return a status value for which NT_SUCCESS(<i>status</i>) equals <b>FALSE</b>.</p>

<p>If NT_SUCCESS(status) equals <b>FALSE</b>, the framework calls the driver's <a href="..\wdfpdo\nc-wdfpdo-evt-wdf-device-disable-wake-at-bus.md">EvtDeviceDisableWakeAtBus</a> callback function.</p>

<p> 

For more information about this callback function's return values, see <a href="wdf.reporting_device_failures">Reporting Device Failures</a>.

</p>

## -remarks
<p>For more information about this callback function, see <a href="wdf.supporting_system_wake_up">Supporting System Wake-Up</a>.</p>

<p>To define an <i>EvtDeviceEnableWakeAtBus</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDeviceEnableWakeAtBus</i> callback function that is named <i>MyDeviceEnableWakeAtBus</i>, use the <b>EVT_WDF_DEVICE_ENABLE_WAKE_AT_BUS</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_DEVICE_ENABLE_WAKE_AT_BUS</b> function type is defined in the Wdfpdo.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DEVICE_ENABLE_WAKE_AT_BUS</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

<p>For more information about this callback function, see <a href="wdf.supporting_system_wake_up">Supporting System Wake-Up</a>.</p>

<p>To define an <i>EvtDeviceEnableWakeAtBus</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDeviceEnableWakeAtBus</i> callback function that is named <i>MyDeviceEnableWakeAtBus</i>, use the <b>EVT_WDF_DEVICE_ENABLE_WAKE_AT_BUS</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_DEVICE_ENABLE_WAKE_AT_BUS</b> function type is defined in the Wdfpdo.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DEVICE_ENABLE_WAKE_AT_BUS</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<dt>Wdfpdo.h (include Wdf.h)</dt>
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
<a href="..\wdfpdo\nc-wdfpdo-evt-wdf-device-disable-wake-at-bus.md">EvtDeviceDisableWakeAtBus</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_DEVICE_ENABLE_WAKE_AT_BUS callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
