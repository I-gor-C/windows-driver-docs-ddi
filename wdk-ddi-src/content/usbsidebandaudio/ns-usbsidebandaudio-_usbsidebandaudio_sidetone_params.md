---
UID: NS:usbsidebandaudio._USBSIDEBANDAUDIO_SIDETONE_PARAMS
title: "_USBSIDEBANDAUDIO_SIDETONE_PARAMS"
author: windows-driver-content
description: TBD.
old-location: audio\usbsidebandaudio_sidetone_params.htm
old-project: audio
ms.assetid: FE97B772-CD08-4F76-88DA-05F24881D062
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: usbsidebandaudio/USBSIDEBANDAUDIO_SIDETONE_PARAMS, _USBSIDEBANDAUDIO_SIDETONE_PARAMS, PUSBSIDEBANDAUDIO_SIDETONE_PARAMS, USBSIDEBANDAUDIO_SIDETONE_PARAMS structure [Audio Devices], usbsidebandaudio/PUSBSIDEBANDAUDIO_SIDETONE_PARAMS, PUSBSIDEBANDAUDIO_SIDETONE_PARAMS structure pointer [Audio Devices], USBSIDEBANDAUDIO_SIDETONE_PARAMS, *PUSBSIDEBANDAUDIO_SIDETONE_PARAMS, audio.usbsidebandaudio_sidetone_params
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbsidebandaudio.h
req.include-header: Usbsidebandaudio.h
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
topictype:
-	kbSyntax
apitype:
-	<TBD>
apilocation:
-
apiname:
-	USBSIDEBANDAUDIO_SIDETONE_PARAMS
product: Windows
targetos: Windows
req.typenames: USBSIDEBANDAUDIO_SIDETONE_PARAMS, *PUSBSIDEBANDAUDIO_SIDETONE_PARAMS
req.product: Windows 10 or later.
---

# _USBSIDEBANDAUDIO_SIDETONE_PARAMS structure
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

TBD

## Syntax
````
typedef struct _USBSIDEBANDAUDIO_SIDETONE_PARAMS {
  ULONG Reserved 0;
  BOOL  Reserved 1;
} USBSIDEBANDAUDIO_SIDETONE_PARAMS, *PUSBSIDEBANDAUDIO_SIDETONE_PARAMS;
````

## Members


`EpIndex`



`Immediate`



`Sidetone`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbsidebandaudio.h (include Usbsidebandaudio.h) |