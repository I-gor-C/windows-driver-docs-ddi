---
UID: NS.d3dumddi._D3DDDIARG_DECRYPTIONBLT
title: D3DDDIARG_DECRYPTIONBLT
author: windows-driver-content
description: The D3DDDIARG_DECRYPTIONBLT structure describes the parameters of an decrypted bit-block transfer (bitblt) in a call to the DecryptionBlt function.
old-location: display\d3dddiarg_decryptionblt.htm
ms.assetid: cc11e153-6be6-4fbc-9535-98bab7ed2b90
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: D3DDDIARG_DECRYPTIONBLT is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_DECRYPTIONBLT
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
ms.keywords: D3DDDIARG_DECRYPTIONBLT, D3DDDIARG_DECRYPTIONBLT
req.iface: 
---

# D3DDDIARG_DECRYPTIONBLT structure



## -description
<p>The D3DDDIARG_DECRYPTIONBLT structure describes the parameters of an decrypted bit-block transfer (bitblt) in a call to the <a href="https://msdn.microsoft.com/1bfe2b9c-90f6-48bf-b0b3-30788ef94110">DecryptionBlt</a> function. </p>


## -syntax

````
typedef struct _D3DDDIARG_DECRYPTIONBLT {
  HANDLE                     hCryptoSession;
  HANDLE                     hSrcResource;
  UINT                       SrcSubResourceIndex;
  HANDLE                     hDstResource;
  UINT                       DstSubResourceIndex;
  UINT                       SrcResourceSize;
  D3DDDIENCRYPTED_BLOCK_INFO *pEncryptedBlockInfo;
  VOID                       *pContentKey;
  VOID                       *pIV;
} D3DDDIARG_DECRYPTIONBLT;
````


## -struct-fields
<dl>

### -field <b>hCryptoSession</b>

<dd>
<p>[in] A handle to the encryption session. </p>
</dd>

### -field <b>hSrcResource</b>

<dd>
<p>[in] A handle to the source resource.</p>
</dd>

### -field <b>SrcSubResourceIndex</b>

<dd>
<p>[in] The index to the source surface within the resource. </p>
</dd>

### -field <b>hDstResource</b>

<dd>
<p>[in] A handle to the destination resource. </p>
</dd>

### -field <b>DstSubResourceIndex</b>

<dd>
<p>[in] The index to the destination surface within the resource. </p>
</dd>

### -field <b>SrcResourceSize</b>

<dd>
<p>[in] The size, in bytes, of the source resource. </p>
</dd>

### -field <b>pEncryptedBlockInfo</b>

<dd>
<p>[in] A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544298">D3DDDIENCRYPTED_BLOCK_INFO</a> structure that describes the portions of the buffer that are encrypted. </p>
</dd>

### -field <b>pContentKey</b>

<dd>
<p>[in] A pointer to a block of memory that contains the content key that is required to decrypt the bitblt data. If <b>pContentKey</b> is <b>NULL</b>, hardware does not require a separate content key to decrypt the data. That is, the session key is used to encrypt the data. </p>
</dd>

### -field <b>pIV</b>

<dd>
<p>[in] A pointer to a block of memory that contains the initialization vector that is required to decrypt the bitblt data. If <b>pIV</b> is <b>NULL</b>, hardware does not require a separate initialization vector to decrypt the data. That is, the session key is used to encrypt the data. </p>
</dd>
</dl>

## -remarks
<p>A pointer to a populated D3DDDIARG_DECRYPTIONBLT structure is passed to the driver's <a href="https://msdn.microsoft.com/1bfe2b9c-90f6-48bf-b0b3-30788ef94110">DecryptionBlt</a> function to write data to a protected surface. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3DDDIARG_DECRYPTIONBLT is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544298">D3DDDIENCRYPTED_BLOCK_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1bfe2b9c-90f6-48bf-b0b3-30788ef94110">DecryptionBlt</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_DECRYPTIONBLT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
