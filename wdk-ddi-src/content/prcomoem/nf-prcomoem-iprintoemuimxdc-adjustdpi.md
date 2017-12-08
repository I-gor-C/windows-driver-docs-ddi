---
UID: NF.prcomoem.IPrintOemUIMXDC.AdjustDPI
title: IPrintOemUIMXDC::AdjustDPI
author: windows-driver-content
description: The IPrintOemUIMXDC::AdjustDPI method enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of image resolution.
old-location: print\iprintoemuimxdc_adjustdpi.htm
old-project: print
ms.assetid: d725d917-08fb-4e11-824c-795e35782a06
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUIMXDC, AdjustDPI, IPrintOemUIMXDC::AdjustDPI
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: Available with Windows Vista and later versions of Unidrvui.dll and Ps5ui.dll, which are redistributable. This method is also available for XPSDrv drivers in Microsoft Windows XP if you have installed the XPS Essentials Pack.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintOemUIMXDC.AdjustDPI
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
req.iface: IPrintOemUIMXDC
req.product: Windows 10 or later.
---

# IPrintOemUIMXDC::AdjustDPI method



## -description
<p>The <code>IPrintOemUIMXDC::AdjustDPI</code> method enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of image resolution.</p>


## -syntax

````
HRESULT AdjustDPI(
         HANDLE   hPrinter,
         DWORD    cbDevMode,
   const PDEVMODE pDevMode,
         DWORD    cbOEMDM,
   const PVOID    pOEMDM,
         PLONG    pDPI
);
````


## -parameters
<dl>

### -param hPrinter 

<dd>
<p>A handle to the printer that is currently being queried.</p>
</dd>

### -param cbDevMode 

<dd>
<p>The size of the <a href="display.devmodew">DEVMODE</a> structure, including appended data.</p>
</dd>

### -param pDevMode 

<dd>
<p>A pointer to the DEVMODE structure that contains the current device settings.</p>
</dd>

### -param cbOEMDM 

<dd>
<p>The number of bytes in the vendor-provided section of the DEVMODE structure.</p>
</dd>

### -param pOEMDM 

<dd>
<p>A pointer to the data that is contained in the vendor portion of the DEVMODE structure that <i>pDevMode</i> points to.</p>
</dd>

### -param pDPI 

<dd>
<p>A pointer to the current resolution, in dots per inch (DPI), assuming square pixels. If this parameter is configured, its returned value must be a positive integer.</p>
</dd>
</dl>

## -returns
<p><code>AdjustDPI</code> returns S_OK if the method succeeds. Otherwise, this method should return E_NOTIMPL if the plug-in does not support the method, or any appropriate failure value if the plug-in cannot complete the operation. For more information, see the following Remarks section.</p>

## -remarks
<p>The <i>pDPI</i> parameter is IN OUT. All other parameters for this function are input only.</p>

<p>If the plug-in cannot complete the operation, it should return an appropriate failure HRESULT, which causes the current print job to fail.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available with Windows Vista and later versions of Unidrvui.dll and Ps5ui.dll, which are redistributable. This method is also available for XPSDrv drivers in Microsoft Windows XP if you have installed the XPS Essentials Pack.</p>
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