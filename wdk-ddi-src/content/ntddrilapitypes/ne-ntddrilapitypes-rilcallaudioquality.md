---
UID: NE.ntddrilapitypes.RILCALLAUDIOQUALITY
title: RILCALLAUDIOQUALITY
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallaudioquality.htm
old-project: netvista
ms.assetid: bdd9879a-ec9b-431a-be95-4a1844e6238f
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: RILCALLAUDIOQUALITY
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

# RILCALLAUDIOQUALITY enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCALLAUDIOQUALITY { 
  RIL_CALLAUDIOQUALITY_STANDARD,
  RIL_CALLAUDIOQUALITY_HIGH,
  RIL_CALLAUDIOQUALITY_AMR_NB,
  RIL_CALLAUDIOQUALITY_AMR_WB,
  RIL_CALLAUDIOQUALITY_EVRC,
  RIL_CALLAUDIOQUALITY_EVRC_B,
  RIL_CALLAUDIOQUALITY_EVRC_NW,
  RIL_CALLAUDIOQUALITY_EVRC_WB,
  RIL_CALLAUDIOQUALITY_EVS_FB,
  RIL_CALLAUDIOQUALITY_EVS_NB,
  RIL_CALLAUDIOQUALITY_EVS_SWB,
  RIL_CALLAUDIOQUALITY_EVS_WB,
  RIL_CALLAUDIOQUALITY_GSM_EFR,
  RIL_CALLAUDIOQUALITY_GSM_FR,
  RIL_CALLAUDIOQUALITY_GSM_HR,
  RIL_CALLAUDIOQUALITY_QCELP13K,
  RIL_CALLAUDIOQUALITY_G711U,
  RIL_CALLAUDIOQUALITY_G711A,
  RIL_CALLAUDIOQUALITY_G722,
  RIL_CALLAUDIOQUALITY_G723,
  RIL_CALLAUDIOQUALITY_G729,
  RIL_CALLAUDIOQUALITY_MAX
} RILCALLAUDIOQUALITY;
````


## -enum-fields
<dl>

### -field <a id="RIL_CALLAUDIOQUALITY_STANDARD"></a><a id="ril_callaudioquality_standard"></a><b>RIL_CALLAUDIOQUALITY_STANDARD</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_HIGH"></a><a id="ril_callaudioquality_high"></a><b>RIL_CALLAUDIOQUALITY_HIGH</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_AMR_NB"></a><a id="ril_callaudioquality_amr_nb"></a><b>RIL_CALLAUDIOQUALITY_AMR_NB</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_AMR_WB"></a><a id="ril_callaudioquality_amr_wb"></a><b>RIL_CALLAUDIOQUALITY_AMR_WB</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_EVRC"></a><a id="ril_callaudioquality_evrc"></a><b>RIL_CALLAUDIOQUALITY_EVRC</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_EVRC_B"></a><a id="ril_callaudioquality_evrc_b"></a><b>RIL_CALLAUDIOQUALITY_EVRC_B</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_EVRC_NW"></a><a id="ril_callaudioquality_evrc_nw"></a><b>RIL_CALLAUDIOQUALITY_EVRC_NW</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_EVRC_WB"></a><a id="ril_callaudioquality_evrc_wb"></a><b>RIL_CALLAUDIOQUALITY_EVRC_WB</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_EVS_FB"></a><a id="ril_callaudioquality_evs_fb"></a><b>RIL_CALLAUDIOQUALITY_EVS_FB</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_EVS_NB"></a><a id="ril_callaudioquality_evs_nb"></a><b>RIL_CALLAUDIOQUALITY_EVS_NB</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_EVS_SWB"></a><a id="ril_callaudioquality_evs_swb"></a><b>RIL_CALLAUDIOQUALITY_EVS_SWB</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_EVS_WB"></a><a id="ril_callaudioquality_evs_wb"></a><b>RIL_CALLAUDIOQUALITY_EVS_WB</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_GSM_EFR"></a><a id="ril_callaudioquality_gsm_efr"></a><b>RIL_CALLAUDIOQUALITY_GSM_EFR</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_GSM_FR"></a><a id="ril_callaudioquality_gsm_fr"></a><b>RIL_CALLAUDIOQUALITY_GSM_FR</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_GSM_HR"></a><a id="ril_callaudioquality_gsm_hr"></a><b>RIL_CALLAUDIOQUALITY_GSM_HR</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_QCELP13K"></a><a id="ril_callaudioquality_qcelp13k"></a><b>RIL_CALLAUDIOQUALITY_QCELP13K</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_G711U"></a><a id="ril_callaudioquality_g711u"></a><b>RIL_CALLAUDIOQUALITY_G711U</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_G711A"></a><a id="ril_callaudioquality_g711a"></a><b>RIL_CALLAUDIOQUALITY_G711A</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_G722"></a><a id="ril_callaudioquality_g722"></a><b>RIL_CALLAUDIOQUALITY_G722</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_G723"></a><a id="ril_callaudioquality_g723"></a><b>RIL_CALLAUDIOQUALITY_G723</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_G729"></a><a id="ril_callaudioquality_g729"></a><b>RIL_CALLAUDIOQUALITY_G729</b>

<dd></dd>

### -field <a id="RIL_CALLAUDIOQUALITY_MAX"></a><a id="ril_callaudioquality_max"></a><b>RIL_CALLAUDIOQUALITY_MAX</b>

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