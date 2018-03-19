---
UID: NS:ks.KSALLOCATOR_FRAMING
title: KSALLOCATOR_FRAMING
author: windows-driver-content
description: The KSALLOCATOR_FRAMING structure is used to query framing requirements and submit allocator creation requests.
old-location: stream\ksallocator_framing.htm
old-project: stream
ms.assetid: db96eccd-6747-458b-9a9e-ec909146f3fa
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PKSALLOCATOR_FRAMING, KSALLOCATOR_FRAMING, KSALLOCATOR_FRAMING structure [Streaming Media Devices], PKSALLOCATOR_FRAMING, PKSALLOCATOR_FRAMING structure pointer [Streaming Media Devices], ks-struct_cc2d8d16-75d5-4ef4-b8de-63197e61424b.xml, ks/KSALLOCATOR_FRAMING, ks/PKSALLOCATOR_FRAMING, stream.ksallocator_framing"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
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
-	ks.h
api_name:
-	KSALLOCATOR_FRAMING
product: Windows
targetos: Windows
req.typenames: KSALLOCATOR_FRAMING, *PKSALLOCATOR_FRAMING
---

# KSALLOCATOR_FRAMING structure
The KSALLOCATOR_FRAMING structure is used to query framing requirements and submit allocator creation requests.

## Syntax
````
typedef struct {
  union {
    ULONG OptionsFlags;
    ULONG RequirementsFlags;
  };
  ULONG PoolType;
  ULONG Frames;
  ULONG FrameSize;
  ULONG FileAlignment;
  ULONG Reserved;
} KSALLOCATOR_FRAMING, *PKSALLOCATOR_FRAMING;
````

## Members


`Frames`

Specifies the total number of allowable outstanding frames. Zero indicates that the filter has no requirement for this member.

`FrameSize`

Specifies the total size of the frame, including prefix and postfix. Zero indicates that the filter has no requirement for this member.

`Reserved`

Reserved for system use. Set to zero.

## Remarks
Use KSALLOCATOR_FRAMING to submit an allocator creation request to a handle of a sink by using IRP_MJ_CREATE.

When you specify a value for the <b>FileAlignment</b> member, the smallest allocation alignment is 1 byte (FILE_BYTE_ALIGNMENT). Software that functions as an allocation should support 4-byte alignment (FILE_LONG_ALIGNMENT), if possible.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="..\ks\nf-ks-kscreateallocator.md">KsCreateAllocator</a>