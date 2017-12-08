---
UID: NF.filterpipeline.IFixedPage.SetPrintTicket
title: IFixedPage::SetPrintTicket
author: windows-driver-content
description: The SetPrintTicket method associates a print ticket with the page.
old-location: print\ifixedpage_setprintticket.htm
old-project: print
ms.assetid: d899211a-e98d-45f6-9574-8b5f51658edf
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IFixedPage, SetPrintTicket, IFixedPage::SetPrintTicket
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
req.alt-api: IFixedPage.SetPrintTicket
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
req.iface: IFixedPage
---

# IFixedPage::SetPrintTicket method



## -description
<p>The <b>SetPrintTicket</b> method associates a print ticket with the page.</p>


## -syntax

````
HRESULT SetPrintTicket(
  [in] IPartPrintTicket *pPrintTicket
);
````


## -parameters
<dl>

### -param pPrintTicket [in]

<dd>
<p>The print ticket object.</p>
</dd>
</dl>

## -returns
<p><b>SetPrintTicket</b> returns an <b>HRESULT</b> value.</p>

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