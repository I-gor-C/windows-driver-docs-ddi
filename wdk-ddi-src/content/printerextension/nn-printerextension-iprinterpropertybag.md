---
UID: NN:printerextension.IPrinterPropertyBag
title: IPrinterPropertyBag
author: windows-driver-content
description: Provides strongly-typed get and set methods.
old-location: print\iprinterpropertybag_interface.htm
old-project: print
ms.assetid: 421397FF-4956-4052-B63D-32F8E79A22D0
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrinterPropertyBag, IPrinterPropertyBag interface [Print Devices], IPrinterPropertyBag interface [Print Devices], described, print.iprinterpropertybag_interface, printerextension/IPrinterPropertyBag
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
-	IPrinterPropertyBag
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrinterPropertyBag interface

Provides strongly-typed <b>get</b> and <b>set</b> methods.

Note that the driver property bag uses the following GUID for its property store format ID:

<dl>
<dd>DEFINE_GUID(FMTID_PrinterPropertyBag, 0x75f9adca, 0x097d, 0x45c3, 0xa6, 0xe4, 0xba, 0xb2, 0x9e, 0x27, 0x6f, 0x3e);</dd>
</dl>


The <b>IPrinterPropertyBag</b> interface is used by all the printer property bags, including driver property bag, user property bag, queue property bag, and DEVMODE property bag.

## Methods

<p>The <b>IPrinterPropertyBag</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrinterPropertyBag::GetBool](nf-printerextension-iprinterpropertybag-getbool.md) | Reads a specified boolean property. |
| [IPrinterPropertyBag::GetBytes](nf-printerextension-iprinterpropertybag-getbytes.md) | Reads a byte array property. |
| [IPrinterPropertyBag::GetInt32](nf-printerextension-iprinterpropertybag-getint32.md) | Reads an integer property. |
| [IPrinterPropertyBag::GetReadStream](nf-printerextension-iprinterpropertybag-getreadstream.md) | Gets a stream in order to read from a stream property. |
| [IPrinterPropertyBag::GetString](nf-printerextension-iprinterpropertybag-getstring.md) | Reads a string property. |
| [IPrinterPropertyBag::GetWriteStream](nf-printerextension-iprinterpropertybag-getwritestream.md) | Gets a stream in order to write a stream property. |
| [IPrinterPropertyBag::SetBool](nf-printerextension-iprinterpropertybag-setbool.md) | Writes a specified boolean property value. |
| [IPrinterPropertyBag::SetBytes](nf-printerextension-iprinterpropertybag-setbytes.md) | Writes a byte array property. |
| [IPrinterPropertyBag::SetInt32](nf-printerextension-iprinterpropertybag-setint32.md) | Writes an integer property. |
| [IPrinterPropertyBag::SetString](nf-printerextension-iprinterpropertybag-setstring.md) | Writes a string property. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/ebbff4bc-36b2-4861-9efa-ffa45e013eb5">IDispatch</a>



<a href="https://msdn.microsoft.com/52EC01D5-43C7-4CE0-ABEC-1604A4198316">IPrinterExtensionContext::DriverProperties</a>



<a href="https://msdn.microsoft.com/21B370C9-BDF7-42A6-B0CC-BC9B19F9D2D5">IPrinterExtensionContext::UserProperties</a>



<a href="https://msdn.microsoft.com/87EED8B5-676C-4056-812B-B0424148FCFA">IPrinterQueue::GetProperties</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh973217">IPrinterScriptablePropertyBag</a>



<a href="https://msdn.microsoft.com/4E20303A-BEB3-4928-BA5A-356D978FA2BE">V4 Printer Driver Property Bags</a>