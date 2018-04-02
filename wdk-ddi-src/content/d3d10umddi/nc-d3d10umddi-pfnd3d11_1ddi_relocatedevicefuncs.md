---
UID: NC:d3d10umddi.PFND3D11_1DDI_RELOCATEDEVICEFUNCS
title: PFND3D11_1DDI_RELOCATEDEVICEFUNCS
author: windows-driver-content
description: Notifies the user-mode display driver about the new location of the driver function table.
old-location: display\relocatedevicefuncs_d3d11_1_.htm
old-project: display
ms.assetid: 5d9f964e-5d7a-4b6c-977e-c718e3424f84
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11_1DDI_RELOCATEDEVICEFUNCS, RelocateDeviceFuncs(D3D11_1), RelocateDeviceFuncs(D3D11_1) callback function [Display Devices], d3d10umddi/RelocateDeviceFuncs(D3D11_1), display.pfnrelocatedevicefuncs, display.relocatedevicefuncs_d3d11_1_
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	UserDefined
api_location:
-	D3d10umddi.h
api_name:
-	RelocateDeviceFuncs(D3D11_1)
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_RELOCATEDEVICEFUNCS callback function
Notifies the user-mode display driver about the new location of the driver function table.

## Syntax

```
PFND3D11_1DDI_RELOCATEDEVICEFUNCS Pfnd3d111DdiRelocatedevicefuncs;

void Pfnd3d111DdiRelocatedevicefuncs(
   D3D10DDI_HDEVICE,
  D3D11_1DDI_DEVICEFUNCS *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

The driver can use the <a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a> callback function to set an error code.

## Remarks

A user-mode display driver can use the <i>RelocateDeviceFuncs(D3D11_1)</i> function to replace function pointers in the driver function table.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh406443">D3D11_1DDI_DEVICEFUNCS</a>



<a href="https://msdn.microsoft.com/968b04a7-8869-410c-a6fc-83d57726858f">pfnSetErrorCb</a>