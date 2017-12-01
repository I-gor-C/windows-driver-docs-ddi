---
UID: NF.wdfresource.WdfIoResourceRequirementsListGetCount
title: WdfIoResourceRequirementsListGetCount
author: windows-driver-content
description: The WdfIoResourceRequirementsListGetCount method returns the number of logical configurations that are contained in a resource requirements list.
old-location: wdf\wdfioresourcerequirementslistgetcount.htm
old-project: wdf
ms.assetid: 00a79e57-5915-49a3-b11f-223cc93c2e99
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.iface: 
req.product: Windows 10 or later.
---

# WdfIoResourceRequirementsListGetCount function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfIoResourceRequirementsListGetCount</b> method returns the number of <a href="https://msdn.microsoft.com/c7a6997b-34f9-4dd9-b384-2321a8b5ce54">logical configurations</a> that are contained in a resource requirements list.</p>


## -syntax

````
ULONG WdfIoResourceRequirementsListGetCount(
  _In_ WDFIORESREQLIST RequirementsList
);
````


## -parameters
<dl>

### -param <i>RequirementsList</i> [in]

<dd>
<p>A handle to a framework resource-requirements-list object that represents a device's resource requirements list.</p>
</dd>
</dl>

## -returns
<p><b>WdfIoResourceRequirementsListGetCount</b> returns the number of logical configurations that are contained in the resource requirements list.</p>

<p>A system bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>For more information about resource requirements lists, see <a href="wdf.hardware_resources_for_kmdf_drivers">Hardware Resources for Framework-Based Drivers</a>.</p>

<p>The following code example shows how an <a href="wdf.evtdevicefilterremoveresourcerequirements">EvtDeviceFilterRemoveResourceRequirements</a> callback function can obtain the number of logical configurations that are contained in a resource requirements list.</p>

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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>