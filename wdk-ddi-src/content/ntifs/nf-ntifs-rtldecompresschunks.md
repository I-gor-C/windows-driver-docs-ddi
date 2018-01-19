---
UID : NF:ntifs.RtlDecompressChunks
title : RtlDecompressChunks function
author : windows-driver-content
description : Reserved for system use.
old-location : ifsk\rtldecompresschunks.htm
old-project : ifsk
ms.assetid : 1bc13892-a7fb-43f9-8e65-70c11baca9ce
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : RtlDecompressChunks
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RtlDecompressChunks
req.alt-loc : ntifs.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : TOKEN_TYPE
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



`UncompressedBufferSize`



`CompressedBuffer`



`CompressedBufferSize`



`CompressedTail`



`CompressedTailSize`



`CompressedDataInfo`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |