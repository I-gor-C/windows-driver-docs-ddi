---
UID: NN:printerextension.IPrintSchemaOptionCollection
title: IPrintSchemaOptionCollection
author: windows-driver-content
description: Exposes a collection of IPrintSchemaOption objects.
old-location: print\iprintschemaoptioncollection.htm
old-project: print
ms.assetid: ED0FD042-EB42-4F4B-AF9C-B8F56909ED66
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintSchemaOptionCollection, IPrintSchemaOptionCollection interface [Print Devices], IPrintSchemaOptionCollection interface [Print Devices], described, print.iprintschemaoptioncollection, printerextension/IPrintSchemaOptionCollection
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
req.lib: printerextension.h
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
-	IPrintSchemaOptionCollection
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrintSchemaOptionCollection interface

Exposes a collection of <a href="..\printerextension\nn-printerextension-iprintschemaoption.md">IPrintSchemaOption</a> objects.

## Methods

<p>The <b>IPrintSchemaOptionCollection</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintSchemaOptionCollection::get_Count](nf-printerextension-iprintschemaoptioncollection-get_count.md) | Gets a count of the number of IPrinterExtensionContext objects in the collection. |
| [IPrintSchemaOptionCollection::GetAt](nf-printerextension-iprintschemaoptioncollection-getat.md) | Gets a pointer to an IPrintSchemaOption object. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/ebbff4bc-36b2-4861-9efa-ffa45e013eb5">IDispatch</a>



<a href="..\printerextension\nn-printerextension-iprintschemaoption.md">IPrintSchemaOption</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintSchemaOptionCollection interface%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>