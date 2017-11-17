---
UID: NE.ndis._IPSEC_OFFLOAD_V2_OPERATION
title: IPSEC_OFFLOAD_V2_OPERATION
author: windows-driver-content
description: The IPSEC_OFFLOAD_V2_OPERATION enumeration specifies the IPsec operation for which a security association (SA) is used.
old-location: netvista\ipsec_offload_v2_operation.htm
ms.assetid: bb26c8af-1564-4cf8-ab40-b50b4811466d
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.1 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPSEC_OFFLOAD_V2_OPERATION
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: RxNameCacheInitialize
req.iface: 
---

# IPSEC_OFFLOAD_V2_OPERATION enumeration



## -description
<p class="CCE_Message">[The IPsec Task Offload feature is deprecated and should not be used.]</p>
<p>The IPSEC_OFFLOAD_V2_OPERATION enumeration specifies the IPsec operation for which a security
  association (SA) is used.</p>


## -syntax

````
typedef enum _IPSEC_OFFLOAD_V2_OPERATION { 
  IPsecOffloadV2Ah   = 1,
  IPsecOffloadV2Esp,
  IPsecOffloadV2Max
} IPSEC_OFFLOAD_V2_OPERATION, *PIPSEC_OFFLOAD_V2_OPERATION;
````


## -enum-fields
<dl>

### -field <a id="IPsecOffloadV2Ah"></a><a id="ipsecoffloadv2ah"></a><a id="IPSECOFFLOADV2AH"></a><b>IPsecOffloadV2Ah</b>

<dd>
<p>The SA is used for authentication (integrity checking).</p>
</dd>

### -field <a id="IPsecOffloadV2Esp"></a><a id="ipsecoffloadv2esp"></a><a id="IPSECOFFLOADV2ESP"></a><b>IPsecOffloadV2Esp</b>

<dd>
<p>The SA is used for encryption/decryption (confidentiality).</p>
</dd>

### -field <a id="IPsecOffloadV2Max"></a><a id="ipsecoffloadv2max"></a><a id="IPSECOFFLOADV2MAX"></a><b>IPsecOffloadV2Max</b>

<dd>
<p>Reserved for NDIS.</p>
</dd>
</dl>

## -remarks
<p>The IPSEC_OFFLOAD_V2_OPERATION enumeration specifies the operation for which an SA is used in the 
    <b>Operation</b> member of the 
    <a href="https://msdn.microsoft.com/b2c5611e-930d-41a5-a07e-7de8f8584283">
    IPSEC_OFFLOAD_V2_SECURITY_ASSOCIATION</a> structure.</p>

<p>The IPSEC_OFFLOAD_V2_OPERATION enumeration specifies the operation for which an SA is used in the 
    <b>Operation</b> member of the 
    <a href="https://msdn.microsoft.com/b2c5611e-930d-41a5-a07e-7de8f8584283">
    IPSEC_OFFLOAD_V2_SECURITY_ASSOCIATION</a> structure.</p>

<p>The IPSEC_OFFLOAD_V2_OPERATION enumeration specifies the operation for which an SA is used in the 
    <b>Operation</b> member of the 
    <a href="https://msdn.microsoft.com/b2c5611e-930d-41a5-a07e-7de8f8584283">
    IPSEC_OFFLOAD_V2_SECURITY_ASSOCIATION</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.1 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/b2c5611e-930d-41a5-a07e-7de8f8584283">
   IPSEC_OFFLOAD_V2_SECURITY_ASSOCIATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20IPSEC_OFFLOAD_V2_OPERATION enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
