---
UID : NS:ksmedia.tagKS_RGBQUAD
title : tagKS_RGBQUAD
author : windows-driver-content
description : The KS_RGBQUAD structure describes a color consisting of relative intensities of red, green, and blue, ranging from 0 to 255 (0x0 to 0xff).
old-location : stream\ks_rgbquad.htm
old-project : stream
ms.assetid : 49231293-286b-486d-b8f9-b44bdb845e7b
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : tagKS_RGBQUAD, KS_RGBQUAD, *PKS_RGBQUAD
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ksmedia.h
req.include-header : Ksmedia.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KS_RGBQUAD
req.alt-loc : ksmedia.h
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
req.typenames : KS_RGBQUAD, *PKS_RGBQUAD
---

# tagKS_RGBQUAD structure
The KS_RGBQUAD structure describes a color consisting of relative intensities of red, green, and blue, ranging from 0 to 255 (0x0 to 0xff).

## Syntax
````
typedef struct tagKS_RGBQUAD {
  BYTE rgbBlue;
  BYTE rgbGreen;
  BYTE rgbRed;
  BYTE rgbReserved;
} KS_RGBQUAD, *PKS_RGBQUAD;
````

## Members

        
            `rgbBlue`

            Specifies the intensity of blue in the color.
        
            `rgbGreen`

            Specifies the intensity of green in the color.
        
            `rgbRed`

            Specifies the intensity of red in the color.
        
            `rgbReserved`

            Reserved. This member must be zero.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksmedia.h (include Ksmedia.h) |