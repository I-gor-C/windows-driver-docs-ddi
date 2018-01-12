---
UID: NC:wdfchildlist.PFN_WDFCHILDLISTUPDATEALLCHILDDESCRIPTIONSASPRESENT
title: PFN_WDFCHILDLISTUPDATEALLCHILDDESCRIPTIONSASPRESENT function
author: windows-driver-content
description: The WdfChildListUpdateAllChildDescriptionsAsPresent method informs the framework that all of the child devices in a specified child list are plugged in and available.
old-location: wdf\wdfchildlistupdateallchilddescriptionsaspresent.htm
old-project: wdf
ms.assetid: 598d2b4f-9b49-480a-9cf8-25661c24483f
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: PFN_WDFCHILDLISTUPDATEALLCHILDDESCRIPTIONSASPRESENT
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
req.typenames: WDBGEXTS_THREAD_OS_INFO, *PWDBGEXTS_THREAD_OS_INFO
req.product: Windows 10 or later.
---

# PFN_WDFCHILDLISTUPDATEALLCHILDDESCRIPTIONSASPRESENT function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfChildListUpdateAllChildDescriptionsAsPresent</b> method informs the framework that all of the child devices in a specified child list are plugged in and available.



## -syntax

````
VOID WdfChildListUpdateAllChildDescriptionsAsPresent(
  _In_ WDFCHILDLIST ChildList
);
````


## -parameters

### -param ChildList [in]

A handle to a child list object.


## -returns
None.

A system bug check occurs if the driver supplies an invalid object handle.



## -remarks
The <b>WdfChildListUpdateAllChildDescriptionsAsPresent</b> method is available in version 1.0 and later versions of KMDF.

For more information about child lists, see <a href="https://msdn.microsoft.com/6e46b456-7d2d-4c6e-8692-7f310366387d">Dynamic Enumeration</a>.

The following code example informs the framework that all of the devices that a device list represents are plugged in and available.


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
<dt>Wdfchildlist.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="https://msdn.microsoft.com/51db6f3c-45cb-46a7-9dd4-2bab67893fea">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>