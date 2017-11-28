---
UID: NE.wditypes._WDI_DS_INFO
title: WDI_DS_INFO
author: windows-driver-content
description: The WDI_DS_INFO enumeration defines values that specify whether the port is connected to the same DS that it was previously associated to.
old-location: netvista\wdi_ds_info.htm
old-project: netvista
ms.assetid: 4375FF5C-8772-43AB-844B-4AD5E044AF55
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: WDI_DS_INFO
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

# WDI_DS_INFO enumeration



## -description
<p>The WDI_DS_INFO enumeration defines values that specify whether the port is connected to the same DS that it was previously associated to.</p>


## -syntax

````
typedef enum _WDI_DS_INFO { 
  WDI_DS_CHANGED    = 1,
  WDI_DS_UNCHANGED  = 2,
  WDI_DS_UNKNOWN    = 3
} WDI_DS_INFO;
````


## -enum-fields
<dl>

### -field <a id="WDI_DS_CHANGED"></a><a id="wdi_ds_changed"></a><b>WDI_DS_CHANGED</b>

<dd>
<p>New DS.</p>
</dd>

### -field <a id="WDI_DS_UNCHANGED"></a><a id="wdi_ds_unchanged"></a><b>WDI_DS_UNCHANGED</b>

<dd>
<p>Same DS as previously associated.</p>
</dd>

### -field <a id="WDI_DS_UNKNOWN"></a><a id="wdi_ds_unknown"></a><b>WDI_DS_UNKNOWN</b>

<dd>
<p>Unable to determine if the DS has changed.</p>
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