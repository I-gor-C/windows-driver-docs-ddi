---
UID: NE.wditypes._WDI_CIPHER_ALGORITHM
title: WDI_CIPHER_ALGORITHM
author: windows-driver-content
description: The WDI_CIPHER_ALGORITHM enumeration defines the cipher algorithm values.
old-location: netvista\wdi_cipher_algorithm.htm
old-project: netvista
ms.assetid: 08413358-DFBC-4AC3-97B3-380D98EFFBF3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_CIPHER_ALGORITHM
req.alt-loc: wditypes.hpp
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDI_CIPHER_ALGORITHM enumeration



## -description
<p>The WDI_CIPHER_ALGORITHM enumeration defines the cipher algorithm values.</p>


## -syntax

````
typedef enum _WDI_CIPHER_ALGORITHM { 
  WDI_CIPHER_ALGO_NONE           = 0x00,
  WDI_CIPHER_ALGO_WEP40          = 0x01,
  WDI_CIPHER_ALGO_TKIP           = 0x02,
  WDI_CIPHER_ALGO_CCMP           = 0x04,
  WDI_CIPHER_ALGO_WEP104         = 0x05,
  WDI_CIPHER_ALGO_BIP            = 0x06,
  WDI_CIPHER_ALGO_GCMP           = 0x08,
  WDI_CIPHER_ALGO_WPA_USE_GROUP  = 0x100,
  WDI_CIPHER_ALGO_RSN_USE_GROUP  = 0x100,
  WDI_CIPHER_ALGO_WEP            = 0x101,
  WDI_CIPHER_ALGO_IHV_START      = 0x80000000,
  WDI_CIPHER_ALGO_IHV_END        = 0xffffffff
} WDI_CIPHER_ALGORITHM;
````


## -enum-fields
<dl>

### -field <a id="WDI_CIPHER_ALGO_NONE"></a><a id="wdi_cipher_algo_none"></a><b>WDI_CIPHER_ALGO_NONE</b>

<dd>
<p>Specifies that no cipher algorithm is enabled or supported.</p>
</dd>

### -field <a id="WDI_CIPHER_ALGO_WEP40"></a><a id="wdi_cipher_algo_wep40"></a><b>WDI_CIPHER_ALGO_WEP40</b>

<dd>
<p>Specifies a Wired Equivalent Privacy (WEP) algorithm, which is the RC4-based algorithm that is specified in the IEEE 802.11-2012 standard. This enumerator specifies the WEP cipher algorithm with a 40-bit cipher key.</p>
</dd>

### -field <a id="WDI_CIPHER_ALGO_TKIP"></a><a id="wdi_cipher_algo_tkip"></a><b>WDI_CIPHER_ALGO_TKIP</b>

<dd>
<p>Specifies a Temporal Key Integrity Protocol (TKIP) algorithm, which is the RC4-based cipher suite that is based on the algorithms that are defined in the WPA specification and IEEE 802.11i-2004 standard. This cipher also uses the Michael Message Integrity Code (MIC) algorithm for forgery protection.</p>
</dd>

### -field <a id="WDI_CIPHER_ALGO_CCMP"></a><a id="wdi_cipher_algo_ccmp"></a><b>WDI_CIPHER_ALGO_CCMP</b>

<dd>
<p>Specifies an AES-CCMP algorithm, as specified in the IEEE 802.11i-2004 standard and RFC 3610. Advanced Encryption Standard (AES) is the encryption algorithm defined in FIPS PUB 197.</p>
</dd>

### -field <a id="WDI_CIPHER_ALGO_WEP104"></a><a id="wdi_cipher_algo_wep104"></a><b>WDI_CIPHER_ALGO_WEP104</b>

<dd>
<p>Specifies a WEP cipher algorithm with a 104-bit cipher key.</p>
</dd>

### -field <a id="WDI_CIPHER_ALGO_BIP"></a><a id="wdi_cipher_algo_bip"></a><b>WDI_CIPHER_ALGO_BIP</b>

<dd>
<p>Specifies a BIP cipher algorithm.</p>
</dd>

### -field <a id="WDI_CIPHER_ALGO_GCMP"></a><a id="wdi_cipher_algo_gcmp"></a><b>WDI_CIPHER_ALGO_GCMP</b>

<dd>
<p>Added in Windows 10, version 1607, WDI version 1.0.21.</p>
<p>Specifies a GCMP (Galois/Counter Mode Protocol) cipher algorithm. It is the only encryption protocol supported for 802.11ad (DMG) Phy.</p>
</dd>

### -field <a id="WDI_CIPHER_ALGO_WPA_USE_GROUP"></a><a id="wdi_cipher_algo_wpa_use_group"></a><b>WDI_CIPHER_ALGO_WPA_USE_GROUP</b>

<dd>
<p>Specifies a Wi-Fi Protected Access (WPA) Use Group Key cipher suite. For more information about the Use Group Key cipher suite, refer to Clause 7.3.2.25.1 of the IEEE 802.11i-2004 standard.

</p>
</dd>

### -field <a id="WDI_CIPHER_ALGO_RSN_USE_GROUP"></a><a id="wdi_cipher_algo_rsn_use_group"></a><b>WDI_CIPHER_ALGO_RSN_USE_GROUP</b>

<dd>
<p>Specifies a Robust Security Network (RSN) Use Group Key cipher suite. For more information about the Use Group Key cipher suite, refer to Clause 7.3.2.25.1 of the IEEE 802.11i-2004 standard.

</p>
</dd>

### -field <a id="WDI_CIPHER_ALGO_WEP"></a><a id="wdi_cipher_algo_wep"></a><b>WDI_CIPHER_ALGO_WEP</b>

<dd>
<p>Specifies a WEP cipher algorithm with a cipher key of any length. </p>
</dd>

### -field <a id="WDI_CIPHER_ALGO_IHV_START"></a><a id="wdi_cipher_algo_ihv_start"></a><b>WDI_CIPHER_ALGO_IHV_START</b>

<dd>
<p>Specifies the start of the range that is used to define proprietary cipher algorithms that are developed by an independent hardware vendor (IHV). 

</p>
</dd>

### -field <a id="WDI_CIPHER_ALGO_IHV_END"></a><a id="wdi_cipher_algo_ihv_end"></a><b>WDI_CIPHER_ALGO_IHV_END</b>

<dd>
<p>Specifies the end of the range that is used to define proprietary authentication algorithms that are developed by an IHV.  </p>
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
<dt>Wditypes.hpp</dt>
</dl>
</td>
</tr>
</table>