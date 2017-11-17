---
UID: NF.prcomoem.IPrintOemPS.EnableDriver
title: IPrintOemPS::EnableDriver
author: windows-driver-content
description: The IPrintOemPS::EnableDriver method allows a rendering plug-in for Pscript to hook out some graphics DDI functions.
old-location: print\iprintoemps_enabledriver.htm
ms.assetid: 12e65e91-f540-49fd-a723-c6b93708b166
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
req.alt-api: IPrintOemPS.EnableDriver
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
ms.keywords: IPrintOemPS, EnableDriver, IPrintOemPS::EnableDriver
req.iface: IPrintOemPS
req.product: Windows 10 or later.
---

# IPrintOemPS::EnableDriver method



## -description
<p>The <code>IPrintOemPS::EnableDriver</code> method allows a rendering plug-in for <a href="wdkgloss.p#wdkgloss.pscript#wdkgloss.pscript"><i>Pscript</i></a> to hook out some graphics DDI functions.</p>


## -syntax

````
STDMETHOD EnableDriver(
   DWORD          DriverVersion,
   DWORD          cbSize,
   PDRVENABLEDATA pded
);
````


## -parameters
<dl>

### -param <i>DriverVersion</i> 

<dd>
<p>Caller-supplied interface version number. This value is defined by PRINTER_OEMINTF_VERSION, in printoem.h.</p>
</dd>

### -param <i>cbSize</i> 

<dd>
<p>Caller-supplied size, in bytes, of the structure pointed to by <i>pded</i>.</p>
</dd>

### -param <i>pded</i> 

<dd>
<p>Caller-supplied pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556206">DRVENABLEDATA</a> structure.</p>
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

## -remarks
<p>The <code>IPrintOemPS::EnableDriver</code> method allows a rendering plug-in to perform the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556210">DrvEnableDriver</a> function that is exported by printer graphics DLLs.</p>

<p>Like the <b>DrvEnableDriver</b> function, the <code>IPrintOemPS::EnableDriver</code> method is responsible for providing addresses of internally supported graphics DDI functions, known as hooking functions. It can also perform other one-time initialization operations. Unlike the <b>DrvEnableDriver</b> function, implementation of the <code>IPrintOemPS::EnableDriver</code> method is optional. </p>

<p>The method should fill the supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff556206">DRVENABLEDATA</a> structure and allocate an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff556221">DRVFN</a> structures. It should fill the array with pointers to hooking functions, along with winddi.h-defined index values that identify the hooked out graphics DDI functions.</p>

<p>A rendering plug-in for Pscript5 can hook out a graphics DDI function only if the Pscript5 driver defines the function. The following graphics DDI functions are defined in Pscript5 and or Unidrv and can therefore be hooked out:</p><dl>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556176">DrvAlphaBlend</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556180">DrvBitBlt</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556182">DrvCopyBits</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556202">DrvDitherColor</a> (Unidrv only)</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556215">DrvEndDoc</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556217">DrvEscape</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556220">DrvFillPath</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556223">DrvFontManagement</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556230">DrvGetGlyphMode</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556236">DrvGradientFill</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556239">DrvIcmCreateColorTransform</a> (Pscript only)</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556241">DrvIcmDeleteColorTransform</a> (Pscript only)</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556245">DrvLineTo</a> (Unidrv only)</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556250">DrvNextBand</a> (Unidrv only)</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556258">DrvPlgBlt</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556260">DrvQueryDeviceSupport</a> (Pscript only)</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556259">DrvQueryAdvanceWidths</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556262">DrvQueryFont</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556264">DrvQueryFontData</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556266">DrvQueryFontTree</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556273">DrvRealizeBrush</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556281">DrvSendPage</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556292">DrvStartBanding</a> (Unidrv only)</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556296">DrvStartDoc</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556298">DrvStartPage</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556302">DrvStretchBlt</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556306">DrvStretchBltROP</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556311">DrvStrokeAndFillPath</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556316">DrvStrokePath</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557277">DrvTextOut</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557283">DrvTransparentBlt</a>
</dd>
</dl><p>If you provide a customized hooking function, it preempts the driver's equivalent graphics DDI function. Hooking functions can also call back into the driver's graphics DDI functions. For more information, see <a href="NULL">Customized Graphics DDI Functions</a>.</p>

<p>Customized hooking functions have the same input and output parameters as the equivalent graphics DDI function, with one exception - where graphics DDI functions receive PDEV pointers, customized hooking functions receive <a href="https://msdn.microsoft.com/library/windows/hardware/ff547573">DEVOBJ</a> pointers. There are two ways for these functions to receive PDEV pointers:</p>

<p>As the contents of the <b>dhpdev</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff569901">SURFOBJ</a> structure for the destination surface.</p>

<p>For the equivalent customized hooking function, the destination SURFOBJ structure's <b>dhpdev</b> member points to a DEVOBJ structure, and must be cast to type PDEVOBJ when referenced. An example graphics DDI function is <b>DrvBitBlt</b>.</p>

<p>As an input argument for a <i>dhpdev</i> parameter.</p>

<p>The equivalent customized hooking function must cast this input parameter to type PDEVOBJ when referencing it. An example graphics DDI function is <b>DrvDitherColor</b>.</p>

