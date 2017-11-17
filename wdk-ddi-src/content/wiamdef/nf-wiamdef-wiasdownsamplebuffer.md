---
UID: NF.wiamdef.wiasDownSampleBuffer
title: wiasDownSampleBuffer
author: windows-driver-content
description: The wiasDownSampleBuffer function takes in a buffer of DWORD-aligned pixel data and downsamples it (produces image data of lower resolution) to the specified size and resolution.
old-location: image\wiasdownsamplebuffer.htm
ms.assetid: 4581b852-f539-4cad-93fd-2638c885c2e7
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: wiamdef.h
req.include-header: Wiamdef.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiasDownSampleBuffer
req.alt-loc: Wiaservc.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wiaservc.lib
req.dll: Wiaservc.dll
req.irql: 
ms.keywords: wiasDownSampleBuffer
req.iface: 
req.product: Windows 10 or later.
---

# wiasDownSampleBuffer function



## -description
<p>The <b>wiasDownSampleBuffer</b> function takes in a buffer of DWORD-aligned pixel data and downsamples it (produces image data of lower resolution) to the specified size and resolution.</p>


## -syntax

````
HRESULT _stdcall wiasDownSampleBuffer(
          LONG                  lFlags,
  _Inout_ WIAS_DOWN_SAMPLE_INFO *pInfo
);
````


## -parameters
<dl>

### -param <i>lFlags</i> 

<dd>
<p>Specifies a set of flags that determine the behavior of this function. Currently, only the following flag is defined.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>WIAS_GET_DOWNSAMPLED_SIZE_ONLY</p>
</td>
<td>
<p>Do not copy the downsampled data to the destination buffer. Instead, set the following members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549546">WIAS_DOWN_SAMPLE_INFO</a> structure: <b>ulDownSampledHeight</b>, <b>ulDownSampleWidth</b>, <b>ulAlignedHeight</b>, <b>ulAlignedWidth</b>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>pInfo</i> [in, out]

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549546">WIAS_DOWN_SAMPLE_INFO</a> structure that contains all of the information needed for the downsampling operation.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Microsoft Windows SDK documentation).</p>

## -remarks
<p>The <b>wiasDownSampleBuffer</b> function can be used in either of the following two ways:</p>

<p>The caller specifies the downsampled (that is, output) width and height by setting the <b>ulDownSampledWidth</b> and <b>ulDownSampledHeight</b> members of the WIA_DOWN_SAMPLE_INFO structure.</p>

<p>The caller sets the <b>ulDownSampledWidth</b> and <b>ulDownSampledHeight</b> members of the WIA_DOWN_SAMPLE_INFO structure to zero, indicating that the function should choose the output width and height. </p>

<p>To see what output width and height values the function chooses, call this function with the <i>lFlags</i> parameter set to WIAS_GET_DOWNSAMPLED_SIZE_ONLY. On return, the <b>ulDownSampledWidth</b> and <b>ulDownSampledHeight</b> members are set to their new values. No downsampling is performed in this case.</p>

<p>The caller of this function is required to fill in the following members of the WIA_DOWN_SAMPLE_INFO structure:</p>

<p><b>ulOriginalWidth</b></p>

<p><b>ulOriginal Height</b></p>

<p><b>ulBitsPerPixel</b></p>

<p><b>ulXRes</b></p>

<p><b>ulYRes</b></p>

<p><b>pSrcBuffer</b></p>

<p>The caller can also specify the size of the downsampled data by filling in the following WIA_DOWN_SAMPLE_INFO structure members:</p>

<p><b>ulDownSampledWidth</b></p>

<p><b>ulDownSampledHeight</b></p>

<p>If the buffer that receives the downsampled data has already been allocated, the caller should fill in these WIA_DOWN_SAMPLE_INFO structure members:</p>

<p><b>ulDestBufSize</b></p>

<p><b>ulSrcBufSize</b></p>

<p><b>pDestBuffer</b></p>

<p>If the caller sets <b>pDestBuffer</b> to <b>NULL</b>, the destination buffer is allocated by the WIA service. On return from this function, <b>pDestBuffer</b> points to the destination buffer. The caller is responsible for freeing this memory when the operation is finished, and does this by calling <b>CoTaskMemFree</b> (described in the Microsoft Windows SDK documentation) on the buffer.</p>

