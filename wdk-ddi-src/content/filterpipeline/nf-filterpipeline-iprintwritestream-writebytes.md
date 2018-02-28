---
UID: NF:filterpipeline.IPrintWriteStream.WriteBytes
title: IPrintWriteStream::WriteBytes method
author: windows-driver-content
description: The WriteBytes method writes a specified number of bytes to a stream.
old-location: print\iprintwritestream_writebytes.htm
old-project: print
ms.assetid: d47c836e-a291-4cc2-9688-82526f8bfb8b
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IPrintWriteStream, IPrintWriteStream interface [Print Devices], WriteBytes method, IPrintWriteStream::WriteBytes, WriteBytes method [Print Devices], WriteBytes method [Print Devices], IPrintWriteStream interface, WriteBytes,IPrintWriteStream.WriteBytes, filterpipeline/IPrintWriteStream::WriteBytes, filterpipeline_168a03b1-8fdc-4a98-9a5f-5c706fcd401b.xml, print.iprintwritestream_writebytes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: filterpipeline.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: Filterpipeline.idl
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
-	IPrintWriteStream.WriteBytes
product: Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---


# WriteBytes method
The <code>WriteBytes</code> method writes a specified number of bytes to a stream.

## Syntax

````
HRESULT WriteBytes(
  [in]  void  pvBuffer,
  [in]  ULONG cbBuffer,
  [out] ULONG *pcbWritten
);
````

## Parameters

`pvBuffer`

A pointer to the buffer that the bytes will be written from.

`cbBuffer`

The size of the buffer to be read from.

`pcbWritten`

A pointer to the number of bytes actually written.


## Return Value

<code>WriteBytes</code> returns an <b>HRESULT</b> value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | filterpipeline.h |
| **Library** | filterpipeline.h |