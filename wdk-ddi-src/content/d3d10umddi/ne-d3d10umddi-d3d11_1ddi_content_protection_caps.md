---
UID: NE:d3d10umddi.D3D11_1DDI_CONTENT_PROTECTION_CAPS
title: D3D11_1DDI_CONTENT_PROTECTION_CAPS
author: windows-driver-content
description: Describes content-protection capabilities.
old-location: display\d3d11_1ddi_content_protection_caps.htm
old-project: display
ms.assetid: de2d5e08-1c8f-4c67-91e0-db7552b0b883
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: D3D11_1DDI_CONTENT_PROTECTION_CAPS, D3D11_1DDI_CONTENT_PROTECTION_CAPS enumeration [Display Devices], D3D11_1DDI_CONTENT_PROTECTION_CAPS_CONTENT_KEY, D3D11_1DDI_CONTENT_PROTECTION_CAPS_DECRYPTION_BLT, D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPTED_READ_BACK, D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPTED_READ_BACK_KEY, D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPT_SLICEDATA_ONLY, D3D11_1DDI_CONTENT_PROTECTION_CAPS_FRESHEN_SESSION_KEY, D3D11_1DDI_CONTENT_PROTECTION_CAPS_HARDWARE, D3D11_1DDI_CONTENT_PROTECTION_CAPS_PARTIAL_DECRYPTION, D3D11_1DDI_CONTENT_PROTECTION_CAPS_PROTECTION_ALWAYS_ON, D3D11_1DDI_CONTENT_PROTECTION_CAPS_SEQUENTIAL_CTR_IV, D3D11_1DDI_CONTENT_PROTECTION_CAPS_SOFTWARE, D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_DRM_COMMUNICATION, D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECTED_MEMORY_PAGEABLE, D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECTED_MEMORY_TRANSITION, D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECT_UNCOMPRESSED, D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_TEARDOWN, d3d10umddi/, d3d10umddi/D3D11_1DDI_CONTENT_PROTECTION_CAPS, d3d10umddi/D3D11_1DDI_CONTENT_PROTECTION_CAPS_CONTENT_KEY, d3d10umddi/D3D11_1DDI_CONTENT_PROTECTION_CAPS_DECRYPTION_BLT, d3d10umddi/D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPTED_READ_BACK, d3d10umddi/D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPTED_READ_BACK_KEY, d3d10umddi/D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPT_SLICEDATA_ONLY, d3d10umddi/D3D11_1DDI_CONTENT_PROTECTION_CAPS_FRESHEN_SESSION_KEY, d3d10umddi/D3D11_1DDI_CONTENT_PROTECTION_CAPS_HARDWARE, d3d10umddi/D3D11_1DDI_CONTENT_PROTECTION_CAPS_PARTIAL_DECRYPTION, d3d10umddi/D3D11_1DDI_CONTENT_PROTECTION_CAPS_PROTECTION_ALWAYS_ON, d3d10umddi/D3D11_1DDI_CONTENT_PROTECTION_CAPS_SEQUENTIAL_CTR_IV, d3d10umddi/D3D11_1DDI_CONTENT_PROTECTION_CAPS_SOFTWARE, d3d10umddi/D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_DRM_COMMUNICATION, d3d10umddi/D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECTED_MEMORY_PAGEABLE, d3d10umddi/D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECTED_MEMORY_TRANSITION, d3d10umddi/D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECT_UNCOMPRESSED, d3d10umddi/D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_TEARDOWN, display.d3d11_1ddi_content_protection_caps
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	D3d10umddi.h
api_name:
-	D3D11_1DDI_CONTENT_PROTECTION_CAPS
product:
- Windows
targetos: Windows
req.typenames: D3D11_1DDI_CONTENT_PROTECTION_CAPS
---

# D3D11_1DDI_CONTENT_PROTECTION_CAPS Enumeration
Describes content-protection capabilities.

## Syntax
```
typedef enum D3D11_1DDI_CONTENT_PROTECTION_CAPS {
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_SOFTWARE                                 ,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_HARDWARE                                 ,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_PROTECTION_ALWAYS_ON                     ,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_PARTIAL_DECRYPTION                       ,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_CONTENT_KEY                              ,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_FRESHEN_SESSION_KEY                      ,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPTED_READ_BACK                      ,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPTED_READ_BACK_KEY                  ,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_SEQUENTIAL_CTR_IV                        ,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPT_SLICEDATA_ONLY                   ,
  D3D11_1DDI_CONTENT_PROTECTION_CAPS_DECRYPTION_BLT                           ,
  D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECT_UNCOMPRESSED         ,
  D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECTED_MEMORY_PAGEABLE    ,
  D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECTED_MEMORY_TRANSITION  ,
  D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_TEARDOWN                     ,
  D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_DRM_COMMUNICATION
} ;
```

