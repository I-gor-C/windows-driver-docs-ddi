---
UID : NC:d3d10umddi.PFND3D11_1DDI_VIDEODECODERGETHANDLE
title : PFND3D11_1DDI_VIDEODECODERGETHANDLE
author : windows-driver-content
description : Returns the driver's handle for a video decoder that can be used by the application to configure content protection.
old-location : display\videodecodergethandle.htm
old-project : display
ms.assetid : 05c16416-d48c-44ce-b025-d62d763682bc
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _SETRESULT_INFO, *PSETRESULT_INFO, SETRESULT_INFO
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : d3d10umddi.h
req.include-header : D3d10umddi.h
req.target-type : Desktop
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : pfnVideoDecoderGetHandle
req.alt-loc : D3d10umddi.h
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
req.typenames : "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11_1DDI_VIDEODECODERGETHANDLE callback function
Returns the driver's handle for a video decoder that can be used by the application  to configure content protection.

## Syntax

```
PFND3D11_1DDI_VIDEODECODERGETHANDLE Pfnd3d111DdiVideodecodergethandle;

HRESULT Pfnd3d111DdiVideodecodergethandle(
  D3D10DDI_HDEVICE hDevice,
   D3D11_1DDI_HDECODE,
  HANDLE *pContentProtectionHandle
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`D3D11_1DDI_HDECODE`



`*pContentProtectionHandle`




## Return Value

<b>VideoDecoderGetHandle</b> returns one of the following values:
<dl>
<dt><b>S_OK</b></dt>
</dl>The handle was returned successfully.
<dl>
<dt><b>D3DDDIERR_DEVICEREMOVED</b></dt>
</dl>The graphics adapter was removed.

<dl>
<dt><b>E_OUTOFMEMORY</b></dt>
</dl>
        Memory was not available to complete the operation.

## Remarks

The <b>VideoDecoderGetHandle</b> function returns a driver handle for the video decoder. This handle can be used by the application to associate the decoder with a cryptographic session over the authenticated channel.

This function allows the driver to define its own handle to its state data for the video decoder. This bypasses any handle mapping that may be performed by the Microsoft Direct3D runtime.

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

<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_createvideodecoder.md">CreateVideoDecoder</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddiarg_videodecoderextension.md">D3D11_1DDIARG_VIDEODECODEREXTENSION</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_VIDEODECODERGETHANDLE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>