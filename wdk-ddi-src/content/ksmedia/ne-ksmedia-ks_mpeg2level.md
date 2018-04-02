---
UID: NE:ksmedia.KS_MPEG2Level
title: KS_MPEG2Level
author: windows-driver-content
description: The KS_MPEG2Level enumeration describes MPEG-2 levels.
old-location: stream\ks_mpeg2level.htm
old-project: stream
ms.assetid: 5ba271ba-ed92-402e-9ef9-ac198a8ea510
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KS_MPEG2Level, KS_MPEG2Level enumeration [Streaming Media Devices], KS_MPEG2Level_High, KS_MPEG2Level_High1440, KS_MPEG2Level_Low, KS_MPEG2Level_Main, ksmedia/KS_MPEG2Level, ksmedia/KS_MPEG2Level_High, ksmedia/KS_MPEG2Level_High1440, ksmedia/KS_MPEG2Level_Low, ksmedia/KS_MPEG2Level_Main, stream.ks_mpeg2level, vidcapstruct_a97daeef-93e4-4ded-98dc-f583c1893095.xml
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
-	KS_MPEG2Level
product:
- Windows
targetos: Windows
req.typenames: KS_MPEG2Level
---

# KS_MPEG2Level Enumeration
The KS_MPEG2Level enumeration describes MPEG-2 levels.

## Syntax
```
typedef enum KS_MPEG2Level {
  KS_MPEG2Level_Low       ,
  KS_MPEG2Level_Main      ,
  KS_MPEG2Level_High1440  ,
  KS_MPEG2Level_High
} ;
```

## Constants

<table>
            
                <tr>
                    <td>KS_MPEG2Level_Low</td>
                    <td>Specifies the low MPEG-2 resolution, or 352 × 240 at 30 frames per second.</td>
                </tr>
            
                <tr>
                    <td>KS_MPEG2Level_Main</td>
                    <td>Specifies the main MPEG-2 resolution, or 720 × 480 at 30 frames per second.</td>
                </tr>
            
                <tr>
                    <td>KS_MPEG2Level_High1440</td>
                    <td>Specifies the high-1440 MPEG-2 resolution, or 1440 × 1152 at 30 frames per second.</td>
                </tr>
            
                <tr>
                    <td>KS_MPEG2Level_High</td>
                    <td>Specifies the high MPEG-2 resolution, or 1920 × 1080 at 30 frames per second.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ksmedia.h (include Ksmedia.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff567667">KS_MPEGVIDEOINFO2</a>