---
UID: NE.rilapitypes.RILREMOTEPARTYINFOVALUEPARAM~r1
title: RILREMOTEPARTYINFOVALUEPARAM
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilremotepartyinfovalueparam_2.htm
old-project: netvista
ms.assetid: eeea39eb-898a-47fe-befe-39c95dd1fc90
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
req.alt-api: RILREMOTEPARTYINFOVALUEPARAM
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

# RILREMOTEPARTYINFOVALUEPARAM enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILREMOTEPARTYINFOVALUEPARAM { 
  RIL_PARAM_RPI_ADDRESS,
  RIL_PARAM_RPI_SUBADDRESS,
  RIL_PARAM_RPI_DESCRIPTION,
  RIL_PARAM_RPI_NUM_PRES_IND,
  RIL_PARAM_RPI_NAME_PRES_IND,
  RIL_PARAM_RPI_ID,
  RIL_PARAM_RPI_ALL
} RILREMOTEPARTYINFOVALUEPARAM;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_RPI_ADDRESS"></a><a id="ril_param_rpi_address"></a><b>RIL_PARAM_RPI_ADDRESS</b>

<dd></dd>

### -field <a id="RIL_PARAM_RPI_SUBADDRESS"></a><a id="ril_param_rpi_subaddress"></a><b>RIL_PARAM_RPI_SUBADDRESS</b>

<dd></dd>

### -field <a id="RIL_PARAM_RPI_DESCRIPTION"></a><a id="ril_param_rpi_description"></a><b>RIL_PARAM_RPI_DESCRIPTION</b>

<dd></dd>

### -field <a id="RIL_PARAM_RPI_NUM_PRES_IND"></a><a id="ril_param_rpi_num_pres_ind"></a><b>RIL_PARAM_RPI_NUM_PRES_IND</b>

<dd></dd>

### -field <a id="RIL_PARAM_RPI_NAME_PRES_IND"></a><a id="ril_param_rpi_name_pres_ind"></a><b>RIL_PARAM_RPI_NAME_PRES_IND</b>

<dd></dd>

### -field <a id="RIL_PARAM_RPI_ID"></a><a id="ril_param_rpi_id"></a><b>RIL_PARAM_RPI_ID</b>

<dd></dd>

### -field <a id="RIL_PARAM_RPI_ALL"></a><a id="ril_param_rpi_all"></a><b>RIL_PARAM_RPI_ALL</b>

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