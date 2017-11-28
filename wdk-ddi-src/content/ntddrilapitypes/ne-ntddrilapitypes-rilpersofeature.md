---
UID: NE.ntddrilapitypes.RILPERSOFEATURE
title: RILPERSOFEATURE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilpersofeature.htm
old-project: netvista
ms.assetid: e212ab20-e9b4-4ccc-b0db-a82ca5b59573
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILPERSOFEATURE
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
req.iface: 
---

# RILPERSOFEATURE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILPERSOFEATURE { 
  RIL_PERSOFEATURE_3GPP_NET,
  RIL_PERSOFEATURE_3GPP_NETSUB,
  RIL_PERSOFEATURE_3GPP_SP,
  RIL_PERSOFEATURE_3GPP_CORP,
  RIL_PERSOFEATURE_3GPP_USIM,
  RIL_PERSOFEATURE_3GPP2_NETTYPE1,
  RIL_PERSOFEATURE_3GPP2_NETTYPE2,
  RIL_PERSOFEATURE_3GPP2_HRPD,
  RIL_PERSOFEATURE_3GPP2_SP,
  RIL_PERSOFEATURE_3GPP2_CORP,
  RIL_PERSOFEATURE_3GPP2_UIM,
  RIL_PERSOFEATURE_ALL
} RILPERSOFEATURE;
````


## -enum-fields
<dl>

### -field <a id="RIL_PERSOFEATURE_3GPP_NET"></a><a id="ril_persofeature_3gpp_net"></a><b>RIL_PERSOFEATURE_3GPP_NET</b>

<dd></dd>

### -field <a id="RIL_PERSOFEATURE_3GPP_NETSUB"></a><a id="ril_persofeature_3gpp_netsub"></a><b>RIL_PERSOFEATURE_3GPP_NETSUB</b>

<dd></dd>

### -field <a id="RIL_PERSOFEATURE_3GPP_SP"></a><a id="ril_persofeature_3gpp_sp"></a><b>RIL_PERSOFEATURE_3GPP_SP</b>

<dd></dd>

### -field <a id="RIL_PERSOFEATURE_3GPP_CORP"></a><a id="ril_persofeature_3gpp_corp"></a><b>RIL_PERSOFEATURE_3GPP_CORP</b>

<dd></dd>

### -field <a id="RIL_PERSOFEATURE_3GPP_USIM"></a><a id="ril_persofeature_3gpp_usim"></a><b>RIL_PERSOFEATURE_3GPP_USIM</b>

<dd></dd>

### -field <a id="RIL_PERSOFEATURE_3GPP2_NETTYPE1"></a><a id="ril_persofeature_3gpp2_nettype1"></a><b>RIL_PERSOFEATURE_3GPP2_NETTYPE1</b>

<dd></dd>

### -field <a id="RIL_PERSOFEATURE_3GPP2_NETTYPE2"></a><a id="ril_persofeature_3gpp2_nettype2"></a><b>RIL_PERSOFEATURE_3GPP2_NETTYPE2</b>

<dd></dd>

### -field <a id="RIL_PERSOFEATURE_3GPP2_HRPD"></a><a id="ril_persofeature_3gpp2_hrpd"></a><b>RIL_PERSOFEATURE_3GPP2_HRPD</b>

<dd></dd>

### -field <a id="RIL_PERSOFEATURE_3GPP2_SP"></a><a id="ril_persofeature_3gpp2_sp"></a><b>RIL_PERSOFEATURE_3GPP2_SP</b>

<dd></dd>

### -field <a id="RIL_PERSOFEATURE_3GPP2_CORP"></a><a id="ril_persofeature_3gpp2_corp"></a><b>RIL_PERSOFEATURE_3GPP2_CORP</b>

<dd></dd>

### -field <a id="RIL_PERSOFEATURE_3GPP2_UIM"></a><a id="ril_persofeature_3gpp2_uim"></a><b>RIL_PERSOFEATURE_3GPP2_UIM</b>

<dd></dd>

### -field <a id="RIL_PERSOFEATURE_ALL"></a><a id="ril_persofeature_all"></a><b>RIL_PERSOFEATURE_ALL</b>

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