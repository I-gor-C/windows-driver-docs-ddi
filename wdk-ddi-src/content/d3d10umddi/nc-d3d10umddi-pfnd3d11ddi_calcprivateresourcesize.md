---
UID: NC:d3d10umddi.PFND3D11DDI_CALCPRIVATERESOURCESIZE
title: PFND3D11DDI_CALCPRIVATERESOURCESIZE
author: windows-driver-content
description: The CalcPrivateResourceSize(D3D11) function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory).
old-location: display\calcprivateresourcesize_d3d11_.htm
old-project: display
ms.assetid: 3b3a2571-012e-4acd-b836-f52e7b88a2fb
ms.author: windowsdriverdev
ms.date: 2/24/2018
ms.keywords: CalcPrivateResourceSize, CalcPrivateResourceSize callback function [Display Devices], PFND3D11DDI_CALCPRIVATERESOURCESIZE, UserModeDisplayDriverDx11_Functions_85fd70d1-91ec-4b9d-b379-18b5d3d43e67.xml, d3d10umddi/CalcPrivateResourceSize, display.calcprivateresourcesize_d3d11_
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: CalcPrivateResourceSize(D3D11) is supported beginning with the Windows 7 operating system.
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
-	UserDefined
api_location:
-	d3d10umddi.h
api_name:
-	CalcPrivateResourceSize
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11DDI_CALCPRIVATERESOURCESIZE callback function
The <b>CalcPrivateResourceSize(D3D11)</b> function determines the size of the user-mode display driver's private region of memory (that is, the size of internal driver structures, not the size of the resource video memory).

## Syntax

```
PFND3D11DDI_CALCPRIVATERESOURCESIZE Pfnd3d11ddiCalcprivateresourcesize;

SIZE_T Pfnd3d11ddiCalcprivateresourcesize(
   D3D10DDI_HDEVICE,
  CONST D3D11DDIARG_CREATERESOURCE *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`




## Return Value

<b>CalcPrivateResourceSize(D3D11)</b> returns the size of the memory region that the driver requires to create resources.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | CalcPrivateResourceSize(D3D11) is supported beginning with the Windows 7 operating system.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_devicefuncs.md">D3D11DDI_DEVICEFUNCS</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddiarg_createresource.md">D3D11DDIARG_CREATERESOURCE</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11DDI_CALCPRIVATERESOURCESIZE callback function%20 RELEASE:%20(2/24/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>