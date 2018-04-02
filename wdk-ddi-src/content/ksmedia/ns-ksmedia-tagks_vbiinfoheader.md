---
UID: NS:ksmedia.tagKS_VBIINFOHEADER
title: tagKS_VBIINFOHEADER
author: windows-driver-content
description: The KS_VBIINFOHEADER structure describes raw vertical blanking interval (VBI) streams.
old-location: stream\ks_vbiinfoheader.htm
old-project: stream
ms.assetid: 4424be3a-6e73-449c-b5fb-5cbc1109490d
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PKS_VBIINFOHEADER, KS_VBIINFOHEADER, KS_VBIINFOHEADER structure [Streaming Media Devices], PKS_VBIINFOHEADER, PKS_VBIINFOHEADER structure pointer [Streaming Media Devices], ksmedia/KS_VBIINFOHEADER, ksmedia/PKS_VBIINFOHEADER, stream.ks_vbiinfoheader, tagKS_VBIINFOHEADER, vidcapstruct_2a637c59-2852-4b59-9d92-f51c9892df85.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
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
-	KS_VBIINFOHEADER
product:
- Windows
targetos: Windows
req.typenames: KS_VBIINFOHEADER, *PKS_VBIINFOHEADER
---

# tagKS_VBIINFOHEADER structure
The KS_VBIINFOHEADER structure describes raw vertical blanking interval (VBI) streams.

## Syntax
```
typedef struct tagKS_VBIINFOHEADER {
  ULONG StartLine;
  ULONG EndLine;
  ULONG SamplingFrequency;
  ULONG MinLineStartTime;
  ULONG MaxLineStartTime;
  ULONG ActualLineStartTime;
  ULONG ActualLineEndTime;
  ULONG VideoStandard;
  ULONG SamplesPerLine;
  ULONG StrideInBytes;
  ULONG BufferSize;
} KS_VBIINFOHEADER, *PKS_VBIINFOHEADER;
```

## Members


`StartLine`

Specifies the line number of the first digitized VBI line.

`EndLine`

Specifies the line number of the last digitized VBI line.

`SamplingFrequency`

Specifies the sampling frequency in hertz (Hz).

`MinLineStartTime`

Specifies the shortest possible interval from the leading edge of H-sync in 10-nanosecond units (that is, in hundredths of microseconds).

`MaxLineStartTime`

Specifies the longest possible interval from the leading edge of H-sync in 10-nanosecond units (that is, in hundredths of microseconds).

`ActualLineStartTime`

Specifies the actual starting point of VBI digitization from the leading edge of H-sync in 10-nanosecond units (that is, in hundredths of microseconds).

`ActualLineEndTime`

Specifies the actual ending point for VBI digitization from the leading edge of H-sync in 10-nanosecond units (that is, in hundredths of microseconds).

`VideoStandard`

Specifies one or more (logically ORed) values from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567297">KS_AnalogVideoStandard</a> enumeration.

`SamplesPerLine`

Specifies the number of samples digitized per video line.

`StrideInBytes`

Specifies the stride in bytes between the first sample on a given line and the first sample on the next line. This value can be larger than <b>SamplesPerLine</b>.

`BufferSize`

Specifies the size in bytes of the buffer to store the entire digitized VBI signal.

## Remarks
VBI streams are usually converted to NABTS, CC, and WST streams by downstream filters.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ksmedia.h (include Ksmedia.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff567297">KS_AnalogVideoStandard</a>