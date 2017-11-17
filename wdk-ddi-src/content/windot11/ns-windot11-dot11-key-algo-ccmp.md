---
UID: NS.windot11.DOT11_KEY_ALGO_CCMP
title: DOT11_KEY_ALGO_CCMP
author: windows-driver-content
description: Important  The Native 802.11 Wireless LAN interface is deprecated in Windows 10 and later.
old-location: netvista\dot11_key_algo_ccmp.htm
ms.assetid: cf89ee80-d19d-4d97-b71f-8ebee4b96562
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: windot11.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating
   systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT11_KEY_ALGO_CCMP
req.alt-loc: windot11.h
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
ms.keywords: DOT11_KEY_ALGO_CCMP, DOT11_KEY_ALGO_CCMP, *PDOT11_KEY_ALGO_CCMP
req.iface: 
req.product: Windows 10 or later.
---

# DOT11_KEY_ALGO_CCMP structure



## -description

## -syntax

````
typedef struct DOT11_KEY_ALGO_CCMP {
  UCHAR ucIV48Counter[6];
  ULONG ulCCMPKeyLength;
  UCHAR ucCCMPKey[1];
} DOT11_KEY_ALGO_CCMP, *PDOT11_KEY_ALGO_CCMP;
````


## -struct-fields
<dl>

### -field <b>ucIV48Counter</b>

<dd>
<p>The initial 48-bit value of the AES-CCMP Packet Number (PN), which is used for replay protection.
     For more information about the PN, see 
     <a href="NULL">AES-CCMP</a>.</p>
</dd>

### -field <b>ulCCMPKeyLength</b>

<dd>
<p>The length, in bytes, of the AES-CCMP key material in the 
     <b>ucCCMPKey</b> array. If the authentication and cipher key derivation is performed by the operating
     system, this member will always have a value of 16.</p>
</dd>

### -field <b>ucCCMPKey</b>

<dd>
<p>The AES-CCMP key material.</p>
</dd>
</dl>

## -remarks
<p>When the AES-CCMP key is created, the 802.11 station must maintain separate PN counters for the key
    for the send and receive path. The station must initialize the PN counters in the following way:</p>

<p>Initialize the PN counter used for the receive path to the value specified in the 
      <b>ucIV48Counter</b> member.</p>

<p>Initialize the PN counter used for the send path to any value.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating
   systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Windot11.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="NULL">AES-CCMP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7362b20a-6ec4-4b22-8981-3a4b647a3cfa">
   DOT11_CIPHER_DEFAULT_KEY_VALUE</a>
</dt>
<dt>
<a href="netvista.oid_dot11_cipher_key_mapping_key">
   OID_DOT11_CIPHER_KEY_MAPPING_KEY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20DOT11_KEY_ALGO_CCMP structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
