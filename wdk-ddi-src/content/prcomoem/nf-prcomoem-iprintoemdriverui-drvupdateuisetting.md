---
UID: NF.prcomoem.IPrintOemDriverUI.DrvUpdateUISetting
title: IPrintOemDriverUI::DrvUpdateUISetting
author: windows-driver-content
description: The IPrintOemDriverUI::DrvUpdateUISetting method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can notify the driver of a modified user interface option.
old-location: print\iprintoemdriverui_drvupdateuisetting.htm
old-project: print
ms.assetid: f5dec76e-16ad-4df0-b3c9-f0cbfb9b8c41
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemDriverUI, DrvUpdateUISetting, IPrintOemDriverUI::DrvUpdateUISetting
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
req.alt-api: IPrintOemDriverUI.DrvUpdateUISetting
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
req.iface: IPrintOemDriverUI
req.product: Windows 10 or later.
---

# IPrintOemDriverUI::DrvUpdateUISetting method



## -description
<p>The <code>IPrintOemDriverUI::DrvUpdateUISetting</code> method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can notify the driver of a modified user interface option.</p>


## -syntax

````
HRESULT DrvUpdateUISetting(
   PVOID pci,
   PVOID pOptItem,
   DWORD dwPreviousSelection,
   DWORD dwMode
);
````


## -parameters
<dl>

### -param <i>pci</i> 

<dd>
<p>Caller-supplied pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559571">OEMUIOBJ</a> structure.</p>
</dd>

### -param <i>pOptItem</i> 

<dd>
<p>Caller-supplied pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559656">OPTITEM</a> structure describing a user interface option item.</p>
</dd>

### -param <i>dwPreviousSelection</i> 

<dd>
<p>Not used.</p>
</dd>

### -param <i>dwMode</i> 

<dd>
<p>Caller-supplied integer constant indicating to which property sheet page the supplied option item belongs. The following constants are valid.</p>
<table>
<tr>
<th>Value</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>OEMCUIP_DOCPROP</p>
</td>
<td>
<p>The supplied option item belongs to the Advanced page of the document property sheet.</p>
</td>
</tr>
<tr>
<td>
<p>OEMCUIP_PRNPROP</p>
</td>
<td>
<p>The supplied option item belongs to the Device Settings page of the printer property sheet.</p>
</td>
</tr>
</table>
<p> </p>
<p>For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>If you are providing a user interface plug-in that implements the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554173">IPrintOemUI::DocumentPropertySheets</a> method or the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554165">IPrintOemUI::DevicePropertySheets</a> method, you typically also supply a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564313">_CPSUICALLBACK</a>-typed callback function to handle user modifications. This callback function must call <code>IPrintOemDriverUI::DrvUpdateUISetting</code> to inform the driver when the value associated with a user interface setting has been modified, if the value is stored in the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure (instead of the plug-in's private DEVMODEW members ) or in registry keys.</p>

<p>The value specified for <i>dwMode</i> should be based on which method specified the callback function.</p>

<p>If you are providing a user interface plug-in that implements the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554173">IPrintOemUI::DocumentPropertySheets</a> method or the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554165">IPrintOemUI::DevicePropertySheets</a> method, you typically also supply a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564313">_CPSUICALLBACK</a>-typed callback function to handle user modifications. This callback function must call <code>IPrintOemDriverUI::DrvUpdateUISetting</code> to inform the driver when the value associated with a user interface setting has been modified, if the value is stored in the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure (instead of the plug-in's private DEVMODEW members ) or in registry keys.</p>

<p>The value specified for <i>dwMode</i> should be based on which method specified the callback function.</p>

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