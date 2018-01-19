---
UID : NS:d3dumddi._FORMATOP
title : _FORMATOP
author : windows-driver-content
description : The FORMATOP structure describes a surface format and operations that can be performed with such a surface.
old-location : display\formatop.htm
old-project : display
ms.assetid : e846a41a-9d9c-4ccb-a478-260f333333f1
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _FORMATOP, FORMATOP
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : d3dumddi.h
req.include-header : D3dumddi.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : FORMATOP
req.alt-loc : d3dumddi.h
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
req.typenames : FORMATOP
---

# _FORMATOP structure
The <b>FORMATOP</b> structure describes a surface format and operations that can be performed with such a surface.

## Syntax
````
typedef struct _FORMATOP {
  D3DDDIFORMAT Format;
  UINT         Operations;
  UINT         FlipMsTypes;
  UINT         BltMsTypes;
  UINT         PrivateFormatBitCount;
} FORMATOP;
````

## Members

        
            `BltMsTypes`

            [out] A 32-bitmask for windowed multiple sampling.
        
            `FlipMsTypes`

            [out] A 32-bitmask for full-screen multiple sampling.
        
            `Format`

            [in] The <a href="..\d3dukmdt\ne-d3dukmdt-_d3dddiformat.md">D3DDDIFORMAT</a>-typed value that indicates the pixel format of the surface.
        
            `Operations`

            [out] A valid bitwise <b>OR</b> of the following flags that indicate the operations that can be performed on surfaces with the pixel format that is specified in the <b>Format</b> member. Some of the following flags imply that other flags should be used. If a driver sets a flag that implies other flags, the driver is not required to set the implied flags, and the Direct3D runtime determines the use of the implied flags.
        
            `PrivateFormatBitCount`

            [out] The bits per pixel of a pixel format that is private to the driver (that is, not one of the standard pixel formats that are defined by the <a href="..\d3dukmdt\ne-d3dukmdt-_d3dddiformat.md">D3DDDIFORMAT</a> enumeration type).


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dumddi.h (include D3dumddi.h) |

    ## See Also

        <dl>
<dt>
<a href="..\d3dukmdt\ns-d3dukmdt-_d3dddi_resourceflags2.md">D3DDDI_RESOURCEFLAGS2</a>
</dt>
<dt>
<a href="..\d3dumddi\ns-d3dumddi-_d3dddiarg_getcaps.md">D3DDDIARG_GETCAPS</a>
</dt>
<dt>
<a href="..\d3dumddi\ne-d3dumddi-_d3dddicaps_type.md">D3DDDICAPS_TYPE</a>
</dt>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt-_d3dddiformat.md">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi_getcaps.md">GetCaps</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20FORMATOP structure%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>