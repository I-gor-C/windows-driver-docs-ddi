---
UID: NN:filterpipeline.IPrintWriteStream
title: IPrintWriteStream
author: windows-driver-content
description: Filters use the IPrintWriteStream interface to write data as a raw stream of bytes.
old-location: print\iprintwritestream.htm
old-project: print
ms.assetid: b76a58fb-fbd4-4afe-83dc-582242b53e05
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintWriteStream, IPrintWriteStream interface [Print Devices], IPrintWriteStream interface [Print Devices], described, filterpipeline/IPrintWriteStream, filterpipeline_edf6ac16-09e1-433a-8f41-50ba308dc7a7.xml, print.iprintwritestream
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
-	IPrintWriteStream
product: Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---

# IPrintWriteStream interface

Filters use the <code>IPrintWriteStream</code> interface to write data as a raw stream of bytes.

## Methods

<p>The <b>IPrintWriteStream</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintWriteStream::Close](nf-filterpipeline-iprintwritestream-close.md) | The Close method closes a stream and ends the writing to that stream. This method is mandatory. You must call this method when the filter is done writing. |
| [IPrintWriteStream::WriteBytes](nf-filterpipeline-iprintwritestream-writebytes.md) | The WriteBytes method writes a specified number of bytes to a stream. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | filterpipeline.h (include Filterpipeline.h) |