---
UID: NF.prcomoem.IPrintOemPS.DisableDriver
title: IPrintOemPS::DisableDriver
author: windows-driver-content
description: The IPrintOemPS::DisableDriver method allows a rendering plug-in for Pscript to free resources that were allocated by the plug-in's IPrintOemPS::EnableDriver method.
old-location: print\iprintoemps_disabledriver.htm
ms.assetid: 4fa25706-dc79-45fd-a805-7b9d110213ed
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
req.alt-api: IPrintOemPS.DisableDriver
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
ms.keywords: IPrintOemPS, DisableDriver, IPrintOemPS::DisableDriver
req.iface: IPrintOemPS
req.product: Windows 10 or later.
---

# IPrintOemPS::DisableDriver method



## -description
<p>The <code>IPrintOemPS::DisableDriver</code> method allows a rendering plug-in for <a href="wdkgloss.p#wdkgloss.pscript#wdkgloss.pscript"><i>Pscript</i></a> to free resources that were allocated by the plug-in's <a href="https://msdn.microsoft.com/library/windows/hardware/ff553212">IPrintOemPS::EnableDriver</a> method.</p>


## -syntax

````
STDMETHOD DisableDriver();
````


## -parameters


## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>The <code>IPrintOemPS::DisableDriver</code> method, provided by rendering plug-ins for Pscript5, performs the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556196">DrvDisableDriver</a> function that is exported by Pscript5's printer graphics DLL.</p>

<p><code>IPrintOemPS::DisableDriver</code> and <b>IPrintOemPS::EnableDriver</b> must be implemented as a pair. If you implement one, you must implement the other. For more information, see the Remarks section in <a href="https://msdn.microsoft.com/library/windows/hardware/ff553212">IPrintOemPS::EnableDriver</a>. </p>

<p>This is the last <b>IPrintOemPS</b> interface method that is called before the rendering plug-in is unloaded.</p>

<p>The <code>IPrintOemPS::DisableDriver</code> method, provided by rendering plug-ins for Pscript5, performs the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556196">DrvDisableDriver</a> function that is exported by Pscript5's printer graphics DLL.</p>

<p><code>IPrintOemPS::DisableDriver</code> and <b>IPrintOemPS::EnableDriver</b> must be implemented as a pair. If you implement one, you must implement the other. For more information, see the Remarks section in <a href="https://msdn.microsoft.com/library/windows/hardware/ff553212">IPrintOemPS::EnableDriver</a>. </p>

<p>This is the last <b>IPrintOemPS</b> interface method that is called before the rendering plug-in is unloaded.</p>

<p>The <code>IPrintOemPS::DisableDriver</code> method, provided by rendering plug-ins for Pscript5, performs the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556196">DrvDisableDriver</a> function that is exported by Pscript5's printer graphics DLL.</p>

<p><code>IPrintOemPS::DisableDriver</code> and <b>IPrintOemPS::EnableDriver</b> must be implemented as a pair. If you implement one, you must implement the other. For more information, see the Remarks section in <a href="https://msdn.microsoft.com/library/windows/hardware/ff553212">IPrintOemPS::EnableDriver</a>. </p>

<p>This is the last <b>IPrintOemPS</b> interface method that is called before the rendering plug-in is unloaded.</p>

<p>The <code>IPrintOemPS::DisableDriver</code> method, provided by rendering plug-ins for Pscript5, performs the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556196">DrvDisableDriver</a> function that is exported by Pscript5's printer graphics DLL.</p>

<p><code>IPrintOemPS::DisableDriver</code> and <b>IPrintOemPS::EnableDriver</b> must be implemented as a pair. If you implement one, you must implement the other. For more information, see the Remarks section in <a href="https://msdn.microsoft.com/library/windows/hardware/ff553212">IPrintOemPS::EnableDriver</a>. </p>

<p>This is the last <b>IPrintOemPS</b> interface method that is called before the rendering plug-in is unloaded.</p>

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