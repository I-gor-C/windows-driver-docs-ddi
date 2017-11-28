---
UID: NS.d3dkmthk._D3DKMT_GETPRESENTHISTORY
title: D3DKMT_GETPRESENTHISTORY
author: windows-driver-content
description: The D3DKMT_GETPRESENTHISTORY structure describes the state of copying history.
old-location: display\d3dkmt_getpresenthistory.htm
old-project: display
ms.assetid: 6d9b0473-544f-43aa-9358-ec51d84d45d9
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_GETPRESENTHISTORY, D3DKMT_GETPRESENTHISTORY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_GETPRESENTHISTORY
req.alt-loc: d3dkmthk.h
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
req.iface: 
---

# D3DKMT_GETPRESENTHISTORY structure



## -description
<p>The D3DKMT_GETPRESENTHISTORY structure describes the state of copying history.</p>


## -syntax

````
typedef struct _D3DKMT_GETPRESENTHISTORY {
  D3DKMT_HANDLE              hAdapter;
  UINT                       ProvidedSize;
  UINT                       WrittenSize;
  D3DKMT_PRESENTHISTORYTOKEN *pTokens;
  UINT                       NumTokens;
} D3DKMT_GETPRESENTHISTORY;
````


## -struct-fields
<dl>

### -field <b>hAdapter</b>

<dd>
<p>[in] The handle to the graphics adapter. </p>
</dd>

### -field <b>ProvidedSize</b>

<dd>
<p>Supported in Windows 7 and later versions.</p>
<p>[in] The size, in bytes, of the provided buffer that the <b>pTokens</b> member points to. </p>
</dd>

### -field <b>WrittenSize</b>

<dd>
<p>Supported in Windows 7 and later versions.</p>
<p>[out] The size, in bytes, that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546987">D3DKMTGetPresentHistory</a> function copies to the buffer that the <b>pTokens</b> member points to or the required size for first token. </p>
</dd>

### -field <b>pTokens</b>

<dd>
<p>Supported in Windows 7 and later versions.</p>
<p>[in/out] A pointer to the buffer that receives the tokens. Each token is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff548188">D3DKMT_PRESENTHISTORYTOKEN</a> structure. </p>
</dd>

### -field <b>NumTokens</b>

<dd>
<p>Supported in Windows 7 and later versions.</p>
<p>[out] The number of tokens that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546987">D3DKMTGetPresentHistory</a> function copies to the buffer that the <b>pTokens</b> member points to. </p>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548188">D3DKMT_PRESENTHISTORYTOKEN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546987">D3DKMTGetPresentHistory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_GETPRESENTHISTORY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
