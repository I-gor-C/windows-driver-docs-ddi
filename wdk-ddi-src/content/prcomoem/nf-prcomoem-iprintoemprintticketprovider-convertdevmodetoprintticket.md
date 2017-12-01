---
UID: NF.prcomoem.IPrintOemPrintTicketProvider.ConvertDevModeToPrintTicket
title: IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket
author: windows-driver-content
description: The IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket method converts a DEVMODEW structure into a print ticket.
old-location: print\iprintoemprintticketprovider_convertdevmodetoprintticket.htm
old-project: print
ms.assetid: b2e029b7-32c0-4cef-8388-9d30aa5610d3
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemPrintTicketProvider, ConvertDevModeToPrintTicket, IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket
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
req.alt-api: IPrintOemPrintTicketProvider.ConvertDevModeToPrintTicket
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

# IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket method



## -description
<p>The <code>IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket</code> method converts a <a href="display.devmodew">DEVMODEW</a> structure into a print ticket. </p>


## -syntax

````
HRESULT ConvertDevModeToPrintTicket(
  [in]      ULONG            cbDevmode,
  [in]      PDEVMODE         pDevmode,
  [in]      ULONG            cbDrvPrivateSize,
  [in]      PVOID            pPrivateDevmode,
  [in, out] IXMLDOMDocument2 *pPrintTicket
);
````


## -parameters
<dl>

### -param <i>cbDevmode</i> [in]

<dd>
<p>The size, in bytes, of the input <a href="display.devmodew">DEVMODEW</a> structure. The size includes both the public and private portions of this structure.</p>
</dd>

### -param <i>pDevmode</i> [in]

<dd>
<p>A pointer to the input DEVMODEW structure.</p>
</dd>

### -param <i>cbDrvPrivateSize</i> [in]

<dd>
<p>The size, in bytes, of the plug-in's private DEVMODEW structure. </p>
</dd>

### -param <i>pPrivateDevmode</i> [in]

<dd>
<p>A pointer to the plug-in's private <a href="display.devmodew">DEVMODEW</a> structure.</p>
</dd>

### -param <i>pPrintTicket</i> [in, out]

<dd>
<p>A pointer to the partially-completed print ticket. When <code>IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket</code> returns, all of the entries in the print ticket should be filled in.</p>
</dd>
</dl>

## -returns
<p><code>IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket</code> should return S_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.</p>

## -remarks
<p>The core driver calls the <code>IPrintTicketProvider::ConvertDevModeToPrintTicket</code> method with an input print ticket that is populated with public and Unidrv-private or Pscript5-private features. The plug-in is free to set <a href="display.devmodew">DEVMODEW</a> settings in the public part or in the plug-in's private part, based on settings in the input print ticket. In addition to setting new DEVMODEW items, the plug-in can modify existing settings in the public portion of the DEVMODEW structure.</p>

<p>The DEVMODEW structure fields that correlate with the part of the DEVMODEW structure of interest to the client will already have been populated before <code>IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket</code> is called, including the public portion of the DEVMODEW structure and excluding the privately-defined values in the public portion of the DEVMODEW structure.</p>

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

## -see-also
<dl>
<dt>
<a href="print.iprintoemprintticketprovider_convertprinttickettodevmode">IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
