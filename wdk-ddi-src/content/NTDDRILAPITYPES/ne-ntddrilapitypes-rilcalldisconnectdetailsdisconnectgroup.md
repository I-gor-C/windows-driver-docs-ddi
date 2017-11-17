---
UID: NE.ntddrilapitypes.RILCALLDISCONNECTDETAILSDISCONNECTGROUP
title: RILCALLDISCONNECTDETAILSDISCONNECTGROUP
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcalldisconnectdetailsdisconnectgroup.htm
ms.assetid: d546e936-f8c6-45ad-8027-a8495b4633dc
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
req.alt-api: RILCALLDISCONNECTDETAILSDISCONNECTGROUP
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

# RILCALLDISCONNECTDETAILSDISCONNECTGROUP enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCALLDISCONNECTDETAILSDISCONNECTGROUP { 
  RIL_CD_AS_CAUSE,
  RIL_CD_3GPP_NETWORK_CAUSE,
  RIL_CD_3GPP2_VENDOR_CAUSE,
  RIL_CD_OTHER_CAUSE,
  RIL_CD_3GPP_REJECT_CAUSE,
  RIL_CD_IMS_SIP_CAUSE,
  RIL_CD_CAUSE_MAX
} RILCALLDISCONNECTDETAILSDISCONNECTGROUP;
````


## -enum-fields
<dl>

### -field <a id="RIL_CD_AS_CAUSE"></a><a id="ril_cd_as_cause"></a><b>RIL_CD_AS_CAUSE</b>

<dd></dd>

### -field <a id="RIL_CD_3GPP_NETWORK_CAUSE"></a><a id="ril_cd_3gpp_network_cause"></a><b>RIL_CD_3GPP_NETWORK_CAUSE</b>

<dd></dd>

### -field <a id="RIL_CD_3GPP2_VENDOR_CAUSE"></a><a id="ril_cd_3gpp2_vendor_cause"></a><b>RIL_CD_3GPP2_VENDOR_CAUSE</b>

<dd></dd>

### -field <a id="RIL_CD_OTHER_CAUSE"></a><a id="ril_cd_other_cause"></a><b>RIL_CD_OTHER_CAUSE</b>

<dd></dd>

### -field <a id="RIL_CD_3GPP_REJECT_CAUSE"></a><a id="ril_cd_3gpp_reject_cause"></a><b>RIL_CD_3GPP_REJECT_CAUSE</b>

<dd></dd>

### -field <a id="RIL_CD_IMS_SIP_CAUSE"></a><a id="ril_cd_ims_sip_cause"></a><b>RIL_CD_IMS_SIP_CAUSE</b>

<dd></dd>

### -field <a id="RIL_CD_CAUSE_MAX"></a><a id="ril_cd_cause_max"></a><b>RIL_CD_CAUSE_MAX</b>

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