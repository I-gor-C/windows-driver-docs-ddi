---
UID : NN:printerextension.IPrinterScriptableStream
title : IPrinterScriptableStream
author : windows-driver-content
description : The IPrinterScriptableStream interface builds on IPrinterScriptableSequentialStream and adds IStream-like semantics.
old-location : print\iprinterscriptablestream.htm
old-project : print
ms.assetid : AD3CDF90-76ED-498B-8DE1-B191504EB415
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : IPrintSchemaTicket2, IPrintSchemaTicket2::GetParameterInitializer, GetParameterInitializer
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : printerextension.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 8
req.target-min-winversvr : Windows Server 2012
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IPrinterScriptableStream
req.alt-loc : Printerextension.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : PrintSchemaSelectionType
req.product : Windows 10 or later.
---

# IPrinterScriptableStream interface

The IPrinterScriptableStream interface builds on <a href="https://msdn.microsoft.com/85DF7DCB-7AB1-4A46-AD70-6D47D9F98079">IPrinterScriptableSequentialStream</a> and adds IStream-like semantics.

## Methods

<p>The <b>IPrinterScriptableStream</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [printerextension.IPrinterScriptableStream.Commit](nf-printerextension-iprinterscriptablestream-commit.md) | Commits the operation. |
| [printerextension.IPrinterScriptableStream.Seek](nf-printerextension-iprinterscriptablestream-seek.md) | Sets the seek pointer. |
| [printerextension.IPrinterScriptableStream.SetSize](nf-printerextension-iprinterscriptablestream-setsize.md) | Sets the size of the scriptable stream, in bytes. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | printerextension.h |
| **DLL** |  |

    ## See Also

        <dl>
<dt>
<a href="https://msdn.microsoft.com/85DF7DCB-7AB1-4A46-AD70-6D47D9F98079">IPrinterScriptableSequentialStream</a>
</dt>
<dt>
<a href="..\printerextension\nn-printerextension-iprinterscriptablepropertybag.md">IPrinterScriptablePropertyBag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/493E6C55-DC3B-4160-9642-BDABADD575B8">IPrinterScriptablePropertyBag::GetReadStream</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/EFF55B5C-55E2-4E03-9D96-FDB1BC550A53">IPrinterScriptablePropertyBag::GetWriteStream</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterScriptableStream interface%20 RELEASE:%20(1/8/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>