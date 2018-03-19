---
UID: NN:printerextension.IPrintSchemaTicket
title: IPrintSchemaTicket
author: windows-driver-content
description: Provides the primary method to access and validate a PrintTicket.
old-location: print\iprintschematicket_interface.htm
old-project: print
ms.assetid: 190B0B88-6018-4B43-8699-78427421D6FF
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintSchemaTicket, IPrintSchemaTicket interface [Print Devices], IPrintSchemaTicket interface [Print Devices], described, print.iprintschematicket_interface, printerextension/IPrintSchemaTicket
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
-	IPrintSchemaTicket
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrintSchemaTicket interface

Provides the primary method to access and validate a PrintTicket.

## Methods

<p>The <b>IPrintSchemaTicket</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintSchemaTicket::CommitAsync](nf-printerextension-iprintschematicket-commitasync.md) | Gets an asynchronous PrintTicket commit operation context. |
| [IPrintSchemaTicket::get_JobCopiesAllDocuments](nf-printerextension-iprintschematicket-get_jobcopiesalldocuments.md) | Gets the copy count. |
| [IPrintSchemaTicket::GetCapabilities](nf-printerextension-iprintschematicket-getcapabilities.md) | Gets an IPrintSchemaCapabilities object that represents the printer capabilities based on the current settings of this IPrintSchemaTicket object. |
| [IPrintSchemaTicket::GetFeature](nf-printerextension-iprintschematicket-getfeature.md) | Gets a named feature from the PrintTicket, by name and full namespace URI. |
| [IPrintSchemaTicket::GetFeatureByKeyName](nf-printerextension-iprintschematicket-getfeaturebykeyname.md) | Gets a feature from the PrintTicket based on the specified key name. |
| [IPrintSchemaTicket::NotifyXmlChanged](nf-printerextension-iprintschematicket-notifyxmlchanged.md) | Notifies the print system that the XML DOM object has changed. |
| [IPrintSchemaTicket::put_JobCopiesAllDocuments](nf-printerextension-iprintschematicket-put_jobcopiesalldocuments.md) | Gets the copy count. |
| [IPrintSchemaTicket::ValidateAsync](nf-printerextension-iprintschematicket-validateasync.md) | Gets an asynchronous PrintTicket validation operation context. |

## Remarks
To obtain an IXMLDOMDocument2 object for the PrintTicket object, you must first dereference the <i>ppXmlNode</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh969196">XmlNode</a> property (using *ppXmlNode ). This retrieves a pointer to an interface of type <b>IUnknown</b>. Use this pointer to  call the <b>QueryInterface</b> method of the PrintTicket object to access the underlying  IXMLDOMDocument2 object.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |

## See Also

<a href="https://msdn.microsoft.com/5E7F2292-1F71-4581-8E34-86F1464EC08F">IPrintSchemaElement::XmlNode</a>



<a href="..\printerextension\nn-printerextension-iprintschemacapabilities.md">IPrintSchemaCapabilities</a>



<a href="https://msdn.microsoft.com/B1599F21-D6DD-497D-9CD8-6C637ABAA33A">IPrintSchemaAsyncOperationEvent::Completed</a>



<a href="..\printerextension\nn-printerextension-iprintschemaelement.md">IPrintSchemaElement</a>