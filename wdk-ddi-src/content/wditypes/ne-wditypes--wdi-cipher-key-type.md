---
UID: NE.wditypes._WDI_CIPHER_KEY_TYPE
title: WDI_CIPHER_KEY_TYPE
author: windows-driver-content
description: The WDI_CIPHER_KEY_TYPE enumeration defines the cipher key types.
old-location: netvista\wdi_cipher_key_type.htm
old-project: netvista
ms.assetid: 09874F77-5A9C-4C98-996F-29BB90CAE4B6
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: WDI_CIPHER_KEY_TYPE
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

# WDI_CIPHER_KEY_TYPE enumeration



## -description
<p>The WDI_CIPHER_KEY_TYPE enumeration defines the cipher key types.</p>


## -syntax

````
typedef enum _WDI_CIPHER_KEY_TYPE { 
  WDI_CIPHER_KEY_TYPE_PAIRWISE_KEY  = 1,
  WDI_CIPHER_KEY_TYPE_GROUP_KEY     = 2,
  WDI_CIPHER_KEY_TYPE_IGTK          = 3
} WDI_CIPHER_KEY_TYPE;
````


## -enum-fields
<dl>

### -field WDI_CIPHER_KEY_TYPE_PAIRWISE_KEY

<dd>
<p>The key is a pairwise key to another station.</p>
</dd>

### -field WDI_CIPHER_KEY_TYPE_GROUP_KEY

<dd>
<p>The key is a group key.</p>
</dd>

### -field WDI_CIPHER_KEY_TYPE_IGTK

<dd>
<p>The key is an IGTK.</p>
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