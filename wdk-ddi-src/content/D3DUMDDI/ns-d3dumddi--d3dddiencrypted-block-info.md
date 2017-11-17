---
UID: NS.d3dumddi._D3DDDIENCRYPTED_BLOCK_INFO
title: D3DDDIENCRYPTED_BLOCK_INFO
author: windows-driver-content
description: The D3DDDIENCRYPTED_BLOCK_INFO structure describes the portions of a buffer that are encrypted.
old-location: display\d3dddiencrypted_block_info.htm
ms.assetid: a02f782f-6918-479a-b3de-9443df2e9ffe
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: D3DDDIENCRYPTED_BLOCK_INFO is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIENCRYPTED_BLOCK_INFO
req.alt-loc: d3dumddi.h
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
ms.keywords: D3DDDIENCRYPTED_BLOCK_INFO, D3DDDIENCRYPTED_BLOCK_INFO
req.iface: 
---

# D3DDDIENCRYPTED_BLOCK_INFO structure



## -description
<p>The D3DDDIENCRYPTED_BLOCK_INFO structure describes the portions of a buffer that are encrypted. </p>


## -syntax

````
typedef struct _D3DDDIENCRYPTED_BLOCK_INFO {
  UINT NumEncryptedBytesAtBeginning;
  UINT NumBytesInSkipPattern;
  UINT NumBytesInEncryptPattern;
} D3DDDIENCRYPTED_BLOCK_INFO;
````


## -struct-fields
<dl>

### -field <b>NumEncryptedBytesAtBeginning</b>

<dd>
<p>[in] The number of bytes at the beginning of the buffer that are encrypted. </p>
</dd>

### -field <b>NumBytesInSkipPattern</b>

<dd>
<p>[in] The number of bytes in the buffer that are skipped from encryption before encryption starts again. </p>
</dd>

### -field <b>NumBytesInEncryptPattern</b>

<dd>
<p>[in] The number of bytes in the buffer that are encrypted after the skip pattern, which the <b>NumBytesInSkipPattern</b> member specifies. The skip and encrypt pattern is then repeated until the buffer ends. For more information about the skip-encrypt pattern, see the Remarks section. </p>
</dd>
</dl>

## -remarks
<p>Because the buffer's encrypted portion is specified in bytes, an application must ensure that the encrypted blocks match the GPU's crypto-block alignment. </p>

<p>The runtime can specify a populated D3DDDIENCRYPTED_BLOCK_INFO structure in the block of memory that the <b>pEncryptedBlockInfo</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543011">D3DDDIARG_DECRYPTIONBLT</a> structure points to when the runtime calls the driver's <a href="https://msdn.microsoft.com/1bfe2b9c-90f6-48bf-b0b3-30788ef94110">DecryptionBlt</a> function to write data to a protected surface. </p>

<p>The following examples show how the runtime can partition a buffer's encryption.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3DDDIENCRYPTED_BLOCK_INFO is supported beginning with the Windows 7 operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543011">D3DDDIARG_DECRYPTIONBLT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1bfe2b9c-90f6-48bf-b0b3-30788ef94110">DecryptionBlt</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIENCRYPTED_BLOCK_INFO structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
