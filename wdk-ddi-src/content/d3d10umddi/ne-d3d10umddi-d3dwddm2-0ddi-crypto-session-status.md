---
UID: NE.d3d10umddi.D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS
title: D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS
author: windows-driver-content
description: Provides status information for an existing CryptoSession object.
old-location: display\d3dwddm2_0ddi_crypto_session_status.htm
old-project: display
ms.assetid: DBAFEAE2-66B6-4F2F-801D-21B7792BCA60
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SETRESULT_INFO, SETRESULT_INFO, *PSETRESULT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS
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

# D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS enumeration



## -description
<p>Provides status information for an existing <i>CryptoSession</i> object.</p>


## -syntax

````
typedef enum _D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS { 
  D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS_OK                    = 0,
  D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS_KEY_LOST              = 1,
  D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS_KEY_AND_CONTENT_LOST  = 2
} D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS;
````


## -enum-fields
<dl>

### -field <a id="D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS_OK"></a><a id="d3dwddm2_0ddi_crypto_session_status_ok"></a><b>D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS_OK</b>

<dd>
<p>The <i>CryptoSession</i> object is in a functional state.</p>
</dd>

### -field <a id="D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS_KEY_LOST"></a><a id="d3dwddm2_0ddi_crypto_session_status_key_lost"></a><b>D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS_KEY_LOST</b>

<dd>
<p>The underlying hardware key for the specified <i>CryptoSession</i> has become lost. </p>
</dd>

### -field <a id="D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS_KEY_AND_CONTENT_LOST"></a><a id="d3dwddm2_0ddi_crypto_session_status_key_and_content_lost"></a><b>D3DWDDM2_0DDI_CRYPTO_SESSION_STATUS_KEY_AND_CONTENT_LOST</b>

<dd>
<p>The underlying hardware key for the specified <i>CryptoSession</i> has become lost and protected content has become corrupted. </p>
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