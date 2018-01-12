---
UID: NC:wdfchildlist.PFN_WDFCHILDLISTGETDEVICE
title: PFN_WDFCHILDLISTGETDEVICE function
author: windows-driver-content
description: The WdfChildListGetDevice method returns a handle to the framework device object that represents the parent device of a specified child list.
old-location: wdf\wdfchildlistgetdevice.htm
old-project: wdf
ms.assetid: 5d51ec82-4891-47f1-8fc1-b20cb611d7fe
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: PFN_WDFCHILDLISTGETDEVICE
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
req.alt-api: WdfChildListGetDevice
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

# PFN_WDFCHILDLISTGETDEVICE function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfChildListGetDevice</b> method returns a handle to the framework device object that represents the parent device of a specified child list.



## -syntax

````
WDFDEVICE WdfChildListGetDevice(
  _In_ WDFCHILDLIST ChildList
);
````


## -parameters

### -param ChildList [in]

A handle to a framework child-list object.


## -returns
<b>WdfChildListGetDevice</b> returns a handle to a framework device object.

A system bug check occurs if the driver supplies an invalid object handle.



## -remarks
For more information about child lists, see <a href="https://msdn.microsoft.com/6e46b456-7d2d-4c6e-8692-7f310366387d">Dynamic Enumeration</a>.

The following code example obtains a handle to the device object that represents the parent device of a child list.


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