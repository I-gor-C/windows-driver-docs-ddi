---
UID: NF.prcomoem.IPrintOemPS.EnablePDEV
title: IPrintOemPS::EnablePDEV
author: windows-driver-content
description: The IPrintOemPS::EnablePDEV method allows a rendering plug-in for Pscript5 to create its own PDEV structure.
old-location: print\iprintoemps_enablepdev.htm
ms.assetid: f284e89f-463e-4d04-8018-5ce02786d921
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
req.alt-api: IPrintOemPS.EnablePDEV
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
ms.keywords: IPrintOemPS, EnablePDEV, IPrintOemPS::EnablePDEV
req.iface: IPrintOemPS
req.product: Windows 10 or later.
---

# IPrintOemPS::EnablePDEV method



## -description
<p>The <code>IPrintOemPS::EnablePDEV</code> method allows a rendering plug-in for Pscript5 to create its own PDEV structure.</p>


## -syntax

````
STDMETHOD EnablePDEV(
        PDEVOBJ       pdevobj,
        PWSTR         pPrinterName,
        ULONG         cPatterns,
        HSURF         *phsurfPatterns,
        ULONG         cjGdiInfo,
        GDIINFO       *pGdiInfo,
        ULONG         cjDevInfo,
        DEVINFO       *pDevInfo,
        DRVENABLEDATA *pded,
  [out] PDEVOEM       *pDevOem
);
````


## -parameters
<dl>

### -param <i>pdevobj</i> 

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547573">DEVOBJ</a> structure.</p>
</dd>

### -param <i>pPrinterName</i> 

<dd>
<p>Caller-supplied pointer to a text string representing the logical address of the printer.</p>
</dd>

### -param <i>cPatterns</i> 

<dd>
<p>Caller-supplied value representing the number of HSURF-typed surface handles contained in the buffer pointed to by <i>phsurfPatterns</i>.</p>
</dd>

### -param <i>phsurfPatterns</i> 

<dd>
<p>Caller-supplied pointer to a buffer that is large enough to contain <i>cPatterns</i> number of HSURF-typed surface handles. The handles represent surface fill patterns.</p>
</dd>

### -param <i>cjGdiInfo</i> 

<dd>
<p>Caller-supplied value representing the size of the structure pointed to by <i>pGdiInfo</i>.</p>
</dd>

### -param <i>pGdiInfo</i> 

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff566484">GDIINFO</a> structure.</p>
</dd>

### -param <i>cjDevInfo</i> 

<dd>
<p>Caller-supplied value representing the size of the structure pointed to by <i>pDevInfo</i>.</p>
</dd>

### -param <i>pDevInfo</i> 

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552835">DEVINFO</a> structure.</p>
</dd>

### -param <i>pded</i> 

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556206">DRVENABLEDATA</a> structure containing the addresses of the printer driver's graphics DDI hooking functions. For more information, see the following Remarks section.</p>
</dd>

### -param <i>pDevOem</i> [out]

<dd>
<p>Receives a method-supplied pointer to a private PDEV structure. (For more information, see the following Remarks section.)</p>
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

<p>If the operation fails, the method should call <b>SetLastError</b> to set an error code.</p>

## -remarks
<p>The <code>IPrintOemPS::EnablePDEV</code> method performs the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556211">DrvEnablePDEV</a> function that is exported by a printer graphics DLL. Its purpose is to allow a rendering plug-in to create its own PDEV structure. (For more information about PDEV structures, see <a href="NULL">Customized PDEV Structures</a>.)</p>

<p>If you provide a rendering plug-in that exports the <code>IPrintOemPS::EnablePDEV</code> method, Pscript5's printer graphics DLL calls the method from within its <a href="https://msdn.microsoft.com/library/windows/hardware/ff556211">DrvEnablePDEV</a> function. </p>

<p>The <code>IPrintOemPS::EnablePDEV</code> method should allocate an instance of its private PDEV structure, initialize it, and return its address as the method's <i>pDevOem</i> parameter. Other plug-in methods receive the address as the <b>pdevOEM</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547573">DEVOBJ</a> structure.</p>

<p>The <b>pdevOEM</b> member of the DEVOBJ structure is not used with the <code>IPrintOemPS::EnablePDEV</code> method.</p>

<p>The structures pointed to by the <i>phsurfPatterns</i>, <i>pGdiInfo</i>, and <i>pDevInfo</i> parameter values are the same ones that Pscript5's <b>DrvEnablePDEV</b> function receives. The rendering plug-in can modify the structure contents as necessary. It can supply surface fill patterns by obtaining HSURF-typed surface handles and placing them in the buffer pointed to by <i>phsurfPatterns</i>. Fill pattern types and handle order are listed in the description of <a href="https://msdn.microsoft.com/library/windows/hardware/ff556211">DrvEnablePDEV</a>.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff556206">DRVENABLEDATA</a> structure pointed to by <i>pded</i> contains the addresses of graphics DDI functions provided by Pscript5's printer graphics DLL. You are allowed to provide customized hooking functions in your plug-in for these graphics DDI functions. The DRVENABLEDATA structure's contents enable your customized hooking functions to call back to the driver's graphics DDI functions. For more information, see <a href="NULL">Customized Graphics DDI Functions</a>.</p>

<p>The <code>IPrintOemPS::EnablePDEV</code> method performs the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556211">DrvEnablePDEV</a> function that is exported by a printer graphics DLL. Its purpose is to allow a rendering plug-in to create its own PDEV structure. (For more information about PDEV structures, see <a href="NULL">Customized PDEV Structures</a>.)</p>

<p>If you provide a rendering plug-in that exports the <code>IPrintOemPS::EnablePDEV</code> method, Pscript5's printer graphics DLL calls the method from within its <a href="https://msdn.microsoft.com/library/windows/hardware/ff556211">DrvEnablePDEV</a> function. </p>

<p>The <code>IPrintOemPS::EnablePDEV</code> method should allocate an instance of its private PDEV structure, initialize it, and return its address as the method's <i>pDevOem</i> parameter. Other plug-in methods receive the address as the <b>pdevOEM</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547573">DEVOBJ</a> structure.</p>

<p>The <b>pdevOEM</b> member of the DEVOBJ structure is not used with the <code>IPrintOemPS::EnablePDEV</code> method.</p>

<p>The structures pointed to by the <i>phsurfPatterns</i>, <i>pGdiInfo</i>, and <i>pDevInfo</i> parameter values are the same ones that Pscript5's <b>DrvEnablePDEV</b> function receives. The rendering plug-in can modify the structure contents as necessary. It can supply surface fill patterns by obtaining HSURF-typed surface handles and placing them in the buffer pointed to by <i>phsurfPatterns</i>. Fill pattern types and handle order are listed in the description of <a href="https://msdn.microsoft.com/library/windows/hardware/ff556211">DrvEnablePDEV</a>.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff556206">DRVENABLEDATA</a> structure pointed to by <i>pded</i> contains the addresses of graphics DDI functions provided by Pscript5's printer graphics DLL. You are allowed to provide customized hooking functions in your plug-in for these graphics DDI functions. The DRVENABLEDATA structure's contents enable your customized hooking functions to call back to the driver's graphics DDI functions. For more information, see <a href="NULL">Customized Graphics DDI Functions</a>.</p>

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