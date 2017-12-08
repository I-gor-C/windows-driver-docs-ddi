---
UID: NS.wiamindr_lh._MINIDRV_TRANSFER_CONTEXT
title: MINIDRV_TRANSFER_CONTEXT
author: windows-driver-content
description: The MINIDRV_TRANSFER_CONTEXT structure is used to store image and other information needed for a memory-callback data transfer or a file data transfer.
old-location: image\minidrv_transfer_context.htm
old-project: image
ms.assetid: 26583873-4f84-4254-86c1-2063df85000c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: MINIDRV_TRANSFER_CONTEXT, MINIDRV_TRANSFER_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MINIDRV_TRANSFER_CONTEXT
req.alt-loc: wiamindr_lh.h
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
req.iface: IWiaMiniDrvTransferCallback
req.product: Windows 10 or later.
---

# MINIDRV_TRANSFER_CONTEXT structure



## -description
<p>The MINIDRV_TRANSFER_CONTEXT structure is used to store image and other information needed for a memory-callback data transfer or a file data transfer.</p>


## -syntax

````
typedef struct _MINIDRV_TRANSFER_CONTEXT {
  LONG                lSize;
  LONG                lWidthInPixels;
  LONG                lLines;
  LONG                lDepth;
  LONG                lXRes;
  LONG                lYRes;
  LONG                lCompression;
  GUID                guidFormatID;
  LONG                tymed;
  LONG_PTR            hFile;
  LONG                cbOffset;
  LONG                lBufferSize;
  LONG                lActiveBuffer;
  LONG                lNumBuffers;
  BYTE                *pBaseBuffer;
  BYTE                *pTransferBuffer;
  BOOL                bTransferDataCB;
  BOOL                bClassDrvAllocBuf;
  LONG_PTR            lClientAddress;
  IWiaMiniDrvCallBack *pIWiaMiniDrvCallBack;
  LONG                lImageSize;
  LONG                lHeaderSize;
  LONG                lItemSize;
  LONG                cbWidthInBytes;
  LONG                lPage;
  LONG                lCurIfdOffset;
  LONG                lPrevIfdOffset;
} MINIDRV_TRANSFER_CONTEXT, *PMINIDRV_TRANSFER_CONTEXT;
````


## -struct-fields
<dl>

### -field lSize

<dd>
<p>Specifies the size in bytes of this MINIDRV_TRANSFER_CONTEXT structure.</p>
</dd>

### -field lWidthInPixels

<dd>
<p>Specifies the width in pixels of the current image. The value of this member is derived from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551615">WIA_IPA_PIXELS_PER_LINE</a> common item property.</p>
</dd>

### -field lLines

<dd>
<p>Specifies the total number of lines (the number of horizontal rows of pixels) in the current image. The value of this member is derived from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551611">WIA_IPA_NUMBER_OF_LINES</a> common item property.</p>
</dd>

### -field lDepth

<dd>
<p>Specifies the color depth value of the current image in bits per pixel. The value of this member is derived from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551546">WIA_IPA_DEPTH</a> common item property.</p>
</dd>

### -field lXRes

<dd>
<p>Specifies the current horizontal resolution of the image in pixels per inch. The value of this member is derived from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552665">WIA_IPS_XRES</a> scanner item property.</p>
</dd>

### -field lYRes

<dd>
<p>Specifies the current vertical resolution of the image in pixels per inch. The value of this member is derived from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552673">WIA_IPS_YRES</a> scanner item property.</p>
</dd>

### -field lCompression

<dd>
<p>Specifies the type of compression used by the device. The value of this member is derived from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551540">WIA_IPA_COMPRESSION</a> common item property.</p>
</dd>

### -field guidFormatID

<dd>
<p>Specifies a GUID that indicates the data format for the device. The value of this member is derived from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551553">WIA_IPA_FORMAT</a> common item property.</p>
</dd>

### -field tymed

<dd>
<p>Specifies the type of data transfer. The data transfer specified can be either a memory-callback transfer (TYMED_CALLBACK or TYMED_MULTIPAGE_CALLBACK) or file transfer (TYMED_FILE or TYMED_MULTIPAGE_FILE). The value of this member is derived from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551656">WIA_IPA_TYMED</a> common item property. </p>
<p>This member conveys information related to that in the <b>bTransferDataCB</b> member. See <b>Remarks</b> for more information.</p>
</dd>