<p>Note that while a <a href="NULL">printer graphics DLL</a> includes the addresses of its <a href="https://msdn.microsoft.com/library/windows/hardware/ff556211">DrvEnablePDEV</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff556198">DrvDisablePDEV</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff556276">DrvResetPDEV</a> functions in the DRVENABLEDATA structure, a rendering plug-in for Pscript5 implements <b>EnablePDEV</b>, <b>DisablePDEV</b>, and <b>ResetPDEV</b> as methods of the <b>IPrintOemPS</b> interface and does not place their addresses in the DRVENABLEDATA structure.</p>

<p>If <code>IPrintOemPS::EnableDriver</code> methods are exported by multiple rendering plug-ins, the methods are called in the order that the plug-ins are specified for installation.</p>

<p>For more information about creating and installing rendering plug-ins, see <a href="NULL">Customizing Microsoft's Printer Drivers</a>.</p>

<p>The <code>IPrintOemPS::EnableDriver</code> method allows a rendering plug-in to perform the same types of operations as the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556210">DrvEnableDriver</a> function that is exported by printer graphics DLLs.</p>

<p>Like the <b>DrvEnableDriver</b> function, the <code>IPrintOemPS::EnableDriver</code> method is responsible for providing addresses of internally supported graphics DDI functions, known as hooking functions. It can also perform other one-time initialization operations. Unlike the <b>DrvEnableDriver</b> function, implementation of the <code>IPrintOemPS::EnableDriver</code> method is optional. </p>

<p>The method should fill the supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff556206">DRVENABLEDATA</a> structure and allocate an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff556221">DRVFN</a> structures. It should fill the array with pointers to hooking functions, along with winddi.h-defined index values that identify the hooked out graphics DDI functions.</p>

<p>A rendering plug-in for Pscript5 can hook out a graphics DDI function only if the Pscript5 driver defines the function. The following graphics DDI functions are defined in Pscript5 and or Unidrv and can therefore be hooked out:</p><dl>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556176">DrvAlphaBlend</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556180">DrvBitBlt</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556182">DrvCopyBits</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556202">DrvDitherColor</a> (Unidrv only)</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556215">DrvEndDoc</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556217">DrvEscape</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556220">DrvFillPath</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556223">DrvFontManagement</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556230">DrvGetGlyphMode</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556236">DrvGradientFill</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556239">DrvIcmCreateColorTransform</a> (Pscript only)</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556241">DrvIcmDeleteColorTransform</a> (Pscript only)</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556245">DrvLineTo</a> (Unidrv only)</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556250">DrvNextBand</a> (Unidrv only)</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556258">DrvPlgBlt</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556260">DrvQueryDeviceSupport</a> (Pscript only)</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556259">DrvQueryAdvanceWidths</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556262">DrvQueryFont</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556264">DrvQueryFontData</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556266">DrvQueryFontTree</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556273">DrvRealizeBrush</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556281">DrvSendPage</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556292">DrvStartBanding</a> (Unidrv only)</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556296">DrvStartDoc</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556298">DrvStartPage</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556302">DrvStretchBlt</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556306">DrvStretchBltROP</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556311">DrvStrokeAndFillPath</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556316">DrvStrokePath</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557277">DrvTextOut</a>
</dd>
<dd>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557283">DrvTransparentBlt</a>
</dd>
</dl><p>If you provide a customized hooking function, it preempts the driver's equivalent graphics DDI function. Hooking functions can also call back into the driver's graphics DDI functions. For more information, see <a href="NULL">Customized Graphics DDI Functions</a>.</p>

<p>Customized hooking functions have the same input and output parameters as the equivalent graphics DDI function, with one exception - where graphics DDI functions receive PDEV pointers, customized hooking functions receive <a href="https://msdn.microsoft.com/library/windows/hardware/ff547573">DEVOBJ</a> pointers. There are two ways for these functions to receive PDEV pointers:</p>

<p>As the contents of the <b>dhpdev</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff569901">SURFOBJ</a> structure for the destination surface.</p>

<p>For the equivalent customized hooking function, the destination SURFOBJ structure's <b>dhpdev</b> member points to a DEVOBJ structure, and must be cast to type PDEVOBJ when referenced. An example graphics DDI function is <b>DrvBitBlt</b>.</p>

<p>As an input argument for a <i>dhpdev</i> parameter.</p>

<p>The equivalent customized hooking function must cast this input parameter to type PDEVOBJ when referencing it. An example graphics DDI function is <b>DrvDitherColor</b>.</p>

<p>Note that while a <a href="NULL">printer graphics DLL</a> includes the addresses of its <a href="https://msdn.microsoft.com/library/windows/hardware/ff556211">DrvEnablePDEV</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff556198">DrvDisablePDEV</a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff556276">DrvResetPDEV</a> functions in the DRVENABLEDATA structure, a rendering plug-in for Pscript5 implements <b>EnablePDEV</b>, <b>DisablePDEV</b>, and <b>ResetPDEV</b> as methods of the <b>IPrintOemPS</b> interface and does not place their addresses in the DRVENABLEDATA structure.</p>

<p>If <code>IPrintOemPS::EnableDriver</code> methods are exported by multiple rendering plug-ins, the methods are called in the order that the plug-ins are specified for installation.</p>

<p>For more information about creating and installing rendering plug-ins, see <a href="NULL">Customizing Microsoft's Printer Drivers</a>.</p>

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