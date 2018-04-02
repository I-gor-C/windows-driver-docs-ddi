---
UID: NS:usbsidebandaudio._USBSIDEBANDAUDIO_EP_SHADOW_RESOURCES
title: "_USBSIDEBANDAUDIO_EP_SHADOW_RESOURCES"
author: windows-driver-content
description: TBD.
old-location: audio\usbsidebandaudio_ep_shadow_resources.htm
old-project: audio
ms.assetid: 56159F97-82CD-4F0A-ADF0-228E876A0266
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: "*PUSBSIDEBANDAUDIO_EP_SHADOW_RESOURCES, PUSBSIDEBANDAUDIO_EP_SHADOW_RESOURCES, PUSBSIDEBANDAUDIO_EP_SHADOW_RESOURCES structure pointer [Audio Devices], USBSIDEBANDAUDIO_EP_SHADOW_RESOURCES, USBSIDEBANDAUDIO_EP_SHADOW_RESOURCES structure [Audio Devices], _USBSIDEBANDAUDIO_EP_SHADOW_RESOURCES, audio.usbsidebandaudio_ep_shadow_resources, usbsidebandaudio/PUSBSIDEBANDAUDIO_EP_SHADOW_RESOURCES, usbsidebandaudio/USBSIDEBANDAUDIO_EP_SHADOW_RESOURCES"
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
topic_type:
-	kbSyntax
api_type:
-	<TBD>
api_location:
-
api_name:
-	USBSIDEBANDAUDIO_EP_SHADOW_RESOURCES
product:
- Windows
targetos: Windows
req.typenames: USBSIDEBANDAUDIO_EP_SHADOW_RESOURCES, *PUSBSIDEBANDAUDIO_EP_SHADOW_RESOURCES
req.product: Windows 10 or later.
---

# _USBSIDEBANDAUDIO_EP_SHADOW_RESOURCES structure
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

TBD

## Syntax
```
typedef struct _USBSIDEBANDAUDIO_EP_SHADOW_RESOURCES {
  ULONG                                          CbSize;
  ULONG                                          CbDataSize;
  PUSBSIDEBANDAUDIO_EP_SHADOW_RESOURCES_FUNCTION pEpFunctionResources;
  LONGLONG                                       ShadowResourceBlob;
} *PUSBSIDEBANDAUDIO_EP_SHADOW_RESOURCES, USBSIDEBANDAUDIO_EP_SHADOW_RESOURCES;
```

## Members


`CbSize`



`CbDataSize`



`pEpFunctionResources`



`ShadowResourceBlob`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbsidebandaudio.h (include Usbsidebandaudio.h) |