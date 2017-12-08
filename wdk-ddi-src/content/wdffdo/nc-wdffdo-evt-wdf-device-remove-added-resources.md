---
UID: NC.wdffdo.EVT_WDF_DEVICE_REMOVE_ADDED_RESOURCES
title: EVT_WDF_DEVICE_REMOVE_ADDED_RESOURCES
author: windows-driver-content
description: A driver's EvtDeviceRemoveAddedResources event callback function removes hardware resources that the driver's EvtDeviceFilterAddResourceRequirements callback function added.
old-location: wdf\evtdeviceremoveaddedresources.htm
old-project: wdf
ms.assetid: b18c2b34-db6d-4553-9340-556da1fd7991
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_DRIVER_VERSION_AVAILABLE_PARAMS, WDF_DRIVER_VERSION_AVAILABLE_PARAMS, *PWDF_DRIVER_VERSION_AVAILABLE_PARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdffdo.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: EvtDeviceRemoveAddedResources
req.alt-loc: Wdffdo.h
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

# EVT_WDF_DEVICE_REMOVE_ADDED_RESOURCES callback



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>A driver's <i>EvtDeviceRemoveAddedResources</i> event callback function removes hardware resources that the driver's <a href="wdf.evtdevicefilteraddresourcerequirements">EvtDeviceFilterAddResourceRequirements</a> callback function added.</p>


## -prototype

````
EVT_WDF_DEVICE_REMOVE_ADDED_RESOURCES EvtDeviceRemoveAddedResources;

NTSTATUS EvtDeviceRemoveAddedResources(
  _In_ WDFDEVICE    Device,
  _In_ WDFCMRESLIST ResourcesRaw,
  _In_ WDFCMRESLIST ResourcesTranslated
)
{ ... }
````


## -parameters
<dl>

### -param Device [in]

<dd>
<p>A handle to the framework device object to which resources will be assigned.</p>
</dd>

### -param ResourcesRaw [in]

<dd>
<p>A handle to a resource list object that identifies the raw hardware resources that the PnP manager has assigned to the device. </p>
</dd>

### -param ResourcesTranslated [in]

<dd>
<p>A handle to a resource list object that identifies the translated hardware resources that the PnP manager has assigned to the device. </p>
</dd>
</dl>

## -returns
<p>If the driver encountered no errors it must return STATUS_SUCCESS. Otherwise it must return an NTSTATUS value that <a href="https://msdn.microsoft.com/fe823930-e3ff-4c95-a640-bb6470c95d1d">NT_SUCCESS</a> evaluates as <b>FALSE</b>.</p>

<p>For more information about return values, see <a href="wdf.reporting_device_failures">Reporting Device Failures</a>.</p>

## -remarks
<p>Framework-based function drivers can provide an <i>EvtDeviceRemoveAddedResources</i> callback function. To register this callback function, drivers call <a href="..\wdffdo\nf-wdffdo-wdffdoinitseteventcallbacks.md">WdfFdoInitSetEventCallbacks</a>.</p>

<p>If a driver provides an <a href="wdf.evtdevicefilteraddresourcerequirements">EvtDeviceFilterAddResourceRequirements</a> callback function that adds resources to a device's hardware requirements list, the driver must also provide an <i>EvtDeviceRemoveAddedResources</i> callback function. The <i>EvtDeviceRemoveAddedResources</i> callback function examines the resource list that the PnP manager has assigned to the device, and removes the resources from the list that the <i>EvtDeviceFilterAddResourceRequirements</i> callback function added. If the driver removes a resource, it must remove it from both the raw and translated resource lists.</p>

<p>For more information about resource lists and the order in which the resources appear, see <a href="wdf.raw_and_translated_resources">raw and translated hardware resources</a>.</p>

<p>The framework calls the driver's <i>EvtDeviceRemoveAddedResources</i> callback function immediately before it passes the device's resource list to the bus driver. This callback function removes added resources so that the bus driver will not attempt to use them. </p>

<p>For more information about the <i>EvtDeviceRemoveAddedResources</i> callback function, see <a href="wdf.modifying_a_resource_list">Modifying a Resource List</a>.</p>

<p>For more information about hardware resources, see <a href="wdf.hardware_resources_for_kmdf_drivers">Hardware Resources for Framework-Based Drivers</a>.</p>

<p>To define an <i>EvtDeviceRemoveAddedResources</i> callback function, you must first provide a function declaration that identifies the type of callback function you’re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps <a href="https://msdn.microsoft.com/2F3549EF-B50F-455A-BDC7-1F67782B8DCA">Code Analysis for Drivers</a>, <a href="https://msdn.microsoft.com/74feeb16-387c-4796-987a-aff3fb79b556">Static Driver Verifier</a> (SDV), and other verification tools find errors, and it’s a requirement for writing drivers for the Windows operating system.</p>

<p>For example, to define an <i>EvtDeviceRemoveAddedResources</i> callback function that is named <i>MyDeviceRemoveAddedResources</i>, use the <b>EVT_WDF_DEVICE_REMOVE_ADDED_RESOURCES</b> type as shown in this code example:</p>

<p>Then, implement your callback function as follows:</p>

<p>The <b>EVT_WDF_DEVICE_REMOVE_ADDED_RESOURCES</b> function type is defined in the Wdffdo.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the _Use_decl_annotations_ annotation to your function definition. The _Use_decl_annotations_ annotation ensures that the annotations that are applied to the <b>EVT_WDF_DEVICE_REMOVE_ADDED_RESOURCES</b> function type in the header file are used. For more information about the requirements for function declarations, see <a href="https://msdn.microsoft.com/73a408ba-0219-4fde-8dad-ca330e4e67c3">Declaring Functions by Using Function Role Types for KMDF Drivers</a>. For information about _Use_decl_annotations_, see <a href="https://msdn.microsoft.com/en-US/library/c0aa268d-6fa3-4ced-a8c6-f7652b152e61">Annotating Function Behavior</a>.</p>

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
<dt>Wdffdo.h (include Wdf.h)</dt>
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
<a href="wdf.evtdevicefilteraddresourcerequirements">EvtDeviceFilterAddResourceRequirements</a>
</dt>
<dt>
<a href="wdf.evtdevicefilterremoveresourcerequirements">EvtDeviceFilterRemoveResourceRequirements</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20EVT_WDF_DEVICE_REMOVE_ADDED_RESOURCES callback function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
