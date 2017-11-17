---
UID: NE.ntddrilapitypes.RILSUPSVCINFOPARAMMASK
title: RILSUPSVCINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsupsvcinfoparammask.htm
ms.assetid: d3a4780f-6fd4-40d3-a629-5dad31720506
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
req.alt-api: RILSUPSVCINFOPARAMMASK
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

# RILSUPSVCINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILSUPSVCINFOPARAMMASK { 
  RIL_PARAM_SSI_FROM_NETWORK,
  RIL_PARAM_SSI_FAILURE_REASON,
  RIL_PARAM_SSI_SUPSVC_ACTION,
  RIL_PARAM_SSI_SUPSVC_TYPE,
  RIL_PARAM_SSI_CALL_FORWARDING_REASON,
  RIL_PARAM_SSI_CALL_BARRING_TYPE,
  RIL_PARAM_SSI_INFOCLASSES,
  RIL_PARAM_SSI_ALPHA_IDENTIFIER,
  RIL_PARAM_SSI_CALL_BARRING_PASSWORD,
  RIL_PARAM_SSI_NEW_CALL_BARRING_PASSWORD,
  RIL_PARAM_SSI_CALL_FORWARDING_SETTINGS,
  RIL_PARAM_SSI_CALLER_ID_SETTINGS,
  RIL_PARAM_SSI_DIALED_ID_SETTINGS,
  RIL_PARAM_SSI_HIDE_ID_SETTINGS,
  RIL_PARAM_SSI_CONNECTED_ID_SETTINGS,
  RIL_PARAM_SSI_SUPSERVICE_DATA,
  RIL_PARAM_SSI_ALL
} RILSUPSVCINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_SSI_FROM_NETWORK"></a><a id="ril_param_ssi_from_network"></a><b>RIL_PARAM_SSI_FROM_NETWORK</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_FAILURE_REASON"></a><a id="ril_param_ssi_failure_reason"></a><b>RIL_PARAM_SSI_FAILURE_REASON</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_SUPSVC_ACTION"></a><a id="ril_param_ssi_supsvc_action"></a><b>RIL_PARAM_SSI_SUPSVC_ACTION</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_SUPSVC_TYPE"></a><a id="ril_param_ssi_supsvc_type"></a><b>RIL_PARAM_SSI_SUPSVC_TYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_CALL_FORWARDING_REASON"></a><a id="ril_param_ssi_call_forwarding_reason"></a><b>RIL_PARAM_SSI_CALL_FORWARDING_REASON</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_CALL_BARRING_TYPE"></a><a id="ril_param_ssi_call_barring_type"></a><b>RIL_PARAM_SSI_CALL_BARRING_TYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_INFOCLASSES"></a><a id="ril_param_ssi_infoclasses"></a><b>RIL_PARAM_SSI_INFOCLASSES</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_ALPHA_IDENTIFIER"></a><a id="ril_param_ssi_alpha_identifier"></a><b>RIL_PARAM_SSI_ALPHA_IDENTIFIER</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_CALL_BARRING_PASSWORD"></a><a id="ril_param_ssi_call_barring_password"></a><b>RIL_PARAM_SSI_CALL_BARRING_PASSWORD</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_NEW_CALL_BARRING_PASSWORD"></a><a id="ril_param_ssi_new_call_barring_password"></a><b>RIL_PARAM_SSI_NEW_CALL_BARRING_PASSWORD</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_CALL_FORWARDING_SETTINGS"></a><a id="ril_param_ssi_call_forwarding_settings"></a><b>RIL_PARAM_SSI_CALL_FORWARDING_SETTINGS</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_CALLER_ID_SETTINGS"></a><a id="ril_param_ssi_caller_id_settings"></a><b>RIL_PARAM_SSI_CALLER_ID_SETTINGS</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_DIALED_ID_SETTINGS"></a><a id="ril_param_ssi_dialed_id_settings"></a><b>RIL_PARAM_SSI_DIALED_ID_SETTINGS</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_HIDE_ID_SETTINGS"></a><a id="ril_param_ssi_hide_id_settings"></a><b>RIL_PARAM_SSI_HIDE_ID_SETTINGS</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_CONNECTED_ID_SETTINGS"></a><a id="ril_param_ssi_connected_id_settings"></a><b>RIL_PARAM_SSI_CONNECTED_ID_SETTINGS</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_SUPSERVICE_DATA"></a><a id="ril_param_ssi_supservice_data"></a><b>RIL_PARAM_SSI_SUPSERVICE_DATA</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSI_ALL"></a><a id="ril_param_ssi_all"></a><b>RIL_PARAM_SSI_ALL</b>

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