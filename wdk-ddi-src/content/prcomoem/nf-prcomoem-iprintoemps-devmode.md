---
UID: NF.prcomoem.IPrintOemPS.DevMode
title: IPrintOemPS::DevMode
author: windows-driver-content
description: The IPrintOemPS::DevMode method, provided by rendering plug-ins for Pscript5, performs operations on private DEVMODEW members.
old-location: print\iprintoemps_devmode.htm
old-project: print
ms.assetid: 72775113-435c-44cf-83e7-9aa62f7f252e
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemPS, DevMode, IPrintOemPS::DevMode
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
req.alt-api: IPrintOemPS.DevMode
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

# IPrintOemPS::DevMode method



## -description
<p>The <code>IPrintOemPS::DevMode</code> method, provided by rendering plug-ins for Pscript5, performs operations on private <a href="display.devmodew">DEVMODEW</a> members.</p>


## -syntax

````
STDMETHOD DevMode(
   DWORD       dwMode,
   POEMDMPARAM pOemDMParam
);
````


## -parameters
<dl>

### -param dwMode 

<dd>
<p>Caller-supplied constant. See the following Remarks section.</p>
</dd>

### -param pOemDMParam 

<dd>
<p>Caller-supplied pointer to an <a href="..\printoem\ns-printoem--oemdmparam.md">OEMDMPARAM</a> structure.</p>
</dd>
</dl>

## -returns
<p>This method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>The method is not implemented.</p>

<p> </p>

## -remarks
<p>If you are providing a user interface plug-in for Pscript5, and if you are adding private members to the driver's DEVMODEW structure, you must implement both the <code>IPrintOemUI::DevMode</code> and the <code>IPrintOemPS::DevMode</code> methods. The code implementing these methods must be identical and can be placed in a library that is statically linked to both the UI plug-in and the rendering plug-in.</p>

<p>For a description of the <code>IPrintOemPS::DevMode</code> method, see <a href="print.iprintoemui_devmode">IPrintOemUI::DevMode</a>.</p>

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