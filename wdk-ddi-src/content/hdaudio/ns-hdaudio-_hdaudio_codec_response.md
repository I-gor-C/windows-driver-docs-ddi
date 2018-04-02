---
UID: NS:hdaudio._HDAUDIO_CODEC_RESPONSE
title: "_HDAUDIO_CODEC_RESPONSE"
author: windows-driver-content
description: The HDAUDIO_CODEC_RESPONSE structure specifies either a response to a codec command or an unsolicited response from a codec.
old-location: audio\hdaudio_codec_response.htm
old-project: audio
ms.assetid: 56b9cdb5-2734-45b5-aeaf-ae6d606d1a5c
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: "*PHDAUDIO_CODEC_RESPONSE, HDAUDIO_CODEC_RESPONSE, HDAUDIO_CODEC_RESPONSE structure [Audio Devices], PHDAUDIO_CODEC_RESPONSE, PHDAUDIO_CODEC_RESPONSE structure pointer [Audio Devices], _HDAUDIO_CODEC_RESPONSE, aud-prop2_2cf51d01-4493-439c-9a5f-30b86d76502b.xml, audio.hdaudio_codec_response, hdaudio/HDAUDIO_CODEC_RESPONSE, hdaudio/PHDAUDIO_CODEC_RESPONSE"
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
-	HDAUDIO_CODEC_RESPONSE
product: Windows
targetos: Windows
req.typenames: HDAUDIO_CODEC_RESPONSE, *PHDAUDIO_CODEC_RESPONSE
---

# _HDAUDIO_CODEC_RESPONSE structure
The HDAUDIO_CODEC_RESPONSE structure specifies either a response to a codec command or an unsolicited response from a codec.

## Syntax
```
typedef struct _HDAUDIO_CODEC_RESPONSE {
  union {
    struct {
      union {
        ULONG Response;
        struct {
          ULONG  : 21 Response;
          ULONG  : 5  SubTag;
          ULONG  : 6  Tag;
        } Unsolicited;
      };
      ULONG  : 4 SDataIn;
      ULONG  : 1 IsUnsolicitedResponse;
      ULONG  : 1 HasFifoOverrun;
      ULONG  : 1 IsValid;
    };
    ULONGLONG CompleteResponse;
  };
} HDAUDIO_CODEC_RESPONSE, *PHDAUDIO_CODEC_RESPONSE;
```

## Members


## Remarks
After calling the <a href="https://msdn.microsoft.com/0ba92f5c-c4a3-48de-b8af-9c444b2e65b5">TransferCodecVerbs</a> routine, function drivers can use the HDAUDIO_CODEC_RESPONSE structure to decode the responses to their codec commands. The commands are contained in the HDAUDIO_CODEC_TRANSFER structures that clients pass to this routine as call parameters.

The callback for the <a href="https://msdn.microsoft.com/0f94146b-aa60-4106-aba6-0f1cb3e53008">RegisterEventCallback</a> routine also uses the HDAUDIO_CODEC_RESPONSE structure.

Most members of this structure contain hardware-generated values that the bus driver copies directly from the corresponding RIRB entry. The two exceptions are the values of the <b>IsValid</b> and <b>HasFifoOverrun</b> members, which the bus driver software writes to the structure to indicate the error status of the response. For information about the RIRB entry format, see the Intel High Definition Audio Specification at the <a href="http://go.microsoft.com/fwlink/p/?linkid=42508">Intel HD Audio</a> website.

If <b>IsValid</b>=0, one of the following has occurred:

<ul>
<li>
If <b>HasFifoOverrun</b>=1, the RIRB FIFO overflowed.

</li>
<li>
If <b>HasFifoOverrun</b>=0, the codec failed to respond.

</li>
</ul>
The unnamed 25-bitfield between the <b>UnsolicitedResponse</b> and <b>HasFifoOverrun</b> members is reserved for future expansion. The HD Audio bus controller currently writes zeros to this field.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | hdaudio.h (include Hdaudio.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff536424">HDAUDIO_CODEC_TRANSFER</a>



<a href="https://msdn.microsoft.com/0f94146b-aa60-4106-aba6-0f1cb3e53008">RegisterEventCallback</a>



<a href="https://msdn.microsoft.com/0ba92f5c-c4a3-48de-b8af-9c444b2e65b5">TransferCodecVerbs</a>