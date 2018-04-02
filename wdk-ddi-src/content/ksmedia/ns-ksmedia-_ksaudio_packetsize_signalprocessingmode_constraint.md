---
UID: NS:ksmedia._KSAUDIO_PACKETSIZE_SIGNALPROCESSINGMODE_CONSTRAINT
title: "_KSAUDIO_PACKETSIZE_SIGNALPROCESSINGMODE_CONSTRAINT"
author: windows-driver-content
description: The KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT structure describes the constraints specific to any signal processing mode.
old-location: audio\ksaudio_packetsize_processingmode_constraint.htm
old-project: audio
ms.assetid: 0BC6A03C-CF6D-4F56-985E-933E87200DFE
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT, KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT structure [Audio Devices], _KSAUDIO_PACKETSIZE_SIGNALPROCESSINGMODE_CONSTRAINT, audio.ksaudio_packetsize_processingmode_constraint, ksmedia/KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
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
-	KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT
product:
- Windows
targetos: Windows
req.typenames: KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT
---

# _KSAUDIO_PACKETSIZE_SIGNALPROCESSINGMODE_CONSTRAINT structure
The <b>KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT</b> structure describes the constraints specific to any signal processing mode.

## Syntax
```
typedef struct _KSAUDIO_PACKETSIZE_SIGNALPROCESSINGMODE_CONSTRAINT {
  GUID  ProcessingMode;
  ULONG SamplesPerProcessingPacket;
  ULONG ProcessingPacketDurationInHns;
} KSAUDIO_PACKETSIZE_PROCESSINGMODE_CONSTRAINT;
```

## Members


`ProcessingMode`

The signal processing mode that this constraint applies to.

`SamplesPerProcessingPacket`

The processing frame size for the processing mode, expressed in number of samples. If this value is 0, the constraint is expressed by the <b>ProcessingPacketDurationInHns</b> field.

`ProcessingPacketDurationInHns`

The processing frame size for the processing mode, expressed in hundred-nanosecond (HNS) units. This field is ignored if <b>SamplesPerProcessingPacket</b> is nonzero.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows 10 |
| **Header** | ksmedia.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn965561">KSAUDIO_PACKETSIZE_CONSTRAINTS</a>