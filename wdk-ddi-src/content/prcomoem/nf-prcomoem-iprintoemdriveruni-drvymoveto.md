---
UID: NF.prcomoem.IPrintOemDriverUni.DrvYMoveTo
title: IPrintOemDriverUni::DrvYMoveTo
author: windows-driver-content
description: The IPrintOemDriverUni::DrvYMoveTo method is provided by the Unidrv driver so that a rendering plug-in can notify the driver of cursor y-position changes.
old-location: print\iprintoemdriveruni_drvymoveto.htm
ms.assetid: ce9b1622-4c02-4496-82ca-cefa49d531da
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
req.alt-api: IPrintOemDriverUni.DrvYMoveTo
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
ms.keywords: IPrintOemDriverUni, DrvYMoveTo, IPrintOemDriverUni::DrvYMoveTo
req.iface: IPrintOemDriverUni
req.product: Windows 10 or later.
---

# IPrintOemDriverUni::DrvYMoveTo method



## -description
<p>The <code>IPrintOemDriverUni::DrvYMoveTo</code> method is provided by the Unidrv driver so that a <a href="https://msdn.microsoft.com/e55ca083-2790-4929-9e5b-6fce49eb0404">rendering plug-in</a> can notify the driver of cursor y-position changes.</p>


## -syntax

````
HRESULT DrvYMoveTo(
        PDEVOBJ pdevobj,
        INT     y,
        DWORD   dwFlags,
  [out] INT     *piResult
);
````


## -parameters
<dl>

### -param <i>pdevobj</i> 

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547573">DEVOBJ</a> structure.</p>
</dd>

### -param <i>y</i> 

<dd>
<p>Caller-supplied value representing the number of units the cursor should be moved. The unit is defined by the MV_GRAPHICS flags in <i>dwFlags</i>.</p>
</dd>

### -param <i>dwFlags</i> 

<dd>
<p>One or more of the following caller-supplied bit flags:</p>
<table>
<tr>
<th>Flag</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>MV_GRAPHICS</p>
</td>
<td>
<p>If set, the <i>y</i> parameter's value is expressed in dots, based on the printer's current resolution. For example, if the y resolution is 150 DPI and <i>y</i> is 75, the movement is ?? inch.</p>
<p>If not set, the <i>y</i> parameter's value is expressed in master units. For example, if the y master unit is 600 and <i>y</i> is 300, the movement is ?? inch.</p>
</td>
</tr>
<tr>
<td>
<p>MV_PHYSICAL</p>
</td>
<td>
<p>If set, the <i>y</i> parameter's value is relative to the cursor origin.</p>
<p>If not set, the <i>y</i> parameter's value is relative to the printable area's origin.</p>
<p>Cannot be set if MV_RELATIVE is set.</p>
</td>
</tr>
<tr>
<td>
<p>MV_RELATIVE</p>
</td>
<td>
<p>If set, specifies that the cursor should be moved <i>y</i> units from its current position.</p>
<p>If not set, specifies that the cursor should be moved <i>y</i> units from its origin.</p>
</td>
</tr>
<tr>
<td>
<p>MV_UPDATE</p>
</td>
<td>
<p>If set, specifies that Unidrv should update its current calculation of the cursor position without actually moving the cursor. (Should be set if <a href="https://msdn.microsoft.com/library/windows/hardware/ff554261">IPrintOemUni::ImageProcessing</a> has moved the cursor.)</p>
<p>If not set, specifies that Unidrv should update its current calculation of the cursor position and also move the cursor.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>piResult</i> [out]

<dd>
<p>Receives the method-supplied result of subtracting the actual new cursor position from the requested new cursor position. This value might be zero, but it is always nonnegative.</p>
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
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff553141">IPrintOemDriverUni::DrvXMoveTo</a> and <code>IPrintOemDriverUni::DrvYMoveTo</code> methods allow a rendering plug-in to send image data to the printer spooler without causing the printer driver to lose track of the printer's cursor position. If you provide an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554261">IPrintOemUni::ImageProcessing</a> method that sends image data directly to the print spooler instead of returning it to the printer driver, the method should call <code>IPrintOemDriverUni::DrvXMoveTo</code> and <code>IPrintOemDriverUni::DrvYMoveTo</code>.</p>

<p>Either of two techniques can be used for updating the cursor position:</p>

<p>Whenever an <b>IPrintOemUni::ImageProcessing</b> method needs to update the cursor position, it can call <code>IPrintOemDriverUni::DrvXMoveTo</code> or <code>IPrintOemDriverUni::DrvYMoveTo</code> with the MV_UPDATE flag cleared. This causes Unidrv to send cursor commands to the print spooler and to update its internal calculation of the current cursor position.</p>

<p>The <b>IPrintOemUni::ImageProcessing</b> method can update the cursor by sending cursor commands directly to the print spooler. When the method has finished its spooling operation, it can call <code>IPrintOemDriverUni::DrvXMoveTo</code> or <code>IPrintOemDriverUni::DrvYMoveTo</code> with the MV_UPDATE flag set. This causes Unidrv to update its internal calculation of the current cursor position without sending cursor commands to the print spooler.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff553141">IPrintOemDriverUni::DrvXMoveTo</a> and <code>IPrintOemDriverUni::DrvYMoveTo</code> methods allow a rendering plug-in to send image data to the printer spooler without causing the printer driver to lose track of the printer's cursor position. If you provide an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554261">IPrintOemUni::ImageProcessing</a> method that sends image data directly to the print spooler instead of returning it to the printer driver, the method should call <code>IPrintOemDriverUni::DrvXMoveTo</code> and <code>IPrintOemDriverUni::DrvYMoveTo</code>.</p>

<p>Either of two techniques can be used for updating the cursor position:</p>

<p>Whenever an <b>IPrintOemUni::ImageProcessing</b> method needs to update the cursor position, it can call <code>IPrintOemDriverUni::DrvXMoveTo</code> or <code>IPrintOemDriverUni::DrvYMoveTo</code> with the MV_UPDATE flag cleared. This causes Unidrv to send cursor commands to the print spooler and to update its internal calculation of the current cursor position.</p>

<p>The <b>IPrintOemUni::ImageProcessing</b> method can update the cursor by sending cursor commands directly to the print spooler. When the method has finished its spooling operation, it can call <code>IPrintOemDriverUni::DrvXMoveTo</code> or <code>IPrintOemDriverUni::DrvYMoveTo</code> with the MV_UPDATE flag set. This causes Unidrv to update its internal calculation of the current cursor position without sending cursor commands to the print spooler.</p>

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