## Constants

<table>
            
                <tr>
                    <td>D3D11_1DDI_CONTENT_PROTECTION_CAPS_SOFTWARE</td>
                    <td>The encryption is implemented in software by the driver.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_CONTENT_PROTECTION_CAPS_HARDWARE</td>
                    <td>The encryption is implemented in hardware by the GPU.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_CONTENT_PROTECTION_CAPS_PROTECTION_ALWAYS_ON</td>
                    <td>Content protection is always applied to a protected surface, regardless of whether the application explicitly enables protection.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_CONTENT_PROTECTION_CAPS_PARTIAL_DECRYPTION</td>
                    <td>The driver can use partially encrypted buffers. If this capability is not present, the entire buffer must be either encrypted or clear.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_CONTENT_PROTECTION_CAPS_CONTENT_KEY</td>
                    <td>The driver can encrypt data using a separate content key that is encrypted using the session key.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_CONTENT_PROTECTION_CAPS_FRESHEN_SESSION_KEY</td>
                    <td>The driver can refresh the session key without renegotiating the key.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPTED_READ_BACK</td>
                    <td>The driver can read back encrypted data from a protected surface. For more information, see <a href="https://msdn.microsoft.com/ea6f1b8c-d65a-4d6d-a7ae-998374bf5bfb">EncryptionBlt(D3D11_1)</a>.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPTED_READ_BACK_KEY</td>
                    <td>The driver requires a separate key to read encrypted data from a protected surface.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_CONTENT_PROTECTION_CAPS_SEQUENTIAL_CTR_IV</td>
                    <td>If the encryption type is <b>D3D11_1DDI_CRYPTO_TYPE_AES128_CTR</b>, the application must use a sequential count in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406334">D3D11_1DDI_AES_CTR_IV</a> structure. For more information, see the Remarks for the <a href="https://msdn.microsoft.com/ea6f1b8c-d65a-4d6d-a7ae-998374bf5bfb">EncryptionBlt(D3D11_1)</a> function.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_CONTENT_PROTECTION_CAPS_ENCRYPT_SLICEDATA_ONLY</td>
                    <td>The driver supports encrypted slice data, but does not support any other encrypted data in the DirectX Video Accelerator (DXVA) 2 compressed buffer. The caller should not encrypt any data within the buffer other than the slice data.</td>
                </tr>
            
                <tr>
                    <td>D3D11_1DDI_CONTENT_PROTECTION_CAPS_DECRYPTION_BLT</td>
                    <td>The driver supports calls to the <a href="https://msdn.microsoft.com/36aeb826-251e-404e-8ce3-6b2246ff07bc">DecryptionBlt(D3D11_1)</a> function.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECT_UNCOMPRESSED</td>
                    <td>The hardware supports the protection of specific resources using the WDDM 2.0 and later versions of the Graphics Content Protection DDI. This protection means:

<ul>
<li>The contents of a protected allocation can never be read by the CPU.</li>
<li>The hardware can ensure that a protected resource cannot be copied to an unprotected resource.</li>
</ul>
Supported starting with Windows 10.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECTED_MEMORY_PAGEABLE</td>
                    <td>The physical pages of a protected resource can be evicted and potentially paged to disk in low memory conditions without losing the contents of the resource when paged back in.

Supported starting with Windows 10.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_PROTECTED_MEMORY_TRANSITION</td>
                    <td>The hardware or driver can transition allocations between protected and unprotected states by calling <a href="https://msdn.microsoft.com/library/windows/hardware/dn906369">SetHardwareProtection</a>  without requiring the allocation to be re-created.

Supported starting with Windows 10.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_TEARDOWN</td>
                    <td>The hardware supports an automatic tear-down mechanism that could trigger hardware keys or protected content to become lost in some conditions.  The application can register to know when these events occur.

Supported starting with Windows 10.</td>
                </tr>
            
                <tr>
                    <td>D3DWDDM2_0DDI_CONTENT_PROTECTION_CAPS_HARDWARE_DRM_COMMUNICATION</td>
                    <td>The secure environment is tightly coupled with the GPU and an <b>ID3D11CryptoSession</b> should be used for communication between the user mode DRM component and the secure execution environment.

Supported starting with Windows 10.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3d10umddi.h (include D3d10umddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh406334">D3D11_1DDI_AES_CTR_IV</a>



<a href="https://msdn.microsoft.com/36aeb826-251e-404e-8ce3-6b2246ff07bc">DecryptionBlt(D3D11_1)</a>



<a href="https://msdn.microsoft.com/ea6f1b8c-d65a-4d6d-a7ae-998374bf5bfb">EncryptionBlt(D3D11_1)</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/dn906369">SetHardwareProtection</a>