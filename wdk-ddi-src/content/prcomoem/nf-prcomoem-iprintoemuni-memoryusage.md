---
UID: NF.prcomoem.IPrintOemUni.MemoryUsage
title: IPrintOemUni::MemoryUsage
author: windows-driver-content
description: The IPrintOemUni::MemoryUsage method can be used with Unidrv-supported printers to specify the amount of memory required for use by a rendering plug-in's IPrintOemUni::ImageProcessing method.
old-location: print\iprintoemuni_memoryusage.htm
old-project: print
ms.assetid: bdf9c43d-d747-40e8-86ba-976f3f6a19d6
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintOemUni, MemoryUsage, IPrintOemUni::MemoryUsage
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
req.alt-api: IPrintOemUni.MemoryUsage
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

# IPrintOemUni::MemoryUsage method



## -description
<p>The <code>IPrintOemUni::MemoryUsage</code> method can be used with Unidrv-supported printers to specify the amount of memory required for use by a rendering plug-in's <a href="print.iprintoemuni_imageprocessing">IPrintOemUni::ImageProcessing</a> method.</p>


## -syntax

````
HRESULT MemoryUsage(
   PDEVOBJ         pdevobj,
   POEMMEMORYUSAGE pMemoryUsage
);
````


## -parameters
<dl>

### -param pdevobj 

<dd>
<p>Caller-supplied pointer to a <a href="..\printoem\ns-printoem--devobj.md">DEVOBJ</a> structure.</p>
</dd>

### -param pMemoryUsage 

<dd>
<p>Caller-supplied pointer to an <a href="..\printoem\nf-printoem-oemmemoryusage.md">OEMMEMORYUSAGE</a> structure.</p>
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
<p>The <code>IPrintOemUni::MemoryUsage</code> method's purpose is to help the Unidrv driver determine the optimum size for the GDI drawing surface, based on the memory requirements of the <a href="print.iprintoemuni_imageprocessing">IPrintOemUni::ImageProcessing</a> method. Implementation of the <code>IPrintOemUni::MemoryUsage</code> method is optional.</p>

<p>The <code>IPrintOemUni::MemoryUsage</code> method should return two values, as follows:</p>

<p>The amount of permanently-allocated, fixed-sized memory that the <b>IPrintOemUni::ImageProcessing</b> method needs to allocate.</p>

<p>This value is returned in the <b>dwFixedMemoryUsage</b> member of the <a href="..\printoem\nf-printoem-oemmemoryusage.md">OEMMEMORYUSAGE</a> structure.</p>

<p>The amount of memory required to hold a bitmap after the <b>IPrintOemUni::ImageProcessing</b> method has finished processing it.</p>

<p>The rendering plug-in either returns this processed bitmap to Unidrv, or spools it. The amount of memory required to store the processed bitmap is returned in the <b>dwPercentMemoryUsage</b> member of the OEMMEMORYUSAGE structure, and is expressed as a percentage of the source bitmap's size.</p>

<p>The value returned in the <b>dwPercentMemoryUsage</b> member should include, in addition to the processed bitmap's size, the amount of any additional memory allocations that are dependent on the size of the source bitmap.</p>

<p>The <b>dwMaxBandSize</b> member of the OEMMEMORYUSAGE structure is supplied by Unidrv and specifies the default maximum band size.</p>

<p>Before the Unidrv driver creates a drawing surface, it requests GDI to determine the optimum size for image banding bitmaps, based on available system memory. This optimum memory space must be shared, for each banding bitmap, between a source bitmap that is passed to the <b>IPrintOemUni::ImageProcessing</b> method and a (typically smaller) processed bitmap that the method either returns or outputs. Unidrv calls the rendering plug-in's <code>IPrintOemUni::MemoryUsage</code> method, if it exists, and uses the result to calculate how best to divide the optimum memory space.</p>

<p>For example, suppose GDI reports that the optimum amount of memory to use for drawing is 6 megabytes (contained in the OEMMEMORYUSAGE structure's <b>dwMaxBandSize</b> member), while the rendering plug-in's <code>IPrintOemUni::MemoryUsage</code> method returns values of zero for <b>dwFixedMemoryUsage</b> and 50 for <b>dwPercentMemoryUsage</b>. The value of 50 means that the <b>IPrintOemUni::ImageProcessing</b> method's output bitmaps will be 50 percent smaller than the source bitmaps. Therefore, Unidrv will allocate a source bitmap size of 4 megabytes, thus causing output bitmaps to be 2 megabytes.</p>

<p>If an <code>IPrintOemUni::MemoryUsage</code> method is not provided, Unidrv allocates all the optimum available space to the source bitmap. This is acceptable if the <b>IPrintOemUni::ImageProcessing</b> method returns the processed bitmap in the memory space allocated for the source bitmap. However, if a rendering plug-in's <b>IPrintOemUni::ImageProcessing</b> method does allocate space for a destination bitmap but does not provide an <code>IPrintOemUni::MemoryUsage</code> method, the result is that more memory will be allocated for bitmaps than the optimum available size, potentially causing performance degradation.</p>

<p>The <code>IPrintOemUni::MemoryUsage</code> method is optional. If a rendering plug-in implements this method, the plug-in's <a href="print.iprintoemuni_getimplementedmethod">IPrintOemUni::GetImplementedMethod</a> method must return S_OK when it receives "MemoryUsage" as input.</p>

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
<dt>
<a href="..\printoem\nf-printoem-oemmemoryusage.md">OEMMEMORYUSAGE</a>
</dt>
<dt>
<a href="..\printoem\ns-printoem--devobj.md">DEVOBJ</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintOemUni::MemoryUsage method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
