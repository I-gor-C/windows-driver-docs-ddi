---
UID: NN:printerextension.IPrinterScriptablePropertyBag
title: IPrinterScriptablePropertyBag
author: windows-driver-content
description: The IPrinterScriptablePropertyBag interface is the property bag interface passed to script clients.
old-location: print\iprinterscriptablepropertybag.htm
old-project: print
ms.assetid: E6F48895-7ED6-479B-BF16-42192461C56D
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrinterScriptablePropertyBag, IPrinterScriptablePropertyBag interface [Print Devices], IPrinterScriptablePropertyBag interface [Print Devices], described, print.iprinterscriptablepropertybag, printerextension/IPrinterScriptablePropertyBag
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
-	IPrinterScriptablePropertyBag
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrinterScriptablePropertyBag interface

The IPrinterScriptablePropertyBag interface is the property bag interface passed to script clients. 

This interface is the same as <a href="https://msdn.microsoft.com/library/windows/hardware/hh439547">IPrinterPropertyBag</a>, except that the GetBytes and SetBytes methods operate on JavaScript arrays and the GetReadStream and GetWriteStream methods operate on <a href="https://msdn.microsoft.com/library/windows/hardware/hh973218">IPrinterScriptableStream</a> objects.

## Methods

<p>The <b>IPrinterScriptablePropertyBag</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrinterScriptablePropertyBag::GetBool](nf-printerextension-iprinterscriptablepropertybag-getbool.md) | Gets a specified boolean property. |
| [IPrinterScriptablePropertyBag::GetBytes](nf-printerextension-iprinterscriptablepropertybag-getbytes.md) | Gets a byte array property. |
| [IPrinterScriptablePropertyBag::GetInt32](nf-printerextension-iprinterscriptablepropertybag-getint32.md) | Gets an integer property. |
| [IPrinterScriptablePropertyBag::GetReadStream](nf-printerextension-iprinterscriptablepropertybag-getreadstream.md) | Gets a read stream and uses it to read from a property. |
| [IPrinterScriptablePropertyBag::GetString](nf-printerextension-iprinterscriptablepropertybag-getstring.md) | Gets a string property. |
| [IPrinterScriptablePropertyBag::GetWriteStream](nf-printerextension-iprinterscriptablepropertybag-getwritestream.md) | Gets a stream and uses it to write to a stream property. |
| [IPrinterScriptablePropertyBag::SetBool](nf-printerextension-iprinterscriptablepropertybag-setbool.md) | Writes a specified boolean property value. |
| [IPrinterScriptablePropertyBag::SetBytes](nf-printerextension-iprinterscriptablepropertybag-setbytes.md) | Writes a byte array property. |
| [IPrinterScriptablePropertyBag::SetInt32](nf-printerextension-iprinterscriptablepropertybag-setint32.md) | Writes an integer property. |
| [IPrinterScriptablePropertyBag::SetString](nf-printerextension-iprinterscriptablepropertybag-setstring.md) | Writes a string property. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439547">IPrinterPropertyBag</a>



<a href="https://msdn.microsoft.com/73BE6E2A-0C46-4C3F-8888-5FE8386A1F50">IPrinterScriptContext::DriverProperties</a>



<a href="https://msdn.microsoft.com/EEC61313-5796-42BC-84BF-CF29F8BE0C96">IPrinterScriptContext::QueueProperties</a>



<a href="https://msdn.microsoft.com/6F181350-41A3-4592-BB72-1E3AD6FEC748">IPrinterScriptContext::UserProperties</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh973218">IPrinterScriptableStream</a>



<a href="https://msdn.microsoft.com/4E20303A-BEB3-4928-BA5A-356D978FA2BE">V4 Printer Driver Property Bags</a>