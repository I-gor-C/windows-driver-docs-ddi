---
UID : NF:filterpipeline.IPrintReadStream.ReadBytes
title : IPrintReadStream::ReadBytes method
author : windows-driver-content
description : The ReadBytes method reads a number of bytes into a buffer.
old-location : print\iprintreadstream_readbytes.htm
old-project : print
ms.assetid : 41ba600d-8b89-4e07-950a-a2518c2572a6
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ReadBytes method [Print Devices], IPrintReadStream interface, IPrintReadStream interface [Print Devices], ReadBytes method, filterpipeline_92cb33c3-6229-47ca-b3da-2f4c268f8b7b.xml, ReadBytes method [Print Devices], print.iprintreadstream_readbytes, IPrintReadStream, IPrintReadStream::ReadBytes, ReadBytes, filterpipeline/IPrintReadStream::ReadBytes
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : filterpipeline.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : Filterpipeline.idl
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


# ReadBytes method
The <code>ReadBytes</code> method reads a number of bytes into a buffer.

## Syntax

````
HRESULT ReadBytes(
  [out] void  *pvBuffer,
  [in]  ULONG cbRequested,
  [out] ULONG *pcbRead,
  [out] BOOL  *pbEndOfFile
);
````

## Parameters

`pvBuffer`

A pointer to the buffer that the bytes will be read into..

`cbRequested`

The number of bytes that are requested for the read.

`pcbRead`

A pointer to the number of bytes actually read.

`pbEndOfFile`

A pointer to a <b>BOOL</b> value that indicates whether the end of file (EOF) was read.


## Return Value

<code>ReadBytes</code> returns an <b>HRESULT</b> value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |