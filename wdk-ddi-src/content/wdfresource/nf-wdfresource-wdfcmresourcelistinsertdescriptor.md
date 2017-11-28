---
UID: NF.wdfresource.WdfCmResourceListInsertDescriptor
title: WdfCmResourceListInsertDescriptor
author: windows-driver-content
description: The WdfCmResourceListInsertDescriptor method inserts a resource descriptor into a specified resource list.
old-location: wdf\wdfcmresourcelistinsertdescriptor.htm
old-project: wdf
ms.assetid: 18406f06-d60c-401e-a745-54caf1d0c21d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfCmResourceListInsertDescriptor
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfresource.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfCmResourceListInsertDescriptor
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfCmResourceListInsertDescriptor function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfCmResourceListInsertDescriptor</b> method inserts a resource descriptor into a specified resource list.</p>


## -syntax

````
NTSTATUS WdfCmResourceListInsertDescriptor(
  _In_ WDFCMRESLIST                    List,
  _In_ PCM_PARTIAL_RESOURCE_DESCRIPTOR Descriptor,
  _In_ ULONG                           Index
);
````


## -parameters
<dl>

### -param <i>List</i> [in]

<dd>
<p>A handle to a framework resource-list object that represents a list of hardware resources for a device.</p>
</dd>

### -param <i>Descriptor</i> [in]

<dd>
<p>A pointer to an <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure that describes a hardware resource.</p>
</dd>

### -param <i>Index</i> [in]

<dd>
<p>A zero-based value that is used as an index into the logical configuration that <i>List</i> specifies. To add a resource descriptor to the end of the resource list, specify WDF_INSERT_AT_END or the return value from <a href="https://msdn.microsoft.com/library/windows/hardware/ff545687">WdfCmResourceListGetCount</a>.</p>
</dd>
</dl>

## -returns
<p><b>WdfCmResourceListInsertDescriptor</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was specified.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The driver was not allowed to add descriptors to the logical configuration that the <i>List</i> parameter specified. For example, the driver could not modify the logical configuration that its <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a> or <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a> callback function received.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>The framework could not allocate space to store the descriptor that the <i>Descriptor</i> parameter points to.</p><dl>
<dt><b>STATUS_ARRAY_BOUNDS_EXCEEDED</b></dt>
</dl><p>The value that the <i>Index</i> parameter specified was too large.</p>

<p> </p>

<p>A system bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>The <b>WdfCmResourceListInsertDescriptor</b> method inserts the resource descriptor that <i>Descriptor</i> specifies into the resource list that <i>List</i> specifies, in front of the resource descriptor that <i>Index</i> value identifies.</p>

<p>To add a resource descriptor to the end of a resource list, specify WDF_INSERT_AT_END or the return value from <a href="https://msdn.microsoft.com/library/windows/hardware/ff545687">WdfCmResourceListGetCount</a> as the <i>Index</i> value. Alternatively, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545683">WdfCmResourceListAppendDescriptor</a> method.</p>

<p>The framework copies the contents of the <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure into internal storage, so the driver routine that calls <b>WdfCmResourceListInsertDescriptor</b> can allocate the structure locally. After the driver calls <b>WdfCmResourceListInsertDescriptor</b>, it can reuse the CM_PARTIAL_RESOURCE_DESCRIPTOR structure.</p>

<p>For more information about resource lists, see <a href="wdf.hardware_resources_for_kmdf_drivers">Hardware Resources for Framework-Based Drivers</a>.</p>

<p>The following code example adds a resource descriptor to the end of the resource list that an <a href="wdf.evtdeviceresourcesquery">EvtDeviceResourcesQuery</a> callback function receives. </p>

<p>The <b>WdfCmResourceListInsertDescriptor</b> method inserts the resource descriptor that <i>Descriptor</i> specifies into the resource list that <i>List</i> specifies, in front of the resource descriptor that <i>Index</i> value identifies.</p>

<p>To add a resource descriptor to the end of a resource list, specify WDF_INSERT_AT_END or the return value from <a href="https://msdn.microsoft.com/library/windows/hardware/ff545687">WdfCmResourceListGetCount</a> as the <i>Index</i> value. Alternatively, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545683">WdfCmResourceListAppendDescriptor</a> method.</p>

<p>The framework copies the contents of the <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure into internal storage, so the driver routine that calls <b>WdfCmResourceListInsertDescriptor</b> can allocate the structure locally. After the driver calls <b>WdfCmResourceListInsertDescriptor</b>, it can reuse the CM_PARTIAL_RESOURCE_DESCRIPTOR structure.</p>

<p>For more information about resource lists, see <a href="wdf.hardware_resources_for_kmdf_drivers">Hardware Resources for Framework-Based Drivers</a>.</p>

<p>The following code example adds a resource descriptor to the end of the resource list that an <a href="wdf.evtdeviceresourcesquery">EvtDeviceResourcesQuery</a> callback function receives. </p>

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
<dt>Wdfresource.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md">EvtDevicePrepareHardware</a>
</dt>
<dt>
<a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md">EvtDeviceReleaseHardware</a>
</dt>
<dt>
<a href="wdf.evtdeviceresourcesquery">EvtDeviceResourcesQuery</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545683">WdfCmResourceListAppendDescriptor</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfCmResourceListInsertDescriptor method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
