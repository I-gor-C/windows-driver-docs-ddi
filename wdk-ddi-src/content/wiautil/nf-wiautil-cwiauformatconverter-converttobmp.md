---
UID: NF.wiautil.CWiauFormatConverter.ConvertToBmp
title: CWiauFormatConverter::ConvertToBmp
author: windows-driver-content
description: The CWiauFormatConverter::ConvertToBmp method converts an image to BMP format.
old-location: image\cwiauformatconverter_converttobmp.htm
ms.assetid: 9ac85fe9-bc44-4a70-9619-bb13e878bb49
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: wiautil.h
req.include-header: Wiautil.h, Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CWiauFormatConverter.ConvertToBmp
req.alt-loc: Wiautil.h
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
ms.keywords: CWiauFormatConverter, ConvertToBmp, CWiauFormatConverter::ConvertToBmp
req.iface: CWiauFormatConverter
req.product: Windows 10 or later.
---

# CWiauFormatConverter::ConvertToBmp method



## -description
<p>The <b>CWiauFormatConverter::ConvertToBmp</b> method converts an image to BMP format.</p>


## -syntax

````
HRESULT ConvertToBmp(
   BYTE           *pSource,
   INT            iSourceSize,
   BYTE           **ppDest,
   INT            *piDestSize,
   BMP_IMAGE_INFO *pBmpImageInfo,
   SKIP_AMOUNT    iSkipAmt = SKIP_OFF

);
````


## -parameters
<dl>

### -param <i>pSource</i> 

<dd>
<p>Points to the memory location containing the first byte of the source image.</p>
</dd>

### -param <i>iSourceSize</i> 

<dd>
<p>Specifies the size, in bytes, of the source image.</p>
</dd>

### -param <i>ppDest</i> 

<dd>
<p>Pointer to a memory location that receives the address of the resulting image.</p>
</dd>

### -param <i>piDestSize</i> 

<dd>
<p>Pointer to a memory location that receives the size, in bytes, of the resulting image.</p>
</dd>

### -param <i>pBmpImageInfo</i> 

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539403">BMP_IMAGE_INFO</a> structure that receives information about the resulting image.</p>
</dd>

### -param <i>iSkipAmt = SKIP_OFF
</i> 

<dd>
<p><i>Optional</i>. Specifies the amount of the BMP header to skip. The default value of this parameter denotes that none of the BMP header is skipped.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error.</p>

## -remarks
<p>The caller of this method can pass a result buffer in <i>ppDest</i> and the size in <i>piDestSize</i>. Alternatively, the caller can set *<i>ppDest</i> to <b>NULL</b> and *<i>piDestSize</i> to zero in the call to indicate that this method should allocate the memory. The caller is responsible for freeing the memory using the <b>delete []</b> operator.</p>

<p>The caller of this method can pass a result buffer in <i>ppDest</i> and the size in <i>piDestSize</i>. Alternatively, the caller can set *<i>ppDest</i> to <b>NULL</b> and *<i>piDestSize</i> to zero in the call to indicate that this method should allocate the memory. The caller is responsible for freeing the memory using the <b>delete []</b> operator.</p>

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
<p>Available in Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiautil.h (include Wiautil.h or Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539403">BMP_IMAGE_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548221">SKIP_AMOUNT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540379">CWiauFormatConverter::IsFormatSupported</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20CWiauFormatConverter::ConvertToBmp method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
