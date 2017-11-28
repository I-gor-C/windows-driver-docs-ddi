---
UID: NS.d3d12umddi.D3D12DDI_DEVICE_FUNCS_CONTENT_PROTECTION_STREAMING_0030
title: D3D12DDI_DEVICE_FUNCS_CONTENT_PROTECTION_STREAMING_0030
author: windows-driver-content
description: Device function for content protection streaming.
old-location: display\d3d12ddi-device-funcs-content-protection-streaming-0030.htm
old-project: display
ms.assetid: 5ddf67c1-5ee7-4948-b631-45aeb031a293
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3D12DDI_DEVICE_FUNCS_CONTENT_PROTECTION_STREAMING_0030, D3D12DDI_DEVICE_FUNCS_CONTENT_PROTECTION_STREAMING_0030
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3d12umddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D12DDI_DEVICE_FUNCS_CONTENT_PROTECTION_STREAMING_0030
req.alt-loc: d3d12umddi.h
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

# D3D12DDI_DEVICE_FUNCS_CONTENT_PROTECTION_STREAMING_0030 structure



## -description
<p>Device function for content protection streaming.</p>


## -syntax

````
typedef struct _D3D12DDI_DEVICE_FUNCS_CONTENT_PROTECTION_STREAMING_0030 {
  PFND3D12DDI_CALCPRIVATECRYPTOSESSIONSIZE_0030              pfnCalcPrivateCryptoSessionSize;
  PFND3D12DDI_CREATECRYPTOSESSION_0030                       pfnCreateCryptoSession;
  PFND3D12DDI_CALCPRIVATEOPENEDCRYPTOSESSIONSIZE_0030        pfnCalcPrivateOpenedCryptoSessionSize;
  PFND3D12DDI_OPENCRYPTOSESSION_0030                         pfnOpenCryptoSession;
  PFND3D12DDI_DESTROYCRYPTOSESSION_0030                      pfnDestroyCryptoSession;
  PFND3D12DDI_GETKEYBASEDATA_0030                            pfnGetKeyBaseData;
  PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030        pfnCalcPrivateCryptoSessionPolicySize;
  PFND3D12DDI_CREATECRYPTOSESSIONPOLICY_0030                 pfnCreateCryptoSessionPolicy;
  PFND3D12DDI_CALCPRIVATEOPENEDCRYPTOSESSIONPOLICYSIZE_0030  pfnCalcPrivateOpenedCryptoSessionPolicySize;
  PFND3D12DDI_OPENCRYPTOSESSIONPOLICY_0030                   pfnOpenCryptoSessionPolicy;
  PFND3D12DDI_DESTROYCRYPTOSESSIONPOLICY_0030                pfnDestroyCryptoSessionPolicy;
  PFND3D12DDI_TRANSFORMENCRYPTEDDATA_0030                    pfnTransformEncryptedData;
} D3D12DDI_DEVICE_FUNCS_CONTENT_PROTECTION_STREAMING_0030, D3D12DDI_DEVICE_FUNCS_CONTENT_PROTECTION_STREAMING_0030;
````


## -struct-fields
<dl>

### -field <b>pfnCalcPrivateCryptoSessionSize</b>

<dd>
<p>Calculate private crypto session size.</p>
</dd>

### -field <b>pfnCreateCryptoSession</b>

<dd>
<p>Create crypto session.</p>
</dd>

### -field <b>pfnCalcPrivateOpenedCryptoSessionSize</b>

<dd>
<p>Calculate private opened crypto session size.</p>
</dd>

### -field <b>pfnOpenCryptoSession</b>

<dd>
<p>Open crypto session.</p>
</dd>

### -field <b>pfnDestroyCryptoSession</b>

<dd>
<p>Destroy crypto session.</p>
</dd>

### -field <b>pfnGetKeyBaseData</b>

<dd>
<p>Get key base data.</p>
</dd>

### -field <b>pfnCalcPrivateCryptoSessionPolicySize</b>

<dd>
<p>Calculate private crypto session policy size.</p>
</dd>

### -field <b>pfnCreateCryptoSessionPolicy</b>

<dd>
<p>Create crypto session policy.</p>
</dd>

### -field <b>pfnCalcPrivateOpenedCryptoSessionPolicySize</b>

<dd>
<p>Calculate private opened crypto session policy size.</p>
</dd>

### -field <b>pfnOpenCryptoSessionPolicy</b>

<dd>
<p>Open crypto session policy.</p>
</dd>

### -field <b>pfnDestroyCryptoSessionPolicy</b>

<dd>
<p>Destroy crypto session policy.</p>
</dd>

### -field <b>pfnTransformEncryptedData</b>

<dd>
<p>Transform encrypted data.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d12umddi.h</dt>
</dl>
</td>
</tr>
</table>