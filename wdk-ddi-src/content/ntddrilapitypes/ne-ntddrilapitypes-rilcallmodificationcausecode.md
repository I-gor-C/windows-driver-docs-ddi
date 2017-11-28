---
UID: NE.ntddrilapitypes.RILCALLMODIFICATIONCAUSECODE
title: RILCALLMODIFICATIONCAUSECODE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmodificationcausecode.htm
old-project: netvista
ms.assetid: d2785ee2-6e5d-474e-9d0f-57da956b6ec7
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
req.alt-api: RILCALLMODIFICATIONCAUSECODE
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

# RILCALLMODIFICATIONCAUSECODE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCALLMODIFICATIONCAUSECODE { 
  RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_RTP_TIMEOUT,
  RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_QOS,
  RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_PACKET_LOSS,
  RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_LOW_THROUGHPUT,
  RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_THERMAL_MITIGATION,
  RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_LIPSYNC,
  RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_GENERIC_ERROR,
  RIL_CALL_MODIFIED_CAUSE_MAX
} RILCALLMODIFICATIONCAUSECODE;
````


## -enum-fields
<dl>

### -field <a id="RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_RTP_TIMEOUT"></a><a id="ril_call_modified_cause_downgrade_rtp_timeout"></a><b>RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_RTP_TIMEOUT</b>

<dd></dd>

### -field <a id="RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_QOS"></a><a id="ril_call_modified_cause_downgrade_qos"></a><b>RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_QOS</b>

<dd></dd>

### -field <a id="RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_PACKET_LOSS"></a><a id="ril_call_modified_cause_downgrade_packet_loss"></a><b>RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_PACKET_LOSS</b>

<dd></dd>

### -field <a id="RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_LOW_THROUGHPUT"></a><a id="ril_call_modified_cause_downgrade_low_throughput"></a><b>RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_LOW_THROUGHPUT</b>

<dd></dd>

### -field <a id="RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_THERMAL_MITIGATION"></a><a id="ril_call_modified_cause_downgrade_thermal_mitigation"></a><b>RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_THERMAL_MITIGATION</b>

<dd></dd>

### -field <a id="RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_LIPSYNC"></a><a id="ril_call_modified_cause_downgrade_lipsync"></a><b>RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_LIPSYNC</b>

<dd></dd>

### -field <a id="RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_GENERIC_ERROR"></a><a id="ril_call_modified_cause_downgrade_generic_error"></a><b>RIL_CALL_MODIFIED_CAUSE_DOWNGRADE_GENERIC_ERROR</b>

<dd></dd>

### -field <a id="RIL_CALL_MODIFIED_CAUSE_MAX"></a><a id="ril_call_modified_cause_max"></a><b>RIL_CALL_MODIFIED_CAUSE_MAX</b>

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