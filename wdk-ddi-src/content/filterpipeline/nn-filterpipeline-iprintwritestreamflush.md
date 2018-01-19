---
UID : NN:filterpipeline.IPrintWriteStreamFlush
title : IPrintWriteStreamFlush
author : windows-driver-content
description : Filters use the IPrintWriteStreamFlush interface to explicitly flush data as a raw stream of bytes from a filter. This interface is retrieved through IPrintWriteStream::QueryInterface().
old-location : print\iprintwritestreamflush.htm
old-project : print
ms.assetid : DB3E1127-B3B1-4C48-9819-EEF705B9985A
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
req.alt-api : IPrintWriteStreamFlush
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

# IPrintWriteStreamFlush interface

Filters use the IPrintWriteStreamFlush interface to explicitly flush data as a raw stream of bytes from a filter.  This interface is retrieved through IPrintWriteStream::QueryInterface().

## Methods

<p>The <b>IPrintWriteStreamFlush</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [filterpipeline.IPrintWriteStreamFlush.FlushData](nf-filterpipeline-iprintwritestreamflush-flushdata.md) | The FlushData method flushes buffered data to a data stream while leaving the stream open, allowing the caller to write additional data to the stream. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h (include Filterpipeline.h) |
| **DLL** |  |