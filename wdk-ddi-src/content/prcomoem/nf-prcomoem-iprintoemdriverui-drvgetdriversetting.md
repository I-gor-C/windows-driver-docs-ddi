---
UID: NF.prcomoem.IPrintOemDriverUI.DrvGetDriverSetting
title: IPrintOemDriverUI::DrvGetDriverSetting
author: windows-driver-content
description: The IPrintOemDriverUI::DrvGetDriverSetting method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can obtain the current status of printer features and other internal information.
old-location: print\iprintoemdriverui_drvgetdriversetting.htm
ms.assetid: 25e8aec7-86af-4753-83d7-e7df5435f602
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemDriverUI.DrvGetDriverSetting
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
ms.keywords: IPrintOemDriverUI, DrvGetDriverSetting, IPrintOemDriverUI::DrvGetDriverSetting
req.iface: IPrintOemDriverUI
req.product: Windows 10 or later.
---

# IPrintOemDriverUI::DrvGetDriverSetting method



## -description
<p>The <code>IPrintOemDriverUI::DrvGetDriverSetting</code> method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can obtain the current status of printer features and other internal information.</p>


## -syntax

````
HRESULT DrvGetDriverSetting(
   PVOID  pci,
   PCSTR  Feature,
   PVOID  pOutput,
   DWORD  cbSize,
   PDWORD pcbNeeded,
   PDWORD pdwOptionsReturned
);
````


## -parameters
<dl>

### -param <i>pci</i> 

<dd>
<p>Caller-supplied pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559571">OEMUIOBJ</a> structure.</p>
</dd>

### -param <i>Feature</i> 

<dd>
<p>Caller-supplied value identifying the printer feature for which option settings are returned. This can be either a string pointer or a constant, as described in the following Remarks section.</p>
</dd>

### -param <i>pOutput</i> 

<dd>
<p>Caller-supplied pointer to a buffer to receive the specified information.</p>
</dd>

### -param <i>cbSize</i> 

<dd>
<p>Caller-supplied size, in bytes, of the buffer pointed to by <i>pOutput</i>.</p>
</dd>

### -param <i>pcbNeeded</i> 

<dd>
<p>Caller-supplied pointer to a location to receive the minimum buffer size required to contain the requested information.</p>
</dd>

### -param <i>pdwOptionsReturned</i> 

<dd>
<p>Caller-supplied pointer to a location to receive the number of option strings placed in <i>pOutput</i>.</p>
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
<p>When calling the <code>IPrintOemDriverUI::DrvGetDriverSetting</code> method, a user interface plug-in can specify either a string pointer or a constant value for <i>pFeatureKeyword</i>.</p>

<p>If <i>pFeatureKeyword</i> is a string, it must represent one of the following:<ul>
<li>A feature name specified in a <a href="https://msdn.microsoft.com/ebf12f61-6194-4033-92a2-2bbccc40a6fd">Unidrv minidriver</a> GPD file, or,</li>
<li>A keyword argument to an *<b>OpenUI</b> entry in a Pscript5 minidriver's PPD file.</li>
</ul>
</p>

<p>The method returns one or more NULL-terminated strings in the buffer pointed to by <i>pOutput</i>. Each string represents the name of a currently selected option.The number of strings is returned in <i>pdwOptionsReturned</i>.</p>

<p>If <i>pFeatureKeyword</i> is a constant, it must be one of the <b>OEMGDS_</b>-prefixed constants defined in printoem.h. The method returns the value indicated by the specified constant by placing it in the buffer pointed to by <i>pOutput</i>. The value returned in <i>pdwOptionsReturned</i> is always 1.</p>

<p>When calling the <code>IPrintOemDriverUI::DrvGetDriverSetting</code> method, a user interface plug-in can specify either a string pointer or a constant value for <i>pFeatureKeyword</i>.</p>

<p>If <i>pFeatureKeyword</i> is a string, it must represent one of the following:<ul>
<li>A feature name specified in a <a href="https://msdn.microsoft.com/ebf12f61-6194-4033-92a2-2bbccc40a6fd">Unidrv minidriver</a> GPD file, or,</li>
<li>A keyword argument to an *<b>OpenUI</b> entry in a Pscript5 minidriver's PPD file.</li>
</ul>
</p>

<p>The method returns one or more NULL-terminated strings in the buffer pointed to by <i>pOutput</i>. Each string represents the name of a currently selected option.The number of strings is returned in <i>pdwOptionsReturned</i>.</p>

<p>If <i>pFeatureKeyword</i> is a constant, it must be one of the <b>OEMGDS_</b>-prefixed constants defined in printoem.h. The method returns the value indicated by the specified constant by placing it in the buffer pointed to by <i>pOutput</i>. The value returned in <i>pdwOptionsReturned</i> is always 1.</p>

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