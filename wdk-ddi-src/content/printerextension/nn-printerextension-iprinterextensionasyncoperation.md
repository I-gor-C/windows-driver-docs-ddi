---
UID: NN:printerextension.IPrinterExtensionAsyncOperation
title: IPrinterExtensionAsyncOperation
author: windows-driver-content
description: Provides the context associated with an asynchronous operation.
old-location: print\iprinterextensionasyncoperation.htm
old-project: print
ms.assetid: AA862667-42D6-4A82-9698-1C43E9EEC434
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrinterExtensionAsyncOperation, IPrinterExtensionAsyncOperation interface [Print Devices], IPrinterExtensionAsyncOperation interface [Print Devices], described, print.iprinterextensionasyncoperation, printerextension/IPrinterExtensionAsyncOperation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: printerextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
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
-	IPrinterExtensionAsyncOperation
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrinterExtensionAsyncOperation interface

Provides the context associated with an asynchronous operation.

## Methods

<p>The <b>IPrinterExtensionAsyncOperation</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrinterExtensionAsyncOperation::Cancel](nf-printerextension-iprinterextensionasyncoperation-cancel.md) | Cancels the asynchronous operation. |

## Remarks
<b>IPrinterExtensionAsyncOperation</b> also helps to make it possible to perform device maintenance from a UWP device app or from a printer extension. For more information, see <a href="https://msdn.microsoft.com/310E92A9-F751-4346-9B2D-0578A136AD20">Device Maintenance</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8.1 Windows 8.1 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/310E92A9-F751-4346-9B2D-0578A136AD20">Device Maintenance</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn265391">SendBidiSetRequestAsync</a>