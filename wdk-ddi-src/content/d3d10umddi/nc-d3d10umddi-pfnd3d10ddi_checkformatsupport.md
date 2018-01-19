---
UID : NC:d3d10umddi.PFND3D10DDI_CHECKFORMATSUPPORT
title : PFND3D10DDI_CHECKFORMATSUPPORT
author : windows-driver-content
description : Retrieves the capabilities that the device has with the specified format.
old-location : display\checkformatsupport.htm
old-project : display
ms.assetid : 463ab1e5-08b1-45a1-b7d8-bdfacb3d4bdb
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _SETRESULT_INFO, *PSETRESULT_INFO, SETRESULT_INFO
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
req.alt-api : CheckFormatSupport
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
req.typenames : "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D10DDI_CHECKFORMATSUPPORT callback function
Retrieves the capabilities that the device has with the specified format.

## Syntax

```
PFND3D10DDI_CHECKFORMATSUPPORT Pfnd3d10ddiCheckformatsupport;

void Pfnd3d10ddiCheckformatsupport(
   D3D10DDI_HDEVICE,
   DXGI_FORMAT,
  UINT *
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`DXGI_FORMAT`



`*`




## Return Value

None.

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see  Remarks .

## Remarks

The driver can call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function to set <b>E_FAIL</b> if the format in the <i>Format</i> parameter does not exist or can set <b>E_INVALIDARG</b> if the <i>pFormatCaps</i> parameter is <b>NULL</b>.

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
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddi_devicefuncs.md">D3D10DDI_DEVICEFUNCS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/dce61bc4-4ed5-4e64-84e8-6db88025e5c2">DXGI_FORMAT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/2aef590f-2328-4175-ab60-c72b1fd83db7">DXGI_FORMAT_R10G10B10_XR_BIAS_A2_UNORM</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D10DDI_CHECKFORMATSUPPORT callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>