### -field hFile

<dd>
<p>Specifies the handle to the open file used during file transfers. The minidriver should not use this member. See <b>Remarks</b> for more information.</p>
</dd>

### -field cbOffset

<dd>
<p>Specifies the current offset in bytes of the next buffer location used during this transfer.</p>
</dd>

### -field lBufferSize

<dd>
<p>Specifies the total size of the transfer buffer.</p>
</dd>

### -field lActiveBuffer

<dd>
<p>Specifies which buffer is used for the current transfer. The value of this member must be in the range of 1 through <b>lNumBuffers</b>.</p>
</dd>

### -field lNumBuffers

<dd>
<p>Specifies the number of buffers available for data transfer. This value can currently be either 1 or 2.</p>
</dd>

### -field pBaseBuffer

<dd>
<p>Points to the start of the base transfer buffer.</p>
</dd>

### -field pTransferBuffer

<dd>
<p>Points to the start of the current transfer buffer. For a callback transfer in which double buffering is used, this member alternates between the two buffers, pointing to the beginning of the first buffer, and then to the beginning of the second, and so on.</p>
</dd>

### -field bTransferDataCB

<dd>
<p>Specifies whether a data transfer is a memory-callback transfer or a file transfer. This member is set to <b>TRUE</b> if the transfer is a memory-callback transfer, and <b>FALSE</b> if the transfer is a file transfer. For file transfers, the WIA service usually provides a callback routine, which enables the application to receive updates from the minidriver about the status of the file transfer. (The WIA service provides a callback routine if the application provides its own callback routine. See <a href="https://msdn.microsoft.com/a535d718-e34f-4cd0-9137-83d28d0b8e9c">IWiaMiniDrvCallback COM Interface</a> for details.) For file transfers, a minidriver should check the value stored in the <b>pIWiaMiniDrvCallBack</b> member. If that member is <b>NULL</b>, the WIA service does not provide a callback routine, so the driver must not attempt to call it. For memory-callback transfers, the WIA service always provides a callback.</p>
<p>This member conveys information related to that in the <b>tymed</b> member. See <b>Remarks</b> for more information.</p>
</dd>

### -field bClassDrvAllocBuf

<dd>
<p>Specifies whether the WIA service has allocated the transfer buffer. This value is <b>TRUE</b> if the WIA service allocated the buffer, and <b>FALSE</b> if not. In that case, it is the minidriver's responsibility to allocate the transfer buffer.</p>
</dd>

### -field lClientAddress

<dd>
<p>Specifies the address, in the client's address space, of the transfer. The minidriver must not change this value.</p>
</dd>

### -field pIWiaMiniDrvCallBack

<dd>
<p>Points to an <a href="image.iwiaminidrvcallback_interface">IWiaMiniDrvCallBack Interface</a> used for data or status callback transfer.</p>
</dd>

### -field lImageSize

<dd>
<p>Specifies the size, in bytes, of uncompressed bits in a single page.</p>
</dd>

### -field lHeaderSize

<dd>
<p>Specifies the size, in bytes, of image header data in a single page.</p>
</dd>

### -field lItemSize

<dd>
<p>Specifies the size, in bytes, of bits and header. This value can be zero if the item size is unknown before acquisition.</p>
</dd>

### -field cbWidthInBytes

<dd>
<p>Specifies the size, in bytes, of an image line.</p>
</dd>

### -field lPage

<dd>
<p>Specifies the page number of the current page when scanning a multipage TIFF image. Page numbering begins with zero.</p>
</dd>

### -field lCurIfdOffset

<dd>
<p>Specifies the image file directory (IFD) offset in the current page of a multipage TIFF image.</p>
</dd>

### -field lPrevIfdOffset

<dd>
<p>Specifies the image file directory (IFD) offset in the previous page of a multipage TIFF image.</p>
</dd>
</dl>

## -remarks
<p>The WIA service sets most of the members of this structure before it calls the minidriver's <a href="image.iwiaminidrv_drvacquireitemdata">IWiaMiniDrv::drvAcquireItemData</a> method. If the minidriver calls <a href="..\wiamdef\nf-wiamdef-wiasgetimageinformation.md">wiasGetImageInformation</a>, then that function fills in the remaining members of the MINIDRV_TRANSFER_CONTEXT passed to it.</p>

