---
UID: NC:d3d10umddi.PFND3D11_1DDI_STARTSESSIONKEYREFRESH
title: PFND3D11_1DDI_STARTSESSIONKEYREFRESH
author: windows-driver-content
description: Gets a random number that can be used to refresh the session key.
old-location: display\startsessionkeyrefresh1.htm
old-project: display
ms.assetid: 0973cef3-41a8-495e-aa8a-ce64df53b892
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D11_1DDI_STARTSESSIONKEYREFRESH, d3d10umddi/pfnStartSessionKeyRefresh, display.startsessionkeyrefresh1, pfnStartSessionKeyRefresh, pfnStartSessionKeyRefresh callback function [Display Devices]
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
-	pfnStartSessionKeyRefresh
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D11_1DDI_STARTSESSIONKEYREFRESH callback function
Gets a random number that can be used to refresh the session key.

## Syntax

```
PFND3D11_1DDI_STARTSESSIONKEYREFRESH Pfnd3d111DdiStartsessionkeyrefresh;

void Pfnd3d111DdiStartsessionkeyrefresh(
  D3D10DDI_HDEVICE hDevice,
  D3D11_1DDI_HCRYPTOSESSION hCryptoSession,
  UINT RandomNumberSize,
  VOID *pRandomNumber
)
{...}
```

## Parameters

`hDevice`

A handle to the display device (graphics context).

`hCryptoSession`

A handle to the cryptographic session object that was created through a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a> function.

`RandomNumberSize`

The size, in bytes, of the number in the buffer that is referenced by the <i>pRandomNumber</i> parameter.

`*pRandomNumber`

A pointer to a buffer that contains the status sequence number for the random start.


## Return Value

This callback function does not return a value.

## Remarks

The hardware and driver can optionally support <b>StartSessionKeyRefresh</b> for all cryptographic types.



When the Microsoft Direct3D runtime calls the driver's <b>StartSessionKeyRefresh</b> function, the driver generates and saves a random number and returns it in the buffer that the <i>pRandomNumber</i> parameter points to.

When the runtime subsequently calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451648">FinishSessionKeyRefresh</a> function, the driver refreshes the session key by performing an XOR operation of the random number with the key.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows Server 2012 |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451648">FinishSessionKeyRefresh</a>