---
UID: NE.ks.KSIRP_REMOVAL_OPERATION
title: KSIRP_REMOVAL_OPERATION
author: windows-driver-content
description: .
old-location: stream\ksirp_removal_operation.htm
old-project: stream
ms.assetid: 10AC7347-6C6B-4A37-9298-B773ADCB3FDA
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: KSIRP_REMOVAL_OPERATION
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

# KSIRP_REMOVAL_OPERATION enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  KsAcquireOnly,
  KsAcquireAndRemove,
  KsAcquireOnlySingleItem,
  KsAcquireAndRemoveOnlySingleItem
} KSIRP_REMOVAL_OPERATION;
````


## -enum-fields
<dl>

### -field KsAcquireOnly

<dd></dd>

### -field KsAcquireAndRemove

<dd></dd>

### -field KsAcquireOnlySingleItem

<dd></dd>

### -field KsAcquireAndRemoveOnlySingleItem

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