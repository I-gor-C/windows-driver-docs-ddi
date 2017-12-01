---
UID: NF.prcomoem.IPrintOemPrintTicketProvider.ConvertPrintTicketToDevMode
title: IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode
author: windows-driver-content
description: The IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode method converts a print ticket to a DEVMODEW structure.
old-location: print\iprintoemprintticketprovider_convertprinttickettodevmode.htm
old-project: print
ms.assetid: 1243f679-76c3-4d2e-8d57-b9d652b21a05
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemPrintTicketProvider, ConvertPrintTicketToDevMode, IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode
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
req.alt-api: IPrintOemPrintTicketProvider.ConvertPrintTicketToDevMode
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

# IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode method



## -description
<p>The <code>IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode</code> method converts a print ticket to a <a href="display.devmodew">DEVMODEW</a> structure. </p>


## -syntax

````
HRESULT ConvertPrintTicketToDevMode(
  [in]      IXMLDOMDocument2 *pPrintTicket,
  [in]      ULONG            cbDevmode,
  [in, out] PDEVMODE         pDevmode,
  [in]      ULONG            cbDrvPrivateSize,
  [in]      PVOID            pPrivateDevmode
);
````


## -parameters
<dl>

### -param <i>pPrintTicket</i> [in]

<dd>
<p>A pointer to the input print ticket.</p>
</dd>

### -param <i>cbDevmode</i> [in]

<dd>
<p>The size, in bytes, of the input <a href="display.devmodew">DEVMODEW</a> structure. This size includes both the public and private sections of the DEVMODEW structure. </p>
</dd>

### -param <i>pDevmode</i> [in, out]

<dd>
<p>A pointer to the input DEVMODEW structure. When <code>IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode</code> returns, the plug-in's private DEVMODEW structure will contain information that was obtained from the print ticket.</p>
</dd>

### -param <i>cbDrvPrivateSize</i> [in]

<dd>
<p>The size, in bytes, of the plug-in's private DEVMODEW structure. </p>
</dd>

### -param <i>pPrivateDevmode</i> [in]

<dd>
<p>A pointer to the plug-in's private <a href="display.devmodew">DEVMODEW</a> structure.</p>
</dd>
</dl>

## -returns
<p><code>IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode</code> should return S_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.</p>

## -remarks
<p>The core driver calls the <code>IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode</code> method before it performs its part of the conversion of a print ticket to a <a href="display.devmodew">DEVMODEW</a> structure. In the call to this method, the core driver passes an input print ticket that is fully populated and a DEVMODEW structure that is set to default values. In the conversion, the plug-in must undo any changes that it made to the print ticket during the previous conversion from a DEVMODEW structure to a print ticket. If, during this previous conversion, the plug-in moved a feature from a private namespace to the public namespace, the plug-in must restore the feature to the private namespace in a format that is suitable for the core driver, that is, the format in which the core driver had previously placed the feature in the print ticket that was provided to the plug-in in the <a href="print.iprintoemprintticketprovider_convertdevmodetoprintticket">IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket</a> method. This restoration is necessary so that the core driver can recognize the feature in the print ticket and reflect its settings in private portion of the core driver's DEVMODEW structure while the core driver performs its part of the print ticket-to-DEVMODEW conversion .</p>

<p>Before the system converts a print ticket back to a <a href="display.devmodew">DEVMODEW</a> structure, it first loads the default DEVMODEW structure. The system then calls the provider's <a href="print.iprintoemprintticketprovider_bindprinter">IPrintOemPrintTicketProvider::BindPrinter</a> method. This method should then read all of the settings that it supported from the print ticket and populate those settings in the DEVMODEW structure. Note that not all of the features necessarily will be represented, and that often Option instances that are present might not contain all of the Scored Property instances that the provider would normally populate. If the provider makes any changes to the settings that are populated by the system during conversion from print ticket to DEVMODEW, the provider should perform the reverse of that change in the <code>IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode</code> method. After the provider returns, the system then overwrites any public DEVMODEW settings that are represented in the print ticket but that are not explicitly disabled by the provider.</p>

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
<a href="print.iprintoemprintticketprovider_convertdevmodetoprintticket">IPrintOemPrintTicketProvider::ConvertDevModeToPrintTicket</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemPrintTicketProvider::ConvertPrintTicketToDevMode method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
