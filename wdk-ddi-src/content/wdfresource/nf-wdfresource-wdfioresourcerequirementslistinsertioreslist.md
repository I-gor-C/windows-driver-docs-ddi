---
UID: NF.wdfresource.WdfIoResourceRequirementsListInsertIoResList
title: WdfIoResourceRequirementsListInsertIoResList function
author: windows-driver-content
description: The WdfIoResourceRequirementsListInsertIoResList method inserts a logical configuration into a resource requirements list.
old-location: wdf\wdfioresourcerequirementslistinsertioreslist.htm
old-project: wdf
ms.assetid: d70d9fed-22fd-4bcf-a4bf-fbd941559529
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfIoResourceRequirementsListInsertIoResList
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
req.alt-api: WdfIoResourceRequirementsListInsertIoResList
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
req.product: Windows 10 or later.
---

# WdfIoResourceRequirementsListInsertIoResList function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfIoResourceRequirementsListInsertIoResList</b> method inserts a <a href="https://msdn.microsoft.com/c7a6997b-34f9-4dd9-b384-2321a8b5ce54">logical configuration</a> into a resource requirements list.



## -syntax

````
NTSTATUS WdfIoResourceRequirementsListInsertIoResList(
  _In_ WDFIORESREQLIST RequirementsList,
  _In_ WDFIORESLIST    IoResList,
  _In_ ULONG           Index
);
````


## -parameters

### -param RequirementsList [in]

A handle to a framework resource-requirements-list object that represents a device's resource requirements list.


### -param IoResList [in]

A handle to a framework resource-range-list object that represents a logical configuration of hardware resources for a device.


### -param Index [in]

A zero-based value that is used as an index into the set of logical configurations that are already in the resource requirements list that <i>RequirementsList</i> specifies. To add a configuration to the end of the list, specify WDF_INSERT_AT_END or the return value from <a href="wdf.wdfioresourcerequirementslistgetcount">WdfIoResourceRequirementsListGetCount</a>.


## -returns
<b>WdfIoResourceRequirementsListInsertIoResList</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An invalid parameter as specified.
<dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl>The specified resource-requirements-list object does not own the specified resource-range-list object.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>The framework could not allocate space to store the resource-range-list object.
<dl>
<dt><b>STATUS_ARRAY_BOUNDS_EXCEEDED</b></dt>
</dl>The specified value for the <i>Index</i> parameter was too large.

 

A system bug check occurs if the driver supplies an invalid object handle.


## -remarks
The <b>WdfIoResourceRequirementsListInsertIoResList</b> method inserts the logical configuration that the <i>IoResList</i> parameter specifies into the resource requirements list that the <i>RequirementsList</i> parameter specifies, in front of the logical configuration that the <i>Index</i> value identifies. 

To add a logical configuration to the end of a resource requirements list, use WDF_INSERT_AT_END or the return value from <a href="wdf.wdfioresourcerequirementslistgetcount">WdfIoResourceRequirementsListGetCount</a> as the <i>Index</i> value. Alternatively, use the <a href="wdf.wdfioresourcerequirementslistappendioreslist">WdfIoResourceRequirementsListAppendIoResList</a> method.

For more information about resource requirements lists, see <a href="wdf.hardware_resources_for_kmdf_drivers">Hardware Resources for Framework-Based Drivers</a>.

The following code example shows how an <a href="..\wdfpdo\nc-wdfpdo-evt_wdf_device_resource_requirements_query.md">EvtDeviceResourceRequirementsQuery</a> callback function can create two empty logical configurations and add them to a resource requirements list.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfresource.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;=DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdfioresourcelistcreate">WdfIoResourceListCreate</a>
</dt>
<dt>
<a href="wdf.wdfioresourcerequirementslistappendioreslist">WdfIoResourceRequirementsListAppendIoResList</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoResourceRequirementsListInsertIoResList method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

