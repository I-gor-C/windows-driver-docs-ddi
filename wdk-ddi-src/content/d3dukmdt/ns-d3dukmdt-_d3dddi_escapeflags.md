---
UID : NS:d3dukmdt._D3DDDI_ESCAPEFLAGS
title : "_D3DDDI_ESCAPEFLAGS"
author : windows-driver-content
description : The D3DDDI_ESCAPEFLAGS structure identifies how the user-mode display driver shares information with the display miniport driver.
old-location : display\d3dddi_escapeflags.htm
old-project : display
ms.assetid : 40648f6a-3393-4374-beff-e097c299f9e9
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.d3dddi_escapeflags, d3dukmdt/D3DDDI_ESCAPEFLAGS, _D3DDDI_ESCAPEFLAGS, D3D_other_Structs_5ff9ad07-6a44-4a53-a70c-5abdbe84065a.xml, D3DDDI_ESCAPEFLAGS structure [Display Devices], D3DDDI_ESCAPEFLAGS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dukmdt.h
req.include-header : D3dumddi.h, D3dkmddi.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating system.
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
req.typenames : D3DDDI_ESCAPEFLAGS
---

# _D3DDDI_ESCAPEFLAGS structure
The D3DDDI_ESCAPEFLAGS structure identifies how the user-mode display driver shares information with the display miniport driver.

## Syntax
````
typedef struct _D3DDDI_ESCAPEFLAGS {
  union {
    struct {
      UINT HardwareAccess  :1;
#if ((DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM1_3) || \
     (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WDDM1_3))

      UINT DeviceStatusQuery  :1;
      UINT ChangeFrameLatency  :1;
      UINT Reserved  :29;
#else 
      UINT Reserved  :31;
#endif 
    };
    UINT   Value;
  };
} D3DDDI_ESCAPEFLAGS;
````

## Members


## Remarks
If <b>ChangeFrameLatency</b> is set, a <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_escapecb.md">pfnEscapeCb</a> call will succeed only if:
<ul>
<li>The display miniport driver is responsible for a linked adapter configuration (LDA) provided by a single vendor.</li>
<li>The app has taken exclusive full-screen ownership of the display at some point in its lifetime.</li>
<li>The app has not overridden the default maximum frame latency value of 3.</li>
</ul>If these conditions are not met, <i>pfnEscapeCb</i> call returns an <b>E_INVALIDARG</b> error code.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating system. Available in Windows Vista and later versions of the Windows operating system. |
| **Header** | d3dukmdt.h (include D3dumddi.h, D3dkmddi.h) |

## See Also

<a href="..\d3dumddi\ns-d3dumddi-_d3dddicb_escape.md">D3DDDICB_ESCAPE</a>

<a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi_escape.md">DxgkDdiEscape</a>

<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_framelatencyescape.md">D3DDDI_FRAMELATENCYESCAPE</a>

<a href="..\d3dkmddi\ns-d3dkmddi-_dxgkarg_escape.md">DXGKARG_ESCAPE</a>

<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_escapecb.md">pfnEscapeCb</a>

<a href="..\d3dumddi\ns-d3dumddi-_d3dddi_executionstateescape.md">D3DDDI_EXECUTIONSTATEESCAPE</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDI_ESCAPEFLAGS structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>