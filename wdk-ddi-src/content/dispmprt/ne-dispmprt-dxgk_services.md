---
UID : NE:dispmprt.DXGK_SERVICES
title : DXGK_SERVICES
author : windows-driver-content
description : The DXGK_SERVICES enumeration indicates the type of interface being requested by a call to the DxgkCbQueryServices function.
old-location : display\dxgk_services.htm
old-project : display
ms.assetid : 8853e0f8-1dd0-4cb5-8dbf-c1d4e62bb0ec
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : DXGK_SERVICES, DXGK_SERVICES
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : dispmprt.h
req.include-header : Dispmprt.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DXGK_SERVICES
req.alt-loc : dispmprt.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : DXGK_SERVICES
---

# DXGK_SERVICES Enumeration
The DXGK_SERVICES enumeration indicates the type of interface being requested by a call to the <a href="..\dispmprt\nc-dispmprt-dxgkcb_query_services.md">DxgkCbQueryServices</a> function.

## Syntax
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

## Constants

<table>

<tr>
<td>DxgkServicesAgp</td>
<td>Indicates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff538228">AGP Interface</a>.</td>
</tr>

<tr>
<td>DxgkServicesBDD</td>
<td>Reserved for system use. Do not use in your driver.

Supported starting with Windows 8.</td>
</tr>

<tr>
<td>DxgkServicesDebugReport</td>
<td>Indicates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551798">Debug Report interface</a>.</td>
</tr>

<tr>
<td>DxgkServicesFirmwareTable</td>
<td>Indicates the <a href="https://msdn.microsoft.com/library/windows/hardware/jj647606">System Firmware Table Interface</a>.

Supported starting with Windows 8.</td>
</tr>

<tr>
<td>DxgkServicesSPB</td>
<td>Indicates the <a href="https://msdn.microsoft.com/D525A961-339D-414B-B40F-14AD9AEA51C5">Simple  Peripheral Bus (SPB) Interface</a>.

Supported starting with Windows 8.</td>
</tr>

<tr>
<td>DxgkServicesTimedOperation</td>
<td>Indicates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570086">Timed Operation interface</a>.</td>
</tr>
</table>

## Remarks

An interface, in this context, is a set of function pointers. The functions in the AGP, Debug Report, Timed Operation, SPB, and System Firmware Table interfaces are implemented by the Microsoft DirectX graphics kernel subsystem and called by the display miniport driver.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | dispmprt.h (include Dispmprt.h) |