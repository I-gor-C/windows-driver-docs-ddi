---
UID: NN:filterpipeline.IPrintReadStream
title: IPrintReadStream
author: windows-driver-content
description: Filters use the IPrintReadStream interface to read data as a raw stream of bytes.
old-location: print\iprintreadstream.htm
old-project: print
ms.assetid: f31a6547-44ec-4331-8f9b-e46192f4966a
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintReadStream, IPrintReadStream interface [Print Devices], IPrintReadStream interface [Print Devices], described, filterpipeline/IPrintReadStream, filterpipeline_51454792-ccd6-4c55-adbc-d5cc1536f93c.xml, print.iprintreadstream
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
-	IPrintReadStream
product: Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---

# IPrintReadStream interface

Filters use the <code>IPrintReadStream</code> interface to read data as a raw stream of bytes.

## Methods

<p>The <b>IPrintReadStream</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintReadStream::ReadBytes](nf-filterpipeline-iprintreadstream-readbytes.md) | The ReadBytes method reads a number of bytes into a buffer. |
| [IPrintReadStream::Seek](nf-filterpipeline-iprintreadstream-seek.md) | The Seek method changes the seek pointer to a new location in the stream. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | filterpipeline.h (include Filterpipeline.h) |