---
UID: NN:printerextension.IPrinterScriptableSequentialStream
title: IPrinterScriptableSequentialStream
author: windows-driver-content
description: The IPrinterScriptableSequentialStream interface is an ISequentialStream-like interface that works in JavaScript. Instead of reading and writing byte arrays, it reads and writes JavaScript arrays of bytes, which are values between 0 and 255.
old-location: print\iprinterscriptablesequentialstream_interface.htm
old-project: print
ms.assetid: 85DF7DCB-7AB1-4A46-AD70-6D47D9F98079
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrinterScriptableSequentialStream, IPrinterScriptableSequentialStream interface [Print Devices], IPrinterScriptableSequentialStream interface [Print Devices], described, print.iprinterscriptablesequentialstream_interface, printerextension/IPrinterScriptableSequentialStream
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: printerextension.h
req.include-header: 
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	printerextension.h
api_name:
-	IPrinterScriptableSequentialStream
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrinterScriptableSequentialStream interface

The IPrinterScriptableSequentialStream interface is an ISequentialStream-like interface that works in JavaScript. Instead of reading and writing byte arrays, it reads and writes JavaScript arrays of bytes, which are values between 0 and 255.

## Methods

<p>The <b>IPrinterScriptableSequentialStream</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrinterScriptableSequentialStream::Read](nf-printerextension-iprinterscriptablesequentialstream-read.md) | The Read method reads bytes from the stream and returns them as a JavaScript array. |
| [IPrinterScriptableSequentialStream::Write](nf-printerextension-iprinterscriptablesequentialstream-write.md) | The Write method writes the provided JavaScript array to the stream and returns the number of bytes written. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | printerextension.h |