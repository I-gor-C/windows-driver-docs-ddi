---
UID: NE.rilapitypes.RILCALLMODIFICATIONINFOPARAMMASK
title: RILCALLMODIFICATIONINFOPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmodificationinfoparammask_2.htm
old-project: netvista
ms.assetid: 78726ec3-f777-4165-baec-c2c013e4c86a
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.alt-api: RILCALLMODIFICATIONINFOPARAMMASK
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

# RILCALLMODIFICATIONINFOPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILCALLMODIFICATIONINFOPARAMMASK { 
  RIL_PARAM_CMI_ID,
  RIL_PARAM_CMI_MODIFICATIONTYPE,
  RIL_PARAM_CMI_OLDCALLTYPE,
  RIL_PARAM_CMI_NEWCALLTYPE,
  RIL_PARAM_CMI_ADDRESS,
  RIL_PARAM_CMI_ALPHAIDENTIFIER,
  RIL_PARAM_CMI_ALL
} RILCALLMODIFICATIONINFOPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_CMI_ID"></a><a id="ril_param_cmi_id"></a><b>RIL_PARAM_CMI_ID</b>

<dd></dd>

### -field <a id="RIL_PARAM_CMI_MODIFICATIONTYPE"></a><a id="ril_param_cmi_modificationtype"></a><b>RIL_PARAM_CMI_MODIFICATIONTYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_CMI_OLDCALLTYPE"></a><a id="ril_param_cmi_oldcalltype"></a><b>RIL_PARAM_CMI_OLDCALLTYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_CMI_NEWCALLTYPE"></a><a id="ril_param_cmi_newcalltype"></a><b>RIL_PARAM_CMI_NEWCALLTYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_CMI_ADDRESS"></a><a id="ril_param_cmi_address"></a><b>RIL_PARAM_CMI_ADDRESS</b>

<dd></dd>

### -field <a id="RIL_PARAM_CMI_ALPHAIDENTIFIER"></a><a id="ril_param_cmi_alphaidentifier"></a><b>RIL_PARAM_CMI_ALPHAIDENTIFIER</b>

<dd></dd>

### -field <a id="RIL_PARAM_CMI_ALL"></a><a id="ril_param_cmi_all"></a><b>RIL_PARAM_CMI_ALL</b>

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