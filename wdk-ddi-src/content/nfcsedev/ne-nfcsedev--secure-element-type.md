---
UID: NE.nfcsedev._SECURE_ELEMENT_TYPE
title: SECURE_ELEMENT_TYPE
author: windows-driver-content
description: Indicates the type of a secure element.
old-location: nfpdrivers\_secure_element_type.htm
ms.assetid: 118B63D1-713A-4F8C-B97A-53BB6D0B819E
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: nfpdrivers
req.header: nfcsedev.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SECURE_ELEMENT_TYPE, *PSECURE_ELEMENT_TYPE
req.alt-loc: nfcsedev.h
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
ms.keywords: NFCCX_DRIVER_GLOBALS, NFCCX_DRIVER_GLOBALS, *PNFCCX_DRIVER_GLOBALS
req.iface: 
---

# SECURE_ELEMENT_TYPE enumeration



## -description
<p>Indicates the type of a secure element.</p>


## -syntax

````
typedef enum _SECURE_ELEMENT_TYPE { 
  Integrated  = 0,
  External    = 1,
  DeviceHost  = 2
} SECURE_ELEMENT_TYPE, *PSECURE_ELEMENT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="Integrated"></a><a id="integrated"></a><a id="INTEGRATED"></a><b>Integrated</b>

<dd>
<p>Integrated secure element.</p>
</dd>

### -field <a id="External"></a><a id="external"></a><a id="EXTERNAL"></a><b>External</b>

<dd>
<p>Separate UICC-based secure element.</p>
</dd>

### -field <a id="DeviceHost"></a><a id="devicehost"></a><a id="DEVICEHOST"></a><b>DeviceHost</b>

<dd>
<p>Separate HCE-based secure element.</p>
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
<dt>Nfcsedev.h</dt>
</dl>
</td>
</tr>
</table>