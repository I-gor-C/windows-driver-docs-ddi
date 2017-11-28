---
UID: NE.ntddrilapitypes.RILSYSTEMSELECTIONPREFSPARAMMASK
title: RILSYSTEMSELECTIONPREFSPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsystemselectionprefsparammask.htm
old-project: netvista
ms.assetid: 69560c05-8a54-4a67-a441-2b3c2ec4c332
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
req.alt-api: RILSYSTEMSELECTIONPREFSPARAMMASK
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

# RILSYSTEMSELECTIONPREFSPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILSYSTEMSELECTIONPREFSPARAMMASK { 
  RIL_PARAM_SSP_SYSTEMTYPES,
  RIL_PARAM_SSP_MODE,
  RIL_PARAM_SSP_PLMNINFO,
  RIL_PARAM_SSP_ROAMINGMODE,
  RIL_PARAM_SSP_ACQUISITIONORDERSIZE,
  RIL_PARAM_SSP_ACQUISITIONORDER,
  RIL_PARAM_SSP_ALL
} RILSYSTEMSELECTIONPREFSPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_SSP_SYSTEMTYPES"></a><a id="ril_param_ssp_systemtypes"></a><b>RIL_PARAM_SSP_SYSTEMTYPES</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSP_MODE"></a><a id="ril_param_ssp_mode"></a><b>RIL_PARAM_SSP_MODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSP_PLMNINFO"></a><a id="ril_param_ssp_plmninfo"></a><b>RIL_PARAM_SSP_PLMNINFO</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSP_ROAMINGMODE"></a><a id="ril_param_ssp_roamingmode"></a><b>RIL_PARAM_SSP_ROAMINGMODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSP_ACQUISITIONORDERSIZE"></a><a id="ril_param_ssp_acquisitionordersize"></a><b>RIL_PARAM_SSP_ACQUISITIONORDERSIZE</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSP_ACQUISITIONORDER"></a><a id="ril_param_ssp_acquisitionorder"></a><b>RIL_PARAM_SSP_ACQUISITIONORDER</b>

<dd></dd>

### -field <a id="RIL_PARAM_SSP_ALL"></a><a id="ril_param_ssp_all"></a><b>RIL_PARAM_SSP_ALL</b>

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