---
UID: NF.prcomoem.IPrintOemUni3.SetBandSize
title: IPrintOemUni3::SetBandSize
author: windows-driver-content
description: The IPrintOemUni3::SetBandSize method can be used with Unidrv-supported printers to specify the desired band size on the printed output.
old-location: print\iprintoemuni3_setbandsize.htm
old-project: print
ms.assetid: e75fdfa5-2b25-4d89-b3ef-40cb445f874f
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUni3, SetBandSize, IPrintOemUni3::SetBandSize
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
req.alt-api: IPrintOemUni3.SetBandSize
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
req.iface: IPrintOemUni3
req.product: Windows 10 or later.
---

# IPrintOemUni3::SetBandSize method



## -description
<p>The <code>IPrintOemUni3::SetBandSize</code> method can be used with Unidrv-supported printers to specify the desired band size on the printed output.</p>


## -syntax

````
HRESULT SetBandSize(
  [in] PDEVOBJ pdevobj,
  [in] INT     iFormat,
  [in] DWORD   dwPageWidthBytes,
  [in] DWORD   dwPageHeight,
  [in] DWORD   dwMaxHeight,
  [in] PDWORD  pdwRequiredHeight
);
````


## -parameters
<dl>

### -param pdevobj [in]

<dd>
<p>A caller-supplied pointer to a <a href="..\printoem\ns-printoem--devobj.md">DEVOBJ</a> structure.</p>
</dd>

### -param iFormat [in]

<dd>
<p>An integer value that specifies the format of the bitmap in terms of the number of bits of color information per pixel that are required. This parameter can be one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="BMF_1BPP"></a><a id="bmf_1bpp"></a><dl>

### -param BMF_1BPP

</dl>
</td>
<td width="60%">
<p>Monochrome</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BMF_4BPP"></a><a id="bmf_4bpp"></a><dl>

### -param BMF_4BPP

</dl>
</td>
<td width="60%">
<p>4 bits per pixel</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BMF_8BPP"></a><a id="bmf_8bpp"></a><dl>

### -param BMF_8BPP

</dl>
</td>
<td width="60%">
<p>8 bits per pixel</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BMF_16BPP"></a><a id="bmf_16bpp"></a><dl>

### -param BMF_16BPP

</dl>
</td>
<td width="60%">
<p>16 bits per pixel</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BMF_24BPP"></a><a id="bmf_24bpp"></a><dl>

### -param BMF_24BPP

</dl>
</td>
<td width="60%">
<p>24 bits per pixel</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BMF_32BPP"></a><a id="bmf_32bpp"></a><dl>

### -param BMF_32BPP

</dl>
</td>
<td width="60%">
<p>32 bits per pixel</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BMF_4RLE"></a><a id="bmf_4rle"></a><dl>

### -param BMF_4RLE

</dl>
</td>
<td width="60%">
<p>4 bits per pixel; run length encoded</p>
</td>
</tr>
<tr>
<td width="40%"><a id="BMF_8RLE"></a><a id="bmf_8rle"></a><dl>

### -param BMF_8RLE

</dl>
</td>
<td width="60%">
<p>8 bits per pixel; run length encoded</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param dwPageWidthBytes [in]

<dd>
<p>A Unidrv-supplied value that specifies the width of the printing area, in bytes.</p>
</dd>

### -param dwPageHeight [in]

<dd>
<p>A Unidrv-supplied value that specifies the height of the printing area, in pixels.</p>
</dd>

### -param dwMaxHeight [in]

<dd>
<p>A Unidrv-supplied value that specifies the maximum allowable height of the printing area, in pixels.</p>
</dd>

### -param pdwRequiredHeight [in]

<dd>
<p>A caller-supplied pointer to a DWORD that contains the height of the printing area, in pixels, required by the rendering plug-in.</p>
</dd>
</dl>

## -returns
<p>The method must return one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation succeeded. See Note.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>The operation failed. See Note.</p><dl>
<dt><b>E_NOTIMPL</b></dt>
</dl><p>Unidrv should compute the banding size.</p>

<p> </p>

## -remarks
<p>This method is available in Windows Vista and later.</p>

<p>This method is used by a rendering plug-in to specify band size using the plug-in's own calculations, rather than using Unidrv's band size calculations.</p>

<p>You can disable banding operations by Unidrv by setting the <i>dwPageHeight</i> value to *<i>pdwRequiredHeight</i>, but you should consider the performance effect of the height value that the rendering plug-in requests. For rendering, Unidrv needs at least the amount of memory that is calculated by multiplying <i>dwPageWidthBytes</i> by *<i>pdwRequiredHeight</i>. If the rendering plug-in supports the <a href="print.iprintoemuni_driverdms">IPrintOemUni::DriverDMS</a> method and that method returns "S_OK", <code>IPrintOemUni3::SetBandSize</code> is not called.</p>

<p>If this method is defined and the printer's generic printer description (GPD) file indicates that preanalysis is disabled (the GPD file includes "*<b>PreAnalysisOptions</b>: 0"), Unidrv calls this method to calculate band size. For information about the <b>PreAnalysisOptions</b> attribute, see <a href="https://msdn.microsoft.com/4c07145a-9a08-4507-8bab-769617e73d77">Preanalysis Infrastructure</a>.</p>

<p>If the rendering plug-in supports <a href="print.iprintoemuni_driverdms">IPrintOemUni::DriverDMS</a> and that method returns S_OK, <code>IPrintOemUni3::SetBandSize</code> is not called.</p>

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