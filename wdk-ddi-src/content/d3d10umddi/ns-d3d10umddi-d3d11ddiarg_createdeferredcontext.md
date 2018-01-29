---
UID : NS:d3d10umddi.D3D11DDIARG_CREATEDEFERREDCONTEXT
title : D3D11DDIARG_CREATEDEFERREDCONTEXT
author : windows-driver-content
description : The D3D11DDIARG_CREATEDEFERREDCONTEXT structure describes the deferred context to create.
old-location : display\d3d11ddiarg_createdeferredcontext.htm
old-project : display
ms.assetid : 4486939d-a35c-4b0b-b0d0-6402a62a4870
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : D3D11DDIARG_CREATEDEFERREDCONTEXT, display.d3d11ddiarg_createdeferredcontext, d3d10umddi/D3D11DDIARG_CREATEDEFERREDCONTEXT, UMDisplayDriver_Dx11param_Structs_c66ddced-4073-4400-8142-4464ceadad74.xml, D3D11DDIARG_CREATEDEFERREDCONTEXT structure [Display Devices]
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
req.typenames : D3D11DDIARG_CREATEDEFERREDCONTEXT
---

# D3D11DDIARG_CREATEDEFERREDCONTEXT structure
The D3D11DDIARG_CREATEDEFERREDCONTEXT structure describes the deferred context to create.

## Syntax
````
typedef struct D3D11DDIARG_CREATEDEFERREDCONTEXT {
  union {
    struct D3D11DDI_DEVICEFUNCS  *p11ContextFuncs;
    struct D3D11_1DDI_DEVICEFUNCS  *p11_1ContextFuncs;
#if D3D11DDI_MINOR_HEADER_VERSION >= 4
    struct D3DWDDM1_3DDI_DEVICEFUNCS  *pWDDM1_3ContextFuncs;
#endif 
  };
  D3D10DDI_HDEVICE      hDrvContext;
  D3D10DDI_HRTCORELAYER hRTCoreLayer;
  union {
    const struct D3D11DDI_CORELAYER_DEVICECALLBACKS  *p11UMCallbacks;
  };
  UINT                  Flags;
} D3D11DDIARG_CREATEDEFERREDCONTEXT;
````

## Members


`Flags`

[in] A valid bitwise OR of flag values that identify how to create a rendering device. The Direct3D runtime supports the following flags:

`hDrvContext`

[in] A handle to the driver context for the driver-private handle storage.

`hRTCoreLayer`

[in] A handle that the driver should use when it calls back into the Direct3D runtime to access core Direct3D 11 functionality (that is, when the driver calls functions that the <b>p11UMCallbacks</b> member specifies).


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_devicefuncs.md">D3D11DDI_DEVICEFUNCS</a>

<a href="..\d3d10umddi\ne-d3d10umddi-d3d11ddi_3dpipelinelevel.md">D3D11DDI_3DPIPELINELEVEL</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_3dpipelinesupport_caps.md">D3D11DDI_3DPIPELINESUPPORT_CAPS</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_devicefuncs.md">D3D11_1DDI_DEVICEFUNCS</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11ddi_corelayer_devicecallbacks.md">D3D11DDI_CORELAYER_DEVICECALLBACKS</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11DDIARG_CREATEDEFERREDCONTEXT structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>