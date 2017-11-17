---
UID: NE.rilapitypes.RILMSGINSTATUSTGTDLVSTATUS
title: RILMSGINSTATUSTGTDLVSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsginstatustgtdlvstatus_2.htm
ms.assetid: 7a370d9c-93c6-4c73-b41e-97b0114690b4
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
req.alt-api: RILMSGINSTATUSTGTDLVSTATUS
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

# RILMSGINSTATUSTGTDLVSTATUS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILMSGINSTATUSTGTDLVSTATUS { 
  RIL_MSGDLVSTATUS_FORWARDEDTOSME,
  RIL_MSGDLVSTATUS_REPLACEDBYSC,
  RIL_MSGDLVSTATUS_CONGESTION_TRYING,
  RIL_MSGDLVSTATUS_SMEBUSY_TRYING,
  RIL_MSGDLVSTATUS_SMENOTRESPONDING_TRYING,
  RIL_MSGDLVSTATUS_SVCREJECTED_TRYING,
  RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TRYING,
  RIL_MSGDLVSTATUS_SMEERROR_TRYING,
  RIL_MSGDLVSTATUS_CONGESTION,
  RIL_MSGDLVSTATUS_SMEBUSY,
  RIL_MSGDLVSTATUS_SMENOTRESPONDING,
  RIL_MSGDLVSTATUS_SVCREJECTED,
  RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TEMP,
  RIL_MSGDLVSTATUS_SMEERROR,
  RIL_MSGDLVSTATUS_REMOTEPROCERROR,
  RIL_MSGDLVSTATUS_INCOMPATIBLEDEST,
  RIL_MSGDLVSTATUS_CONNECTIONREJECTED,
  RIL_MSGDLVSTATUS_NOTOBTAINABLE,
  RIL_MSGDLVSTATUS_NOINTERNETWORKING,
  RIL_MSGDLVSTATUS_VPEXPIRED,
  RIL_MSGDLVSTATUS_DELETEDBYORIGSME,
  RIL_MSGDLVSTATUS_DELETEDBYSC,
  RIL_MSGDLVSTATUS_NOLONGEREXISTS,
  RIL_MSGDLVSTATUS_QUALITYUNAVAIL,
  RIL_MSGDLVSTATUS_RESERVED_COMPLETED,
  RIL_MSGDLVSTATUS_RESERVED_TRYING,
  RIL_MSGDLVSTATUS_RESERVED_ERROR,
  RIL_MSGDLVSTATUS_RESERVED_TMPERROR,
  RIL_MSGDLVSTATUS_SCSPECIFIC_COMPLETED,
  RIL_MSGDLVSTATUS_SCSPECIFIC_TRYING,
  RIL_MSGDLVSTATUS_SCSPECIFIC_ERROR,
  RIL_MSGDLVSTATUS_SCSPECIFIC_TMPERROR,
  RIL_MSGDLVSTATUS_MAX
} RILMSGINSTATUSTGTDLVSTATUS;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGDLVSTATUS_FORWARDEDTOSME"></a><a id="ril_msgdlvstatus_forwardedtosme"></a><b>RIL_MSGDLVSTATUS_FORWARDEDTOSME</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_REPLACEDBYSC"></a><a id="ril_msgdlvstatus_replacedbysc"></a><b>RIL_MSGDLVSTATUS_REPLACEDBYSC</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_CONGESTION_TRYING"></a><a id="ril_msgdlvstatus_congestion_trying"></a><b>RIL_MSGDLVSTATUS_CONGESTION_TRYING</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_SMEBUSY_TRYING"></a><a id="ril_msgdlvstatus_smebusy_trying"></a><b>RIL_MSGDLVSTATUS_SMEBUSY_TRYING</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_SMENOTRESPONDING_TRYING"></a><a id="ril_msgdlvstatus_smenotresponding_trying"></a><b>RIL_MSGDLVSTATUS_SMENOTRESPONDING_TRYING</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_SVCREJECTED_TRYING"></a><a id="ril_msgdlvstatus_svcrejected_trying"></a><b>RIL_MSGDLVSTATUS_SVCREJECTED_TRYING</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TRYING"></a><a id="ril_msgdlvstatus_qualityunavail_trying"></a><b>RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TRYING</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_SMEERROR_TRYING"></a><a id="ril_msgdlvstatus_smeerror_trying"></a><b>RIL_MSGDLVSTATUS_SMEERROR_TRYING</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_CONGESTION"></a><a id="ril_msgdlvstatus_congestion"></a><b>RIL_MSGDLVSTATUS_CONGESTION</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_SMEBUSY"></a><a id="ril_msgdlvstatus_smebusy"></a><b>RIL_MSGDLVSTATUS_SMEBUSY</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_SMENOTRESPONDING"></a><a id="ril_msgdlvstatus_smenotresponding"></a><b>RIL_MSGDLVSTATUS_SMENOTRESPONDING</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_SVCREJECTED"></a><a id="ril_msgdlvstatus_svcrejected"></a><b>RIL_MSGDLVSTATUS_SVCREJECTED</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TEMP"></a><a id="ril_msgdlvstatus_qualityunavail_temp"></a><b>RIL_MSGDLVSTATUS_QUALITYUNAVAIL_TEMP</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_SMEERROR"></a><a id="ril_msgdlvstatus_smeerror"></a><b>RIL_MSGDLVSTATUS_SMEERROR</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_REMOTEPROCERROR"></a><a id="ril_msgdlvstatus_remoteprocerror"></a><b>RIL_MSGDLVSTATUS_REMOTEPROCERROR</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_INCOMPATIBLEDEST"></a><a id="ril_msgdlvstatus_incompatibledest"></a><b>RIL_MSGDLVSTATUS_INCOMPATIBLEDEST</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_CONNECTIONREJECTED"></a><a id="ril_msgdlvstatus_connectionrejected"></a><b>RIL_MSGDLVSTATUS_CONNECTIONREJECTED</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_NOTOBTAINABLE"></a><a id="ril_msgdlvstatus_notobtainable"></a><b>RIL_MSGDLVSTATUS_NOTOBTAINABLE</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_NOINTERNETWORKING"></a><a id="ril_msgdlvstatus_nointernetworking"></a><b>RIL_MSGDLVSTATUS_NOINTERNETWORKING</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_VPEXPIRED"></a><a id="ril_msgdlvstatus_vpexpired"></a><b>RIL_MSGDLVSTATUS_VPEXPIRED</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_DELETEDBYORIGSME"></a><a id="ril_msgdlvstatus_deletedbyorigsme"></a><b>RIL_MSGDLVSTATUS_DELETEDBYORIGSME</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_DELETEDBYSC"></a><a id="ril_msgdlvstatus_deletedbysc"></a><b>RIL_MSGDLVSTATUS_DELETEDBYSC</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_NOLONGEREXISTS"></a><a id="ril_msgdlvstatus_nolongerexists"></a><b>RIL_MSGDLVSTATUS_NOLONGEREXISTS</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_QUALITYUNAVAIL"></a><a id="ril_msgdlvstatus_qualityunavail"></a><b>RIL_MSGDLVSTATUS_QUALITYUNAVAIL</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_RESERVED_COMPLETED"></a><a id="ril_msgdlvstatus_reserved_completed"></a><b>RIL_MSGDLVSTATUS_RESERVED_COMPLETED</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_RESERVED_TRYING"></a><a id="ril_msgdlvstatus_reserved_trying"></a><b>RIL_MSGDLVSTATUS_RESERVED_TRYING</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_RESERVED_ERROR"></a><a id="ril_msgdlvstatus_reserved_error"></a><b>RIL_MSGDLVSTATUS_RESERVED_ERROR</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_RESERVED_TMPERROR"></a><a id="ril_msgdlvstatus_reserved_tmperror"></a><b>RIL_MSGDLVSTATUS_RESERVED_TMPERROR</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_SCSPECIFIC_COMPLETED"></a><a id="ril_msgdlvstatus_scspecific_completed"></a><b>RIL_MSGDLVSTATUS_SCSPECIFIC_COMPLETED</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_SCSPECIFIC_TRYING"></a><a id="ril_msgdlvstatus_scspecific_trying"></a><b>RIL_MSGDLVSTATUS_SCSPECIFIC_TRYING</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_SCSPECIFIC_ERROR"></a><a id="ril_msgdlvstatus_scspecific_error"></a><b>RIL_MSGDLVSTATUS_SCSPECIFIC_ERROR</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_SCSPECIFIC_TMPERROR"></a><a id="ril_msgdlvstatus_scspecific_tmperror"></a><b>RIL_MSGDLVSTATUS_SCSPECIFIC_TMPERROR</b>

<dd></dd>

### -field <a id="RIL_MSGDLVSTATUS_MAX"></a><a id="ril_msgdlvstatus_max"></a><b>RIL_MSGDLVSTATUS_MAX</b>

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