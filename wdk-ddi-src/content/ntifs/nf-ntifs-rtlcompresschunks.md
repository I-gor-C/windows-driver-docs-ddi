---
UID : NF:ntifs.RtlCompressChunks
title : RtlCompressChunks function
author : windows-driver-content
description : Reserved for system use.
old-location : ifsk\rtlcompresschunks.htm
old-project : ifsk
ms.assetid : d67ad000-0f9e-4b08-a5d7-04743a3a3007
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : RtlCompressChunks
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
req.alt-api : RtlCompressChunks
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


# RtlCompressChunks function
The <b>RtlCompressChunks</b> routine is reserved for system use.

## Syntax

````
  RtlCompressChunks(
    
);
````

## Parameters

`UncompressedBuffer`



`UncompressedBufferSize`



`CompressedBuffer`



`CompressedBufferSize`



`CompressedDataInfo`



`CompressedDataInfoLength`



`WorkSpace`




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