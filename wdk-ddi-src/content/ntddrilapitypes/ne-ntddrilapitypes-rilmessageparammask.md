---
UID: NE.ntddrilapitypes.RILMESSAGEPARAMMASK
title: RILMESSAGEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmessageparammask.htm
old-project: netvista
ms.assetid: 718c9d10-fd89-4d31-815e-da4dea0a3f34
ms.author: windowsdriverdev
ms.date: 11/30/2017
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

### -field RIL_PARAM_M_TYPE

<dd></dd>

### -field RIL_PARAM_M_FLAGS

<dd></dd>

### -field RIL_PARAM_M_ORIGADDRESS

<dd></dd>

### -field RIL_PARAM_M_TGTRECIPADDRESS

<dd></dd>

### -field RIL_PARAM_M_DESTADDRESS

<dd></dd>

### -field RIL_PARAM_M_SCRECEIVETIME

<dd></dd>

### -field RIL_PARAM_M_TGTSCRECEIVETIME

<dd></dd>

### -field RIL_PARAM_M_TGTDISCHARGETIME

<dd></dd>

### -field RIL_PARAM_M_PROTOCOLID

<dd></dd>

### -field RIL_PARAM_M_DATACODING

<dd></dd>

### -field RIL_PARAM_M_TGTDLVSTATUS

<dd></dd>

### -field RIL_PARAM_M_VPFORMAT

<dd></dd>

### -field RIL_PARAM_M_VP

<dd></dd>

### -field RIL_PARAM_M_GEOSCOPE

<dd></dd>

### -field RIL_PARAM_M_MSGCODE

<dd></dd>

### -field RIL_PARAM_M_UPDATENUMBER

<dd></dd>

### -field RIL_PARAM_M_ID

<dd></dd>

### -field RIL_PARAM_M_TOTALPAGES

<dd></dd>

### -field RIL_PARAM_M_PAGENUMBER

<dd></dd>

### -field RIL_PARAM_M_HDRLENGTH

<dd></dd>

### -field RIL_PARAM_M_SERIALNUMBER

<dd></dd>

### -field RIL_PARAM_M_MSGLENGTH

<dd></dd>

### -field RIL_PARAM_M_HDR

<dd></dd>

### -field RIL_PARAM_M_MSG

<dd></dd>

### -field RIL_PARAM_M_WARNINGTYPE

<dd></dd>

### -field RIL_PARAM_M_EUSERALERT

<dd></dd>

### -field RIL_PARAM_M_POPUP

<dd></dd>

### -field RIL_PARAM_M_MSGID

<dd></dd>

### -field RIL_PARAM_M_ORIGSUBADDRESS

<dd></dd>

### -field RIL_PARAM_M_DESTSUBADDRESS

<dd></dd>

### -field RIL_PARAM_M_DIGIT

<dd></dd>

### -field RIL_PARAM_M_PRIVACY

<dd></dd>

### -field RIL_PARAM_M_PRIORITY

<dd></dd>

### -field RIL_PARAM_M_TELESERVICE

<dd></dd>

### -field RIL_PARAM_M_LANG

<dd></dd>

### -field RIL_PARAM_M_VALIDITYPERIODABS

<dd></dd>

### -field RIL_PARAM_M_VALIDITYPERIODREL

<dd></dd>

### -field RIL_PARAM_M_DEFERREDDELTIMEABS

<dd></dd>

### -field RIL_PARAM_M_DEFERREDDELTIMEREL

<dd></dd>

### -field RIL_PARAM_M_ENCODING

<dd></dd>

### -field RIL_PARAM_M_USERRESPONSECODE

<dd></dd>

### -field RIL_PARAM_M_DISPLAYMODE

<dd></dd>

### -field RIL_PARAM_M_CALLBACKNUM

<dd></dd>

### -field RIL_PARAM_M_NUMMSGS

<dd></dd>

### -field RIL_PARAM_M_CAUSECODE

<dd></dd>

### -field RIL_PARAM_M_REPLYSEQNUMBER

<dd></dd>

### -field RIL_PARAM_M_SERVICEID

<dd></dd>

### -field RIL_PARAM_M_USERACK

<dd></dd>

### -field RIL_PARAM_M_DELIVERYACK

<dd></dd>

### -field RIL_PARAM_M_ALERTONMSGDELIVERY

<dd></dd>

### -field RIL_PARAM_M_HDRLENGTHCDMA

<dd></dd>

### -field RIL_PARAM_M_MSGSTATUSTYPE

<dd></dd>

### -field RIL_PARAM_M_BEARERREPLYACK

<dd></dd>

### -field RIL_PARAM_M_ALL_IN_DELIVER

<dd></dd>

### -field RIL_PARAM_M_ALL_IN_STATUS

<dd></dd>

### -field RIL_PARAM_M_ALL_OUT_SUBMIT

<dd></dd>

### -field RIL_PARAM_M_ALL_BC_GENERAL

<dd></dd>

### -field RIL_PARAM_M_ALL_IN_IS637DELIVER

<dd></dd>

### -field RIL_PARAM_M_ALL_OUT_IS637SUBMIT

<dd></dd>

### -field RIL_PARAM_M_ALL_IN_IS637STATUS

<dd></dd>

### -field RIL_PARAM_M_ALL_OUT_IS637STATUS

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