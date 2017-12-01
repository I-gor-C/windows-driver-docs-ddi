---
UID: NF.prcomoem.IPrintOemUni.OutputCharStr
title: IPrintOemUni::OutputCharStr
author: windows-driver-content
description: The IPrintOemUni::OutputCharStr method enables a rendering plug-in to control the printing of font glyphs.
old-location: print\iprintoemuni_outputcharstr.htm
old-project: print
ms.assetid: 73518253-d65a-40ab-8735-44e92fbbed57
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUni, OutputCharStr, IPrintOemUni::OutputCharStr
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
req.alt-api: IPrintOemUni.OutputCharStr
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
req.iface: IPrintOemUni
req.product: Windows 10 or later.
---

# IPrintOemUni::OutputCharStr method



## -description
<p>The <code>IPrintOemUni::OutputCharStr</code> method enables a rendering plug-in to control the printing of font glyphs.</p>


## -syntax

````
HRESULT OutputCharStr(
   PDEVOBJ     pdevobj,
   PUNIFONTOBJ pUFObj,
   DWORD       dwType,
   DWORD       dwCount,
   PVOID       pGlyph
);
````


## -parameters
<dl>

### -param <i>pdevobj</i> 

<dd>
<p>Caller-supplied pointer to a <a href="..\printoem\ns-printoem--devobj.md">DEVOBJ</a> structure.</p>
</dd>

### -param <i>pUFObj</i> 

<dd>
<p>Caller-supplied pointer to a <a href="..\printoem\ns-printoem--unifontobj.md">UNIFONTOBJ</a> structure.</p>
</dd>

### -param <i>dwType</i> 

<dd>
<p>Caller-supplied value indicating the type of glyph specifier array pointed to by <i>pGlyph</i>. Valid values are as follows:</p>
<table>
<tr>
<th>Value</th>
<th>Definition</th>
</tr>
<tr>
<td>
<p>TYPE_GLYPHHANDLE</p>
</td>
<td>
<p>The <i>pGlyph</i> array elements are glyph handles of type HGLYPH.</p>
</td>
</tr>
<tr>
<td>
<p>TYPE_GLYPHID</p>
</td>
<td>
<p>The <i>pGlyph</i> array elements are glyph identifiers of type DWORD.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>dwCount</i> 

<dd>
<p>Caller-supplied value representing the number of glyph specifiers in the array pointed to by <i>pGlyph</i>.</p>
</dd>

### -param <i>pGlyph</i> 

<dd>
<p>Caller-supplied pointer to an array of glyph specifiers, where the array element type is indicated by <i>dwType</i>.</p>
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
<p>The <code>IPrintOemUni::OutputCharStr</code> method is used for supporting printers that do not recognize the <a href="wdkgloss.p#wdkgloss.pcl#wdkgloss.pcl"><i>PCL</i></a>, CAPSL, or PPDS-formatted character output commands supported by Unidrv. Its purpose is to allow a rendering plug-in to control the printing of a font's glyphs, and to provide glyph substitutions if necessary.</p>

<p>If a rendering plug-in implements the <code>IPrintOemUni::OutputCharStr</code> method, Unidrv calls the method each time a string of characters is ready to be spooled.</p>

<p>The method receives an array of glyph specifiers. The value received for <i>dwType</i> indicates the identifier type.</p>

<p>If the specified font is a device font, the array contains glyph handles. The handles need to be translated to character codes or commands, and then sent to the print spooler to cause device glyphs to be printed.</p>

<p>If the specified font is a soft (TrueType) font, the array contains glyph identifiers. The identifiers represent previously downloaded glyphs that need to be printed.</p>

<p>If the specified font is a device font, the method must do the following:</p>

<p>Allocate a <a href="..\printoem\ns-printoem--getinfo-glyphstring.md">GETINFO_GLYPHSTRING</a> structure with <i>dwTypeIn</i> set to TYPE_GLYPHHANDLE and <i>dwTypeOut</i> set to TYPE_TRANSDATA.</p>

<p>Call the <a href="print.unifontobj_getinfo">UNIFONTOBJ_GetInfo</a> function, passing the GETINFO_GLYPHSTRING structure as input, to obtain glyph translations as <a href="..\prntfont\ns-prntfont--transdata.md">TRANSDATA</a> structure contents.</p>

<p>Call <a href="print.iprintoemdriveruni_drvwritespoolbuf">IPrintOemDriverUni::DrvWriteSpoolBuf</a> to send TRANSDATA structure contents to the print spooler, in order to print the glyphs.</p>

<p>If the specified font is a soft font, the method can just call <b>IPrintOemDriverUni::DrvWriteSpoolBuf</b> to send commands to the print spooler that will cause the specified previously-downloaded glyphs to be printed.</p>

<p>The <code>IPrintOemUni::OutputCharStr</code> method is optional. If a rendering plug-in implements this method, the plug-in's <a href="print.iprintoemuni_getimplementedmethod">IPrintOemUni::GetImplementedMethod</a> method must return S_OK when it receives "OutputCharStr" as input.</p>

<p>For additional information see <a href="NULL">Customized Font Management</a>.</p>

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