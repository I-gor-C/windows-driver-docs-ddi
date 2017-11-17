---
UID: NE.wditypes._WDI_FIPS_MODE
title: WDI_FIPS_MODE
author: windows-driver-content
description: The WDI_FIPS_MODE enumeration defines values that specify if FIPS mode is enabled or not.
old-location: netvista\wdi_fips_mode.htm
ms.assetid: 88EE4C63-C9D8-41D2-800E-9FFD5EF4962A
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_FIPS_MODE
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
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WDI_FIPS_MODE enumeration



## -description
<p>The 
  WDI_FIPS_MODE enumeration defines values that specify if FIPS mode is enabled or not.</p>


## -syntax

````
typedef enum _WDI_FIPS_MODE { 
  WDI_FIPS_MODE_DISABLED  = 0,
  WDI_FIPS_MODE_ENABLED   = 1,
  WDI_FIPS_MODE_UNKNOWN   = 2
} WDI_FIPS_MODE;
````


## -enum-fields
<dl>

### -field <a id="WDI_FIPS_MODE_DISABLED"></a><a id="wdi_fips_mode_disabled"></a><b>WDI_FIPS_MODE_DISABLED</b>

<dd>
<p>FIPS mode is disabled.</p>
</dd>

### -field <a id="WDI_FIPS_MODE_ENABLED"></a><a id="wdi_fips_mode_enabled"></a><b>WDI_FIPS_MODE_ENABLED</b>

<dd>
<p>FIPS mode is enabled.</p>
</dd>

### -field <a id="WDI_FIPS_MODE_UNKNOWN"></a><a id="wdi_fips_mode_unknown"></a><b>WDI_FIPS_MODE_UNKNOWN</b>

<dd>
<p>Unknown.</p>
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