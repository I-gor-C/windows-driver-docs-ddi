---
UID : NC:d3d10umddi.PFND3D10DDI_RELOCATEDEVICEFUNCS
title : PFND3D10DDI_RELOCATEDEVICEFUNCS
author : windows-driver-content
description : The RelocateDeviceFuncs function notifies the user-mode display driver about the new location of the driver function table.
old-location : display\relocatedevicefuncs.htm
old-project : display
ms.assetid : 3932a2a1-7b1d-4921-bd4a-905b44166091
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.relocatedevicefuncs, RelocateDeviceFuncs callback function [Display Devices], RelocateDeviceFuncs, PFND3D10DDI_RELOCATEDEVICEFUNCS, PFND3D10DDI_RELOCATEDEVICEFUNCS, d3d10umddi/RelocateDeviceFuncs, UserModeDisplayDriverDx10_Functions_01a40916-8ba8-4e29-87d7-32e9c3fe337f.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
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


# PFND3D10DDI_RELOCATEDEVICEFUNCS callback function
The <i>RelocateDeviceFuncs</i> function notifies the user-mode display driver about the new location of the driver function table.

## Syntax

```
PFND3D10DDI_RELOCATEDEVICEFUNCS Pfnd3d10ddiRelocatedevicefuncs;

void Pfnd3d10ddiRelocatedevicefuncs(
   D3D10DDI_HDEVICE,
  D3D10DDI_DEVICEFUNCS *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code.

## Remarks

A user-mode display driver can use the <i>RelocateDeviceFuncs</i> function to replace function pointers in the driver function table.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi_devicefuncs.md">D3D10DDI_DEVICEFUNCS</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_RELOCATEDEVICEFUNCS callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>