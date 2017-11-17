---
UID: NE.rilapitypes.RILMSGPROTOCOLID
title: RILMSGPROTOCOLID
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgprotocolid_2.htm
ms.assetid: a4dc4bc4-f636-46be-b99c-12d2bf4a577f
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
req.alt-api: RILMSGPROTOCOLID
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

# RILMSGPROTOCOLID enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILMSGPROTOCOLID { 
  RIL_MSGPROTOCOL_SMETOSME,
  RIL_MSGPROTOCOL_IMPLICIT,
  RIL_MSGPROTOCOL_TELEX,
  RIL_MSGPROTOCOL_TELEFAX_GROUP3,
  RIL_MSGPROTOCOL_TELEFAX_GROUP4,
  RIL_MSGPROTOCOL_VOICEPHONE,
  RIL_MSGPROTOCOL_ERMES,
  RIL_MSGPROTOCOL_PAGING,
  RIL_MSGPROTOCOL_VIDEOTEX,
  RIL_MSGPROTOCOL_TELETEX,
  RIL_MSGPROTOCOL_TELETEX_PSPDN,
  RIL_MSGPROTOCOL_TELETEX_CSPDN,
  RIL_MSGPROTOCOL_TELETEX_PSTN,
  RIL_MSGPROTOCOL_TELETEX_ISDN,
  RIL_MSGPROTOCOL_UCI,
  RIL_MSGPROTOCOL_MSGHANDLING,
  RIL_MSGPROTOCOL_X400,
  RIL_MSGPROTOCOL_EMAIL,
  RIL_MSGPROTOCOL_SCSPECIFIC1,
  RIL_MSGPROTOCOL_SCSPECIFIC2,
  RIL_MSGPROTOCOL_SCSPECIFIC3,
  RIL_MSGPROTOCOL_SCSPECIFIC4,
  RIL_MSGPROTOCOL_SCSPECIFIC5,
  RIL_MSGPROTOCOL_SCSPECIFIC6,
  RIL_MSGPROTOCOL_SCSPECIFIC7,
  RIL_MSGPROTOCOL_GSMSTATION,
  RIL_MSGPROTOCOL_SM_TYPE0,
  RIL_MSGPROTOCOL_RSM_TYPE1,
  RIL_MSGPROTOCOL_RSM_TYPE2,
  RIL_MSGPROTOCOL_RSM_TYPE3,
  RIL_MSGPROTOCOL_RSM_TYPE4,
  RIL_MSGPROTOCOL_RSM_TYPE5,
  RIL_MSGPROTOCOL_RSM_TYPE6,
  RIL_MSGPROTOCOL_RSM_TYPE7,
  RIL_MSGPROTOCOL_RETURNCALL,
  RIL_MSGPROTOCOL_ME_DOWNLOAD,
  RIL_MSGPROTOCOL_DEPERSONALIZATION,
  RIL_MSGPROTOCOL_UICC_DOWNLOAD,
  RIL_MSGPROTOCOL_MAX
} RILMSGPROTOCOLID;
````


## -enum-fields
<dl>

