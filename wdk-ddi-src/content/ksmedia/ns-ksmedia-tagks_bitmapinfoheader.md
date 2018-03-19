---
UID: NS:ksmedia.tagKS_BITMAPINFOHEADER
title: tagKS_BITMAPINFOHEADER
author: windows-driver-content
description: The KS_BITMAPINFOHEADER structure describes details about the video stream, such as image dimensions and pixel depth.
old-location: stream\ks_bitmapinfoheader.htm
old-project: stream
ms.assetid: 77101494-97bb-4049-8c6c-cdb4ee82f312
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PKS_BITMAPINFOHEADER, KS_BITMAPINFOHEADER, KS_BITMAPINFOHEADER structure [Streaming Media Devices], PKS_BITMAPINFOHEADER, PKS_BITMAPINFOHEADER structure pointer [Streaming Media Devices], ksmedia/KS_BITMAPINFOHEADER, ksmedia/PKS_BITMAPINFOHEADER, stream.ks_bitmapinfoheader, tagKS_BITMAPINFOHEADER, vidcapstruct_14e65a26-c943-4fad-949a-87aaf584e50c.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
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
-	ksmedia.h
api_name:
-	KS_BITMAPINFOHEADER
product: Windows
targetos: Windows
req.typenames: KS_BITMAPINFOHEADER, *PKS_BITMAPINFOHEADER
---

# tagKS_BITMAPINFOHEADER structure
The KS_BITMAPINFOHEADER structure describes details about the video stream, such as image dimensions and pixel depth.

## Syntax
````
typedef struct tagKS_BITMAPINFOHEADER {
  DWORD biSize;
  LONG  biWidth;
  LONG  biHeight;
  WORD  biPlanes;
  WORD  biBitCount;
  DWORD biCompression;
  DWORD biSizeImage;
  LONG  biXPelsPerMeter;
  LONG  biYPelsPerMeter;
  DWORD biClrUsed;
  DWORD biClrImportant;
} KS_BITMAPINFOHEADER, *PKS_BITMAPINFOHEADER;
````

## Members


`biSize`

Specifies the size of the structure in bytes.

`biWidth`

Specifies the width of the bitmap in pixels.

`biHeight`

Specifies the height of the bitmap in pixels.

`biPlanes`

Specifies the number of planes. This is always set to 1.

`biBitCount`

Specifies the color bits per pixel. For example, 1, 4, 8, or 24.

`biCompression`

Specifies the compression scheme.

`biSizeImage`

Specifies the size of bitmap bits in bytes. (Only required if using compression.)

`biXPelsPerMeter`

Specifies the horizontal resolution in pixels per meter.

`biYPelsPerMeter`

Specifies the vertical resolution in pixels per meter.

`biClrUsed`

Specifies the number of colors used in the image.

`biClrImportant`

Specifies the number of important colors in the image.

## Remarks
This is the same structure as the user-mode GDI bitmap header (BITMAPINFOHEADER) structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ksmedia.h (include Ksmedia.h) |