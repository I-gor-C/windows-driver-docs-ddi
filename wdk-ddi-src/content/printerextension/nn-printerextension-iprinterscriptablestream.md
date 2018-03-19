---
UID: NN:printerextension.IPrinterScriptableStream
title: IPrinterScriptableStream
author: windows-driver-content
description: The IPrinterScriptableStream interface builds on IPrinterScriptableSequentialStream and adds IStream-like semantics.
old-location: print\iprinterscriptablestream.htm
old-project: print
ms.assetid: AD3CDF90-76ED-498B-8DE1-B191504EB415
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrinterScriptableStream, IPrinterScriptableStream interface [Print Devices], IPrinterScriptableStream interface [Print Devices], described, print.iprinterscriptablestream, printerextension/IPrinterScriptableStream
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: printerextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
-	Printerextension.h
api_name:
-	IPrinterScriptableStream
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrinterScriptableStream interface

The IPrinterScriptableStream interface builds on <a href="..\printerextension\nn-printerextension-iprinterscriptablesequentialstream.md">IPrinterScriptableSequentialStream</a> and adds IStream-like semantics.

## Methods

<p>The <b>IPrinterScriptableStream</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrinterScriptableStream::Commit](nf-printerextension-iprinterscriptablestream-commit.md) | Commits the operation. |
| [IPrinterScriptableStream::Seek](nf-printerextension-iprinterscriptablestream-seek.md) | Sets the seek pointer. |
| [IPrinterScriptableStream::SetSize](nf-printerextension-iprinterscriptablestream-setsize.md) | Sets the size of the scriptable stream, in bytes. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="..\printerextension\nn-printerextension-iprinterscriptablepropertybag.md">IPrinterScriptablePropertyBag</a>



<a href="https://msdn.microsoft.com/493E6C55-DC3B-4160-9642-BDABADD575B8">IPrinterScriptablePropertyBag::GetReadStream</a>



<a href="https://msdn.microsoft.com/EFF55B5C-55E2-4E03-9D96-FDB1BC550A53">IPrinterScriptablePropertyBag::GetWriteStream</a>



<a href="..\printerextension\nn-printerextension-iprinterscriptablesequentialstream.md">IPrinterScriptableSequentialStream</a>