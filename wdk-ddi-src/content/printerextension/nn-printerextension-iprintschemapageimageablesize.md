---
UID: NN.printerextension.IPrintSchemaPageImageableSize
title: IPrintSchemaPageImageableSize
author: windows-driver-content
description: Exposes the PageImageableSize property of PrintCapabilities. The properties of this interface map directly to those in the PageImageableSize property of PrintCapabilities.
old-location: print\iprintschemapageimageablesize_interface.htm
old-project: print
ms.assetid: C8E9278D-D24A-4EEC-8F68-D77C76ECCC40
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
req.alt-api: IPrintSchemaPageImageableSize
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

# IPrintSchemaPageImageableSize interface



## -description
<p>Exposes the PageImageableSize property of PrintCapabilities. The properties of this interface map directly to those in the PageImageableSize property of PrintCapabilities.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaPageImageableSize</b> interface inherits from <a href="..\printerextension\nn-printerextension-iprintschemaelement.md">IPrintSchemaElement</a>. <b>IPrintSchemaPageImageableSize</b> also has these types of members:</p>

<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IPrintSchemaPageImageableSize</b> interface has these properties.</p>

<p>
<a href="print.iprintschemapageimageablesize_extentheightinmicrons">ExtentHeightInMicrons</a>
</p>

<p>Read-only</p>

<p>Gets the vertical distance between the origin and the bounding limit of the canvas application media size.</p>

<p>
<a href="print.iprintschemapageimageablesize_extentwidthinmicrons">ExtentWidthInMicrons</a>
</p>

<p>Read-only</p>

<p>Gets the horizontal distance between the origin and the bounding limit of the application media size.</p>

<p>
<a href="print.iprintschemapageimageablesize_imageablesizeheightinmicrons">ImageableSizeHeightInMicrons</a>
</p>

<p>Read-only</p>

<p>Gets the vertical dimension of the application media size relative to the page orientation.</p>

<p>
<a href="print.iprintschemapageimageablesize_imageablesizewidthinmicrons">ImageableSizeWidthInMicrons</a>
</p>

<p>Read-only</p>

<p>Gets the horizontal dimension of the application media size relative to the page orientation.</p>

<p>
<a href="print.iprintschemapageimageablesize_originheightinmicrons">OriginHeightInMicrons</a>
</p>

<p>Read-only</p>

<p>Gets the vertical origin of the imageable area relative to the application media size.</p>

<p>
<a href="print.iprintschemapageimageablesize_originwidthinmicrons">OriginWidthInMicrons</a>
</p>

<p>Read-only</p>

<p>Gets the horizontal origin of the imageable area relative to the application media size.</p>

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