---
UID : NN:filterpipeline.IPrintReadStream
title : IPrintReadStream
author : windows-driver-content
description : Filters use the IPrintReadStream interface to read data as a raw stream of bytes.
old-location : print\iprintreadstream.htm
old-project : print
ms.assetid : f31a6547-44ec-4331-8f9b-e46192f4966a
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : IXpsPartIterator, IXpsPartIterator::Reset, Reset
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : filterpipeline.h
req.include-header : Filterpipeline.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IPrintReadStream
req.alt-loc : filterpipeline.h
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
req.typenames : EXpsFontRestriction
---

# IPrintReadStream interface

Filters use the <code>IPrintReadStream</code> interface to read data as a raw stream of bytes.

## Methods

<p>The <b>IPrintReadStream</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [filterpipeline.IPrintReadStream.ReadBytes](nf-filterpipeline-iprintreadstream-readbytes.md) | The ReadBytes method reads a number of bytes into a buffer. |
| [filterpipeline.IPrintReadStream.Seek](nf-filterpipeline-iprintreadstream-seek.md) | The Seek method changes the seek pointer to a new location in the stream. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h (include Filterpipeline.h) |
| **DLL** |  |