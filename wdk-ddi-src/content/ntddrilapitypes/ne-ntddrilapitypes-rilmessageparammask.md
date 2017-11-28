---
UID: NE.ntddrilapitypes.RILMESSAGEPARAMMASK
title: RILMESSAGEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmessageparammask.htm
old-project: netvista
ms.assetid: 718c9d10-fd89-4d31-815e-da4dea0a3f34
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
req.alt-api: RILMESSAGEPARAMMASK
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

# RILMESSAGEPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMESSAGEPARAMMASK { 
  RIL_PARAM_M_TYPE,
  RIL_PARAM_M_FLAGS,
  RIL_PARAM_M_ORIGADDRESS,
  RIL_PARAM_M_TGTRECIPADDRESS,
  RIL_PARAM_M_DESTADDRESS,
  RIL_PARAM_M_SCRECEIVETIME,
  RIL_PARAM_M_TGTSCRECEIVETIME,
  RIL_PARAM_M_TGTDISCHARGETIME,
  RIL_PARAM_M_PROTOCOLID,
  RIL_PARAM_M_DATACODING,
  RIL_PARAM_M_TGTDLVSTATUS,
  RIL_PARAM_M_VPFORMAT,
  RIL_PARAM_M_VP,
  RIL_PARAM_M_GEOSCOPE,
  RIL_PARAM_M_MSGCODE,
  RIL_PARAM_M_UPDATENUMBER,
  RIL_PARAM_M_ID,
  RIL_PARAM_M_TOTALPAGES,
  RIL_PARAM_M_PAGENUMBER,
  RIL_PARAM_M_HDRLENGTH,
  RIL_PARAM_M_SERIALNUMBER,
  RIL_PARAM_M_MSGLENGTH,
  RIL_PARAM_M_HDR,
  RIL_PARAM_M_MSG,
  RIL_PARAM_M_WARNINGTYPE,
  RIL_PARAM_M_EUSERALERT,
  RIL_PARAM_M_POPUP,
  RIL_PARAM_M_MSGID,
  RIL_PARAM_M_ORIGSUBADDRESS,
  RIL_PARAM_M_DESTSUBADDRESS,
  RIL_PARAM_M_DIGIT,
  RIL_PARAM_M_PRIVACY,
  RIL_PARAM_M_PRIORITY,
  RIL_PARAM_M_TELESERVICE,
  RIL_PARAM_M_LANG,
  RIL_PARAM_M_VALIDITYPERIODABS,
  RIL_PARAM_M_VALIDITYPERIODREL,
  RIL_PARAM_M_DEFERREDDELTIMEABS,
  RIL_PARAM_M_DEFERREDDELTIMEREL,
  RIL_PARAM_M_ENCODING,
  RIL_PARAM_M_USERRESPONSECODE,
  RIL_PARAM_M_DISPLAYMODE,
  RIL_PARAM_M_CALLBACKNUM,
  RIL_PARAM_M_NUMMSGS,
  RIL_PARAM_M_CAUSECODE,
  RIL_PARAM_M_REPLYSEQNUMBER,
  RIL_PARAM_M_SERVICEID,
  RIL_PARAM_M_USERACK,
  RIL_PARAM_M_DELIVERYACK,
  RIL_PARAM_M_ALERTONMSGDELIVERY,
  RIL_PARAM_M_HDRLENGTHCDMA,
  RIL_PARAM_M_MSGSTATUSTYPE,
  RIL_PARAM_M_BEARERREPLYACK,
  RIL_PARAM_M_ALL_IN_DELIVER,
  RIL_PARAM_M_ALL_IN_STATUS,
  RIL_PARAM_M_ALL_OUT_SUBMIT,
  RIL_PARAM_M_ALL_BC_GENERAL,
  RIL_PARAM_M_ALL_IN_IS637DELIVER,
  RIL_PARAM_M_ALL_OUT_IS637SUBMIT,
  RIL_PARAM_M_ALL_IN_IS637STATUS,
  RIL_PARAM_M_ALL_OUT_IS637STATUS
} RILMESSAGEPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_M_TYPE"></a><a id="ril_param_m_type"></a><b>RIL_PARAM_M_TYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_FLAGS"></a><a id="ril_param_m_flags"></a><b>RIL_PARAM_M_FLAGS</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_ORIGADDRESS"></a><a id="ril_param_m_origaddress"></a><b>RIL_PARAM_M_ORIGADDRESS</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_TGTRECIPADDRESS"></a><a id="ril_param_m_tgtrecipaddress"></a><b>RIL_PARAM_M_TGTRECIPADDRESS</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_DESTADDRESS"></a><a id="ril_param_m_destaddress"></a><b>RIL_PARAM_M_DESTADDRESS</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_SCRECEIVETIME"></a><a id="ril_param_m_screceivetime"></a><b>RIL_PARAM_M_SCRECEIVETIME</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_TGTSCRECEIVETIME"></a><a id="ril_param_m_tgtscreceivetime"></a><b>RIL_PARAM_M_TGTSCRECEIVETIME</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_TGTDISCHARGETIME"></a><a id="ril_param_m_tgtdischargetime"></a><b>RIL_PARAM_M_TGTDISCHARGETIME</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_PROTOCOLID"></a><a id="ril_param_m_protocolid"></a><b>RIL_PARAM_M_PROTOCOLID</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_DATACODING"></a><a id="ril_param_m_datacoding"></a><b>RIL_PARAM_M_DATACODING</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_TGTDLVSTATUS"></a><a id="ril_param_m_tgtdlvstatus"></a><b>RIL_PARAM_M_TGTDLVSTATUS</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_VPFORMAT"></a><a id="ril_param_m_vpformat"></a><b>RIL_PARAM_M_VPFORMAT</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_VP"></a><a id="ril_param_m_vp"></a><b>RIL_PARAM_M_VP</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_GEOSCOPE"></a><a id="ril_param_m_geoscope"></a><b>RIL_PARAM_M_GEOSCOPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_MSGCODE"></a><a id="ril_param_m_msgcode"></a><b>RIL_PARAM_M_MSGCODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_UPDATENUMBER"></a><a id="ril_param_m_updatenumber"></a><b>RIL_PARAM_M_UPDATENUMBER</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_ID"></a><a id="ril_param_m_id"></a><b>RIL_PARAM_M_ID</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_TOTALPAGES"></a><a id="ril_param_m_totalpages"></a><b>RIL_PARAM_M_TOTALPAGES</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_PAGENUMBER"></a><a id="ril_param_m_pagenumber"></a><b>RIL_PARAM_M_PAGENUMBER</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_HDRLENGTH"></a><a id="ril_param_m_hdrlength"></a><b>RIL_PARAM_M_HDRLENGTH</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_SERIALNUMBER"></a><a id="ril_param_m_serialnumber"></a><b>RIL_PARAM_M_SERIALNUMBER</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_MSGLENGTH"></a><a id="ril_param_m_msglength"></a><b>RIL_PARAM_M_MSGLENGTH</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_HDR"></a><a id="ril_param_m_hdr"></a><b>RIL_PARAM_M_HDR</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_MSG"></a><a id="ril_param_m_msg"></a><b>RIL_PARAM_M_MSG</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_WARNINGTYPE"></a><a id="ril_param_m_warningtype"></a><b>RIL_PARAM_M_WARNINGTYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_EUSERALERT"></a><a id="ril_param_m_euseralert"></a><b>RIL_PARAM_M_EUSERALERT</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_POPUP"></a><a id="ril_param_m_popup"></a><b>RIL_PARAM_M_POPUP</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_MSGID"></a><a id="ril_param_m_msgid"></a><b>RIL_PARAM_M_MSGID</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_ORIGSUBADDRESS"></a><a id="ril_param_m_origsubaddress"></a><b>RIL_PARAM_M_ORIGSUBADDRESS</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_DESTSUBADDRESS"></a><a id="ril_param_m_destsubaddress"></a><b>RIL_PARAM_M_DESTSUBADDRESS</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_DIGIT"></a><a id="ril_param_m_digit"></a><b>RIL_PARAM_M_DIGIT</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_PRIVACY"></a><a id="ril_param_m_privacy"></a><b>RIL_PARAM_M_PRIVACY</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_PRIORITY"></a><a id="ril_param_m_priority"></a><b>RIL_PARAM_M_PRIORITY</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_TELESERVICE"></a><a id="ril_param_m_teleservice"></a><b>RIL_PARAM_M_TELESERVICE</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_LANG"></a><a id="ril_param_m_lang"></a><b>RIL_PARAM_M_LANG</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_VALIDITYPERIODABS"></a><a id="ril_param_m_validityperiodabs"></a><b>RIL_PARAM_M_VALIDITYPERIODABS</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_VALIDITYPERIODREL"></a><a id="ril_param_m_validityperiodrel"></a><b>RIL_PARAM_M_VALIDITYPERIODREL</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_DEFERREDDELTIMEABS"></a><a id="ril_param_m_deferreddeltimeabs"></a><b>RIL_PARAM_M_DEFERREDDELTIMEABS</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_DEFERREDDELTIMEREL"></a><a id="ril_param_m_deferreddeltimerel"></a><b>RIL_PARAM_M_DEFERREDDELTIMEREL</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_ENCODING"></a><a id="ril_param_m_encoding"></a><b>RIL_PARAM_M_ENCODING</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_USERRESPONSECODE"></a><a id="ril_param_m_userresponsecode"></a><b>RIL_PARAM_M_USERRESPONSECODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_DISPLAYMODE"></a><a id="ril_param_m_displaymode"></a><b>RIL_PARAM_M_DISPLAYMODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_CALLBACKNUM"></a><a id="ril_param_m_callbacknum"></a><b>RIL_PARAM_M_CALLBACKNUM</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_NUMMSGS"></a><a id="ril_param_m_nummsgs"></a><b>RIL_PARAM_M_NUMMSGS</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_CAUSECODE"></a><a id="ril_param_m_causecode"></a><b>RIL_PARAM_M_CAUSECODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_REPLYSEQNUMBER"></a><a id="ril_param_m_replyseqnumber"></a><b>RIL_PARAM_M_REPLYSEQNUMBER</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_SERVICEID"></a><a id="ril_param_m_serviceid"></a><b>RIL_PARAM_M_SERVICEID</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_USERACK"></a><a id="ril_param_m_userack"></a><b>RIL_PARAM_M_USERACK</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_DELIVERYACK"></a><a id="ril_param_m_deliveryack"></a><b>RIL_PARAM_M_DELIVERYACK</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_ALERTONMSGDELIVERY"></a><a id="ril_param_m_alertonmsgdelivery"></a><b>RIL_PARAM_M_ALERTONMSGDELIVERY</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_HDRLENGTHCDMA"></a><a id="ril_param_m_hdrlengthcdma"></a><b>RIL_PARAM_M_HDRLENGTHCDMA</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_MSGSTATUSTYPE"></a><a id="ril_param_m_msgstatustype"></a><b>RIL_PARAM_M_MSGSTATUSTYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_BEARERREPLYACK"></a><a id="ril_param_m_bearerreplyack"></a><b>RIL_PARAM_M_BEARERREPLYACK</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_ALL_IN_DELIVER"></a><a id="ril_param_m_all_in_deliver"></a><b>RIL_PARAM_M_ALL_IN_DELIVER</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_ALL_IN_STATUS"></a><a id="ril_param_m_all_in_status"></a><b>RIL_PARAM_M_ALL_IN_STATUS</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_ALL_OUT_SUBMIT"></a><a id="ril_param_m_all_out_submit"></a><b>RIL_PARAM_M_ALL_OUT_SUBMIT</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_ALL_BC_GENERAL"></a><a id="ril_param_m_all_bc_general"></a><b>RIL_PARAM_M_ALL_BC_GENERAL</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_ALL_IN_IS637DELIVER"></a><a id="ril_param_m_all_in_is637deliver"></a><b>RIL_PARAM_M_ALL_IN_IS637DELIVER</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_ALL_OUT_IS637SUBMIT"></a><a id="ril_param_m_all_out_is637submit"></a><b>RIL_PARAM_M_ALL_OUT_IS637SUBMIT</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_ALL_IN_IS637STATUS"></a><a id="ril_param_m_all_in_is637status"></a><b>RIL_PARAM_M_ALL_IN_IS637STATUS</b>

<dd></dd>

### -field <a id="RIL_PARAM_M_ALL_OUT_IS637STATUS"></a><a id="ril_param_m_all_out_is637status"></a><b>RIL_PARAM_M_ALL_OUT_IS637STATUS</b>

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