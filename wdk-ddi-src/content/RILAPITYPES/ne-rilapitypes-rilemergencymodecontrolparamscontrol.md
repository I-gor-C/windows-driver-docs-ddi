---
UID: NE.rilapitypes.RILEMERGENCYMODECONTROLPARAMSCONTROL
title: RILEMERGENCYMODECONTROLPARAMSCONTROL
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilemergencymodecontrolparamscontrol_2.htm
ms.assetid: b169e3a3-141b-4bca-9eaa-ce55f7194e4f
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
req.alt-api: RILEMERGENCYMODECONTROLPARAMSCONTROL
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

# RILEMERGENCYMODECONTROLPARAMSCONTROL enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILEMERGENCYMODECONTROLPARAMSCONTROL { 
  RIL_EMC_OTHER_MODEM_IN_EMERGECY_MODE,
  RIL_EMC_ALL_MODEMS_ARE_IN_NORMAL_MODE,
  RIL_EMC_MAX
} RILEMERGENCYMODECONTROLPARAMSCONTROL;
````


## -enum-fields
<dl>

### -field <a id="RIL_EMC_OTHER_MODEM_IN_EMERGECY_MODE"></a><a id="ril_emc_other_modem_in_emergecy_mode"></a><b>RIL_EMC_OTHER_MODEM_IN_EMERGECY_MODE</b>

<dd></dd>

### -field <a id="RIL_EMC_ALL_MODEMS_ARE_IN_NORMAL_MODE"></a><a id="ril_emc_all_modems_are_in_normal_mode"></a><b>RIL_EMC_ALL_MODEMS_ARE_IN_NORMAL_MODE</b>

<dd></dd>

### -field <a id="RIL_EMC_MAX"></a><a id="ril_emc_max"></a><b>RIL_EMC_MAX</b>

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