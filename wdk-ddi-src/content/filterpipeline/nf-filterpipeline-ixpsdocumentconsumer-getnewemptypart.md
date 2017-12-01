---
UID: NF.filterpipeline.IXpsDocumentConsumer.GetNewEmptyPart
title: IXpsDocumentConsumer::GetNewEmptyPart
author: windows-driver-content
description: The GetNewEmptyPart method creates a new XPS part.
old-location: print\ixpsdocumentconsumer_getnewemptypart.htm
old-project: print
ms.assetid: cc0911da-46ca-4cf7-a59e-da0d53e1d10c
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IXpsDocumentConsumer, GetNewEmptyPart, IXpsDocumentConsumer::GetNewEmptyPart
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: filterpipeline.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IXpsDocumentConsumer.GetNewEmptyPart
req.alt-loc: filterpipeline.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: Filterpipeline.idl
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IXpsDocumentConsumer
---

# IXpsDocumentConsumer::GetNewEmptyPart method



## -description
<p>The <code>GetNewEmptyPart</code> method creates a new XPS part.</p>


## -syntax

````
HRESULT GetNewEmptyPart(
  [in]  const wchar_t           *uri,
  [in]        REFIID            riid,
  [out]       void              **ppNewObject,
  [out]       IPrintWriteStream **ppWriteStream
);
````


## -parameters
<dl>

### -param <i>uri</i> [in]

<dd>
<p>The URI for the new part to be created.</p>
</dd>

### -param <i>riid</i> [in]

<dd>
<p>A reference identifier (REFIID) for one of the following interfaces: </p>
<ul>
<li>
<p>
<a href="print.ifixeddocument">IFixedDocument</a>
</p>
</li>
<li>
<p>
<a href="print.ifixedpage">IFixedPage</a>
</p>
</li>
<li>
<p>
<a href="print.ipartimage">IPartImage</a>
</p>
</li>
<li>
<p>
<a href="print.ipartthumbnail">IPartThumbnail</a>
</p>
</li>
<li>
<p>
<a href="print.ipartfont">IPartFont</a>
</p>
</li>
<li>
<p>
<a href="print.ipartprintticket">IPartPrintTicket</a>
</p>
</li>
<li>
<p>
<a href="print.ipartcolorprofile">IPartColorProfile</a>
</p>
</li>
</ul>
</dd>

### -param <i>ppNewObject</i> [out]

<dd>
<p>A pointer to the new object to be created.</p>
</dd>

### -param <i>ppWriteStream</i> [out]

<dd>
<p>A data stream object that the part will be written to. Each part is associated with a data stream object.</p>
</dd>
</dl>

## -returns
<p><code>GetNewEmptyPart</code> returns an <b>HRESULT</b>.</p>

## -remarks
<p>A filter can create new XPS parts by using the <code>GetNewEmptyPart</code> method. Typically, the filter receives XPS parts from the inter-filter object.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Filterpipeline.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IDL</p>
</th>
<td width="70%">
<dl>
<dt>Filterpipeline.idl</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="print.ifixeddocument">IFixedDocument</a>
</dt>
<dt>
<a href="print.ifixedpage">IFixedPage</a>
</dt>
<dt>
<a href="print.ipartcolorprofile">IPartColorProfile</a>
</dt>
<dt>
<a href="print.ipartfont">IPartFont</a>
</dt>
<dt>
<a href="print.ipartimage">IPartImage</a>
</dt>
<dt>
<a href="print.ipartprintticket">IPartPrintTicket</a>
</dt>
<dt>
<a href="print.ipartthumbnail">IPartThumbnail</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IXpsDocumentConsumer::GetNewEmptyPart method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
