---
UID : NF:winddiui.DrvDeviceCapabilities
title : DrvDeviceCapabilities function
author : windows-driver-content
description : A printer interface DLL's DrvDeviceCapabilities function returns requested information about a printer's capabilities.
old-location : print\drvdevicecapabilities.htm
old-project : print
ms.assetid : a8ea236d-42f9-45c5-b2f6-035e0ba28f75
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : DrvDeviceCapabilities
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : winddiui.h
req.include-header : Winddiui.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : DrvDeviceCapabilities
req.alt-loc : winddiui.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : WINBIO_VERSION, *PWINBIO_VERSION
req.product : Windows 10 or later.
---


# DrvDeviceCapabilities function
A printer interface DLL's <b>DrvDeviceCapabilities</b> function returns requested information about a printer's capabilities.

## Syntax

````
DWORD DrvDeviceCapabilities(
        HANDLE   hPrinter,
  _In_  PWSTR    pDeviceName,
        WORD     iDevCap,
  _Out_ PVOID    pvOutput,
  _In_  PDEVMODE pDevMode
);
````

## Parameters

`hPrinter`

Caller-supplied printer handle.

`pszDeviceName`



`Capability`



`pOutput`



`pDevmode`




## Return Value

The function's return value is dependent on the value received for the <i>iDevCap</i> parameter. If the received <i>iDevCap</i> value represents a capability that the driver does not support, or if an error is encountered, the function should return GDI_ERROR.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | winddiui.h (include Winddiui.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |