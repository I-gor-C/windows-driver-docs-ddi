---
UID: NF.wdfresource.WdfIoResourceListGetDescriptor
title: WdfIoResourceListGetDescriptor
author: windows-driver-content
description: The WdfIoResourceListGetDescriptor method returns a pointer to a resource descriptor that is contained in a resource requirements list's logical configuration.
old-location: wdf\wdfioresourcelistgetdescriptor.htm
ms.assetid: 1722e6f6-7509-4ae1-b394-3c69f4596e6d
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfresource.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfIoResourceListGetDescriptor
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
ms.keywords: WdfIoResourceListGetDescriptor
req.iface: 
req.product: Windows 10 or later.
---

# WdfIoResourceListGetDescriptor function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfIoResourceListGetDescriptor</b> method returns a pointer to a resource descriptor that is contained in a resource requirements list's <a href="https://msdn.microsoft.com/c7a6997b-34f9-4dd9-b384-2321a8b5ce54">logical configuration</a>.</p>


## -syntax

````
PIO_RESOURCE_DESCRIPTOR WdfIoResourceListGetDescriptor(
  _In_ WDFIORESLIST ResourceList,
  _In_ ULONG        Index
);
````


## -parameters
<dl>

### -param <i>ResourceList</i> [in]

<dd>
<p>A handle to a framework resource-range-list object that represents a logical configuration of hardware resources for a device.</p>
</dd>

### -param <i>Index</i> [in]

<dd>
<p>A zero-based value that is used as an index into the logical configuration that <i>ResourceList</i> specifies.</p>
</dd>
</dl>

## -returns
<p><b>WdfIoResourceListGetDescriptor</b> returns a pointer to the <a href="https://msdn.microsoft.com/03e3a656-c691-4aff-bcc8-4e0bc8390fd7">IO_RESOURCE_DESCRIPTOR</a> structure that describes the hardware resource that the <i>Index</i> parameter identifies, if the index value is valid. Otherwise, the method returns <b>NULL</b>.</p>

<p>A system bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Your driver cannot modify the contents of the <a href="https://msdn.microsoft.com/03e3a656-c691-4aff-bcc8-4e0bc8390fd7">IO_RESOURCE_DESCRIPTOR</a> structure that <b>WdfIoResourceListGetDescriptor</b> retrieves. To modify a resource descriptor, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548533">WdfIoResourceListUpdateDescriptor</a>.</p>

<p>For more information about resource requirements lists and logical configurations, see <a href="wdf.hardware_resources_for_kmdf_drivers">Hardware Resources for Framework-Based Drivers</a>.</p>

<p>For a code example that uses <b>WdfIoResourceListGetDescriptor</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548553">WdfIoResourceRequirementsListGetIoResList</a>.</p>

<p>Your driver cannot modify the contents of the <a href="https://msdn.microsoft.com/03e3a656-c691-4aff-bcc8-4e0bc8390fd7">IO_RESOURCE_DESCRIPTOR</a> structure that <b>WdfIoResourceListGetDescriptor</b> retrieves. To modify a resource descriptor, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548533">WdfIoResourceListUpdateDescriptor</a>.</p>

<p>For more information about resource requirements lists and logical configurations, see <a href="wdf.hardware_resources_for_kmdf_drivers">Hardware Resources for Framework-Based Drivers</a>.</p>

<p>For a code example that uses <b>WdfIoResourceListGetDescriptor</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548553">WdfIoResourceRequirementsListGetIoResList</a>.</p>

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
<a href="https://msdn.microsoft.com/03e3a656-c691-4aff-bcc8-4e0bc8390fd7">IO_RESOURCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548533">WdfIoResourceListUpdateDescriptor</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfIoResourceListGetDescriptor method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