### -field <a id="RIL_MSGPROTOCOL_SMETOSME"></a><a id="ril_msgprotocol_smetosme"></a><b>RIL_MSGPROTOCOL_SMETOSME</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_IMPLICIT"></a><a id="ril_msgprotocol_implicit"></a><b>RIL_MSGPROTOCOL_IMPLICIT</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_TELEX"></a><a id="ril_msgprotocol_telex"></a><b>RIL_MSGPROTOCOL_TELEX</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_TELEFAX_GROUP3"></a><a id="ril_msgprotocol_telefax_group3"></a><b>RIL_MSGPROTOCOL_TELEFAX_GROUP3</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_TELEFAX_GROUP4"></a><a id="ril_msgprotocol_telefax_group4"></a><b>RIL_MSGPROTOCOL_TELEFAX_GROUP4</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_VOICEPHONE"></a><a id="ril_msgprotocol_voicephone"></a><b>RIL_MSGPROTOCOL_VOICEPHONE</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_ERMES"></a><a id="ril_msgprotocol_ermes"></a><b>RIL_MSGPROTOCOL_ERMES</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_PAGING"></a><a id="ril_msgprotocol_paging"></a><b>RIL_MSGPROTOCOL_PAGING</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_VIDEOTEX"></a><a id="ril_msgprotocol_videotex"></a><b>RIL_MSGPROTOCOL_VIDEOTEX</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_TELETEX"></a><a id="ril_msgprotocol_teletex"></a><b>RIL_MSGPROTOCOL_TELETEX</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_TELETEX_PSPDN"></a><a id="ril_msgprotocol_teletex_pspdn"></a><b>RIL_MSGPROTOCOL_TELETEX_PSPDN</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_TELETEX_CSPDN"></a><a id="ril_msgprotocol_teletex_cspdn"></a><b>RIL_MSGPROTOCOL_TELETEX_CSPDN</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_TELETEX_PSTN"></a><a id="ril_msgprotocol_teletex_pstn"></a><b>RIL_MSGPROTOCOL_TELETEX_PSTN</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_TELETEX_ISDN"></a><a id="ril_msgprotocol_teletex_isdn"></a><b>RIL_MSGPROTOCOL_TELETEX_ISDN</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_UCI"></a><a id="ril_msgprotocol_uci"></a><b>RIL_MSGPROTOCOL_UCI</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_MSGHANDLING"></a><a id="ril_msgprotocol_msghandling"></a><b>RIL_MSGPROTOCOL_MSGHANDLING</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_X400"></a><a id="ril_msgprotocol_x400"></a><b>RIL_MSGPROTOCOL_X400</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_EMAIL"></a><a id="ril_msgprotocol_email"></a><b>RIL_MSGPROTOCOL_EMAIL</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_SCSPECIFIC1"></a><a id="ril_msgprotocol_scspecific1"></a><b>RIL_MSGPROTOCOL_SCSPECIFIC1</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_SCSPECIFIC2"></a><a id="ril_msgprotocol_scspecific2"></a><b>RIL_MSGPROTOCOL_SCSPECIFIC2</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_SCSPECIFIC3"></a><a id="ril_msgprotocol_scspecific3"></a><b>RIL_MSGPROTOCOL_SCSPECIFIC3</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_SCSPECIFIC4"></a><a id="ril_msgprotocol_scspecific4"></a><b>RIL_MSGPROTOCOL_SCSPECIFIC4</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_SCSPECIFIC5"></a><a id="ril_msgprotocol_scspecific5"></a><b>RIL_MSGPROTOCOL_SCSPECIFIC5</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_SCSPECIFIC6"></a><a id="ril_msgprotocol_scspecific6"></a><b>RIL_MSGPROTOCOL_SCSPECIFIC6</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_SCSPECIFIC7"></a><a id="ril_msgprotocol_scspecific7"></a><b>RIL_MSGPROTOCOL_SCSPECIFIC7</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_GSMSTATION"></a><a id="ril_msgprotocol_gsmstation"></a><b>RIL_MSGPROTOCOL_GSMSTATION</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_SM_TYPE0"></a><a id="ril_msgprotocol_sm_type0"></a><b>RIL_MSGPROTOCOL_SM_TYPE0</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_RSM_TYPE1"></a><a id="ril_msgprotocol_rsm_type1"></a><b>RIL_MSGPROTOCOL_RSM_TYPE1</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_RSM_TYPE2"></a><a id="ril_msgprotocol_rsm_type2"></a><b>RIL_MSGPROTOCOL_RSM_TYPE2</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_RSM_TYPE3"></a><a id="ril_msgprotocol_rsm_type3"></a><b>RIL_MSGPROTOCOL_RSM_TYPE3</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_RSM_TYPE4"></a><a id="ril_msgprotocol_rsm_type4"></a><b>RIL_MSGPROTOCOL_RSM_TYPE4</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_RSM_TYPE5"></a><a id="ril_msgprotocol_rsm_type5"></a><b>RIL_MSGPROTOCOL_RSM_TYPE5</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_RSM_TYPE6"></a><a id="ril_msgprotocol_rsm_type6"></a><b>RIL_MSGPROTOCOL_RSM_TYPE6</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_RSM_TYPE7"></a><a id="ril_msgprotocol_rsm_type7"></a><b>RIL_MSGPROTOCOL_RSM_TYPE7</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_RETURNCALL"></a><a id="ril_msgprotocol_returncall"></a><b>RIL_MSGPROTOCOL_RETURNCALL</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_ME_DOWNLOAD"></a><a id="ril_msgprotocol_me_download"></a><b>RIL_MSGPROTOCOL_ME_DOWNLOAD</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_DEPERSONALIZATION"></a><a id="ril_msgprotocol_depersonalization"></a><b>RIL_MSGPROTOCOL_DEPERSONALIZATION</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_UICC_DOWNLOAD"></a><a id="ril_msgprotocol_uicc_download"></a><b>RIL_MSGPROTOCOL_UICC_DOWNLOAD</b>

<dd></dd>

### -field <a id="RIL_MSGPROTOCOL_MAX"></a><a id="ril_msgprotocol_max"></a><b>RIL_MSGPROTOCOL_MAX</b>

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