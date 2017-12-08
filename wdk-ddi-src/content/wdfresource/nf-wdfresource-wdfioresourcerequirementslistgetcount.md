---
UID: NF.wdfresource.WdfIoResourceRequirementsListGetCount
title: WdfIoResourceRequirementsListGetCount function
author: windows-driver-content
description: The WdfIoResourceRequirementsListGetCount method returns the number of logical configurations that are contained in a resource requirements list.
old-location: wdf\wdfioresourcerequirementslistgetcount.htm
old-project: wdf
ms.assetid: 00a79e57-5915-49a3-b11f-223cc93c2e99
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfIoResourceRequirementsListGetCount
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
req.alt-api: WdfIoResourceRequirementsListGetCount
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

# WdfIoResourceRequirementsListGetCount function



## -description
<p class="CCE_Message">[Applies to KMDF only]
The <b>WdfIoResourceRequirementsListGetCount</b> method returns the number of <a href="https://msdn.microsoft.com/c7a6997b-34f9-4dd9-b384-2321a8b5ce54">logical configurations</a> that are contained in a resource requirements list.


## -syntax

````
ULONG WdfIoResourceRequirementsListGetCount(
  _In_ WDFIORESREQLIST RequirementsList
);
````


## -parameters

### -param RequirementsList [in]

A handle to a framework resource-requirements-list object that represents a device's resource requirements list.

## -returns
<b>WdfIoResourceRequirementsListGetCount</b> returns the number of logical configurations that are contained in the resource requirements list.

A system bug check occurs if the driver supplies an invalid object handle.

## -remarks
For more information about resource requirements lists, see <a href="wdf.hardware_resources_for_kmdf_drivers">Hardware Resources for Framework-Based Drivers</a>.

The following code example shows how an <a href="wdf.evtdevicefilterremoveresourcerequirements">EvtDeviceFilterRemoveResourceRequirements</a> callback function can obtain the number of logical configurations that are contained in a resource requirements list.

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