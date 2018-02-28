---
UID: NF:ntifs.RtlDecompressChunks
title: RtlDecompressChunks function
author: windows-driver-content
description: Reserved for system use.
old-location: ifsk\rtldecompresschunks.htm
old-project: ifsk
ms.assetid: 1bc13892-a7fb-43f9-8e65-70c11baca9ce
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: RtlDecompressChunks, RtlDecompressChunks function [Installable File System Drivers], ifsk.rtldecompresschunks, ntifs/RtlDecompressChunks, rtlref_0fadf009-d363-4001-9981-7eb646be1a8b.xml
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
req.lib: NtosKrnl.exe
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
-	RtlDecompressChunks
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# RtlDecompressChunks function
The <b>RtlDecompressChunks</b> routine is reserved for system use.

## Syntax

````
  RtlDecompressChunks(
    
);
````

## Parameters

`UncompressedBuffer`

TBD

`UncompressedBufferSize`

TBD

`CompressedBuffer`

TBD

`CompressedBufferSize`

TBD

`CompressedTail`

TBD

`CompressedTailSize`

TBD

`CompressedDataInfo`

TBD


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** | NtosKrnl.exe |