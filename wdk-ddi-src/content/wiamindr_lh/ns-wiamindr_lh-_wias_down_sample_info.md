---
UID : NS:wiamindr_lh._WIAS_DOWN_SAMPLE_INFO
title : "_WIAS_DOWN_SAMPLE_INFO"
author : windows-driver-content
description : The WIAS_DOWN_SAMPLE_INFO structure stores information used by the downsampling helper function, wiasDownSampleBuffer.
old-location : image\wias_down_sample_info.htm
old-project : image
ms.assetid : af9d35d8-9e3c-4be0-8ba4-a0b548b1d7ac
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : wiamindr_lh/PWIAS_DOWN_SAMPLE_INFO, PWIAS_DOWN_SAMPLE_INFO, wiastrct_f7468047-47a4-4c3a-ada4-3bf329b32304.xml, WIAS_DOWN_SAMPLE_INFO, wiamindr_lh/WIAS_DOWN_SAMPLE_INFO, _WIAS_DOWN_SAMPLE_INFO, *PWIAS_DOWN_SAMPLE_INFO, WIAS_DOWN_SAMPLE_INFO structure [Imaging Devices], image.wias_down_sample_info, PWIAS_DOWN_SAMPLE_INFO structure pointer [Imaging Devices]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : wiamindr_lh.h
req.include-header : Wiamindr.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr : 
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
req.typenames : WIAS_DOWN_SAMPLE_INFO, *PWIAS_DOWN_SAMPLE_INFO
req.product : Windows 10 or later.
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


`pDestBuffer`

Points to the destination buffer.

`pSrcBuffer`

Points to the source buffer.

`ulActualSize`

Specifies the number of bytes placed in the destination buffer.

`ulBitsPerPixel`

Specifies the number of bits per pixel of the input data.

`ulDestBufSize`

Specifies the size, in bytes, of the destination buffer.

`ulDownSampledHeight`

Specifies the width, in pixels, of the output data.

`ulDownSampledWidth`

Specifies the width, in pixels, of the output data.

`ulOriginalHeight`

Specifies the height, in pixels, of the input data.

`ulOriginalWidth`

Specifies the width, in pixels, of the input data.

`ulSrcBufSize`

Specifies the size, in bytes, of the source buffer.

`ulXRes`

Specifies the horizontal resolution of the input data.

`ulYRes`

Specifies the vertical resolution of the input data.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wiamindr_lh.h (include Wiamindr.h) |

## See Also

<a href="..\wiamdef\nf-wiamdef-wiasdownsamplebuffer.md">wiasDownSampleBuffer</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20WIAS_DOWN_SAMPLE_INFO structure%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>