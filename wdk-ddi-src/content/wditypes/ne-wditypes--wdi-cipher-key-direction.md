---
UID: NE.wditypes._WDI_CIPHER_KEY_DIRECTION
title: WDI_CIPHER_KEY_DIRECTION
author: windows-driver-content
description: The WDI_CIPHER_KEY_DIRECTION enumeration defines the traffic directions decrypted by a cipher key.
old-location: netvista\wdi_cipher_key_direction.htm
old-project: netvista
ms.assetid: BE054858-F61A-488B-87A3-615A646C27F0
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
req.alt-api: WDI_CIPHER_KEY_DIRECTION
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

# WDI_CIPHER_KEY_DIRECTION enumeration



## -description
<p>The WDI_CIPHER_KEY_DIRECTION enumeration defines the traffic directions decrypted by a cipher key.</p>


## -syntax

````
typedef enum _WDI_CIPHER_KEY_DIRECTION { 
  WDI_CIPHER_KEY_DIRECTION_INBOUND   = 1,
  WDI_CIPHER_KEY_DIRECTION_OUTBOUND  = 2,
  WDI_CIPHER_KEY_DIRECTION_BOTH      = 3
} WDI_CIPHER_KEY_DIRECTION;
````


## -enum-fields
<dl>

### -field <a id="WDI_CIPHER_KEY_DIRECTION_INBOUND"></a><a id="wdi_cipher_key_direction_inbound"></a><b>WDI_CIPHER_KEY_DIRECTION_INBOUND</b>

<dd>
<p>The cipher key decrypts packets received from a peer.</p>
</dd>

### -field <a id="WDI_CIPHER_KEY_DIRECTION_OUTBOUND"></a><a id="wdi_cipher_key_direction_outbound"></a><b>WDI_CIPHER_KEY_DIRECTION_OUTBOUND</b>

<dd>
<p>The cipher key decrypts packets transmitted to a peer.</p>
</dd>

### -field <a id="WDI_CIPHER_KEY_DIRECTION_BOTH"></a><a id="wdi_cipher_key_direction_both"></a><b>WDI_CIPHER_KEY_DIRECTION_BOTH</b>

<dd>
<p>The cipher key  decrypts packets received from or transmitted to a peer.</p>
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