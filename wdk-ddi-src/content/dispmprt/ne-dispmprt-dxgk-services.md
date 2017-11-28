---
UID: NE.dispmprt.DXGK_SERVICES
title: DXGK_SERVICES
author: windows-driver-content
description: The DXGK_SERVICES enumeration indicates the type of interface being requested by a call to the DxgkCbQueryServices function.
old-location: display\dxgk_services.htm
old-project: display
ms.assetid: 8853e0f8-1dd0-4cb5-8dbf-c1d4e62bb0ec
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
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
req.iface: IDebugSystemObjects4
---

# DXGK_SERVICES enumeration



## -description
<p>The DXGK_SERVICES enumeration indicates the type of interface being requested by a call to the <a href="..\dispmprt\nc-dispmprt-dxgkcb-query-services.md">DxgkCbQueryServices</a> function.</p>


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
<dl>

### -field <a id="DxgkServicesAgp"></a><a id="dxgkservicesagp"></a><a id="DXGKSERVICESAGP"></a><b>DxgkServicesAgp</b>

<dd>
<p>Indicates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff538228">AGP Interface</a>.</p>
</dd>

### -field <a id="DxgkServicesDebugReport"></a><a id="dxgkservicesdebugreport"></a><a id="DXGKSERVICESDEBUGREPORT"></a><b>DxgkServicesDebugReport</b>

<dd>
<p>Indicates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551798">Debug Report interface</a>.</p>
</dd>

### -field <a id="DxgkServicesTimedOperation"></a><a id="dxgkservicestimedoperation"></a><a id="DXGKSERVICESTIMEDOPERATION"></a><b>DxgkServicesTimedOperation</b>

<dd>
<p>Indicates the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570086">Timed Operation interface</a>.</p>
</dd>

### -field <a id="DxgkServicesSPB"></a><a id="dxgkservicesspb"></a><a id="DXGKSERVICESSPB"></a><b>DxgkServicesSPB</b>

<dd>
<p>Indicates the <a href="display.simple__peripheral_bus__spb__interface">Simple  Peripheral Bus (SPB) Interface</a>.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="DxgkServicesBDD"></a><a id="dxgkservicesbdd"></a><a id="DXGKSERVICESBDD"></a><b>DxgkServicesBDD</b>

<dd>
<p>Reserved for system use. Do not use in your driver.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <a id="DxgkServicesFirmwareTable"></a><a id="dxgkservicesfirmwaretable"></a><a id="DXGKSERVICESFIRMWARETABLE"></a><b>DxgkServicesFirmwareTable</b>

<dd>
<p>Indicates the <a href="https://msdn.microsoft.com/library/windows/hardware/jj647606">System Firmware Table Interface</a>.</p>
<p>Supported starting with Windows 8.</p>
</dd>
</dl>

## -remarks
<p>An interface, in this context, is a set of function pointers. The functions in the AGP, Debug Report, Timed Operation, SPB, and System Firmware Table interfaces are implemented by the Microsoft DirectX graphics kernel subsystem and called by the display miniport driver.</p>

<p>An interface, in this context, is a set of function pointers. The functions in the AGP, Debug Report, Timed Operation, SPB, and System Firmware Table interfaces are implemented by the Microsoft DirectX graphics kernel subsystem and called by the display miniport driver.</p>

<p>An interface, in this context, is a set of function pointers. The functions in the AGP, Debug Report, Timed Operation, SPB, and System Firmware Table interfaces are implemented by the Microsoft DirectX graphics kernel subsystem and called by the display miniport driver.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
</table>