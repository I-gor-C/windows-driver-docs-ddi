---
UID : NN:filterpipeline.IXpsPartIterator
title : IXpsPartIterator
author : windows-driver-content
description : The IXpsPartIterator interface is an iterator for XPS parts.
old-location : print\ixpspartiterator.htm
old-project : print
ms.assetid : 6fd51647-e7e4-4c9a-ae87-00eb3e1d3fbb
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : print.ixpspartiterator, IXpsPartIterator interface [Print Devices], IXpsPartIterator interface [Print Devices], described, IXpsPartIterator, filterpipeline/IXpsPartIterator, filterpipeline_75476300-7fcc-46a5-8a48-abde1dcd5e36.xml
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
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : filterpipeline.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : EXpsFontRestriction
---

# IXpsPartIterator interface

The <code>IXpsPartIterator</code> interface is an iterator for XPS parts.

## Methods

<p>The <b>IXpsPartIterator</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [filterpipeline.IXpsPartIterator.Current](nf-filterpipeline-ixpspartiterator-current.md) | The Current method provides the current URI and part. |
| [filterpipeline.IXpsPartIterator.IsDone](nf-filterpipeline-ixpspartiterator-isdone.md) | The IsDone method determines whether the iterator has finished the iteration. |
| [filterpipeline.IXpsPartIterator.Next](nf-filterpipeline-ixpspartiterator-next.md) | The Next method advances the iterator to the next part. |
| [filterpipeline.IXpsPartIterator.Reset](nf-filterpipeline-ixpspartiterator-reset.md) | The Reset method sets the iterator to the first element. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | filterpipeline.h (include Filterpipeline.h) |