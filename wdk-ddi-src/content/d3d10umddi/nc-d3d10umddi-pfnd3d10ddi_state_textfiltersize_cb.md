---
UID: NC:d3d10umddi.PFND3D10DDI_STATE_TEXTFILTERSIZE_CB
title: PFND3D10DDI_STATE_TEXTFILTERSIZE_CB
author: windows-driver-content
description: The pfnStateTextFilterSizeCb function causes the Microsoft Direct3D 10 runtime to refresh the width and height of the monochrome convolution filter.
old-location: display\pfnstatetextfiltersizecb.htm
old-project: display
ms.assetid: f53f73bf-8297-4c56-81f9-443d10a6b701
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PFND3D10DDI_STATE_TEXTFILTERSIZE_CB, d3d10state_functions_96a0da1a-c30d-4872-a54d-b24e83d76c95.xml, d3d10umddi/pfnStateTextFilterSizeCb, display.pfnstatetextfiltersizecb, pfnStateTextFilterSizeCb, pfnStateTextFilterSizeCb callback function [Display Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	d3d10umddi.h
api_name:
-	pfnStateTextFilterSizeCb
product:
- Windows
targetos: Windows
req.typenames: SETRESULT_INFO, *PSETRESULT_INFO
---


# PFND3D10DDI_STATE_TEXTFILTERSIZE_CB callback function
The <b>pfnStateTextFilterSizeCb</b> function causes the Microsoft Direct3D 10 runtime to refresh the width and height of the monochrome convolution filter.

## Syntax

```
PFND3D10DDI_STATE_TEXTFILTERSIZE_CB Pfnd3d10ddiStateTextfiltersizeCb;

void Pfnd3d10ddiStateTextfiltersizeCb(
   D3D10DDI_HRTCORELAYER
)
{...}
```

## Parameters

`D3D10DDI_HRTCORELAYER`




## Return Value

None

## Remarks

The <b>pfnStateTextFilterSizeCb</b> function calls the user-mode display driver's <a href="https://msdn.microsoft.com/663fd3c3-7a8f-446d-b45a-392716116407">SetTextFilterSize</a> function with the current monochrome convolution filter settings.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff541820">D3D10DDI_CORELAYER_DEVICECALLBACKS</a>



<a href="https://msdn.microsoft.com/663fd3c3-7a8f-446d-b45a-392716116407">SetTextFilterSize</a>