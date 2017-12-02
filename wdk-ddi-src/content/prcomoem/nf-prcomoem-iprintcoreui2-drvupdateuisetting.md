---
UID: NF.prcomoem.IPrintCoreUI2.DrvUpdateUISetting
title: IPrintCoreUI2::DrvUpdateUISetting
author: windows-driver-content
description: The IPrintCoreUI2::DrvUpdateUISetting method is provided by the Windows XP Pscript5 driver so that Pscript5 user interface plug-ins can notify the driver of a modified user interface option.
old-location: print\iprintcoreui2_drvupdateuisetting.htm
old-project: print
ms.assetid: 64cbb304-51f6-4db4-93cb-a64ea5e03599
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintCoreUI2, DrvUpdateUISetting, IPrintCoreUI2::DrvUpdateUISetting
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
req.alt-api: IPrintCoreUI2.DrvUpdateUISetting
req.alt-loc: Prcomoem.h
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
req.iface: IPrintCoreUI2
req.product: Windows 10 or later.
---

# IPrintCoreUI2::DrvUpdateUISetting method



## -description
<p>The <code>IPrintCoreUI2::DrvUpdateUISetting</code> method is provided by the Windows XP Pscript5 driver so that Pscript5 user interface plug-ins can notify the driver of a modified user interface option.</p>


## -syntax

````
STDMETHOD DrvUpdateUISetting(
   PVOID pci,
   PVOID pOptItem,
   DWORD dwPreviousSelection,
   DWORD dwMode
);
````


## -parameters
<dl>

### -param pci 

<dd>
<p>Caller-supplied pointer to an <a href="..\printoem\ns-printoem--oemuiobj.md">OEMUIOBJ</a> structure. </p>
</dd>

### -param pOptItem 

<dd>
<p>Caller-supplied pointer to an <a href="..\compstui\ns-compstui--optitem.md">OPTITEM</a> structure describing a user interface option item.</p>
</dd>

### -param dwPreviousSelection 

<dd>
<p>Not used. </p>
</dd>

### -param dwMode 

<dd>
<p>Caller-supplied integer constant indicating to which property sheet page the supplied option item belongs. The following constants are valid. </p>
<table>
<tr>
<th>Value</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>OEMCUIP_DOCPROP </p>
</td>
<td>
<p>The supplied option item belongs to the Advanced page of the document property sheet. </p>
</td>
</tr>
<tr>
<td>
<p>OEMCUIP_PRNPROP </p>
</td>
<td>
<p>The supplied option item belongs to the Device Settings page of the printer property sheet. </p>
</td>
</tr>
<tr>
<td>
<p>OEMCUIP_PRNPROP </p>
</td>
<td>
<p>The supplied option item belongs to the Device Settings page of the printer property sheet. </p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>This method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>This method is inherited from the <a href="https://msdn.microsoft.com/ed11789f-750d-4f29-b5e0-ab299a1388db">IPrintOemDriverUI COM Interface</a>, and can be called only by Windows XP Pscript5 UI plug-ins that do not fully replace the core driver's standard UI pages, and is supported during the UI plug-in's <a href="print.iprintoemui_documentpropertysheets">IPrintOemUI::DocumentPropertySheets</a> and <a href="print.iprintoemui_devicepropertysheets">IPrintOemUI::DevicePropertySheets</a> functions, and their property sheet callback routines. When this method is supported, it has the same behavior as <a href="print.iprintoemdriverui_drvupdateuisetting">IPrintOemDriverUI::DrvUpdateUISetting</a>. When it is not supported, this method should return E_NOTIMPL.</p>

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
<a href="print.iprintoemdriverui_drvupdateuisetting">IPrintOemDriverUI::DrvUpdateUISetting</a>
</dt>
<dt>
<a href="print.iprintoemui_documentpropertysheets">IPrintOemUI::DocumentPropertySheets</a>
</dt>
<dt>
<a href="print.iprintoemui_devicepropertysheets">IPrintOemUI::DevicePropertySheets</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreUI2::DrvUpdateUISetting method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
