---
UID : NN:filterpipeline.IXpsDocumentProvider
title : IXpsDocumentProvider
author : windows-driver-content
description : The IxpsDocumentProvider interface provides interfaces to consume parts of a document.
old-location : print\ixpsdocumentprovider.htm
old-project : print
ms.assetid : e1fac90f-5c21-4857-a52f-04c5366d7b18
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
req.alt-api : IXpsDocumentProvider
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

# IXpsDocumentProvider interface

The <code>IxpsDocumentProvider</code> interface provides interfaces to consume parts of a document.

## Methods

<p>The <b>IXpsDocumentProvider</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [filterpipeline.IXpsDocumentProvider.GetXpsPart](nf-filterpipeline-ixpsdocumentprovider-getxpspart.md) | The GetXpsPart method retrieves several objects that make up an XPS document. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h (include Filterpipeline.h) |
| **DLL** |  |