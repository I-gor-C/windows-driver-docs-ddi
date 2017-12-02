---
UID: NF.prcomoem.IPrintOemUni.EnablePDEV
title: IPrintOemUni::EnablePDEV
author: windows-driver-content
description: The IPrintOemUni::EnablePDEV method allows a rendering plug-in for Unidrv to create its own PDEV structure.
old-location: print\iprintoemuni_enablepdev.htm
old-project: print
ms.assetid: 93028b21-7995-42cd-af14-97e74ae75092
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUni, EnablePDEV, IPrintOemUni::EnablePDEV
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
req.alt-api: IPrintOemUni.EnablePDEV
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

# IPrintOemUni::EnablePDEV method



## -description
<p>The <code>IPrintOemUni::EnablePDEV</code> method allows a rendering plug-in for <a href="wdkgloss.u#wdkgloss.unidrv#wdkgloss.unidrv"><i>Unidrv</i></a> to create its own PDEV structure.</p>


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

### -param pdevobj 

<dd>
<p>Caller-supplied pointer to a <a href="..\printoem\ns-printoem--devobj.md">DEVOBJ</a> structure.</p>
</dd>

### -param pPrinterName 

<dd>
<p>Caller-supplied pointer to a text string representing the logical address of the printer.</p>
</dd>

### -param cPatterns 

<dd>
<p>Caller-supplied value representing the number of HSURF-typed surface handles contained in the buffer pointed to by <i>phsurfPatterns</i>.</p>
</dd>

### -param phsurfPatterns 

<dd>
<p>Caller-supplied pointer to a buffer that is large enough to contain <i>cPatterns</i> number of HSURF-typed surface handles. The handles represent surface fill patterns.</p>
</dd>

### -param cjGdiInfo 

<dd>
<p>Caller-supplied value representing the size of the structure pointed to by <i>pGdiInfo</i>.</p>
</dd>

### -param pGdiInfo 

<dd>
<p>Caller-supplied pointer to a <a href="display.gdiinfo">GDIINFO</a> structure.</p>
</dd>

### -param cjDevInfo 

<dd>
<p>Caller-supplied value representing the size of the structure pointed to by <i>pDevInfo</i>.</p>
</dd>

### -param pDevInfo 

<dd>
<p>Caller-supplied pointer to a <a href="display.devinfo">DEVINFO</a> structure.</p>
</dd>

### -param pded 

<dd>
<p>Caller-supplied pointer to a <a href="display.drvenabledata">DRVENABLEDATA</a> structure containing the addresses of the printer driver's graphics DDI hooking functions. For more information, see the following Remarks section.</p>
</dd>

### -param pDevOem [out]

<dd>
<p>Receives a method-supplied pointer to a private PDEV structure. (For more information, see the following Remarks section.)</p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed</p>

<p> </p>

<p>If the operation fails, the method should call <b>SetLastError</b> to set an error code.</p>

## -remarks
<p>A rendering plug-in for Unidrv must implement the <code>IPrintOemUni::EnablePDEV</code> method.</p>

<p>The <code>IPrintOemUni::EnablePDEV</code> method performs the same types of operations as the <a href="display.drvenablepdev">DrvEnablePDEV</a> function that is exported by a printer graphics DLL. Its purpose is to allow a rendering plug-in to create its own PDEV structure. (For more information about PDEV structures, see <a href="https://msdn.microsoft.com/e5c51b9a-5f73-4411-88d8-931981a8450c">Customized PDEV Structures</a>.)</p>

<p>If you provide a rendering plug-in that exports the <code>IPrintOemUni::EnablePDEV</code> method, Undrv's printer graphics DLL calls the method from within its <a href="display.drvenablepdev">DrvEnablePDEV</a> function.</p>

<p>The <code>IPrintOemUni::EnablePDEV</code> method should allocate an instance of its private PDEV structure, initialize it, and return its address as the method's <i>pDevOem</i> parameter. Other plug-in methods receive the address as the <i>pdevOEM</i> member of the <a href="..\printoem\ns-printoem--devobj.md">DEVOBJ</a> structure.</p>

<p>The <b>pdevOEM</b> member of the DEVOBJ structure is not used with the <code>IPrintOemUni::EnablePDEV</code> method.</p>

<p>The structures pointed to by the <i>phsurfPatterns</i>, <i>pGdiInfo</i>, and <i>pDevInfo</i> parameter values are the same ones that Unidrv's <b>DrvEnablePDEV</b> function receives. The rendering plug-in can modify the structure contents as necessary. It can supply surface fill patterns by obtaining HSURF-typed surface handles and placing them in the buffer pointed to by <i>phsurfPatterns</i>. Fill pattern types and handle order are listed in the description of <a href="display.drvenablepdev">DrvEnablePDEV</a>.</p>

<p>The <a href="display.drvenabledata">DRVENABLEDATA</a> structure pointed to by <i>pded</i> contains the addresses of graphics DDI functions provided Unidrv's printer graphics DLL. You are allowed to provide customized hooking functions in your plug-in for these graphics DDI functions. The DRVENABLEDATA structure's contents enable your customized hooking functions to call back to the driver's graphics DDI functions. For more information, see <a href="https://msdn.microsoft.com/33d7d567-5371-4873-a4ef-cd2b06f65d73">Customized Graphics DDI Functions</a>.</p>

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