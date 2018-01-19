---
UID : NS:d3d10umddi.D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE
title : D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE
author : windows-driver-content
description : The D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE structure describes the parameters that the user-mode display driver uses to calculate the size of a memory block that the driver requires to store frequently-accessed data.
old-location : display\d3d11ddiarg_calcprivatedeferredcontextsize.htm
old-project : display
ms.assetid : 7889400e-bd26-43b5-a860-bea9f9217002
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE, D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Windows
req.target-min-winverclnt : D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE is supported beginning with the Windows 7 operating system.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE
req.alt-loc : d3d10umddi.h
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
req.typenames : D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE
---

# D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE structure
The D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE structure describes the parameters that the user-mode display driver uses to calculate the size of a memory block that the driver requires to store frequently-accessed data.

## Syntax
````
typedef struct D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE {
  UINT Flags;
} D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE;
````

## Members

        
            `Flags`

            [in] A valid bitwise OR of flag values that identify how to create a rendering device. The Direct3D runtime supports the following flags:


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

    ## See Also

        <dl>
<dt>
<a href="..\d3d10umddi\ne-d3d10umddi-d3d11ddi_3dpipelinelevel.md">D3D11DDI_3DPIPELINELEVEL</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_3dpipelinesupport_caps.md">D3D11DDI_3DPIPELINESUPPORT_CAPS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11DDIARG_CALCPRIVATEDEFERREDCONTEXTSIZE structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>