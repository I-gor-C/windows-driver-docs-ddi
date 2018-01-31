---
UID : NS:ks.KS_COMPRESSION
title : KS_COMPRESSION
author : windows-driver-content
description : The KS_COMPRESSION structure defines the compression of frames on an output pin.
old-location : stream\ks_compression.htm
old-project : stream
ms.assetid : 065f51c3-f476-4f04-880a-5c42e493d458
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ks/KS_COMPRESSION, PKS_COMPRESSION structure pointer [Streaming Media Devices], stream.ks_compression, ks-struct_e554d828-61e3-45cd-8ddf-fe1c0b96e02d.xml, *PKS_COMPRESSION, KS_COMPRESSION structure [Streaming Media Devices], KS_COMPRESSION, PKS_COMPRESSION, ks/PKS_COMPRESSION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ks.h
req.include-header : Ks.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PKS_COMPRESSION, KS_COMPRESSION"
---

# KS_COMPRESSION structure
The KS_COMPRESSION structure defines the compression of frames on an output pin.

## Syntax
````
typedef struct {
  ULONG RatioNumerator;
  ULONG RatioDenominator;
  ULONG RatioConstantMargin;
} KS_COMPRESSION, *PKS_COMPRESSION;
````

## Members


`RatioConstantMargin`

Specifies a scalar constant to apply to the compression ratio. Set this to zero for no compression.

`RatioDenominator`

Specifies the denominator of the compression/expansion ratio.

`RatioNumerator`

Specifies the numerator of the compression/expansion ratio.

## Remarks
For compression, specify a fraction less than 1. For decompression, specify a fraction greater than 1. For example, a compressor might specify 1:3. A decompressor could specify 3:1.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |