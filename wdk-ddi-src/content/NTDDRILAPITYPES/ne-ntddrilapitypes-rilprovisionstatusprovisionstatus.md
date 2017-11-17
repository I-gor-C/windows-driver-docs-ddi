---
UID: NE.ntddrilapitypes.RILPROVISIONSTATUSPROVISIONSTATUS
title: RILPROVISIONSTATUSPROVISIONSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilprovisionstatusprovisionstatus.htm
ms.assetid: ed7fc20a-b5d5-4dc6-ab95-5ee9258dbdae
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILPROVISIONSTATUSPROVISIONSTATUS
req.alt-loc: ntddrilapitypes.h
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
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
req.iface: 
---

# RILPROVISIONSTATUSPROVISIONSTATUS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILPROVISIONSTATUSPROVISIONSTATUS { 
  RIL_PROVISIONSTAT_SUCCESS,
  RIL_PROVISIONSTAT_FAILURE_END,
  RIL_PROVISIONSTAT_FAILURE_RETRY,
  RIL_PROVISIONSTAT_NEEDED,
  RIL_PROVISIONSTAT_BIP_STARTED,
  RIL_PROVISIONSTAT_BIP_SUCCESS,
  RIL_PROVISIONSTAT_MAX
} RILPROVISIONSTATUSPROVISIONSTATUS;
````


## -enum-fields
<dl>

### -field <a id="RIL_PROVISIONSTAT_SUCCESS"></a><a id="ril_provisionstat_success"></a><b>RIL_PROVISIONSTAT_SUCCESS</b>

<dd></dd>

### -field <a id="RIL_PROVISIONSTAT_FAILURE_END"></a><a id="ril_provisionstat_failure_end"></a><b>RIL_PROVISIONSTAT_FAILURE_END</b>

<dd></dd>

### -field <a id="RIL_PROVISIONSTAT_FAILURE_RETRY"></a><a id="ril_provisionstat_failure_retry"></a><b>RIL_PROVISIONSTAT_FAILURE_RETRY</b>

<dd></dd>

### -field <a id="RIL_PROVISIONSTAT_NEEDED"></a><a id="ril_provisionstat_needed"></a><b>RIL_PROVISIONSTAT_NEEDED</b>

<dd></dd>

### -field <a id="RIL_PROVISIONSTAT_BIP_STARTED"></a><a id="ril_provisionstat_bip_started"></a><b>RIL_PROVISIONSTAT_BIP_STARTED</b>

<dd></dd>

### -field <a id="RIL_PROVISIONSTAT_BIP_SUCCESS"></a><a id="ril_provisionstat_bip_success"></a><b>RIL_PROVISIONSTAT_BIP_SUCCESS</b>

<dd></dd>

### -field <a id="RIL_PROVISIONSTAT_MAX"></a><a id="ril_provisionstat_max"></a><b>RIL_PROVISIONSTAT_MAX</b>

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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>