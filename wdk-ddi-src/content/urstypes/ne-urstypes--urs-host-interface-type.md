---
UID: NE.urstypes._URS_HOST_INTERFACE_TYPE
title: URS_HOST_INTERFACE_TYPE
author: windows-driver-content
description: Defines values for the various types of USB host controllers.
old-location: buses\urs_host_interface_type.htm
old-project: usbref
ms.assetid: E019CCED-3511-4B7B-B6C9-09FF31B0547A
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: URS_CONFIG, URS_CONFIG, *PURS_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: urstypes.h
req.include-header: Urscx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 
req.alt-api: URS_HOST_INTERFACE_TYPE
req.alt-loc: urstypes.h
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
req.iface: 
req.product: Windows 10 or later.
---

# URS_HOST_INTERFACE_TYPE enumeration



## -description
<p>Defines values for the various types of USB host controllers.</p>


## -syntax

````
typedef enum _URS_HOST_INTERFACE_TYPE { 
  UrsHostInterfaceTypeEhci   = 0,
  UrsHostInterfaceTypeXhci,
  UrsHostInterfaceTypeOther
} URS_HOST_INTERFACE_TYPE;
````


## -enum-fields
<dl>

### -field UrsHostInterfaceTypeEhci

<dd>
<p>Indicates an EHCI host controller.</p>
</dd>

### -field UrsHostInterfaceTypeXhci

<dd>
<p>Indicates an xHCI host controller.</p>
</dd>

### -field UrsHostInterfaceTypeOther

<dd>
<p>Indicates a generic host controller.</p>
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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Urstypes.h (include Urscx.h)</dt>
</dl>
</td>
</tr>
</table>