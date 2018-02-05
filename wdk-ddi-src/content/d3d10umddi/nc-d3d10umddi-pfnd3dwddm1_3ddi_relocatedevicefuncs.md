---
UID : NC:d3d10umddi.PFND3DWDDM1_3DDI_RELOCATEDEVICEFUNCS
title : PFND3DWDDM1_3DDI_RELOCATEDEVICEFUNCS
author : windows-driver-content
description : Notifies the user-mode display driver about the new location of the driver function table. Implemented by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers.
old-location : display\relocatedevicefuncs_d3d11_2_.htm
old-project : display
ms.assetid : BA2A1F90-6E30-4055-9374-943540AE2446
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.relocatedevicefuncs_d3d11_2_, RelocateDeviceFuncs(D3D11_2) callback function [Display Devices], RelocateDeviceFuncs(D3D11_2), PFND3DWDDM1_3DDI_RELOCATEDEVICEFUNCS, PFND3DWDDM1_3DDI_RELOCATEDEVICEFUNCS, d3d10umddi/RelocateDeviceFuncs(D3D11_2)
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : Windows 8.1,WDDM 1.3
req.target-min-winversvr : Windows Server 2012 R2
req.kmdf-ver : 
req.umdf-ver : 
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3DWDDM1_3DDI_RELOCATEDEVICEFUNCS callback function
Notifies the user-mode display driver about the new location of the driver function table.

Implemented by Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers.

## Syntax

```
PFND3DWDDM1_3DDI_RELOCATEDEVICEFUNCS Pfnd3dwddm13DdiRelocatedevicefuncs;

void Pfnd3dwddm13DdiRelocatedevicefuncs(
   D3D10DDI_HDEVICE,
  D3DWDDM1_3DDI_DEVICEFUNCS *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code.

## Remarks

A user-mode display driver can use the <i>RelocateDeviceFuncs(D3D11_2)</i> function to replace function pointers in the driver function table.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1,WDDM 1.3 Windows 8.1,WDDM 1.3 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3dwddm1_3ddi_relocatedevicefuncs.md">RelocateDeviceFuncs(D3D11_2)</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3dwddm1_3ddi_devicefuncs.md">D3DWDDM1_3DDI_DEVICEFUNCS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DWDDM1_3DDI_RELOCATEDEVICEFUNCS callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>