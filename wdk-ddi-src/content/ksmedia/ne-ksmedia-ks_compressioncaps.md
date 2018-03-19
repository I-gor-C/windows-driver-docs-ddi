---
UID: NE:ksmedia.KS_CompressionCaps
title: KS_CompressionCaps
author: windows-driver-content
description: The KS_CompressionCaps enumeration defines compression capabilities of a device.
old-location: stream\ks_compressioncaps.htm
old-project: stream
ms.assetid: 47781af6-bf14-4b95-bef2-506aadb2d1fb
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KS_CompressionCaps, KS_CompressionCaps enumeration [Streaming Media Devices], KS_CompressionCaps_CanBFrame, KS_CompressionCaps_CanCrunch, KS_CompressionCaps_CanKeyFrame, KS_CompressionCaps_CanQuality, KS_CompressionCaps_CanWindow, ksmedia/KS_CompressionCaps, ksmedia/KS_CompressionCaps_CanBFrame, ksmedia/KS_CompressionCaps_CanCrunch, ksmedia/KS_CompressionCaps_CanKeyFrame, ksmedia/KS_CompressionCaps_CanQuality, ksmedia/KS_CompressionCaps_CanWindow, stream.ks_compressioncaps, vidcapstruct_77c66492-8105-4cf2-a303-7819d83adbb4.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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
-	KS_CompressionCaps
product: Windows
targetos: Windows
req.typenames: KS_CompressionCaps
---

# KS_CompressionCaps Enumeration
The KS_CompressionCaps enumeration defines compression capabilities of a device.

## Syntax
````
typedef enum  { 
  KS_CompressionCaps_CanQuality   = 1,
  KS_CompressionCaps_CanCrunch    = 2,
  KS_CompressionCaps_CanKeyFrame  = 4,
  KS_CompressionCaps_CanBFrame    = 8,
  KS_CompressionCaps_CanWindow    = 0x10
} KS_CompressionCaps;
````

## Constants

<table>
            
                <tr>
                    <td>KS_CompressionCaps_CanQuality</td>
                    <td>The video compressor supports quality settings.</td>
                </tr>
            
                <tr>
                    <td>KS_CompressionCaps_CanCrunch</td>
                    <td>The video compressor can compress the video to a specified data rate. If a minidriver supports this capability, the <b>dwBitRate</b> member of the <a href="..\ksmedia\ns-ksmedia-tagks_videoinfoheader.md">KS_VIDEOINFOHEADER</a> structure specifies the default data rate.</td>
                </tr>
            
                <tr>
                    <td>KS_CompressionCaps_CanKeyFrame</td>
                    <td>The video compressor supports a user-specified key-frame rate.</td>
                </tr>
            
                <tr>
                    <td>KS_CompressionCaps_CanBFrame</td>
                    <td>The video compressor supports a user-specified P frame interval. The frames that occur between the key frames and P frames are bidirectional (B) frames.</td>
                </tr>
            
                <tr>
                    <td>KS_CompressionCaps_CanWindow</td>
                    <td>The video compressor supports a user-specified window size (that is, the number of frames whose average size cannot exceed the specified data rate).</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ksmedia.h (include Ksmedia.h) |

## See Also

<a href="..\ksmedia\ns-ksmedia-tagks_videoinfoheader.md">KS_VIDEOINFOHEADER</a>



<a href="..\ksmedia\ns-ksmedia-ksproperty_videocompression_getinfo_s.md">KSPROPERTY_VIDEOCOMPRESSION_GETINFO_S</a>