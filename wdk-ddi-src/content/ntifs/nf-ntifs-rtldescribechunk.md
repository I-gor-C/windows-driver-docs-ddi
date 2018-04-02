---
UID: NF:ntifs.RtlDescribeChunk
title: RtlDescribeChunk function
author: windows-driver-content
description: Reserved for system use.
old-location: ifsk\rtldescribechunk.htm
old-project: ifsk
ms.assetid: a59899e7-baa0-476b-b65e-1d464a14b811
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: RtlDescribeChunk, RtlDescribeChunk function [Installable File System Drivers], ifsk.rtldescribechunk, ntifs/RtlDescribeChunk, rtlref_03ffe48d-5d72-4f8b-ac88-e79909151d2f.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
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
-	ntifs.h
api_name:
-	RtlDescribeChunk
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# RtlDescribeChunk function
The <b>RtlDescribeChunk</b> routine is reserved for system use.

## Syntax

```
NTSYSAPI NTSTATUS RtlDescribeChunk(
  USHORT CompressionFormat,
  PUCHAR *CompressedBuffer,
  PUCHAR EndOfCompressedBufferPlus1,
  PUCHAR *ChunkBuffer,
  PULONG ChunkSize
);
```

## Parameters

`CompressionFormat`

TBD

`CompressedBuffer`

TBD

`EndOfCompressedBufferPlus1`

TBD

`ChunkBuffer`

TBD

`ChunkSize`

TBD


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ntifs.h (include Ntifs.h) |