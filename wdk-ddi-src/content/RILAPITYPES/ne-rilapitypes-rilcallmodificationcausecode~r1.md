---
UID: NE.rilapitypes.RILCALLMODIFICATIONCAUSECODE~r1
title: RILCALLMODIFICATIONCAUSECODE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmodificationcausecode_2.htm
ms.assetid: 44309e4e-a0a0-4aed-b942-2d15b8ab07dc
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILCALLMODIFICATIONCAUSECODE
req.alt-loc: rilapitypes.h
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
ms.keywords: RIL_WritePhonebookEntry
req.iface: 
req.product: Windows 10 or later.
---

# RILCALLMODIFICATIONCAUSECODE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>