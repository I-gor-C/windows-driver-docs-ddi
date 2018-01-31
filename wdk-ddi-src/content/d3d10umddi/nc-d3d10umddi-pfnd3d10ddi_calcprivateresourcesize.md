---
UID : NC:d3d10umddi.PFND3D10DDI_CALCPRIVATERESOURCESIZE
title : PFND3D10DDI_CALCPRIVATERESOURCESIZE
author : windows-driver-content
description : The CalcPrivateResourceSize function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory).
old-location : display\calcprivateresourcesize.htm
old-project : display
ms.assetid : 2c4eb002-4788-46ab-92b9-3bb2dcb44ee3
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.calcprivateresourcesize, CalcPrivateResourceSize callback function [Display Devices], CalcPrivateResourceSize, PFND3D10DDI_CALCPRIVATERESOURCESIZE, PFND3D10DDI_CALCPRIVATERESOURCESIZE, d3d10umddi/CalcPrivateResourceSize, UserModeDisplayDriverDx10_Functions_bc7bb9a2-6fe2-49fb-b7d2-81297a828418.xml
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
req.typenames : SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_CALCPRIVATERESOURCESIZE callback function
The <b>CalcPrivateResourceSize</b> function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory).

## Syntax

```
PFND3D10DDI_CALCPRIVATERESOURCESIZE Pfnd3d10ddiCalcprivateresourcesize;

SIZE_T Pfnd3d10ddiCalcprivateresourcesize(
   D3D10DDI_HDEVICE,
  CONST D3D10DDIARG_CREATERESOURCE *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

<b>CalcPrivateResourceSize</b> returns the size of the memory region that the driver requires for creating resources.


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

<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg_createresource.md">D3D10DDIARG_CREATERESOURCE</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi_devicefuncs.md">D3D10DDI_DEVICEFUNCS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_CALCPRIVATERESOURCESIZE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>