---
UID: NF:winddiui.DrvDeviceCapabilities
title: DrvDeviceCapabilities function
author: windows-driver-content
description: A printer interface DLL's DrvDeviceCapabilities function returns requested information about a printer's capabilities.
old-location: print\drvdevicecapabilities.htm
old-project: print
ms.assetid: a8ea236d-42f9-45c5-b2f6-035e0ba28f75
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DrvDeviceCapabilities, DrvDeviceCapabilities function [Print Devices], print.drvdevicecapabilities, print_interface-graphics_cbe99c7b-a94f-47b2-8c51-d99bdcdec7d3.xml, winddiui/DrvDeviceCapabilities
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
-	DrvDeviceCapabilities
product: Windows
targetos: Windows
req.typenames: WINBIO_VERSION, *PWINBIO_VERSION
req.product: Windows 10 or later.
---


# DrvDeviceCapabilities function
A printer interface DLL's <b>DrvDeviceCapabilities</b> function returns requested information about a printer's capabilities.

## Syntax

```
DWORD DrvDeviceCapabilities(
  HANDLE   hPrinter,
  PWSTR    pszDeviceName,
  WORD     Capability,
  PVOID    pOutput,
  PDEVMODE pDevmode
);
```

## Parameters

`hPrinter`

Caller-supplied printer handle.

`pszDeviceName`

TBD

`Capability`

TBD

`pOutput`

TBD

`pDevmode`

TBD


## Return Value

The function's return value is dependent on the value received for the <i>iDevCap</i> parameter. If the received <i>iDevCap</i> value represents a capability that the driver does not support, or if an error is encountered, the function should return GDI_ERROR.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | winddiui.h (include Winddiui.h) |