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

````
DWORD DrvSplDeviceCaps(
            HANDLE   hPrinter,
  _In_      PWSTR    pwDeviceName,
            WORD     DeviceCap,
  _Out_opt_ PVOID    pvOutput,
            DWORD    cchBuf,
  _In_opt_  PDEVMODE pDM
);
````

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

For descriptions of the DC_<i>XXX</i> flags, see <a href="..\winddiui\nf-winddiui-drvdevicecapabilities.md">DrvDeviceCapabilities</a>.

This function must be defined in the .def file as DrvSplDeviceCaps @ 254, because the spooler uses the ordinal number 254 to obtain the driver function pointer.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | winddiui.h (include Winddiui.h) |

## See Also

<a href="..\winddiui\nf-winddiui-drvdevicecapabilities.md">DrvDeviceCapabilities</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20DrvSplDeviceCaps function%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>