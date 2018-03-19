---
UID: NS:wiamindr_lh._WIAS_DOWN_SAMPLE_INFO
title: "_WIAS_DOWN_SAMPLE_INFO"
author: windows-driver-content
description: The WIAS_DOWN_SAMPLE_INFO structure stores information used by the downsampling helper function, wiasDownSampleBuffer.
old-location: image\wias_down_sample_info.htm
old-project: image
ms.assetid: af9d35d8-9e3c-4be0-8ba4-a0b548b1d7ac
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PWIAS_DOWN_SAMPLE_INFO, PWIAS_DOWN_SAMPLE_INFO, PWIAS_DOWN_SAMPLE_INFO structure pointer [Imaging Devices], WIAS_DOWN_SAMPLE_INFO, WIAS_DOWN_SAMPLE_INFO structure [Imaging Devices], _WIAS_DOWN_SAMPLE_INFO, image.wias_down_sample_info, wiamindr_lh/PWIAS_DOWN_SAMPLE_INFO, wiamindr_lh/WIAS_DOWN_SAMPLE_INFO, wiastrct_f7468047-47a4-4c3a-ada4-3bf329b32304.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
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
-	HeaderDef
api_location:
-	wiamindr_lh.h
api_name:
-	WIAS_DOWN_SAMPLE_INFO
product: Windows
targetos: Windows
req.typenames: WIAS_DOWN_SAMPLE_INFO, *PWIAS_DOWN_SAMPLE_INFO
req.product: Windows 10 or later.
---

# _WIAS_DOWN_SAMPLE_INFO structure
The WIAS_DOWN_SAMPLE_INFO structure stores information used by the downsampling helper function, <a href="..\wiamdef\nf-wiamdef-wiasdownsamplebuffer.md">wiasDownSampleBuffer</a>.

## Syntax
````
typedef struct _WIAS_DOWN_SAMPLE_INFO {
  ULONG ulOriginalWidth;
  ULONG ulOriginalHeight;
  ULONG ulBitsPerPixel;
  ULONG ulXRes;
  ULONG ulYRes;
  ULONG ulDownSampledWidth;
  ULONG ulDownSampledHeight;
  ULONG ulActualSize;
  ULONG ulDestBufSize;
  ULONG ulSrcBufSize;
  BYTE  *pSrcBuffer;
  BYTE  *pDestBuffer;
} WIAS_DOWN_SAMPLE_INFO, *PWIAS_DOWN_SAMPLE_INFO;
````

## Members


`ulOriginalWidth`

Specifies the width, in pixels, of the input data.

`ulOriginalHeight`

Specifies the height, in pixels, of the input data.

`ulBitsPerPixel`

Specifies the number of bits per pixel of the input data.

`ulXRes`

Specifies the horizontal resolution of the input data.

`ulYRes`

Specifies the vertical resolution of the input data.

`ulDownSampledWidth`

Specifies the width, in pixels, of the output data.

`ulDownSampledHeight`

Specifies the width, in pixels, of the output data.

`ulActualSize`

Specifies the number of bytes placed in the destination buffer.

`ulDestBufSize`

Specifies the size, in bytes, of the destination buffer.

`ulSrcBufSize`

Specifies the size, in bytes, of the source buffer.

`pSrcBuffer`

Points to the source buffer.

`pDestBuffer`

Points to the destination buffer.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Me and in Windows XP and later versions of the Windows operating systems. Available in Windows Me and in Windows XP and later versions of the Windows operating systems. |
| **Header** | wiamindr_lh.h (include Wiamindr.h) |

## See Also

<a href="..\wiamdef\nf-wiamdef-wiasdownsamplebuffer.md">wiasDownSampleBuffer</a>