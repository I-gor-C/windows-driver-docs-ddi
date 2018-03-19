---
UID: NS:hdaudio._HDAUDIO_CODEC_COMMAND
title: "_HDAUDIO_CODEC_COMMAND"
author: windows-driver-content
description: The HDAUDIO_CODEC_COMMAND structure specifies a codec command.
old-location: audio\hdaudio_codec_command.htm
old-project: audio
ms.assetid: 803e3506-fb63-4d64-b562-1956e99f9d9b
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: "*PHDAUDIO_CODEC_COMMAND, HDAUDIO_CODEC_COMMAND, HDAUDIO_CODEC_COMMAND structure [Audio Devices], PHDAUDIO_CODEC_COMMAND, PHDAUDIO_CODEC_COMMAND structure pointer [Audio Devices], _HDAUDIO_CODEC_COMMAND, aud-prop2_9e7db610-d310-4285-8556-7a88567c22b6.xml, audio.hdaudio_codec_command, hdaudio/HDAUDIO_CODEC_COMMAND, hdaudio/PHDAUDIO_CODEC_COMMAND"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hdaudio.h
req.include-header: Hdaudio.h
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
req.irql: PASSIVE_LEVEL.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	hdaudio.h
api_name:
-	HDAUDIO_CODEC_COMMAND
product: Windows
targetos: Windows
req.typenames: HDAUDIO_CODEC_COMMAND, *PHDAUDIO_CODEC_COMMAND
---

# _HDAUDIO_CODEC_COMMAND structure
The HDAUDIO_CODEC_COMMAND structure specifies a codec command.

## Syntax
````
typedef struct _HDAUDIO_CODEC_COMMAND {
  union {
    struct {
      ULONG Data  :8;
      ULONG VerbId  :12;
      ULONG Node  :8;
      ULONG CodecAddress  :4;
    } Verb8;
    struct {
      ULONG Data  :16;
      ULONG VerbId  :4;
      ULONG Node  :8;
      ULONG CodecAddress  :4;
    } Verb16;
    ULONG  Command;
  };
} HDAUDIO_CODEC_COMMAND, *PHDAUDIO_CODEC_COMMAND;
````

## Members


## Remarks
Clients call the <a href="..\hdaudio\nc-hdaudio-ptransfer_codec_verbs.md">TransferCodecVerbs</a> routine to pass commands to codecs. The commands are in the <a href="..\hdaudio\ns-hdaudio-_hdaudio_codec_transfer.md">HDAUDIO_CODEC_TRANSFER</a> structures that clients pass to this routine as call parameters. Before calling <b>TransferCodecVerbs</b>, function drivers can use the HDAUDIO_CODEC_COMMAND structure to encode the codec commands.

The validity of individual members depends on the type of command sent.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | hdaudio.h (include Hdaudio.h) |

## See Also

<a href="..\hdaudio\ns-hdaudio-_hdaudio_codec_transfer.md">HDAUDIO_CODEC_TRANSFER</a>



<a href="..\hdaudio\nc-hdaudio-ptransfer_codec_verbs.md">TransferCodecVerbs</a>