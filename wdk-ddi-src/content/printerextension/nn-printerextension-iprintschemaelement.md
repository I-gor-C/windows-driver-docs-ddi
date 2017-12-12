---
UID: NN.printerextension.IPrintSchemaElement
title: IPrintSchemaElement
author: windows-driver-content
description: Provides access to the underlying XML node and &#0034;name&#0034; attribute information for a Print Schema element.
old-location: print\iprintschemaelement_interface.htm
old-project: print
ms.assetid: E6F6F00B-E116-4AEA-AF9A-55209DA20DC6
ms.author: windowsdriverdev
ms.date: 12/9/2017
ms.keywords: tagPrintSchemaSelectionType, PrintSchemaSelectionType
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
req.alt-api: IPrintSchemaElement
req.alt-loc: Printerextension.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.product: Windows 10 or later.
---

# IPrintSchemaElement interface



## -description
Provides access to the underlying XML node and "name" attribute information  for a Print Schema element.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaElement</b> interface inherits from the <a href="ebbff4bc-36b2-4861-9efa-ffa45e013eb5" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IDispatch</b></a> interface. <b>IPrintSchemaElement</b> also has these types of members:

The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaElement</b> interface has these properties.


<a href="print.iprintschemaelement_name">Name</a>


Read-only

Gets the base value of the "name" attribute of this node.


<a href="print.iprintschemaelement_namespaceuri">NamespaceUri</a>


Read-only

Gets the namespace URI  value of the "name" attribute of this node.


<a href="print.iprintschemaelement_xmlnode">XmlNode</a>


Read-only

Gets the IXMLDOMNode object associated with this item.

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client

</th>
<td width="70%">
Windows 8

</td>
</tr>
<tr>
<th width="30%">
Minimum supported server

</th>
<td width="70%">
Windows Server 2012

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Printerextension.h</dt>
</dl>
</td>
</tr>
</table>