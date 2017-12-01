---
UID: NF.prcomoem.IPrintOemUni.HalftonePattern
title: IPrintOemUni::HalftonePattern
author: windows-driver-content
description: The IPrintOemUni::HalftonePattern method can be used with Unidrv-supported printers to create or modify a halftone pattern before it is used in a halftoning operation.
old-location: print\iprintoemuni_halftonepattern.htm
old-project: print
ms.assetid: 1b899492-f4a7-4c13-9e19-0f086b2b6b47
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUni, HalftonePattern, IPrintOemUni::HalftonePattern
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
req.alt-api: IPrintOemUni.HalftonePattern
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

# IPrintOemUni::HalftonePattern method



## -description
<p>The <code>IPrintOemUni::HalftonePattern</code> method can be used with Unidrv-supported printers to create or modify a halftone pattern before it is used in a halftoning operation.</p>


## -syntax

````
HRESULT HalftonePattern(
   PDEVOBJ pdevobj,
   PBYTE   pHTPattern,
   DWORD   dwHTPatternX,
   DWORD   dwHTPatternY,
   DWORD   dwHTNumPatterns,
   DWORD   dwCallbackID,
   PBYTE   pResource,
   DWORD   dwResourceSize
);
````


## -parameters
<dl>

### -param <i>pdevobj</i> 

<dd>
<p>Caller-supplied pointer to a <a href="..\printoem\ns-printoem--devobj.md">DEVOBJ</a> structure.</p>
</dd>

### -param <i>pHTPattern</i> 

<dd>
<p>Caller-supplied pointer to a buffer that receives the method-supplied halftone pattern. Buffer size, in bytes, is:</p>
<p>(((<i>dwHTPatternX</i> * <i>dwHTPatternY</i>) + 3)/4) * 4 * <i>dwHTNumPatterns</i>.</p>
</dd>

### -param <i>dwHTPatternX</i> 

<dd>
<p>Caller-supplied length, in pixels, of the halftone pattern, as specified by the first value in the <a href="wdkgloss.g#wdkgloss.generic_printer_description__gpd_#wdkgloss.generic_printer_description__gpd_"><i>GPD</i></a> file's *<b>HTPatternSize</b> attribute.</p>
</dd>

### -param <i>dwHTPatternY</i> 

<dd>
<p>Caller-supplied height, in pixels, of the halftone pattern, as specified by the second value in the GPD file's *<b>HTPatternSize</b> attribute.</p>
</dd>

### -param <i>dwHTNumPatterns</i> 

<dd>
<p>Caller-supplied number of patterns, as specified by the GPD file's *<b>HTNumPatterns</b> attribute. The number of patterns can be either 1 or 3.</p>
</dd>

### -param <i>dwCallbackID</i> 

<dd>
<p>Caller-supplied value identifying the halftone method, as specified by the GPD file's *<b>HTCallbackID</b> attribute.</p>
</dd>

### -param <i>pResource</i> 

<dd>
<p>Caller-supplied pointer to a buffer containing a halftone pattern, as specified by the GPD file's *<b>rcHTPatternID</b> attribute. This can be <b>NULL</b>.</p>
</dd>

### -param <i>dwResourceSize</i> 

<dd>
<p>Caller-supplied size of the halftone pattern contained in the buffer pointed to by <i>pResource</i>. This is zero if <i>pResource</i> is <b>NULL</b>.</p>
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
<p>The <code>IPrintOemUni::HalftonePattern</code> method is used to create or modify a halftone pattern before Unidrv passes it to GDI. Its purpose is to allow proprietary halftone patterns to be either stored as encrypted resources or generated at run time.</p>

<p>If the <code>IPrintOemUni::HalftonePattern</code> method is implemented, and if the GPD file entry for the currently selected halftoning method includes an *<b>HTCallbackID</b> attribute, Unidrv calls the <code>IPrintOemUni::HalftonePattern</code> method before passing a halftone pattern to GDI.</p>

<p>If the GPD file entry for the currently selected halftoning method contains an *rcHTPatternID entry identifying an RC_HTPATTERN resource, Unidrv obtains the pattern and passes a pointer to it as the <i>pResource</i> parameter value. This allows you to store the pattern as an encrypted resource, and to use the <code>IPrintOemUni::HalftonePattern</code> method to decode the pattern. The decoded pattern should be returned in the buffer pointed to by <i>pHTPattern</i>.</p>

<p>You can also use the <code>IPrintOemUni::HalftonePattern</code> method to generate a halftone pattern. In this case an RC_HTPATTERN resource is not needed, so <i>pResource</i> is <b>NULL</b>. The <code>IPrintOemUni::HalftonePattern</code> method should generate a pattern and return it in the buffer pointed to by <i>pHTPattern</i>.</p>

<p>If the <code>IPrintOemUni::HalftonePattern</code> method returns one pattern, it is used for all colors. If the method returns three patterns, they must be specified in RGB order.</p>

<p>The following example shows an implementation of a rendering plug-in's <code>HalftonePattern</code> method. The method calculates the length in bytes of the HTPattern_DDK pattern array, and then copies the bytes in the pattern array to the buffer pointed to by this method's <i>pHTPattern</i> parameter. The pattern array can contain either one or three patterns, depending on whether the pattern is used for all colors or has separate red, green, and blue patterns. For the sake of brevity, not all elements of the pattern array are listed. </p>

<p>An implementation of a <code>HalftonePattern</code> method in the rendering plug-in must be accompanied by a Halftone feature in the GPD file. The following GPD example shows a Halftone feature whose HT_PAT_DDK_16x16 option describes the customized pattern generated in the previous sample. </p>

<p>*Feature: Halftone</p>

<p>{</p>

<p>    *rcNameID: =HALFTONING_DISPLAY</p>

<p>    *HelpIndex: 12005</p>

<p>    *DefaultOption: HT_PATSIZE_AUTO</p>

<p>    *Option: HT_PATSIZE_AUTO</p>

<p>    {</p>

<p>        *rcNameID: =HT_AUTO_SELECT_DISPLAY</p>

<p>    }</p>

<p>    *Option: HT_PATSIZE_SUPERCELL_M</p>

<p>        *rcNameID: =HT_SUPERCELL_DISPLAY</p>

<p>    *Option: HT_PATSIZE_6x6_M</p>

<p>        *rcNameID: =HT_DITHER6X6_DISPLAY</p>

<p>    *Option: HT_PATSIZE_8x8_M</p>

<p>        *rcNameID: =HT_DITHER8X8_DISPLAY</p>

<p>    *Option: HT_PAT_DDK_16x16</p>

<p>        *Name: "DDK 16x16"</p>

<p>        *HTPatternSize: PAIR(16, 16)</p>

<p>        *HTNumPatterns: 1</p>

<p>        *HTCallbackID: 1</p>

<p>}</p>

<p>The <code>IPrintOemUni::HalftonePattern</code> method is optional. If a rendering plug-in implements this method, the plug-in's <a href="print.iprintoemuni_getimplementedmethod">IPrintOemUni::GetImplementedMethod</a> method must return S_OK when it receives "HalftonePattern" as input.</p>

<p>For more information about halftoning, see <a href="NULL">Customized Halftoning</a> and <a href="NULL">Option Attributes for the Halftone Feature</a>.</p>

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

## -see-also
<dl>
<dt>
<a href="print.iprintoemuni_imageprocessing">IPrintOemUni::ImageProcessing</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUni::HalftonePattern method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
