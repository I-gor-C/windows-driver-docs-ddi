---
UID: NC:d3d10umddi.PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE
title: PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE
author: windows-driver-content
description: Returns the number of bytes that the driver requires to store private data for the authenticated channel state.
old-location: display\calcprivateauthenticatedchannelsize.htm
old-project: display
ms.assetid: f22dee75-a7e3-4ad4-a0d1-584adff3230e
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: CalcPrivateAuthenticatedChannelSize, CalcPrivateAuthenticatedChannelSize callback function [Display Devices], PFND3D11_1DDI_CALCPRIVATEAUTHENTICATEDCHANNELSIZE, d3d10umddi/CalcPrivateAuthenticatedChannelSize, display.calcprivateauthenticatedchannelsize
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	D3d10umddi.h
api_name:
-	CalcPrivateAuthenticatedChannelSize
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
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

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh406306">D3D11_1DDIARG_CREATEAUTHENTICATEDCHANNEL</a> structure that describes the authenticated channel.


## Return Value

The required number of bytes for the authenticated channel state.

## Remarks

This function is not expected to fail.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh406306">D3D11_1DDIARG_CREATEAUTHENTICATEDCHANNEL</a>