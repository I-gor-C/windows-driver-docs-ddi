---
UID: NC:d3d10umddi.PFND3D11_1DDI_SETCONSTANTBUFFERS
title: PFND3D11_1DDI_SETCONSTANTBUFFERS
author: windows-driver-content
description: Sets constant buffers for a compute shader.
old-location: display\cssetconstantbuffers_d3d11_1_.htm
old-project: display
ms.assetid: 6A2B50BF-415D-47BB-9514-B15F717A76EA
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: display.cssetconstantbuffers_d3d11_1_, CsSetConstantBuffers(D3D11_1) callback function [Display Devices], CsSetConstantBuffers(D3D11_1), PFND3D11_1DDI_SETCONSTANTBUFFERS, PFND3D11_1DDI_SETCONSTANTBUFFERS, d3d10umddi/CsSetConstantBuffers(D3D11_1)
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	D3d10umddi.h
apiname:
-	CsSetConstantBuffers(D3D11_1)
product: Windows
targetos: Windows
req.typenames: "*PSETRESULT_INFO, SETRESULT_INFO"
---


# PFND3D11_1DDI_SETCONSTANTBUFFERS callback function
Sets constant buffers for a compute shader.

## Syntax

```
PFND3D11_1DDI_SETCONSTANTBUFFERS Pfnd3d111DdiSetconstantbuffers;

void Pfnd3d111DdiSetconstantbuffers(
   D3D10DDI_HDEVICE,
  UINT StartSlot,
  UINT NumBuffers,
  CONST D3D10DDI_HRESOURCE *,
  CONST UINT *pFirstConstant,
  CONST UINT *pNumConstants
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`StartSlot`



`NumBuffers`

The total number of buffers to set.

`*`



`*pFirstConstant`

A pointer to the first constant in the buffer pointed to by <i>StartBuffer</i>.

`*pNumConstants`

The number of constants in the  buffer pointed to by  <i>StartBuffer</i>.


## Return Value

None

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the following Remarks section.

## Remarks

Buffers that this function specifies are created with the D3D10_BIND_CONSTANT_BUFFER flag. 

The driver should not encounter any error, except for D3DDDIERR_DEVICEREMOVED. Therefore, if the driver passes any error, except for D3DDDIERR_DEVICEREMOVED, in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function, the Direct3D runtime determines that the error is critical. Even if the device is removed, the driver is not required to return D3DDDIERR_DEVICEREMOVED; however, if device removal interferes with the operation of this function (which typically should not happen), the driver can return D3DDDIERR_DEVICEREMOVED.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>



<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddi_devicefuncs.md">D3D11_1DDI_DEVICEFUNCS</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_SETCONSTANTBUFFERS callback function%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>