---
UID: NN:filterpipeline.IFixedDocument
title: IFixedDocument
author: windows-driver-content
description: The IFixedDocument interface represents a fixed document for an XPS document sequence.
old-location: print\ifixeddocument.htm
old-project: print
ms.assetid: 3f9f64a1-8681-4b70-8cdc-7c944912f767
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IFixedDocument, IFixedDocument interface [Print Devices], IFixedDocument interface [Print Devices], described, filterpipeline/IFixedDocument, filterpipeline_f295da8e-1444-40c4-8ecf-e3aadc1d324f.xml, print.ifixeddocument
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: filterpipeline.h
req.include-header: Filterpipeline.h
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
req.lib: filterpipeline.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	filterpipeline.h
api_name:
-	IFixedDocument
product: Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---

# IFixedDocument interface

The <b>IFixedDocument</b> interface represents a fixed document for an XPS document sequence.  An XPS fixed document sequence will have one or more fixed documents in it.

## Methods

<p>The <b>IFixedDocument</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IFixedDocument::GetPrintTicket](nf-filterpipeline-ifixeddocument-getprintticket.md) | The GetPrintTicket method gets the print ticket object for the fixed document. |
| [IFixedDocument::GetUri](nf-filterpipeline-ifixeddocument-geturi.md) | The GetUri method gets the URI of the fixed document. |
| [IFixedDocument::SetPrintTicket](nf-filterpipeline-ifixeddocument-setprintticket.md) | The SetPrintTicket method inserts a print ticket into the fixed document. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | filterpipeline.h (include Filterpipeline.h) |