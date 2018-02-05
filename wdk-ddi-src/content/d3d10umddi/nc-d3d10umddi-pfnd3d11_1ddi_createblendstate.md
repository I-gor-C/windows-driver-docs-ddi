---
UID : NC:d3d10umddi.PFND3D11_1DDI_CREATEBLENDSTATE
title : PFND3D11_1DDI_CREATEBLENDSTATE
author : windows-driver-content
description : Creates a blend state.
old-location : display\createblendstate_d3d11_1_.htm
old-project : display
ms.assetid : 5956412e-ae35-4960-afc0-a82c6a2aa9f1
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.createblendstate_d3d11_1_, CreateBlendState(D3D11_1) callback function [Display Devices], CreateBlendState(D3D11_1), PFND3D11_1DDI_CREATEBLENDSTATE, PFND3D11_1DDI_CREATEBLENDSTATE, d3d10umddi/CreateBlendState(D3D11_1), display.pfncreateblendstate
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


# PFND3D11_1DDI_CREATEBLENDSTATE callback function
Creates a blend state.

## Syntax

```
PFND3D11_1DDI_CREATEBLENDSTATE Pfnd3d111DdiCreateblendstate;

void Pfnd3d111DdiCreateblendstate(
   D3D10DDI_HDEVICE,
  CONST D3D11_1_DDI_BLEND_DESC *,
   D3D10DDI_HBLENDSTATE,
   D3D10DDI_HRTBLENDSTATE
)
{...}
```

## Parameters

`D3D10DDI_HDEVICE`



`*`



`D3D10DDI_HBLENDSTATE`



`D3D10DDI_HRTBLENDSTATE`




## Return Value

The driver can use the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> callback function to set an error code. For more information about setting error codes, see the Remarks section.

## Remarks

The driver can pass E_OUTOFMEMORY (if the driver runs out of memory) or D3DDDIERR_DEVICEREMOVED (if the device has been removed) in a call to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a> function. The Direct3D runtime will determine that any other errors are critical. If the driver passes any errors, including D3DDDIERR_DEVICEREMOVED, the Direct3D runtime will determine that the handle is incorrect; therefore, the runtime will not call the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroyblendstate.md">DestroyBlendState</a> function to destroy the handle that the <i>hBlendState</i> parameter specifies.

The user-mode display driver is not required to create more than 4,096 unique instances of blend-state objects on a device at one time.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_destroyblendstate.md">DestroyBlendState</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi_seterror_cb.md">pfnSetErrorCb</a>

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1_ddi_blend_desc.md">D3D11_1_DDI_BLEND_DESC</a>

<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11_1ddi_calcprivateblendstatesize.md">CalcPrivateBlendStateSize(D3D11_1)</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_CREATEBLENDSTATE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>