---
UID: NE.ks.KSSTACK_USE
title: KSSTACK_USE
author: windows-driver-content
description: .
old-location: stream\ksstack_use.htm
old-project: stream
ms.assetid: 76B45154-5E81-4515-ADEE-11401FDF4681
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSSTACK_USE
req.alt-loc: Ks.h
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
req.iface: 
---

# KSSTACK_USE enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  KsStackCopyToNewLocation,
  KsStackReuseCurrentLocation,
  KsStackUseNewLocation
} KSSTACK_USE;
````


## -enum-fields
<dl>

### -field <a id="KsStackCopyToNewLocation"></a><a id="ksstackcopytonewlocation"></a><a id="KSSTACKCOPYTONEWLOCATION"></a><b>KsStackCopyToNewLocation</b>

<dd></dd>

### -field <a id="KsStackReuseCurrentLocation"></a><a id="ksstackreusecurrentlocation"></a><a id="KSSTACKREUSECURRENTLOCATION"></a><b>KsStackReuseCurrentLocation</b>

<dd></dd>

### -field <a id="KsStackUseNewLocation"></a><a id="ksstackusenewlocation"></a><a id="KSSTACKUSENEWLOCATION"></a><b>KsStackUseNewLocation</b>

<dd></dd>
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
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>