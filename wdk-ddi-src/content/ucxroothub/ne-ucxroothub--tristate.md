---
UID: NE.ucxroothub._TRISTATE
title: TRISTATE
author: windows-driver-content
description: The TRISTATE enumeration indicates generic state values for true or false.
old-location: buses\tristate.htm
old-project: usbref
ms.assetid: 16D8981B-53D3-4886-A85F-B487701ED172
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS, UCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS, *PUCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ucxroothub.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TRISTATE
req.alt-loc: ucxroothub.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# TRISTATE enumeration



## -description
<p>The <b>TRISTATE</b> enumeration indicates generic state values for true or false.</p>


## -syntax

````
typedef enum _TRISTATE { 
  TriStateUnknown  = u,
  TriStateFalse    = f,
  TriStateTrue     = t
} TRISTATE;
````


## -enum-fields
<dl>

### -field <a id="TriStateUnknown"></a><a id="tristateunknown"></a><a id="TRISTATEUNKNOWN"></a><b>TriStateUnknown</b>

<dd>
<p>State is unknown.</p>
</dd>

### -field <a id="TriStateFalse"></a><a id="tristatefalse"></a><a id="TRISTATEFALSE"></a><b>TriStateFalse</b>

<dd>
<p>State is a false boolean value.</p>
</dd>

### -field <a id="TriStateTrue"></a><a id="tristatetrue"></a><a id="TRISTATETRUE"></a><b>TriStateTrue</b>

<dd>
<p>State is a true boolean value.</p>
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
<dt>Ucxroothub.h (include Ucxclass.h)</dt>
</dl>
</td>
</tr>
</table>