---
UID: NF.wiamdef.wiasWritePageBufToFile
title: wiasWritePageBufToFile
author: windows-driver-content
description: The wiasWritePageBufToFile function writes the contents of a temporary page buffer to an image file.
old-location: image\wiaswritepagebuftofile.htm
old-project: image
ms.assetid: aa04ef8c-5b69-4d7e-8af4-8cbdb680a23a
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: wiasWritePageBufToFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiamdef.h
req.include-header: Wiamdef.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiasWritePageBufToFile
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
req.iface: 
req.product: Windows 10 or later.
---

# wiasWritePageBufToFile function



## -description
<p>The <b>wiasWritePageBufToFile </b>function writes the contents of a temporary page buffer to an image file.</p>


## -syntax

````
HRESULT _stdcall wiasWritePageBufToFile(
  _In_ PMINIDRV_TRANSFER_CONTEXT pmdtc
);
````


## -parameters
<dl>

### -param pmdtc [in]

<dd>
<p>Pointer to a <a href="..\wiamindr_lh\ns-wiamindr-lh--minidrv-transfer-context.md">MINIDRV_TRANSFER_CONTEXT</a> structure.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Microsoft Windows SDK documentation).</p>

## -remarks
<p>The function writes data from a minidriver-allocated temporary page buffer to the image file opened by the WIA service. Minidrivers typically call this function after acquiring a page of data for which the minidriver allocated a temporary buffer.</p>

<p>This function is similar to <a href="..\wiamdef\nf-wiamdef-wiaswritebuftofile.md">wiasWriteBufToFile</a>, which can be used to write a buffer of image data to any type of image file. If a WIA minidriver intends to write a page of image data to a multipage TIFF file, including all appropriate tags, image file directory (IFD) entries, and other nonimage data, it should call this function, rather than <b>wiasWriteBufToFile</b>.</p>

<p>The expression <i>pmdtc</i>-&gt;<i>hFile</i> contains the handle to the file in TYMED_FILE (and TYMED_MULTIPAGE_FILE) transfers. This can be used to directly access the file that is being written to.</p>

<p>An example of how to use it is:</p>

<p>However, if you are considering using just the file handle in your TYMED_FILE and TYMED_MULTIPAGE_FILE transfers (to write data directly to the file using the file handle, instead of calling <b>wiasWritePageBufToFile</b>), use <a href="..\wiamdef\nf-wiamdef-wiaswritebuftofile.md">wiasWriteBufToFile</a>. This function performs the equivalent of:</p>

<p>This is essentially what you would do if you used the file handle directly. The advantage of the first example is that if the implementation was changed in a future release of WIA (for example, if the WIA service began using pipes instead of files, internally), the driver would not need to be updated.</p>

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
<a href="..\wiamindr_lh\ns-wiamindr-lh--minidrv-transfer-context.md">MINIDRV_TRANSFER_CONTEXT</a>
</dt>
<dt>
<a href="..\wiamdef\nf-wiamdef-wiaswritebuftofile.md">wiasWriteBufToFile</a>
</dt>
<dt>
<a href="..\wiamdef\nf-wiamdef-wiaswritepagebuftostream.md">wiasWritePageBufToStream</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiasWritePageBufToFile function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
