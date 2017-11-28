---
UID: NE.rilapitypes.RILRILREGSTATUSINFOREJECTREASON
title: RILRILREGSTATUSINFOREJECTREASON
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilrilregstatusinforejectreason_2.htm
old-project: netvista
ms.assetid: 5cc78c46-f426-470c-8f08-bbcf5e8fa1b8
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILRILREGSTATUSINFOREJECTREASON
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
req.iface: 
req.product: Windows 10 or later.
---

# RILRILREGSTATUSINFOREJECTREASON enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILRILREGSTATUSINFOREJECTREASON { 
  RIL_REGREJECTREASON_IMSIUNK_HLR,
  RIL_REGREJECTREASON_ILLEGAL_MS,
  RIL_REGREJECTREASON_IMSIUNK_VLR,
  RIL_REGREJECTREASON_IMSI_NOTACCEPTED,
  RIL_REGREJECTREASON_ILLEGAL_ME,
  RIL_REGREJECTREASON_PLMN_NOTALLOWED,
  RIL_REGREJECTREASON_LOCAREA_NOTALLOWED,
  RIL_REGREJECTREASON_ROAMING_NOTALLOWED,
  RIL_REGREJECTREASON_NOSUITABLECELL,
  RIL_REGREJECTREASON_NETWORKFAILURE,
  RIL_REGREJECTREASON_MACFAILURE,
  RIL_REGREJECTREASON_SYNCHFAILURE,
  RIL_REGREJECTREASON_CONGESTION,
  RIL_REGREJECTREASON_GSMAUTH_NOTACCEPTED,
  RIL_REGREJECTREASON_CSG_NOTAUTHORIZED,
  RIL_REGREJECTREASON_SVCOPT_NOTSUPPORTED,
  RIL_REGREJECTREASON_REQSVCOPT_NOTSUBSCRIBED,
  RIL_REGREJECTREASON_SVCOPT_OUTOFORDER
} RILRILREGSTATUSINFOREJECTREASON;
````


## -enum-fields
<dl>

### -field <a id="RIL_REGREJECTREASON_IMSIUNK_HLR"></a><a id="ril_regrejectreason_imsiunk_hlr"></a><b>RIL_REGREJECTREASON_IMSIUNK_HLR</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_ILLEGAL_MS"></a><a id="ril_regrejectreason_illegal_ms"></a><b>RIL_REGREJECTREASON_ILLEGAL_MS</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_IMSIUNK_VLR"></a><a id="ril_regrejectreason_imsiunk_vlr"></a><b>RIL_REGREJECTREASON_IMSIUNK_VLR</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_IMSI_NOTACCEPTED"></a><a id="ril_regrejectreason_imsi_notaccepted"></a><b>RIL_REGREJECTREASON_IMSI_NOTACCEPTED</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_ILLEGAL_ME"></a><a id="ril_regrejectreason_illegal_me"></a><b>RIL_REGREJECTREASON_ILLEGAL_ME</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_PLMN_NOTALLOWED"></a><a id="ril_regrejectreason_plmn_notallowed"></a><b>RIL_REGREJECTREASON_PLMN_NOTALLOWED</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_LOCAREA_NOTALLOWED"></a><a id="ril_regrejectreason_locarea_notallowed"></a><b>RIL_REGREJECTREASON_LOCAREA_NOTALLOWED</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_ROAMING_NOTALLOWED"></a><a id="ril_regrejectreason_roaming_notallowed"></a><b>RIL_REGREJECTREASON_ROAMING_NOTALLOWED</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_NOSUITABLECELL"></a><a id="ril_regrejectreason_nosuitablecell"></a><b>RIL_REGREJECTREASON_NOSUITABLECELL</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_NETWORKFAILURE"></a><a id="ril_regrejectreason_networkfailure"></a><b>RIL_REGREJECTREASON_NETWORKFAILURE</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_MACFAILURE"></a><a id="ril_regrejectreason_macfailure"></a><b>RIL_REGREJECTREASON_MACFAILURE</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_SYNCHFAILURE"></a><a id="ril_regrejectreason_synchfailure"></a><b>RIL_REGREJECTREASON_SYNCHFAILURE</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_CONGESTION"></a><a id="ril_regrejectreason_congestion"></a><b>RIL_REGREJECTREASON_CONGESTION</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_GSMAUTH_NOTACCEPTED"></a><a id="ril_regrejectreason_gsmauth_notaccepted"></a><b>RIL_REGREJECTREASON_GSMAUTH_NOTACCEPTED</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_CSG_NOTAUTHORIZED"></a><a id="ril_regrejectreason_csg_notauthorized"></a><b>RIL_REGREJECTREASON_CSG_NOTAUTHORIZED</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_SVCOPT_NOTSUPPORTED"></a><a id="ril_regrejectreason_svcopt_notsupported"></a><b>RIL_REGREJECTREASON_SVCOPT_NOTSUPPORTED</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_REQSVCOPT_NOTSUBSCRIBED"></a><a id="ril_regrejectreason_reqsvcopt_notsubscribed"></a><b>RIL_REGREJECTREASON_REQSVCOPT_NOTSUBSCRIBED</b>

<dd></dd>

### -field <a id="RIL_REGREJECTREASON_SVCOPT_OUTOFORDER"></a><a id="ril_regrejectreason_svcopt_outoforder"></a><b>RIL_REGREJECTREASON_SVCOPT_OUTOFORDER</b>

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