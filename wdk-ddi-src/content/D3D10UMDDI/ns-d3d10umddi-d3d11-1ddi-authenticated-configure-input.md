---
UID: NS.d3d10umddi.D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT
title: D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT
author: windows-driver-content
description: Contains input data for the ConfigureAuthenticatedChannel(D3D11_1) function.
old-location: display\d3d11_1ddi_authenticated_configure_input.htm
ms.assetid: a481fb2d-60bb-441d-998d-acb983b2c0ed
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT
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
ms.keywords: D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT, D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT
req.iface: 
---

# D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT structure



## -description
<p>Contains input data for the <a href="https://msdn.microsoft.com/28d32813-15f5-4b9c-9bdb-5ad9b47bbe3b">ConfigureAuthenticatedChannel(D3D11_1)</a> function.</p>


## -syntax

````
typedef struct D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT {
  D3D11_1DDI_OMAC omac;
  GUID            ConfigureType;
  HANDLE          hChannel;
  UINT            SequenceNumber;
} D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT;
````


## -struct-fields
<dl>

### -field <b>omac</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh406450">D3D11_1DDI_OMAC</a> structure that contains a Message Authentication Code (MAC) of the data. The driver uses Advanced Encryption Standard (AES)-based one-key CBC MAC (OMAC) to calculate this value for the block of data that appears after this structure member.</p>
</dd>

### -field <b>ConfigureType</b>

<dd>
<p>A GUID that specifies the command. The following GUIDs are defined.</p>
<dl class="indent">

### -field <a id="D3D11_1DDI_AUTHENTICATED_CONFIGURE_ENCRYPTION_WHEN_ACCESSIBLE_GUID"></a><a id="d3d11_1ddi_authenticated_configure_encryption_when_accessible_guid"></a><p><a id="D3D11_1DDI_AUTHENTICATED_CONFIGURE_ENCRYPTION_WHEN_ACCESSIBLE_GUID"></a><a id="d3d11_1ddi_authenticated_configure_encryption_when_accessible_guid"></a><b>D3D11_1DDI_AUTHENTICATED_CONFIGURE_ENCRYPTION_WHEN_ACCESSIBLE_GUID</b></p>


<dd>
<p>Sets the level of encryption that is performed before protected content becomes accessible to the CPU or bus.</p>
<p>Input data: <a href="https://msdn.microsoft.com/library/windows/hardware/hh406347">D3D11_1DDI_AUTHENTICATED_CONFIGURE_ACCESSIBLE_ENCRYPTION</a>
</p>
</dd>

### -field <a id="D3D11_1DDI_AUTHENTICATED_CONFIGURE_CRYPTO_SESSION_GUID"></a><a id="d3d11_1ddi_authenticated_configure_crypto_session_guid"></a><p><a id="D3D11_1DDI_AUTHENTICATED_CONFIGURE_CRYPTO_SESSION_GUID"></a><a id="d3d11_1ddi_authenticated_configure_crypto_session_guid"></a><b>D3D11_1DDI_AUTHENTICATED_CONFIGURE_CRYPTO_SESSION_GUID</b></p>


<dd>
<p>Associates a cryptographic session with a DirectX Video Acceleration 2 (DXVA-2) decode device and a Direct3D device.</p>
<p>Input data: <a href="https://msdn.microsoft.com/library/windows/hardware/hh406350">D3D11_1DDI_AUTHENTICATED_CONFIGURE_CRYPTO_SESSION</a>
</p>
</dd>

### -field <a id="D3D11_1DDI_AUTHENTICATED_CONFIGURE_INITIALIZE_GUID"></a><a id="d3d11_1ddi_authenticated_configure_initialize_guid"></a><p><a id="D3D11_1DDI_AUTHENTICATED_CONFIGURE_INITIALIZE_GUID"></a><a id="d3d11_1ddi_authenticated_configure_initialize_guid"></a><b>D3D11_1DDI_AUTHENTICATED_CONFIGURE_INITIALIZE_GUID</b></p>


<dd>
<p>Initializes the authenticated channel.

</p>
<p>Input data: <a href="https://msdn.microsoft.com/library/windows/hardware/hh406354">D3D11_1DDI_AUTHENTICATED_CONFIGURE_INITIALIZE</a>
</p>
</dd>

### -field <a id="D3D11_1DDI_AUTHENTICATED_CONFIGURE_PROTECTION_GUID"></a><a id="d3d11_1ddi_authenticated_configure_protection_guid"></a><p><a id="D3D11_1DDI_AUTHENTICATED_CONFIGURE_PROTECTION_GUID"></a><a id="d3d11_1ddi_authenticated_configure_protection_guid"></a><b>D3D11_1DDI_AUTHENTICATED_CONFIGURE_PROTECTION_GUID</b></p>


<dd>
<p>Enables or disables protection for the device.

</p>
<p>Input data: <a href="https://msdn.microsoft.com/library/windows/hardware/hh406366">D3D11_1DDI_AUTHENTICATED_CONFIGURE_PROTECTION</a>
</p>
</dd>

### -field <a id="D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE_GUID"></a><a id="d3d11_1ddi_authenticated_configure_shared_resource_guid"></a><p><a id="D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE_GUID"></a><a id="d3d11_1ddi_authenticated_configure_shared_resource_guid"></a><b>D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE_GUID</b></p>


<dd>
<p>Enables a process to open a shared resource, or disables a process from opening shared resources.

</p>
<p>Input data: <a href="https://msdn.microsoft.com/library/windows/hardware/hh406369">D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE</a>
</p>
</dd>
</dl>
</dd>

### -field <b>hChannel</b>

<dd>
<p>A handle to the authenticated channel. This handle was created through a call to the <a href="https://msdn.microsoft.com/90b43bc3-6569-4799-8be3-e4e60f59164f">CreateAuthenticatedChannel(D3D11_1)</a> function. 

</p>
</dd>

### -field <b>SequenceNumber</b>

<dd>
<p>The query sequence number.</p>
<div class="alert"><b>Note</b>  The sequence number must increase with each successive call to the <a href="https://msdn.microsoft.com/28d32813-15f5-4b9c-9bdb-5ad9b47bbe3b">ConfigureAuthenticatedChannel(D3D11_1)</a> function.</div>
<div> </div>
</dd>
</dl>

## -remarks
<p>For information on the usage of this structure, see the Remarks of the <a href="https://msdn.microsoft.com/28d32813-15f5-4b9c-9bdb-5ad9b47bbe3b">ConfigureAuthenticatedChannel(D3D11_1)</a> function.</p>

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
<a href="https://msdn.microsoft.com/28d32813-15f5-4b9c-9bdb-5ad9b47bbe3b">ConfigureAuthenticatedChannel(D3D11_1)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/90b43bc3-6569-4799-8be3-e4e60f59164f">CreateAuthenticatedChannel(D3D11_1)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406347">D3D11_1DDI_AUTHENTICATED_CONFIGURE_ACCESSIBLE_ENCRYPTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406350">D3D11_1DDI_AUTHENTICATED_CONFIGURE_CRYPTO_SESSION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406354">D3D11_1DDI_AUTHENTICATED_CONFIGURE_INITIALIZE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406366">D3D11_1DDI_AUTHENTICATED_CONFIGURE_PROTECTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406369">D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406450">D3D11_1DDI_OMAC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
