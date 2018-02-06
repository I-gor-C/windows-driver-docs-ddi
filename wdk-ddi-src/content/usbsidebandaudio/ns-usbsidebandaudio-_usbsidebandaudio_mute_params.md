---
UID: NS:usbsidebandaudio._USBSIDEBANDAUDIO_MUTE_PARAMS
title: "_USBSIDEBANDAUDIO_MUTE_PARAMS"
author: windows-driver-content
description: TBD.
old-location: audio\usbsidebandaudio_mute_params.htm
old-project: audio
ms.assetid: 11FA1378-335A-402A-867C-F509D61153CA
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: usbsidebandaudio/PUSBSIDEBANDAUDIO_MUTE_PARAMS, audio.usbsidebandaudio_mute_params, USBSIDEBANDAUDIO_MUTE_PARAMS structure [Audio Devices], USBSIDEBANDAUDIO_MUTE_PARAMS, PUSBSIDEBANDAUDIO_MUTE_PARAMS structure pointer [Audio Devices], usbsidebandaudio/USBSIDEBANDAUDIO_MUTE_PARAMS, _USBSIDEBANDAUDIO_MUTE_PARAMS, *PUSBSIDEBANDAUDIO_MUTE_PARAMS, PUSBSIDEBANDAUDIO_MUTE_PARAMS
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
-	USBSIDEBANDAUDIO_MUTE_PARAMS
product: Windows
targetos: Windows
req.typenames: USBSIDEBANDAUDIO_MUTE_PARAMS, *PUSBSIDEBANDAUDIO_MUTE_PARAMS
req.product: Windows 10 or later.
---

# _USBSIDEBANDAUDIO_MUTE_PARAMS structure
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

TBD

## Syntax
````
typedef struct _USBSIDEBANDAUDIO_MUTE_PARAMS {
  ULONG Reserved 0;
  BOOL  Reserved 1;
  BOOL  Reserved 2;
} USBSIDEBANDAUDIO_MUTE_PARAMS, *PUSBSIDEBANDAUDIO_MUTE_PARAMS;
````

## Members


`EpIndex`



`Immediate`



`Value`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbsidebandaudio.h (include Usbsidebandaudio.h) |