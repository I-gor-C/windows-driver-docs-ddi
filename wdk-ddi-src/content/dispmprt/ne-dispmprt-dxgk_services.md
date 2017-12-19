---
UID: NE.dispmprt.DXGK_SERVICES
title: DXGK_SERVICES
author: windows-driver-content
description: The DXGK_SERVICES enumeration indicates the type of interface being requested by a call to the DxgkCbQueryServices function.
old-location: display\dxgk_services.htm
old-project: display
ms.assetid: 8853e0f8-1dd0-4cb5-8dbf-c1d4e62bb0ec
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: DXGK_SERVICES, DXGK_SERVICES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_SERVICES
req.alt-loc: dispmprt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
---

# DXGK_SERVICES enumeration



## -description
The DXGK_SERVICES enumeration indicates the type of interface being requested by a call to the <a href="..\dispmprt\nc-dispmprt-dxgkcb_query_services.md">DxgkCbQueryServices</a> function.



## -syntax

````
typedef enum  { 
  DxgkServicesAgp             = 0,
  DxgkServicesDebugReport     = 1,
  DxgkServicesTimedOperation  = 2,
  DxgkServicesSPB             = 3,
  DxgkServicesBDD             = 4,
  DxgkServicesFirmwareTable   = 4
} DXGK_SERVICES;
````


## -enum-fields

### -field DxgkServicesAgp

Indicates the <a href="display.agp_interface">AGP Interface</a>.


### -field DxgkServicesDebugReport

Indicates the <a href="display.debug_report_interface">Debug Report interface</a>.


### -field DxgkServicesTimedOperation

Indicates the <a href="display.timed_operation_interface">Timed Operation interface</a>.


### -field DxgkServicesSPB

Indicates the <a href="display.simple__peripheral_bus__spb__interface">Simple  Peripheral Bus (SPB) Interface</a>.

Supported starting with Windows 8.


### -field DxgkServicesBDD

Reserved for system use. Do not use in your driver.

Supported starting with Windows 8.


### -field DxgkServicesFirmwareTable

Indicates the <a href="display.system_firmware_table_interface">System Firmware Table Interface</a>.

Supported starting with Windows 8.


## -remarks
An interface, in this context, is a set of function pointers. The functions in the AGP, Debug Report, Timed Operation, SPB, and System Firmware Table interfaces are implemented by the Microsoft DirectX graphics kernel subsystem and called by the display miniport driver.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>