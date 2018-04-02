---
UID: NE:ksmedia.KS_VideoControlFlags
title: KS_VideoControlFlags
author: windows-driver-content
description: The KS_VideoControlFlags enumeration defines video control capabilities for a specific stream.
old-location: stream\ks_videocontrolflags.htm
old-project: stream
ms.assetid: 7f8b3727-132c-41c8-a252-0f9c8812002f
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: KS_Obsolete_VideoControlFlag_ExternalTriggerEnable, KS_Obsolete_VideoControlFlag_Trigger, KS_VideoControlFlag_ExternalTriggerEnable, KS_VideoControlFlag_FlipHorizontal, KS_VideoControlFlag_FlipVertical, KS_VideoControlFlag_IndependentImagePin, KS_VideoControlFlag_StartPhotoSequenceCapture, KS_VideoControlFlag_StillCapturePreviewFrame, KS_VideoControlFlag_StopPhotoSequenceCapture, KS_VideoControlFlag_Trigger, KS_VideoControlFlags, KS_VideoControlFlags enumeration [Streaming Media Devices], ksmedia/KS_Obsolete_VideoControlFlag_ExternalTriggerEnable, ksmedia/KS_Obsolete_VideoControlFlag_Trigger, ksmedia/KS_VideoControlFlag_ExternalTriggerEnable, ksmedia/KS_VideoControlFlag_FlipHorizontal, ksmedia/KS_VideoControlFlag_FlipVertical, ksmedia/KS_VideoControlFlag_IndependentImagePin, ksmedia/KS_VideoControlFlag_StartPhotoSequenceCapture, ksmedia/KS_VideoControlFlag_StillCapturePreviewFrame, ksmedia/KS_VideoControlFlag_StopPhotoSequenceCapture, ksmedia/KS_VideoControlFlag_Trigger, ksmedia/KS_VideoControlFlags, stream.ks_videocontrolflags, vidcapstruct_ae01591c-4ee4-4e70-bfc2-c78ad73a296f.xml
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
-	KS_VideoControlFlags
product: Windows
targetos: Windows
req.typenames: KS_VideoControlFlags
---

# KS_VideoControlFlags Enumeration
The KS_VideoControlFlags enumeration defines video control capabilities for a specific stream.

## Syntax
```
typedef enum KS_VideoControlFlags {
  KS_VideoControlFlag_FlipHorizontal                  ,
  KS_VideoControlFlag_FlipVertical                    ,
  KS_Obsolete_VideoControlFlag_ExternalTriggerEnable  ,
  KS_Obsolete_VideoControlFlag_Trigger                ,
  KS_VideoControlFlag_ExternalTriggerEnable           ,
  KS_VideoControlFlag_Trigger                         ,
  KS_VideoControlFlag_IndependentImagePin             ,
  KS_VideoControlFlag_StillCapturePreviewFrame        ,
  KS_VideoControlFlag_StartPhotoSequenceCapture       ,
  KS_VideoControlFlag_StopPhotoSequenceCapture
} ;
```

## Constants

<table>
            
                <tr>
                    <td>KS_VideoControlFlag_FlipHorizontal</td>
                    <td>The minidriver is capable of flipping the image horizontally.</td>
                </tr>
            
                <tr>
                    <td>KS_VideoControlFlag_FlipVertical</td>
                    <td>The minidriver is capable of flipping the image vertically.</td>
                </tr>
            
                <tr>
                    <td>KS_Obsolete_VideoControlFlag_ExternalTriggerEnable</td>
                    <td>This value is obsolete. Do not use.</td>
                </tr>
            
                <tr>
                    <td>KS_Obsolete_VideoControlFlag_Trigger</td>
                    <td>This value is obsolete. Do not use.</td>
                </tr>
            
                <tr>
                    <td>KS_VideoControlFlag_ExternalTriggerEnable</td>
                    <td>The minidriver can enable acquisition of a single video frame based on an external trigger. An external trigger typically is hardware-specific.</td>
                </tr>
            
                <tr>
                    <td>KS_VideoControlFlag_Trigger</td>
                    <td>The minidriver can enable acquisition of a single video frame based on a programmatic trigger.</td>
                </tr>
            
                <tr>
                    <td>KS_VideoControlFlag_IndependentImagePin</td>
                    <td>Determines if the image pin is independent of the video pin.

Supported starting with Windows 8.</td>
                </tr>
            
                <tr>
                    <td>KS_VideoControlFlag_StillCapturePreviewFrame</td>
                    <td>Reserved for system use. Do not use in your driver.

Supported starting with Windows 8.</td>
                </tr>
            
                <tr>
                    <td>KS_VideoControlFlag_StartPhotoSequenceCapture</td>
                    <td>Begin photo sequence capture operation.

Supported starting with Windows 8.1.</td>
                </tr>
            
                <tr>
                    <td>KS_VideoControlFlag_StopPhotoSequenceCapture</td>
                    <td>Stop photo sequence operation.

Supported starting with Windows 8.1.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ksmedia.h (include Ksmedia.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff566036">KSPROPERTY_VIDEOCONTROL_CAPS_S</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566043">KSPROPERTY_VIDEOCONTROL_MODE_S</a>