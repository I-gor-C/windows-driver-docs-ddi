---
UID: NC:wdfresource.PFN_WDFIORESOURCEREQUIREMENTSLISTSETSLOTNUMBER
title: PFN_WDFIORESOURCEREQUIREMENTSLISTSETSLOTNUMBER function
author: windows-driver-content
description: The WdfIoResourceRequirementsListSetSlotNumber method assigns a slot number to a resource requirements list.
old-location: wdf\wdfioresourcerequirementslistsetslotnumber.htm
old-project: wdf
ms.assetid: 1dc18c48-2331-4980-b741-59a73d3edaa6
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: PFN_WDFIORESOURCEREQUIREMENTSLISTSETSLOTNUMBER
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
req.alt-api: WdfIoResourceRequirementsListSetSlotNumber
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
req.typenames: *PWDF_REQUEST_SEND_OPTIONS, WDF_REQUEST_SEND_OPTIONS
req.product: Windows 10 or later.
---

# PFN_WDFIORESOURCEREQUIREMENTSLISTSETSLOTNUMBER function



## -description
<p class="CCE_Message">[Applies to KMDF only]

The <b>WdfIoResourceRequirementsListSetSlotNumber</b> method assigns a slot number to a resource requirements list.



## -syntax

````
VOID WdfIoResourceRequirementsListSetSlotNumber(
  _In_ WDFIORESREQLIST RequirementsList,
  _In_ ULONG           SlotNumber
);
````


## -parameters

### -param RequirementsList [in]

A handle to a framework resource-requirements-list object that represents a device's resource requirements list.


### -param SlotNumber [in]

A value that identifies the bus slot number to which the device is connected.


## -returns
None.

A system bug check occurs if the driver supplies an invalid object handle.


## -remarks
Your driver must provide a slot number if your device does not support Plug and Play (PnP). 

For more information about resource requirements lists, see <a href="wdf.hardware_resources_for_kmdf_drivers">Hardware Resources for Framework-Based Drivers</a>.

The following code example shows how an <a href="..\wdfpdo\nc-wdfpdo-evt_wdf_device_resource_requirements_query.md">EvtDeviceResourceRequirementsQuery</a> callback function for a nonPnP device calls <b>WdfIoResourceRequirementsListSetSlotNumber</b> to assign slot 0 to a device.


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
<dt>Wdf01000.sys (see <a href="https://msdn.microsoft.com/51db6f3c-45cb-46a7-9dd4-2bab67893fea">Framework Library Versioning</a>.)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>