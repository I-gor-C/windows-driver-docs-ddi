---
UID: NF.prcomoem.IPrintOemUni3.GetPDEVAdjustment
title: IPrintOemUni3::GetPDEVAdjustment
author: windows-driver-content
description: The IPrintOemUni3::GetPDEVAdjustment method enables a plug-in to override specific PDEV settings.
old-location: print\iprintoemuni3_getpdevadjustment.htm
old-project: print
ms.assetid: bb7d7248-9520-4bc8-8483-b05b78608fc7
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUni3, GetPDEVAdjustment, IPrintOemUni3::GetPDEVAdjustment
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
req.alt-api: IPrintOemUni3.GetPDEVAdjustment
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

# IPrintOemUni3::GetPDEVAdjustment method



## -description
<p>The <code>IPrintOemUni3::GetPDEVAdjustment</code> method enables a plug-in to override specific <a href="wdkgloss.p#wdkgloss.pdev#wdkgloss.pdev"><i>PDEV</i></a> settings.</p>


## -syntax

````
HRESULT GetPDEVAdjustment(
        PDEVOBJ pdevobj,
        DWORD   dwAdjustType,
        PVOID   pBuf,
        DWORD   cbBuffer,
  [out] BOOL    *pbAdjustmentDone
);
````


## -parameters
<dl>

### -param <i>pdevobj</i> 

<dd>
<p>Pointer to a <a href="..\printoem\ns-printoem--devobj.md">DEVOBJ</a> structure.</p>
</dd>

### -param <i>dwAdjustType</i> 

<dd>
<p>Specifies the type of adjustment asked for. The following flags are currently supported.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>PDEV_ADJUST_GRAPHICS_RESOLUTION_TYPE</p>
</td>
<td>
<p>Adjust the graphics resolution setting that is reported in the PDEV structure. For more information, see the <a href="..\printoem\ns-printoem--pdev-adjust-graphics-resolution.md">PDEV_ADJUST_GRAPHICS RESOLUTION</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p>PDEV_IMAGEABLE_ORIGIN_AREA_TYPE</p>
</td>
<td>
<p>Adjust the imageable origin area that is reported in the PDEV structure. For more information, see the <a href="..\printoem\ns-printoem--pdev-adjust-imageable-origin-area.md">PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p>PDEV_ADJUST_PHYSICAL_PAPER_SIZE_TYPE</p>
</td>
<td>
<p>Adjust the physical paper size that is reported in the PDEV structure. For more information, see the <a href="print.pdev_adjust_paper_physical_size">PDEV_ADJUST_PAPER_PHYSICAL_SIZE</a> structure.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>pBuf</i> 

<dd>
<p>Pointer to a structure that contains the planned settings that are used if there is no change. These structures are listed in the preceding table. The plug-in can overwrite the settings in the relevant structure.</p>
</dd>

### -param <i>cbBuffer</i> 

<dd>
<p>Specifies the size, in bytes, of the structure pointed to by <i>pBuf</i>.</p>
</dd>

### -param <i>pbAdjustmentDone</i> [out]

<dd>
<p>Pointer to a memory location that the plug-in sets to <b>TRUE</b> when it actually changes a value in the buffer. This may be used by the driver for optimizations.</p>
</dd>
</dl>

## -returns
<p>The <code>IPrintOemUni3::GetPDEVAdjustment</code> method should return S_OK if it recognizes the adjustment type, and S_FALSE if it does not. If the method fails, it should return E_FAIL. The chain of plug-ins is called until either S_OK or a failure code other than E_NOTIMPL is returned. That is, the chain of plug-ins is called until the first plug-in that is capable of handling the adjustment is found.</p>

## -remarks
<p>This function is available in Windows Vista and later.</p>

<p>Currently, the Unidrv driver calls <code>IPrintOemUni3::GetPDEVAdjustment</code> to adjust the graphics resolution setting, as reported in the PDEV, to adjust the imageable origin area, or to adjust the physical paper size.</p>

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
<a href="..\printoem\ns-printoem--pdev-adjust-graphics-resolution.md">PDEV_ADJUST_GRAPHICS RESOLUTION</a>
</dt>
<dt>
<a href="..\printoem\ns-printoem--pdev-adjust-imageable-origin-area.md">PDEV_ADJUST_IMAGEABLE_ORIGIN_AREA</a>
</dt>
<dt>
<a href="..\printoem\ns-printoem--pdev-adjust-paper-margin.md">PDEV_ADJUST_PAPER_MARGIN</a>
</dt>
<dt>
<a href="print.pdev_adjust_paper_physical_size">PDEV_ADJUST_PAPER_PHYSICAL_SIZE</a>
</dt>
<dt>
<a href="..\printoem\ns-printoem--pdev-hostfont-enabled.md">PDEV_HOSTFONT_ENABLED</a>
</dt>
<dt>
<a href="..\printoem\ns-printoem--pdev-use-true-color.md">PDEV_USE_TRUE_COLOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUni3::GetPDEVAdjustment method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
