---
UID: NC:d3d10umddi.PFND3D11_1DDI_FINISHSESSIONKEYREFRESH
title: PFND3D11_1DDI_FINISHSESSIONKEYREFRESH
author: windows-driver-content
description: Completes the switch to a new session key.
old-location: display\finishsessionkeyrefresh1.htm
old-project: display
ms.assetid: 95c0433f-e4da-4566-b128-34cb758b8001
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11_1DDI_FINISHSESSIONKEYREFRESH, d3d10umddi/pfnFinishSessionKeyRefresh, display.finishsessionkeyrefresh1, pfnFinishSessionKeyRefresh, pfnFinishSessionKeyRefresh callback function [Display Devices]
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
-	pfnFinishSessionKeyRefresh
product: Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_FINISHSESSIONKEYREFRESH callback function
Completes the switch to a new session key.

## Syntax

```
PFND3D11_1DDI_FINISHSESSIONKEYREFRESH Pfnd3d111DdiFinishsessionkeyrefresh;

void Pfnd3d111DdiFinishsessionkeyrefresh(
  D3D10DDI_HDEVICE hDevice,
  D3D11_1DDI_HCRYPTOSESSION hCryptoSession
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`hCryptoSession`

A handle to the driver's private data for the cryptographic session. This handle was created by the Direct3D runtime and passed to the driver in the call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a>.


## Return Value

This callback function does not return a value.

## Remarks

<b>FinishSessionKeyRefresh</b> indicates that all buffers from that point in time will use the updated session key value.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a>