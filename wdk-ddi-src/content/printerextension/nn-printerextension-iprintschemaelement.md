---
UID: NN:printerextension.IPrintSchemaElement
title: IPrintSchemaElement
author: windows-driver-content
description: Provides access to the underlying XML node and &#0034;name&#0034; attribute information for a Print Schema element.
old-location: print\iprintschemaelement_interface.htm
old-project: print
ms.assetid: E6F6F00B-E116-4AEA-AF9A-55209DA20DC6
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPrintSchemaElement, IPrintSchemaElement interface [Print Devices], IPrintSchemaElement interface [Print Devices], described, print.iprintschemaelement_interface, printerextension/IPrintSchemaElement
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
-	IPrintSchemaElement
product: Windows
targetos: Windows
req.typenames: PrintSchemaSelectionType
req.product: Windows 10 or later.
---

# IPrintSchemaElement interface

Provides access to the underlying XML node and "name" attribute information  for a Print Schema element.

## Methods

<p>The <b>IPrintSchemaElement</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPrintSchemaElement::get_Name](nf-printerextension-iprintschemaelement-get_name.md) | Gets the name of the printer for this print queue. |
| [IPrintSchemaElement::get_NamespaceUri](nf-printerextension-iprintschemaelement-get_namespaceuri.md) | Gets the namespace URI value of the &#0034;name&#0034; attribute of this node. |
| [IPrintSchemaElement::get_XmlNode](nf-printerextension-iprintschemaelement-get_xmlnode.md) | Gets the IXMLDOMNode object associated with this item. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Windows |
| **Header** | printerextension.h |