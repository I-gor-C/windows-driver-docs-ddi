---
UID: NS:ksmedia.tagKS_DATARANGE_IMAGE
title: tagKS_DATARANGE_IMAGE
author: windows-driver-content
description: Specifies an image data range that is used in the KSPIN_DESCRIPTOR structure that describes a pin (or stream).
old-location: stream\ks_datarange_image.htm
old-project: stream
ms.assetid: 81ad341a-5f68-43aa-98ea-193780a7c5b2
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PKS_DATARANGE_IMAGE, KS_DATARANGE_IMAGE, KS_DATARANGE_IMAGE structure [Streaming Media Devices], PKS_DATARANGE_IMAGE, PKS_DATARANGE_IMAGE structure pointer [Streaming Media Devices], ksmedia/KS_DATARANGE_IMAGE, ksmedia/PKS_DATARANGE_IMAGE, stream.ks_datarange_image, tagKS_DATARANGE_IMAGE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
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
-	HeaderDef
api_location:
-	Ksmedia.h
api_name:
-	KS_DATARANGE_IMAGE
product:
- Windows
targetos: Windows
req.typenames: KS_DATARANGE_IMAGE, *PKS_DATARANGE_IMAGE
---

# tagKS_DATARANGE_IMAGE structure
Specifies an image data range that is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563533">KSPIN_DESCRIPTOR</a> structure that describes a pin (or stream).

## Syntax
```
typedef struct tagKS_DATARANGE_IMAGE {
  KSDATARANGE                 DataRange;
  KS_VIDEO_STREAM_CONFIG_CAPS ConfigCaps;
  KS_BITMAPINFOHEADER         ImageInfoHeader;
} *PKS_DATARANGE_IMAGE, KS_DATARANGE_IMAGE;
```

## Members


`DataRange`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a> structure that specifies the data range supported by this pin type.

`ConfigCaps`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff567706">KS_VIDEO_STREAM_CONFIG_CAPS</a> structure that specifies the configuration of the stream, including scaling, cropping, and frame and data rates.

`ImageInfoHeader`

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff567305">KS_BITMAPINFOHEADER</a> structure that specifies image color and dimension information that the still image capture stream would provide.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | ksmedia.h (include Ksmedia.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff561658">KSDATARANGE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563533">KSPIN_DESCRIPTOR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567305">KS_BITMAPINFOHEADER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567706">KS_VIDEO_STREAM_CONFIG_CAPS</a>