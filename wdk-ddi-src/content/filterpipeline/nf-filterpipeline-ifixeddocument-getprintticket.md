---
UID: NF.filterpipeline.IFixedDocument.GetPrintTicket
title: IFixedDocument::GetPrintTicket
author: windows-driver-content
description: The GetPrintTicket method gets the print ticket object for the fixed document.
old-location: print\ifixeddocument_getprintticket.htm
old-project: print
ms.assetid: b9c4768e-8292-4311-b64a-ac1ef7d2ad10
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IFixedDocument, GetPrintTicket, IFixedDocument::GetPrintTicket
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
req.alt-api: IFixedDocument.GetPrintTicket
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
req.iface: IFixedDocument
---

# IFixedDocument::GetPrintTicket method



## -description
<p>The <b>GetPrintTicket</b> method gets the print ticket object for the fixed document.</p>


## -syntax

````
HRESULT GetPrintTicket(
  [out] IPartPrintTicket **ppPrintTicket
);
````


## -parameters
<dl>

### -param ppPrintTicket [out]

<dd>
<p>The print ticket object for the fixed document.</p>
</dd>
</dl>

## -returns
<p><b>GetPrintTicket</b> returns an <b>HRESULT</b> value. If a print ticket is not in the fixed document, this method might return E_ELEMENT_NOT_FOUND.</p>

## -remarks


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