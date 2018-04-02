---
UID: NF:icm.WcsTranslateColors
title: WcsTranslateColors function
author: windows-driver-content
description: The WcsTranslateColors function translates an array of colors from the source color space to the destination color space as defined by a color transform.
old-location: print\wcstranslatecolors.htm
old-project: print
ms.assetid: 99843150-9e27-4f09-a3ba-5ff87d3f1c88
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: WcsTranslateColors, WcsTranslateColors function [Print Devices], colorfnc_3fac2d89-165e-4d5e-8dd2-cd68f7a9a47a.xml, icm/WcsTranslateColors, print.wcstranslatecolors
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: icm.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Included in Windows Vista and later.
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
req.lib: Mscms.lib
req.dll: Mscms.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Mscms.dll
api_name:
-	WcsTranslateColors
product: Windows
targetos: Windows
req.typenames: WCS_PROFILE_MANAGEMENT_SCOPE
---


# WcsTranslateColors function
The <code>WcsTranslateColors</code> function translates an array of colors from the source color space to the destination color space as defined by a color transform.

## Syntax

```
BOOL WcsTranslateColors(
  HTRANSFORM    hColorTransform,
  DWORD         nColors,
  DWORD         nInputChannels,
  COLORDATATYPE cdtInput,
  DWORD         cbInput,
  PVOID         pInputData,
  DWORD         nOutputChannels,
  COLORDATATYPE cdtOutput,
  DWORD         cbOutput,
  PVOID         pOutputData
);
```

## Parameters

`hColorTransform`

A handle to the WCS color transform to use.

`nColors`

The number of elements in the array pointed to by <i>pInputData</i> and <i>pOutputData</i>.

`nInputChannels`

The number of channels per element in the array pointed to by <i>pInputData</i>.

`cdtInput`

The input <a href="https://msdn.microsoft.com/library/windows/hardware/ff546006">COLORDATATYPE</a> color data type.

`cbInput`

The buffer size, in bytes, of <i>pInputData</i>.

`pInputData`

A pointer to an array of input colors.

`nOutputChannels`

The number of channels per element in the array pointed to by <i>pOutputData</i>.

`cdtOutput`

The output <a href="https://msdn.microsoft.com/library/windows/hardware/ff546006">COLORDATATYPE</a> color data type.

`cbOutput`

The buffer size, in bytes, of <i>pOutputData</i>.

`pOutputData`

A pointer to an array of colors that receives the results of the color translation.


## Return Value

None

## Remarks

If the input and the output color data types are not compatible with the color transform, this function will fail.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Included in Windows Vista and later.  |
| **Target Platform** | Universal |
| **Header** | icm.h |
| **Library** | Mscms.lib |
| **DLL** | Mscms.dll |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff546006">COLORDATATYPE</a>