---
UID: NE.ntddrilapitypes.RILCALLINFOPARAMMASK
title: RILCALLINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallinfoparammask.htm
old-project: netvista
ms.assetid: 7e6138f6-4728-4072-9600-749594f23b68
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
req.alt-api: RILCALLINFOPARAMMASK
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

# RILCALLINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCALLINFOPARAMMASK { 
  RIL_PARAM_CI_ID,
  RIL_PARAM_CI_DIRECTION,
  RIL_PARAM_CI_STATUS,
  RIL_PARAM_CI_TYPE,
  RIL_PARAM_CI_MULTIPARTY,
  RIL_PARAM_CI_ADDRESS,
  RIL_PARAM_CI_SUBADDRESS,
  RIL_PARAM_CI_DESCRIPTION,
  RIL_PARAM_CI_NUM_PRES_IND,
  RIL_PARAM_CI_NAME_PRES_IND,
  RIL_PARAM_CI_FLAGS,
  RIL_PARAM_CI_DISCONNECTINITIATOR,
  RIL_PARAM_CI_DISCONNECTREASON,
  RIL_PARAM_CI_DISCONNECTDETAILS,
  RIL_PARAM_CI_OFFERANSWER,
  RIL_PARAM_CI_HANDOVERSTATE,
  RIL_PARAM_CI_CALLMODIFICATIONCAUSE,
  RIL_PARAM_CI_RTTMODETYPE,
  RIL_PARAM_CI_RTTCAPINFO,
  RIL_PARAM_CI_RTTACTION,
  RIL_PARAM_CI_ALL
} RILCALLINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_CI_ID"></a><a id="ril_param_ci_id"></a><b>RIL_PARAM_CI_ID</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_DIRECTION"></a><a id="ril_param_ci_direction"></a><b>RIL_PARAM_CI_DIRECTION</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_STATUS"></a><a id="ril_param_ci_status"></a><b>RIL_PARAM_CI_STATUS</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_TYPE"></a><a id="ril_param_ci_type"></a><b>RIL_PARAM_CI_TYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_MULTIPARTY"></a><a id="ril_param_ci_multiparty"></a><b>RIL_PARAM_CI_MULTIPARTY</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_ADDRESS"></a><a id="ril_param_ci_address"></a><b>RIL_PARAM_CI_ADDRESS</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_SUBADDRESS"></a><a id="ril_param_ci_subaddress"></a><b>RIL_PARAM_CI_SUBADDRESS</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_DESCRIPTION"></a><a id="ril_param_ci_description"></a><b>RIL_PARAM_CI_DESCRIPTION</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_NUM_PRES_IND"></a><a id="ril_param_ci_num_pres_ind"></a><b>RIL_PARAM_CI_NUM_PRES_IND</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_NAME_PRES_IND"></a><a id="ril_param_ci_name_pres_ind"></a><b>RIL_PARAM_CI_NAME_PRES_IND</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_FLAGS"></a><a id="ril_param_ci_flags"></a><b>RIL_PARAM_CI_FLAGS</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_DISCONNECTINITIATOR"></a><a id="ril_param_ci_disconnectinitiator"></a><b>RIL_PARAM_CI_DISCONNECTINITIATOR</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_DISCONNECTREASON"></a><a id="ril_param_ci_disconnectreason"></a><b>RIL_PARAM_CI_DISCONNECTREASON</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_DISCONNECTDETAILS"></a><a id="ril_param_ci_disconnectdetails"></a><b>RIL_PARAM_CI_DISCONNECTDETAILS</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_OFFERANSWER"></a><a id="ril_param_ci_offeranswer"></a><b>RIL_PARAM_CI_OFFERANSWER</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_HANDOVERSTATE"></a><a id="ril_param_ci_handoverstate"></a><b>RIL_PARAM_CI_HANDOVERSTATE</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_CALLMODIFICATIONCAUSE"></a><a id="ril_param_ci_callmodificationcause"></a><b>RIL_PARAM_CI_CALLMODIFICATIONCAUSE</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_RTTMODETYPE"></a><a id="ril_param_ci_rttmodetype"></a><b>RIL_PARAM_CI_RTTMODETYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_RTTCAPINFO"></a><a id="ril_param_ci_rttcapinfo"></a><b>RIL_PARAM_CI_RTTCAPINFO</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_RTTACTION"></a><a id="ril_param_ci_rttaction"></a><b>RIL_PARAM_CI_RTTACTION</b>

<dd></dd>

### -field <a id="RIL_PARAM_CI_ALL"></a><a id="ril_param_ci_all"></a><b>RIL_PARAM_CI_ALL</b>

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