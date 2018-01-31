---
UID : NF:filterpipeline.IPrintWriteStream.Close
title : IPrintWriteStream::Close method
author : windows-driver-content
description : The Close method closes a stream and ends the writing to that stream. This method is mandatory. You must call this method when the filter is done writing.
old-location : print\iprintwritestream_close.htm
old-project : print
ms.assetid : d3f828bf-854f-4d2d-a869-ee5c002a1728
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : Close method [Print Devices], Close, IPrintWriteStream::Close, IPrintWriteStream interface [Print Devices], Close method, filterpipeline/IPrintWriteStream::Close, print.iprintwritestream_close, IPrintWriteStream, Close method [Print Devices], IPrintWriteStream interface, filterpipeline_68b1e38f-f42a-4fa1-92f1-2181ac15033e.xml
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


# Close method
The <code>Close</code> method closes a stream and ends the writing to that stream. This method is mandatory. You must call this method when the filter is done writing.

## Syntax

````
void STDMETHODCALLTYPE Close(
    None
);
````

## Parameters

This function has no parameters.

## Return Value

None


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