---
UID: NC.wdfchildlist.EVT_WDF_CHILD_LIST_DEVICE_REENUMERATED
title: EVT_WDF_CHILD_LIST_DEVICE_REENUMERATED
author: windows-driver-content
description: A driver's EvtChildListDeviceReenumerated event callback function enables the driver to approve or cancel a reenumeration of a specified device.
old-location: wdf\evtchildlistdevicereenumerated.htm
old-project: wdf
ms.assetid: 404436c3-6ddb-4212-ad51-23a956d7df52
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDBGEXTS_THREAD_OS_INFO, WDBGEXTS_THREAD_OS_INFO, *PWDBGEXTS_THREAD_OS_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: EvtChildListDeviceReenumerated
req.alt-loc: WdfChildlist.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDF_CHILD_LIST_DEVICE_REENUMERATED callback



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>A driver's <i>EvtChildListDeviceReenumerated</i> event callback function enables the driver to approve or cancel a reenumeration of a specified device. </p>


## -prototype

````
EVT_WDF_CHILD_LIST_DEVICE_REENUMERATED EvtChildListDeviceReenumerated;

BOOLEAN EvtChildListDeviceReenumerated(
  _In_  WDFCHILDLIST                          ChildList,
  _In_  WDFDEVICE                             OldDevice,
  _In_  PWDF_CHILD_ADDRESS_DESCRIPTION_HEADER OldAddressDescription,
  _Out_ PWDF_CHILD_ADDRESS_DESCRIPTION_HEADER NewAddressDescription
)
{ ... }
````


## -parameters
<dl>

### -param <i>ChildList</i> [in]

<dd>
<p>A handle to a framework child list object.</p>
</dd>

### -param <i>OldDevice</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>OldAddressDescription</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551219">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</a> structure that identifies a child address description. This structure contains address information that was relevant before the device was reenumerated.</p>
</dd>

### -param <i>NewAddressDescription</i> [out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551219">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</a> structure that identifies a child address description. The callback function fills in this structure with new address information about the device.</p>
</dd>
</dl>

## -returns
<p>The <i>EvtChildListDeviceReenumerated</i> callback function returns <b>TRUE</b> to approve the reenumeration or <b>FALSE</b> to cancel it. </p>

## -remarks
<p>If a bus driver is using <a href="wdf.dynamic_enumeration">dynamic enumeration</a>, it can register an <i>EvtChildListDeviceReenumerated</i> callback function by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547258">WdfFdoInitSetDefaultChildListConfig</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545615">WdfChildListCreate</a>.</p>

<p>Framework-based bus drivers can receive a request from a function driver to reenumerate a particular child device. For more information about these requests, see <a href="wdf.handling_enumeration_requests">Handling Enumeration Requests</a>. </p>

<p>The bus driver's <i>EvtChildListDeviceReenumerated</i> callback function enables the driver to approve or cancel the reenumeration. The <i>OldDevice</i> parameter identifies the device, and the <i>ChildList</i> parameter identifies the child list that the device is a member of. If the callback function returns <b>TRUE</b> to approve the reenumeration, or if the callback function does not exist, the framework does the following:</p>

<p>Removes the device's framework device object (which is identified by <i>OldDevice</i>) but retains the device's identification description.</p>

<p>Calls the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-create-device.md">EvtChildListCreateDevice</a> callback function, passing the saved identification description, so that the callback function can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a> to create a new framework device object.</p>

<p>The <i>EvtChildListDeviceReenumerated</i> callback function receives pointers to two address descriptions. One points to the address description that is associated with the old device object. The other points to an address description that the callback function must fill in with information that describes the device's current location.</p>

<p>For more information about dynamic enumeration, see <a href="wdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a>.</p>

<p>To define an <i>EvtChildListDeviceReenumerated</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtChildListDeviceReenumerated</i> callback function that is named <i>MyChildListDeviceReenumerated</i>, use the <b>EVT_WDF_CHILD_LIST_DEVICE_REENUMERATED</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_CHILD_LIST_DEVICE_REENUMERATED</b> function type is defined in the WdfChildlist.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_CHILD_LIST_DEVICE_REENUMERATED</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

<p>If a bus driver is using <a href="wdf.dynamic_enumeration">dynamic enumeration</a>, it can register an <i>EvtChildListDeviceReenumerated</i> callback function by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff547258">WdfFdoInitSetDefaultChildListConfig</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff545615">WdfChildListCreate</a>.</p>

<p>Framework-based bus drivers can receive a request from a function driver to reenumerate a particular child device. For more information about these requests, see <a href="wdf.handling_enumeration_requests">Handling Enumeration Requests</a>. </p>

<p>The bus driver's <i>EvtChildListDeviceReenumerated</i> callback function enables the driver to approve or cancel the reenumeration. The <i>OldDevice</i> parameter identifies the device, and the <i>ChildList</i> parameter identifies the child list that the device is a member of. If the callback function returns <b>TRUE</b> to approve the reenumeration, or if the callback function does not exist, the framework does the following:</p>

<p>Removes the device's framework device object (which is identified by <i>OldDevice</i>) but retains the device's identification description.</p>

<p>Calls the driver's <a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-create-device.md">EvtChildListCreateDevice</a> callback function, passing the saved identification description, so that the callback function can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a> to create a new framework device object.</p>

<p>The <i>EvtChildListDeviceReenumerated</i> callback function receives pointers to two address descriptions. One points to the address description that is associated with the old device object. The other points to an address description that the callback function must fill in with information that describes the device's current location.</p>

<p>For more information about dynamic enumeration, see <a href="wdf.enumerating_the_devices_on_a_bus">Enumerating the Devices on a Bus</a>.</p>

<p>To define an <i>EvtChildListDeviceReenumerated</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="NULL">Code Analysis for Drivers</a>, <a href="NULL">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtChildListDeviceReenumerated</i> callback function that is named <i>MyChildListDeviceReenumerated</i>, use the <b>EVT_WDF_CHILD_LIST_DEVICE_REENUMERATED</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_CHILD_LIST_DEVICE_REENUMERATED</b> function type is defined in the WdfChildlist.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_CHILD_LIST_DEVICE_REENUMERATED</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="NULL">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<dt>WdfChildlist.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-create-device.md">EvtChildListCreateDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551219">WDF_CHILD_ADDRESS_DESCRIPTION_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545615">WdfChildListCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545926">WdfDeviceCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547258">WdfFdoInitSetDefaultChildListConfig</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_CHILD_LIST_DEVICE_REENUMERATED callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
