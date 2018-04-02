---
UID: NF:icm.WcsCheckColors
title: WcsCheckColors function
author: windows-driver-content
description: The WcsCheckColors function determines whether the colors in an array lie within the output gamut of a specified WCS color transform.
old-location: print\wcscheckcolors.htm
old-project: print
ms.assetid: 1254b0d4-cb72-4171-b09d-f0bca58a137a
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: WcsCheckColors, WcsCheckColors function [Print Devices], colorfnc_abd03c7d-c516-4c81-a0ff-df351cac753e.xml, icm/WcsCheckColors, print.wcscheckcolors
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
-	WcsCheckColors
product:
- Windows
targetos: Windows
req.typenames: WCS_PROFILE_MANAGEMENT_SCOPE
---


# WcsCheckColors function
The <code>WcsCheckColors</code> function determines whether the colors in an array lie within the output gamut of a specified WCS color transform.

## Syntax

```
BOOL WcsCheckColors(
  HTRANSFORM    hColorTransform,
  DWORD         nColors,
  DWORD         nInputChannels,
  COLORDATATYPE cdtInput,
  DWORD         cbInput,
  PVOID         pInputData,
  PBYTE         paResult
);
```

## Parameters

`hColorTransform`

A handle to the WCS color transform to use.

`nColors`

The number of elements in the array pointed to by <i>pInputData</i> and <i>paResult</i>.

`nInputChannels`

The number of channels per element in the array pointed to by <i>pInputData</i>.

`cdtInput`

The input COLORDATATYPE color data type.

`cbInput`

The buffer size of <i>pInputData</i>.

`pInputData`

A pointer to an array of input colors. Colors in this array correspond to the color space of the source profile.

`paResult`

A pointer to an array of <i>nColors</i> bytes that receives the results of the test.


## Return Value

None

## Remarks

If the input and the output color data types are not compatible with the color transform, this function will convert the input color data as required.

This function will fail if an ICC transform is used.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Included in Windows Vista and later.  |
| **Target Platform** | Universal |
| **Header** | icm.h |
| **Library** | Mscms.lib |
| **DLL** | Mscms.dll |