<p>Because this function is not able to produce partial output lines, the number of scan lines in the input buffer must be an integer multiple of the scaling factor. For example, suppose the input buffer contains an image sampled at 600 dpi, which you intend to downsample to an equivalent 50 dpi image. In this case, you are scaling down the original image by a factor of 12 (because 600 / 50 = 12). This means that the function must receive 12 input lines for each output line that it produces. </p>

<p>More generally, if the original image has a resolution of R<i>in</i> dpi, and is to be scaled down to an image with a resolution of R<i>out</i> dpi, the scale-down factor is R<i>in</i> / R<i>out</i>, and the number of lines in the input buffer should be a multiple of R<i>in</i> / R<i>out</i>. If the scan head reaches the last band of the original image, and there are too few scan lines in the input buffer to produce an output line, pad the input buffer so that it contains the required number of data lines. Failure to do so causes unpredictable results, and can even result in a driver crash.</p>

<p>The <b>wiasDownSampleBuffer</b> function can be used in either of the following two ways:</p>

<p>The caller specifies the downsampled (that is, output) width and height by setting the <b>ulDownSampledWidth</b> and <b>ulDownSampledHeight</b> members of the WIA_DOWN_SAMPLE_INFO structure.</p>

<p>The caller sets the <b>ulDownSampledWidth</b> and <b>ulDownSampledHeight</b> members of the WIA_DOWN_SAMPLE_INFO structure to zero, indicating that the function should choose the output width and height. </p>

<p>To see what output width and height values the function chooses, call this function with the <i>lFlags</i> parameter set to WIAS_GET_DOWNSAMPLED_SIZE_ONLY. On return, the <b>ulDownSampledWidth</b> and <b>ulDownSampledHeight</b> members are set to their new values. No downsampling is performed in this case.</p>

<p>The caller of this function is required to fill in the following members of the WIA_DOWN_SAMPLE_INFO structure:</p>

<p><b>ulOriginalWidth</b></p>

<p><b>ulOriginal Height</b></p>

<p><b>ulBitsPerPixel</b></p>

<p><b>ulXRes</b></p>

<p><b>ulYRes</b></p>

<p><b>pSrcBuffer</b></p>

<p>The caller can also specify the size of the downsampled data by filling in the following WIA_DOWN_SAMPLE_INFO structure members:</p>

<p><b>ulDownSampledWidth</b></p>

<p><b>ulDownSampledHeight</b></p>

<p>If the buffer that receives the downsampled data has already been allocated, the caller should fill in these WIA_DOWN_SAMPLE_INFO structure members:</p>

<p><b>ulDestBufSize</b></p>

<p><b>ulSrcBufSize</b></p>

<p><b>pDestBuffer</b></p>

<p>If the caller sets <b>pDestBuffer</b> to <b>NULL</b>, the destination buffer is allocated by the WIA service. On return from this function, <b>pDestBuffer</b> points to the destination buffer. The caller is responsible for freeing this memory when the operation is finished, and does this by calling <b>CoTaskMemFree</b> (described in the Microsoft Windows SDK documentation) on the buffer.</p>

<p>Because this function is not able to produce partial output lines, the number of scan lines in the input buffer must be an integer multiple of the scaling factor. For example, suppose the input buffer contains an image sampled at 600 dpi, which you intend to downsample to an equivalent 50 dpi image. In this case, you are scaling down the original image by a factor of 12 (because 600 / 50 = 12). This means that the function must receive 12 input lines for each output line that it produces. </p>

<p>More generally, if the original image has a resolution of R<i>in</i> dpi, and is to be scaled down to an image with a resolution of R<i>out</i> dpi, the scale-down factor is R<i>in</i> / R<i>out</i>, and the number of lines in the input buffer should be a multiple of R<i>in</i> / R<i>out</i>. If the scan head reaches the last band of the original image, and there are too few scan lines in the input buffer to produce an output line, pad the input buffer so that it contains the required number of data lines. Failure to do so causes unpredictable results, and can even result in a driver crash.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamdef.h (include Wiamdef.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wiaservc.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Wiaservc.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549546">WIAS_DOWN_SAMPLE_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiasDownSampleBuffer function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
