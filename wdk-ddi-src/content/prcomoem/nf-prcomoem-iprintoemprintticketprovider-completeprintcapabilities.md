---
UID: NF.prcomoem.IPrintOemPrintTicketProvider.CompletePrintCapabilities
title: IPrintOemPrintTicketProvider::CompletePrintCapabilities
author: windows-driver-content
description: The IPrintOemPrintTicketProvider::CompletePrintCapabilities method fills in the remaining entries of the specified print capabilities document.
old-location: print\iprintoemprintticketprovider_completeprintcapabilities.htm
old-project: print
ms.assetid: 067eca3b-f487-405a-9799-bd62376f9e24
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemPrintTicketProvider, CompletePrintCapabilities, IPrintOemPrintTicketProvider::CompletePrintCapabilities
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemPrintTicketProvider.CompletePrintCapabilities
req.alt-loc: prcomoem.h
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
req.iface: IPrintOemPrintTicketProvider
req.product: Windows 10 or later.
---

# IPrintOemPrintTicketProvider::CompletePrintCapabilities method



## -description
<p>The <code>IPrintOemPrintTicketProvider::CompletePrintCapabilities</code> method fills in the remaining entries of the specified print capabilities document. </p>


## -syntax

````
HRESULT CompletePrintCapabilities(
  [in]      IXMLDOMDocument2 *pPrintTicket,
  [in, out] IXMLDOMDocument2 *pCapabilities
);
````


## -parameters
<dl>

### -param <i>pPrintTicket</i> [in]

<dd>
<p>A pointer to an input print ticket. Any configuration-dependent data in the print capabilities (that is, data that would be represented by a *<b>Switch</b> / *<b>Case</b> construct in a GPD file) must be based on the settings in the print ticket. If the application does not provide a print ticket, this parameter can be <b>NULL</b>. In such situations, the provider should assume default settings for feature and parameter constructs.</p>
</dd>

### -param <i>pCapabilities</i> [in, out]

<dd>
<p>A pointer to a partially-complete print capabilities document. When <code>IPrintOemPrintTicketProvider::CompletePrintCapabilities</code> returns, the buffer that is pointed to by <i>pCapablities</i> should contain a completed print capabilities document.</p>
</dd>
</dl>

## -returns
<p><code>IPrintOemPrintTicketProvider::CompletePrintCapabilities</code> should return S_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.</p>

## -remarks
<p>A Unidrv or Pscript5 plug-in should fill in only those capabilities that it explicitly supports, over and above the features and options that the driver supports. The plug-in should at least fill in the capabilities that it supports, as listed in its private DEVMODEW structure. If the plug-in provider changes the representation of features provided by the core driver in the print ticket, the provider must make equivalent changes to the representation here.</p>

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
<dt>Prcomoem.h (include Prcomoem.h)</dt>
</dl>
</td>
</tr>
</table>