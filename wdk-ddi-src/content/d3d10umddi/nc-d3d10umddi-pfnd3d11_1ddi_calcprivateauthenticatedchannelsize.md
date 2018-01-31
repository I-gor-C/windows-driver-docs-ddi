---
UID : NC:d3d10umddi.PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE
title : PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE
author : windows-driver-content
description : Returns the number of bytes that the driver requires to store private data for the authenticated channel state.
old-location : display\calcprivateauthenticatedchannelsize.htm
old-project : display
ms.assetid : f22dee75-a7e3-4ad4-a0d1-584adff3230e
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.calcprivateauthenticatedchannelsize, CalcPrivateAuthenticatedChannelSize callback function [Display Devices], CalcPrivateAuthenticatedChannelSize, PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE, PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE, d3d10umddi/CalcPrivateAuthenticatedChannelSize
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
req.typenames : SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE callback function
Returns the number of bytes that the driver requires to store private data for the authenticated channel state.

## Syntax

```
PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE Pfnd3d111DdiCalcprivateauthenticatedchannelsize;

SIZE_T Pfnd3d111DdiCalcprivateauthenticatedchannelsize(
  D3D10DDI_HDEVICE hDevice,
  CONST D3D11_1DDIARG_CREATEAUTHENTICATEDCHANNEL *pCreateData
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`*pCreateData`




## Return Value

The required number of bytes for the authenticated channel state.

## Remarks

This function is not expected to fail.

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

<a href="..\d3d10umddi\ns-d3d10umddi-d3d11_1ddiarg_createauthenticatedchannel.md">D3D11_1DDIARG_CREATEAUTHENTICATEDCHANNEL</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE callback function%20 RELEASE:%20(12/29/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>