<p>Because the WIA service currently uses only the TYMED_FILE and TYMED_CALLBACK constants, the <b>tymed</b> and <b>bTransferDataCB</b> members store essentially the same information. For file transfers, when <b>bTransferDataCB</b> is set to <b>FALSE</b>, <b>tymed</b> is set to either TYMED_FILE or TYMED_MULTIPAGE_FILE. For memory-callback transfers, when <b>bTransferDataCB</b> is set to <b>TRUE</b>, <b>tymed</b> is set to either TYMED_CALLBACK or TYMED_MULTIPAGE_CALLBACK.</p>

<p>The <b>hFile</b> member is reserved for use solely by the WIA service. Rather than using this member for file transfers, the minidriver should instead write the data to a buffer, and then call <a href="..\wiamdef\nf-wiamdef-wiaswritepagebuftofile.md">wiasWritePageBufToFile</a> to complete the file transfer.</p>

<p>The minidriver obtains values from specific common or scanner item properties to set the members shown in the following table:</p>

<p><b>lWidthInPixels</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551615">WIA_IPA_PIXELS_PER_LINE</a>
</p>

<p><b>lLines</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551611">WIA_IPA_NUMBER_OF_LINES</a>
</p>

<p><b>lDepth</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551546">WIA_IPA_DEPTH</a>
</p>

<p><b>lXRes</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552665">WIA_IPS_XRES</a>
</p>

<p><b>lYRes</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552673">WIA_IPS_YRES</a>
</p>

<p><b>lCompression</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551540">WIA_IPA_COMPRESSION</a>
</p>

<p><b>guidFormatID</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551553">WIA_IPA_FORMAT</a>
</p>

<p><b>tymed</b></p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551656">WIA_IPA_TYMED</a>
</p>

<p>Usually, the minidriver sets the preceding structure members directly from the values of the item properties. An application or the minidriver will have set the item properties earlier. The WIA service fills in its service context, using the property values. The driver can use the values stored in this context for quick reference.</p>

<p>The WIA service sets the following structure members:</p>

<p><b>hFile</b></p>

<p><b>bTransferDataCB</b></p>

<p><b>bClassDrvAllocBuf</b></p>

<p>Either the minidriver or the <a href="..\wiamdef\nf-wiamdef-wiasgetimageinformation.md">wiasGetImageInformation</a> service library function sets the following structure members:</p>

<p><b>lImageSize</b></p>

<p><b>lHeaderSize</b></p>

<p><b>lItemSize</b></p>

<p><b>cbWidthInBytes</b></p>

<p>The following members of this structure are used in data transfer callbacks. The WIA service or the minidriver sets these members. In several cases, the value stored in <b>bClassDrvAllocBuf</b> determines whether the WIA service or the minidriver sets the member.</p>

<p><b>cbOffset</b></p>

<p>Minidriver</p>

<p><b>lBufferSize</b></p>

<p>WIA service or minidriver</p>

<p>If <b>bClassDrvAllocBuf</b> is <b>TRUE</b>, the WIA service sets this member; otherwise, the minidriver sets it.</p>

<p><b>lActiveBuffer</b></p>

<p>WIA service</p>

<p>The minidriver must not modify this member.</p>

<p><b>lNumBuffers</b></p>

<p><b>pBaseBuffer</b></p>

<p><b>pTransferBuffer</b></p>

<p><b>lClientAddress</b></p>

<p><b>pIWiaMiniDrvCallBack</b></p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamindr_lh.h (include Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="image.iwiaminidrvcallback_minidrvcallback">IWiaMiniDrvCallBack::MiniDrvCallback</a>
</dt>
<dt>
<a href="image.iwiaminidrv_drvacquireitemdata">IWiaMiniDrv::drvAcquireItemData</a>
</dt>
<dt>
<a href="..\wiamdef\nf-wiamdef-wiasgetimageinformation.md">wiasGetImageInformation</a>
</dt>
<dt>
<a href="..\wiamdef\nf-wiamdef-wiaswritepagebuftofile.md">wiasWritePageBufToFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20MINIDRV_TRANSFER_CONTEXT structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
