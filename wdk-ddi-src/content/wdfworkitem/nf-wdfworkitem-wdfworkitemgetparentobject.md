---
UID: NF.wdfworkitem.WdfWorkItemGetParentObject
title: WdfWorkItemGetParentObject
author: windows-driver-content
description: The WdfWorkItemGetParentObject method returns the framework object that a specified work item is associated with.
old-location: wdf\wdfworkitemgetparentobject.htm
old-project: wdf
ms.assetid: 6ebb1955-1ffc-4869-84c8-69d672ac782e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfWorkItemGetParentObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfworkitem.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfWorkItemGetParentObject
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfWorkItemGetParentObject function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfWorkItemGetParentObject</b> method returns the framework object that a specified work item is associated with.</p>


## -syntax

````
WDFOBJECT WdfWorkItemGetParentObject(
  _In_ WDFWORKITEM WorkItem
);
````


## -parameters
<dl>

### -param <i>WorkItem</i> [in]

<dd>
<p>A handle to a framework work-item object that is obtained from a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff551201">WdfWorkItemCreate</a>.</p>
</dd>
</dl>

## -returns
<p><b>WdfWorkItemGetParentObject</b> returns a handle to the framework object that the driver specified as the <b>ParentObject</b> member of the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure when the driver previously called <a href="https://msdn.microsoft.com/library/windows/hardware/ff551201">WdfWorkItemCreate</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>For more information about work items, see <a href="wdf.using_framework_work_items">Using Framework Work Items</a>.</p>

<p>The following code example is an <a href="wdf.evtworkitem">EvtWorkItem</a> callback function from the <a href="wdf.sample_kmdf_drivers">1394</a> sample driver. The example obtains a work item's parent device object, calls a driver-defined routine to process the work item, and then deletes the work item object.</p>

<p>For more information about work items, see <a href="wdf.using_framework_work_items">Using Framework Work Items</a>.</p>

<p>The following code example is an <a href="wdf.evtworkitem">EvtWorkItem</a> callback function from the <a href="wdf.sample_kmdf_drivers">1394</a> sample driver. The example obtains a work item's parent device object, calls a driver-defined routine to process the work item, and then deletes the work item object.</p>

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
<dt>Wdfworkitem.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551201">WdfWorkItemCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfWorkItemGetParentObject method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
