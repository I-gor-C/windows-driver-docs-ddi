---
UID: NF:winddiui.DrvSplDeviceCaps
title: DrvSplDeviceCaps function
author: windows-driver-content
description: A printer interface DLL's DrvSplDeviceCaps function queries a printer for its capabilities.
old-location: print\drvspldevicecaps.htm
old-project: print
ms.assetid: 3d129a30-a892-4f4d-b8e3-f277d97980f4
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DrvSplDeviceCaps, DrvSplDeviceCaps function [Print Devices], print.drvspldevicecaps, print_interface-graphics_8c345fd4-e513-44ff-94b0-2f035db6a022.xml, winddiui/DrvSplDeviceCaps
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: winddiui.h
req.include-header: Winddiui.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	winddiui.h
api_name:
-	DrvSplDeviceCaps
product: Windows
targetos: Windows
req.typenames: WINBIO_VERSION, *PWINBIO_VERSION
req.product: Windows 10 or later.
---


# DrvSplDeviceCaps function
A printer interface DLL's <b>DrvSplDeviceCaps</b> function queries a printer for its capabilities.

## Syntax

```
DWORD DrvSplDeviceCaps(
  HANDLE   hPrinter,
  PWSTR    pszDeviceName,
  WORD     Capability,
  PVOID    pOutput,
  DWORD    cchBufSize,
  PDEVMODE pDevmode
);
```

## Parameters

`hPrinter`

Caller-supplied handle to the printer.

`pszDeviceName`

TBD

`Capability`

TBD

`pOutput`

TBD

`cchBufSize`

TBD

`pDevmode`

TBD


## Return Value

The return value depends on the <i>DeviceCap</i> parameter. If <i>DeviceCap</i> indicates a capability that the driver does not support, or if an error is encountered, the function should return GDI_ERROR.

## Remarks

The <b>DrvSplDeviceCaps</b> function is available in Microsoft Windows Server 2003 and later.

For descriptions of the DC_<i>XXX</i> flags, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548539">DrvDeviceCapabilities</a>.

This function must be defined in the .def file as DrvSplDeviceCaps @ 254, because the spooler uses the ordinal number 254 to obtain the driver function pointer.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | winddiui.h (include Winddiui.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff548539">DrvDeviceCapabilities</a>