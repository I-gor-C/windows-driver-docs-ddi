---
UID: NF:d3dkmthk.D3DKMTGetPresentHistory
title: D3DKMTGetPresentHistory function
author: windows-driver-content
description: The D3DKMTGetPresentHistory function retrieves copying history.
old-location: display\d3dkmtgetpresenthistory.htm
old-project: display
ms.assetid: e00af04e-4770-4505-a06c-c44405dcaab5
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3DKMTGetPresentHistory, D3DKMTGetPresentHistory function [Display Devices], OpenGL_Functions_9070e169-207c-478d-8eab-b0bcfad65362.xml, d3dkmthk/D3DKMTGetPresentHistory, display.d3dkmtgetpresenthistory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Gdi32.lib
req.dll: Gdi32.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Gdi32.dll
-	API-MS-Win-dx-d3dkmt-l1-1-0.dll
-	API-MS-Win-dx-d3dkmt-l1-1-1.dll
-	API-MS-Win-DX-D3DKMT-L1-1-2.dll
api_name:
-	D3DKMTGetPresentHistory
product:
- Windows
targetos: Windows
req.typenames: D3DKMT_DRIVERVERSION
---


# D3DKMTGetPresentHistory function
The <b>D3DKMTGetPresentHistory</b> function retrieves copying history.

## Syntax

```
NTSTATUS D3DKMTGetPresentHistory(

);
```

## Parameters

This function has no parameters.

## Return Value

Returns <b>STATUS_SUCCESS</b> if copying history is successfully retrieved; otherwise an appropriate error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Universal |
| **Header** | d3dkmthk.h (include D3dkmthk.h) |
| **Library** | Gdi32.lib |
| **DLL** | Gdi32.dll |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff548052">D3DKMT_GETPRESENTHISTORY</a>