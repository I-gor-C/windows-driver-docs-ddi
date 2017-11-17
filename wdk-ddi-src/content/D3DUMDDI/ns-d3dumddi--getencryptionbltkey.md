---
UID: NS.d3dumddi._GETENCRYPTIONBLTKEY
title: GETENCRYPTIONBLTKEY
author: windows-driver-content
description: The D3DDDIARG_GETENCRYPTIONBLTKEY structure describes an encrypted bit-block transfer (bitblt) session for which the GetEncryptionBltKey function retrieves the encryption key.
old-location: display\d3dddiarg_getencryptionbltkey.htm
ms.assetid: 6f481646-b665-46cb-b551-10515b8603c5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: D3DDDIARG_GETENCRYPTIONBLTKEY is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_GETENCRYPTIONBLTKEY
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
ms.keywords: GETENCRYPTIONBLTKEY, D3DDDIARG_GETENCRYPTIONBLTKEY
req.iface: 
---

# GETENCRYPTIONBLTKEY structure



## -description
<p>The D3DDDIARG_GETENCRYPTIONBLTKEY structure describes an encrypted bit-block transfer (bitblt) session for which the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451660">GetEncryptionBltKey</a> function retrieves the encryption key. </p>


## -syntax

````
typedef struct _GETENCRYPTIONBLTKEY {
  HANDLE hCryptoSession;
  VOID   *pReadBackKey;
  UINT   KeySize;
} D3DDDIARG_GETENCRYPTIONBLTKEY;
````


## -struct-fields
<dl>

### -field <b>hCryptoSession</b>

<dd>
<p>[in] A handle to the encryption session that is created in a call to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a> function. </p>
</dd>

### -field <b>pReadBackKey</b>

<dd>
<p>[in] A pointer to a buffer that contains the encryption key. </p>
</dd>

### -field <b>KeySize</b>

<dd>
<p>[in] The size, in bytes, of the encryption key that the <b>pReadBackKey</b> member points to. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3DDDIARG_GETENCRYPTIONBLTKEY is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451619">CreateCryptoSession</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451660">GetEncryptionBltKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_GETENCRYPTIONBLTKEY structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
