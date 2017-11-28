---
UID: NF.prcomoem.IPrintOemPS.ResetPDEV
title: IPrintOemPS::ResetPDEV
author: windows-driver-content
description: The IPrintOemPS::ResetPDEV method allows a rendering plug-in for Pscript5 to reset its PDEV structure.
old-location: print\iprintoemps_resetpdev.htm
old-project: print
ms.assetid: 10248026-471a-4419-9c96-3502c24a6e96
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemPS, ResetPDEV, IPrintOemPS::ResetPDEV
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
req.alt-api: IPrintOemPS.ResetPDEV
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
req.iface: IPrintOemPS
req.product: Windows 10 or later.
---

# IPrintOemPS::ResetPDEV method



## -description
<p>The <code>IPrintOemPS::ResetPDEV</code> method allows a rendering plug-in for Pscript5 to reset its PDEV structure.</p>


## -syntax

````
STDMETHOD ResetPDEV(
   PDEVOBJ pdevobjOld,
   PDEVOBJ pdevobjNew
);
````


## -parameters
<dl>

### -param <i>pdevobjOld</i> 

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547573">DEVOBJ</a> structure containing current PDEV information.</p>
</dd>

### -param <i>pdevobjNew</i> 

<dd>
<p>Caller-supplied pointer to a DEVOBJ structure into which the method should place new PDEV information.</p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

<p>If the operation fails it should call <b>SetLastError</b>.</p>

## -remarks
<p>A rendering plug-in's <code>IPrintOemPS::ResetPDEV</code> method performs the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556276">DrvResetPDEV</a> function that is exported by a printer graphics DLL. During the processing of an application's call to the Microsoft Windows SDK <b>ResetDC</b> function, the <code>IPrintOemPS::ResetPDEV</code> method is called by the <b>DrvResetPDEV</b> function in Pscript5's printer graphics DLL. For more information about when <b>DrvResetPDEV</b> is called, see its description.</p>

<p>The rendering plug-in's private PDEV structure's address is contained in the <b>pdevOEM</b> member of the DEVOBJ structure pointed to by <i>pdevobjOld</i>. The <code>IPrintOemPS::ResetPDEV</code> method should use relevant members of this old structure to fill in the new structure, which is referenced through <i>pdevobjNew</i>.</p>

<p>A rendering plug-in's <code>IPrintOemPS::ResetPDEV</code> method performs the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556276">DrvResetPDEV</a> function that is exported by a printer graphics DLL. During the processing of an application's call to the Microsoft Windows SDK <b>ResetDC</b> function, the <code>IPrintOemPS::ResetPDEV</code> method is called by the <b>DrvResetPDEV</b> function in Pscript5's printer graphics DLL. For more information about when <b>DrvResetPDEV</b> is called, see its description.</p>

<p>The rendering plug-in's private PDEV structure's address is contained in the <b>pdevOEM</b> member of the DEVOBJ structure pointed to by <i>pdevobjOld</i>. The <code>IPrintOemPS::ResetPDEV</code> method should use relevant members of this old structure to fill in the new structure, which is referenced through <i>pdevobjNew</i>.</p>

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