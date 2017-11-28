---
UID: NF.prcomoem.IPrintOemUni.DisableDriver
title: IPrintOemUni::DisableDriver
author: windows-driver-content
description: The IPrintOemuNI::DisableDriver method allows a rendering plug-in for Unidrv to free resources that were allocated by the plug-in's IPrintOemUni::EnableDriver method.
old-location: print\iprintoemuni_disabledriver.htm
old-project: print
ms.assetid: a92d8c2e-52b5-4941-b49e-42e067e56e91
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUni, DisableDriver, IPrintOemUni::DisableDriver
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
req.alt-api: IPrintOemUni.DisableDriver
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
req.iface: IPrintOemUni
req.product: Windows 10 or later.
---

# IPrintOemUni::DisableDriver method



## -description
<p>The <code>IPrintOemuNI::DisableDriver</code> method allows a rendering plug-in for <a href="wdkgloss.u#wdkgloss.unidrv#wdkgloss.unidrv"><i>Unidrv</i></a> to free resources that were allocated by the plug-in's <a href="https://msdn.microsoft.com/library/windows/hardware/ff554248">IPrintOemUni::EnableDriver</a> method.</p>


## -syntax

````
STDMETHOD DisableDriver(
    None
);
````


## -parameters
<dl>

### -param <i>None</i> 

<dd></dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed</p>

<p> </p>

## -remarks
<p>A rendering plug-in for Unidrv must implement the <code>IPrintOemUni::DisableDriver</code> method.</p>

<p>The <code>IPrintOemUni::DisableDriver</code> method, provided by rendering plug-ins for Unidrv, performs the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556196">DrvDisableDriver</a> function that is exported by Unidrv's printer graphics DLL.</p>

<p><code>IPrintOemUni::DisableDriver</code> and <b>IPrintOemUni::EnableDriver</b> must be implemented as a pair. If you implement one, you must implement the other. For more information, see the Remarks section in <a href="https://msdn.microsoft.com/library/windows/hardware/ff554248">IPrintOemUni::EnableDriver</a>. </p>

<p>This is the last <b>IPrintOemUni</b> interface method that is called before the rendering plug-in is unloaded.</p>

<p>A rendering plug-in for Unidrv must implement the <code>IPrintOemUni::DisableDriver</code> method.</p>

<p>The <code>IPrintOemUni::DisableDriver</code> method, provided by rendering plug-ins for Unidrv, performs the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556196">DrvDisableDriver</a> function that is exported by Unidrv's printer graphics DLL.</p>

<p><code>IPrintOemUni::DisableDriver</code> and <b>IPrintOemUni::EnableDriver</b> must be implemented as a pair. If you implement one, you must implement the other. For more information, see the Remarks section in <a href="https://msdn.microsoft.com/library/windows/hardware/ff554248">IPrintOemUni::EnableDriver</a>. </p>

<p>This is the last <b>IPrintOemUni</b> interface method that is called before the rendering plug-in is unloaded.</p>

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