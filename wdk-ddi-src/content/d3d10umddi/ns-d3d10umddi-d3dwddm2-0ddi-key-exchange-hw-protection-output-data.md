---
UID: NS.d3d10umddi.D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA
title: D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA
author: windows-driver-content
description: D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA is used with D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_DATA in the implementation of Digital Rights Management (DRM).
old-location: display\d3dwddm2_0ddi_key_exchange_hw_protection_output_data.htm
old-project: display
ms.assetid: 4287B32C-FE40-4B24-801C-455610E4F627
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA, D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA
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

# D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA structure



## -description
<p><b>D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA</b> is used with <a href="https://msdn.microsoft.com/library/windows/hardware/dn894610">D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_DATA</a> in the implementation of Digital Rights Management (DRM).</p>


## -syntax

````
typedef struct D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA {
  UINT   PrivateDataSize;
  UINT   MaxHWProtectionDataSize;
  UINT   HWProtectionDataSize;
  UINT64 TransportTime;
  UINT64 ExecutionTime;
  BYTE   pbOutput[4];
} D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA;
````


## -struct-fields
<dl>

### -field <b>PrivateDataSize</b>

<dd>
<p>Contains the size of the private data reserved for IHV usage. This size is determined from the <b>pPrivateInputSize</b> member returned by <a href="https://msdn.microsoft.com/library/windows/hardware/dn906349">GetCryptoSessionPrivateDataSize</a>.</p>
</dd>

### -field <b>MaxHWProtectionDataSize</b>

<dd>
<p>The maximum size of data that the driver can return in the output buffer. The last byte that it can write to is <b>pbOuput</b>[<b>PrivateDataSize</b> + <b>MaxHWProtectionDataSize</b> – 1].</p>
</dd>

### -field <b>HWProtectionDataSize</b>

<dd>
<p>Returns the size of the output data written by the driver.</p>
</dd>

### -field <b>TransportTime</b>

<dd>
<p>Returns the number of 100 nanosecond units spent transporting the data.</p>
</dd>

### -field <b>ExecutionTime</b>

<dd>
<p>Returns the number of 100 nanosecond units spent executing the content protection command.</p>
</dd>

### -field <b>pbOutput</b>

<dd>
<p>If <b>PrivateDataSize</b> is greater than 0, <b>pbOutput</b>[0] – <b>pbOutput</b>[<b>PrivateDataSize</b> - 1] is reserved for IHV use.

</p>
<p><b>pbOutput</b>[<b>PrivateDataSize</b>] – <b>pbOutput</b>[<b>MaxHWProtectionDataSize</b> + <b>PrivateDataSize</b> - 1] contains the region into which the driver should return the output data from the DRM command. The format and size of the DRM command is defined by the DRM specification.
</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906349">GetCryptoSessionPrivateDataSize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn894610">D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_DATA</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d11-1ddi-negotiatecryptosessionkeyeschange.md">NegotiateCryptoSessionKeyExchange</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DWDDM2_0DDI_KEY_EXCHANGE_HW_PROTECTION_OUTPUT_DATA structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
