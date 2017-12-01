---
UID: NN.printerextension.IPrintSchemaElement~r1
title: IPrintSchemaElement
author: windows-driver-content
description: Provides access to the underlying XML node and &#0034;name&#0034; attribute information for a Print Schema element.
old-location: print\iprintschemaelement_interface.htm
old-project: print
ms.assetid: E6F6F00B-E116-4AEA-AF9A-55209DA20DC6
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintSchemaTicket2, GetParameterInitializer, IPrintSchemaTicket2::GetParameterInitializer
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
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# IPrintSchemaElement interface



## -description
<p>Provides access to the underlying XML node and "name" attribute information  for a Print Schema element.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaElement</b> interface inherits from the <a href="ebbff4bc-36b2-4861-9efa-ffa45e013eb5" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IDispatch</b></a> interface. <b>IPrintSchemaElement</b> also has these types of members:</p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaElement</b> interface has these properties.</p>

<p>
<a href="print.iprintschemaelement_name">Name</a>
</p>

<p>Read-only</p>

<p>Gets the base value of the "name" attribute of this node.</p>

<p>
<a href="print.iprintschemaelement_namespaceuri">NamespaceUri</a>
</p>

<p>Read-only</p>

<p>Gets the namespace URI  value of the "name" attribute of this node.</p>

<p>
<a href="print.iprintschemaelement_xmlnode">XmlNode</a>
</p>

<p>Read-only</p>

<p>Gets the IXMLDOMNode object associated with this item.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Printerextension.h</dt>
</dl>
</td>
</tr>
</table>