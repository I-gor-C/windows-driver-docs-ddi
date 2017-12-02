---
UID: NE.d3d10umddi.D3D11_1DDI_CONTENT_PROTECTION_CAPS
title: D3D11_1DDI_CONTENT_PROTECTION_CAPS
author: windows-driver-content
description: Describes content-protection capabilities.
old-location: display\d3d11_1ddi_content_protection_caps.htm
old-project: display
ms.assetid: de2d5e08-1c8f-4c67-91e0-db7552b0b883
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_CONTENT_PROTECTION_CAPS
req.alt-loc: D3d10umddi.h
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

# D3D11_1DDI_CONTENT_PROTECTION_CAPS enumeration



## -description
<p>Describes content-protection capabilities.</p>


## -syntax

````
typedef enum D3D11_1DDI_CONTENT_PROTECTION_CAPS { 
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_SOFTWARE                                 = 0x00000001,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_HARDWARE                                 = 0x00000002,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_PROTECTION_ALWAYS_ON                     = 0x00000004,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_PARTIAL_DECRYPTION                       = 0x00000008,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_CONTENT_KEY                              = 0x00000010,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_FRESHEN_SESSION_KEY                      = 0x00000020,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPTED_READ_BACK                      = 0x00000040,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPTED_READ_BACK_KEY                  = 0x00000080,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_SEQUENTIAL_CTR_IV                        = 0x00000100,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPT_SLICEDATA_ONLY                   = 0x00000200,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_DECRYPTION_BLT                           = 0x00000400,
#if D3D11DDI_MINOR_HEADER_VERSION >= 5
  D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECT_UNCOMPRESSED         = 0x00000800,
  D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECTED_MEMORY_PAGEABLE    = 0x00001000,
  D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECTED_MEMORY_TRANSITION  = 0x00002000,
  D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_TEARDOWN                     = 0x00004000,
  D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_DRM_COMMUNICATION            = 0x00008000,
#endif 
  
} D3D11_1DDI_CONTENT_PROTECTION_CAPS;
````


## -enum-fields
<dl>

### -field D3D11_1DDI_CONTENT_PROTECTION_CAPS_SOFTWARE

<dd>
<p>The encryption is implemented in software by the driver.</p>
</dd>

### -field D3D11_1DDI_CONTENT_PROTECTION_CAPS_HARDWARE

<dd>
<p>The encryption is implemented in hardware by the GPU.</p>
</dd>

### -field D3D11_1DDI_CONTENT_PROTECTION_CAPS_PROTECTION_ALWAYS_ON

<dd>
<p>Content protection is always applied to a protected surface, regardless of whether the application explicitly enables protection.</p>
</dd>

### -field D3D11_1DDI_CONTENT_PROTECTION_CAPS_PARTIAL_DECRYPTION

<dd>
<p>The driver can use partially encrypted buffers. If this capability is not present, the entire buffer must be either encrypted or clear.</p>
</dd>

### -field D3D11_1DDI_CONTENT_PROTECTION_CAPS_CONTENT_KEY

<dd>
<p>The driver can encrypt data using a separate content key that is encrypted using the session key.</p>
</dd>

### -field D3D11_1DDI_CONTENT_PROTECTION_CAPS_FRESHEN_SESSION_KEY

<dd>
<p>The driver can refresh the session key without renegotiating the key.</p>
</dd>

### -field D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPTED_READ_BACK

<dd>
<p>The driver can read back encrypted data from a protected surface. For more information, see <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-encryptionblt.md">EncryptionBlt(D3D11_1)</a>.</p>
</dd>

### -field D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPTED_READ_BACK_KEY

<dd>
<p>The driver requires a separate key to read encrypted data from a protected surface.</p>
</dd>

### -field D3D11_1DDI_CONTENT_PROTECTION_CAPS_SEQUENTIAL_CTR_IV

<dd>
<p>If the encryption type is <b>D3D11_1DDI_CRYPTO_TYPE_AES128_CTR</b>, the application must use a sequential count in the <a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-aes-ctr-iv.md">D3D11_1DDI_AES_CTR_IV</a> structure. For more information, see the Remarks for the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-encryptionblt.md">EncryptionBlt(D3D11_1)</a> function.</p>
</dd>

### -field D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPT_SLICEDATA_ONLY

<dd>
<p>The driver supports encrypted slice data, but does not support any other encrypted data in the DirectX Video Accelerator (DXVA) 2 compressed buffer. The caller should not encrypt any data within the buffer other than the slice data.</p>
</dd>

### -field D3D11_1DDI_CONTENT_PROTECTION_CAPS_DECRYPTION_BLT

<dd>
<p>The driver supports calls to the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-decryptionblt.md">DecryptionBlt(D3D11_1)</a> function.</p>
</dd>

### -field D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECT_UNCOMPRESSED

<dd>
<p>The hardware supports the protection of specific resources using the WDDM 2.0 and later versions of the Graphics Content Protection DDI. This protection means:</p>
<ul>
<li>The contents of a protected allocation can never be read by the CPU.</li>
<li>The hardware can ensure that a protected resource cannot be copied to an unprotected resource.</li>
</ul>
<p>Supported starting with Windows 10.</p>
</dd>

### -field D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECTED_MEMORY_PAGEABLE

<dd>
<p>The physical pages of a protected resource can be evicted and potentially paged to disk in low memory conditions without losing the contents of the resource when paged back in.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECTED_MEMORY_TRANSITION

<dd>
<p>The hardware or driver can transition allocations between protected and unprotected states by calling <a href="display.sethardwareprotection">SetHardwareProtection</a>  without requiring the allocation to be re-created.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_TEARDOWN

<dd>
<p>The hardware supports an automatic tear-down mechanism that could trigger hardware keys or protected content to become lost in some conditions.  The application can register to know when these events occur.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_DRM_COMMUNICATION

<dd>
<p>The secure environment is tightly coupled with the GPU and an <b>ID3D11CryptoSession</b> should be used for communication between the user mode DRM component and the secure execution environment.</p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field 

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d11-1ddi-aes-ctr-iv.md">D3D11_1DDI_AES_CTR_IV</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-decryptionblt.md">DecryptionBlt(D3D11_1)</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-encryptionblt.md">EncryptionBlt(D3D11_1)</a>
</dt>
<dt>
<a href="display.sethardwareprotection">SetHardwareProtection</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDI_CONTENT_PROTECTION_CAPS enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
