---
UID : NN:filterpipeline.IPrintReadStreamFactory
title : IPrintReadStreamFactory
author : windows-driver-content
description : The IPrintReadStreamFactory interface creates a stream reader that a filter can use to access the stream. For example, a filter could use this stream to access the per-user print ticket.
old-location : print\iprintreadstreamfactory.htm
old-project : print
ms.assetid : 91f82cab-64c4-4f25-bf9a-b0757b1a83ca
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
req.alt-api : IPrintReadStreamFactory
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

# IPrintReadStreamFactory interface

The <code>IPrintReadStreamFactory</code> interface creates a stream reader that a filter can use to access the stream. For example, a filter could use this stream to access the per-user print ticket.

## Methods

<p>The <b>IPrintReadStreamFactory</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [filterpipeline.IPrintReadStreamFactory.GetStream](nf-filterpipeline-iprintreadstreamfactory-getstream.md) | The GetStream method gets the stream interface. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h (include Filterpipeline.h) |
| **DLL** |  |