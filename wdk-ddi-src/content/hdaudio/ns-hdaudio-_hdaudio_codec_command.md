---
UID: NS:hdaudio._HDAUDIO_CODEC_COMMAND
title: "_HDAUDIO_CODEC_COMMAND"
author: windows-driver-content
description: The HDAUDIO_CODEC_COMMAND structure specifies a codec command.
old-location: audio\hdaudio_codec_command.htm
old-project: audio
ms.assetid: 803e3506-fb63-4d64-b562-1956e99f9d9b
ms.author: windowsdriverdev
ms.date: 3/19/2018
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
product:
- Windows
targetos: Windows
req.typenames: HDAUDIO_CODEC_COMMAND, *PHDAUDIO_CODEC_COMMAND
---

# _HDAUDIO_CODEC_COMMAND structure
The HDAUDIO_CODEC_COMMAND structure specifies a codec command.

## Syntax
```
typedef struct _HDAUDIO_CODEC_COMMAND {
  union {
    ULONG Command;
    struct {
      ULONG  : 8  Data;
      ULONG  : 12 VerbId;
      ULONG  : 8  Node;
      ULONG  : 4  CodecAddress;
    } Verb8;
    struct {
      ULONG  : 16 Data;
      ULONG  : 4  VerbId;
      ULONG  : 8  Node;
      ULONG  : 4  CodecAddress;
    } Verb16;
  };
} *PHDAUDIO_CODEC_COMMAND, HDAUDIO_CODEC_COMMAND;
```

## Members


## Remarks
Clients call the <a href="https://msdn.microsoft.com/0ba92f5c-c4a3-48de-b8af-9c444b2e65b5">TransferCodecVerbs</a> routine to pass commands to codecs. The commands are in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536424">HDAUDIO_CODEC_TRANSFER</a> structures that clients pass to this routine as call parameters. Before calling <b>TransferCodecVerbs</b>, function drivers can use the HDAUDIO_CODEC_COMMAND structure to encode the codec commands.

The validity of individual members depends on the type of command sent.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | hdaudio.h (include Hdaudio.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff536424">HDAUDIO_CODEC_TRANSFER</a>



<a href="https://msdn.microsoft.com/0ba92f5c-c4a3-48de-b8af-9c444b2e65b5">TransferCodecVerbs</a>