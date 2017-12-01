---
UID: NF.prcomoem.IPrintOemPrintTicketProvider.ExpandIntentOptions
title: IPrintOemPrintTicketProvider::ExpandIntentOptions
author: windows-driver-content
description: The IPrintOemPrintTicketProvider::ExpandIntentOptions method enables the plug-in to expand printer options (such as photo printing) into individual feature settings in the print ticket.
old-location: print\iprintoemprintticketprovider_expandintentoptions.htm
old-project: print
ms.assetid: c0499a9b-8f02-4a88-bffa-e088e9098a6c
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemPrintTicketProvider, ExpandIntentOptions, IPrintOemPrintTicketProvider::ExpandIntentOptions
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
req.alt-api: IPrintOemPrintTicketProvider.ExpandIntentOptions
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

# IPrintOemPrintTicketProvider::ExpandIntentOptions method



## -description
<p>The <code>IPrintOemPrintTicketProvider::ExpandIntentOptions</code> method enables the plug-in to expand printer options (such as photo printing) into individual feature settings in the print ticket. </p>


## -syntax

````
HRESULT ExpandIntentOptions(
  [in, out] IXMLDOMDocument2 *pPrintTicket
);
````


## -parameters
<dl>

### -param <i>pPrintTicket</i> [in, out]

<dd>
<p>A pointer to a print ticket.</p>
</dd>
</dl>

## -returns
<p><code>IPrintOemPrintTicketProvider::ExpandIntentOptions</code> should return S_OK if the operation succeeds or when the plug-in does not support intent features. Otherwise, this method should return a standard COM error code.</p>

## -remarks
<p>The Unidrv or Pscript5 driver calls <code>IPrintOemPrintTicketProvider::ExpandIntentOptions</code> to enable the plug-in to expand options that represent intent into their individual settings in other features in the print ticket before print ticket validation. Such option expansion has two important effects: the client receives information about the results of the intent expansion, and the core driver resolves constraints against the individual features that are affected by the intent.</p>

<p>We recommend that the driver preserve the state of the intent option in the driver's private <a href="display.devmodew">DEVMODEW</a> structure when it converts a print ticket to a DEVMODEW, and then from a DEVMODEW back to a print ticket.</p>

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