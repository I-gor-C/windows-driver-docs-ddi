---
UID: NF.wdfchildlist.WdfChildListUpdateAllChildDescriptionsAsPresent
title: WdfChildListUpdateAllChildDescriptionsAsPresent
author: windows-driver-content
description: The WdfChildListUpdateAllChildDescriptionsAsPresent method informs the framework that all of the child devices in a specified child list are plugged in and available.
old-location: wdf\wdfchildlistupdateallchilddescriptionsaspresent.htm
old-project: wdf
ms.assetid: 598d2b4f-9b49-480a-9cf8-25661c24483f
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfChildListUpdateAllChildDescriptionsAsPresent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfchildlist.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfChildListUpdateAllChildDescriptionsAsPresent
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfChildListUpdateAllChildDescriptionsAsPresent function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfChildListUpdateAllChildDescriptionsAsPresent</b> method informs the framework that all of the child devices in a specified child list are plugged in and available.</p>


## -syntax

````
VOID WdfChildListUpdateAllChildDescriptionsAsPresent(
  _In_ WDFCHILDLIST ChildList
);
````


## -parameters
<dl>

### -param <i>ChildList</i> [in]

<dd>
<p>A handle to a child list object.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A system bug check occurs if the driver supplies an invalid object handle.
</p>

## -remarks
<p>The <b>WdfChildListUpdateAllChildDescriptionsAsPresent</b> method is available in version 1.0 and later versions of KMDF.</p>

<p>For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>The following code example informs the framework that all of the devices that a device list represents are plugged in and available.</p>

<p>The <b>WdfChildListUpdateAllChildDescriptionsAsPresent</b> method is available in version 1.0 and later versions of KMDF.</p>

<p>For more information about child lists, see <a href="wdf.dynamic_enumeration">Dynamic Enumeration</a>.</p>

<p>The following code example informs the framework that all of the devices that a device list represents are plugged in and available.</p>

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
<dt>Wdfchildlist.h (include Wdf.h)</dt>
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