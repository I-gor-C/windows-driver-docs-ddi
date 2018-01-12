---
UID: NF:filterpipeline.IXpsDocumentProvider.GetXpsPart
title: IXpsDocumentProvider::GetXpsPart method
author: windows-driver-content
description: The GetXpsPart method retrieves several objects that make up an XPS document.
old-location: print\ixpsdocumentprovider_getxpspart.htm
old-project: print
ms.assetid: 7e36cf90-a84a-447c-bec3-2b5175fffd7c
ms.author: windowsdriverdev
ms.date: 1/8/2018
ms.keywords: IXpsDocumentProvider, IXpsDocumentProvider::GetXpsPart, GetXpsPart
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: filterpipeline.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IXpsDocumentProvider.GetXpsPart
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
req.typenames: EXpsFontRestriction
---

# IXpsDocumentProvider::GetXpsPart method



## -description
The <code>GetXpsPart</code> method retrieves several objects that make up an XPS document.



## -syntax

````
HRESULT GetXpsPart(
  [out] IUnknown **ppIXpsPart
);
````


## -parameters

### -param ppIXpsPart [out]

The XPS part. This part is the <b>IUnknown</b> interface of an object that is an XPS part. If <i>ppIXpsPart</i> is NULL, there are no more XPS parts to consume and the filter is ready to finish processing.


## -returns
<code>GetXpsPart</code> returns an <b>HRESULT</b>.


## -remarks
Use <b>QueryInterface</b> on the value that the <b>GetXpsPart</b> method returns to determine the type of object that it retrieved.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Filterpipeline.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IDL

</th>
<td width="70%">
<dl>
<dt>Filterpipeline.idl</dt>
</dl>
</td>
</tr>
</table>