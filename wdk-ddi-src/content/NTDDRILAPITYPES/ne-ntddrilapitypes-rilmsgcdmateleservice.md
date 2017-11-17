---
UID: NE.ntddrilapitypes.RILMSGCDMATELESERVICE
title: RILMSGCDMATELESERVICE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmateleservice.htm
ms.assetid: 01c45c31-2cae-4f9f-a3dc-4a164a3df670
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
req.alt-api: RILMSGCDMATELESERVICE
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

# RILMSGCDMATELESERVICE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMSGCDMATELESERVICE { 
  RIL_MSGTELESERVICE_MESSAGING_OLD,
  RIL_MSGTELESERVICE_VOICEMAIL_OLD,
  RIL_MSGTELESERVICE_WAP_OLD,
  RIL_MSGTELESERVICE_BROADCAST_OLD,
  RIL_MSGTELESERVICE_SELFREG_OLD,
  RIL_MSGTELESERVICE_PAGING,
  RIL_MSGTELESERVICE_MESSAGING,
  RIL_MSGTELESERVICE_WEMT,
  RIL_MSGTELESERVICE_VOICEMAIL_VMN_95,
  RIL_MSGTELESERVICE_VOICEMAIL_MWI,
  RIL_MSGTELESERVICE_WAP,
  RIL_MSGTELESERVICE_WAP_CT_MMS,
  RIL_MSGTELESERVICE_WAP_CT_OMA,
  RIL_MSGTELESERVICE_BROADCAST,
  RIL_MSGTELESERVICE_SELFREG
} RILMSGCDMATELESERVICE;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGTELESERVICE_MESSAGING_OLD"></a><a id="ril_msgteleservice_messaging_old"></a><b>RIL_MSGTELESERVICE_MESSAGING_OLD</b>

<dd></dd>

### -field <a id="RIL_MSGTELESERVICE_VOICEMAIL_OLD"></a><a id="ril_msgteleservice_voicemail_old"></a><b>RIL_MSGTELESERVICE_VOICEMAIL_OLD</b>

<dd></dd>

### -field <a id="RIL_MSGTELESERVICE_WAP_OLD"></a><a id="ril_msgteleservice_wap_old"></a><b>RIL_MSGTELESERVICE_WAP_OLD</b>

<dd></dd>

### -field <a id="RIL_MSGTELESERVICE_BROADCAST_OLD"></a><a id="ril_msgteleservice_broadcast_old"></a><b>RIL_MSGTELESERVICE_BROADCAST_OLD</b>

<dd></dd>

### -field <a id="RIL_MSGTELESERVICE_SELFREG_OLD"></a><a id="ril_msgteleservice_selfreg_old"></a><b>RIL_MSGTELESERVICE_SELFREG_OLD</b>

<dd></dd>

### -field <a id="RIL_MSGTELESERVICE_PAGING"></a><a id="ril_msgteleservice_paging"></a><b>RIL_MSGTELESERVICE_PAGING</b>

<dd></dd>

### -field <a id="RIL_MSGTELESERVICE_MESSAGING"></a><a id="ril_msgteleservice_messaging"></a><b>RIL_MSGTELESERVICE_MESSAGING</b>

<dd></dd>

### -field <a id="RIL_MSGTELESERVICE_WEMT"></a><a id="ril_msgteleservice_wemt"></a><b>RIL_MSGTELESERVICE_WEMT</b>

<dd></dd>

### -field <a id="RIL_MSGTELESERVICE_VOICEMAIL_VMN_95"></a><a id="ril_msgteleservice_voicemail_vmn_95"></a><b>RIL_MSGTELESERVICE_VOICEMAIL_VMN_95</b>

<dd></dd>

### -field <a id="RIL_MSGTELESERVICE_VOICEMAIL_MWI"></a><a id="ril_msgteleservice_voicemail_mwi"></a><b>RIL_MSGTELESERVICE_VOICEMAIL_MWI</b>

<dd></dd>

### -field <a id="RIL_MSGTELESERVICE_WAP"></a><a id="ril_msgteleservice_wap"></a><b>RIL_MSGTELESERVICE_WAP</b>

<dd></dd>

### -field <a id="RIL_MSGTELESERVICE_WAP_CT_MMS"></a><a id="ril_msgteleservice_wap_ct_mms"></a><b>RIL_MSGTELESERVICE_WAP_CT_MMS</b>

<dd></dd>

### -field <a id="RIL_MSGTELESERVICE_WAP_CT_OMA"></a><a id="ril_msgteleservice_wap_ct_oma"></a><b>RIL_MSGTELESERVICE_WAP_CT_OMA</b>

<dd></dd>

### -field <a id="RIL_MSGTELESERVICE_BROADCAST"></a><a id="ril_msgteleservice_broadcast"></a><b>RIL_MSGTELESERVICE_BROADCAST</b>

<dd></dd>

### -field <a id="RIL_MSGTELESERVICE_SELFREG"></a><a id="ril_msgteleservice_selfreg"></a><b>RIL_MSGTELESERVICE_SELFREG</b>

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