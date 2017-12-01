---
UID: NE.rilapitypes.RILIMSNWENABLEDFLAGS
title: RILIMSNWENABLEDFLAGS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimsnwenabledflags_2.htm
old-project: netvista
ms.assetid: 3295b0f0-a498-47fb-9744-06ea74626bb5
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
req.alt-api: RILIMSNWENABLEDFLAGS
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

# RILIMSNWENABLEDFLAGS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILIMSNWENABLEDFLAGS { 
  RIL_IMS_NW_ENABLED_FLAG_PROVISION,
  RIL_IMS_NW_ENABLED_FLAG_VOICE,
  RIL_IMS_NW_ENABLED_FLAG_VIDEO,
  RIL_IMS_NW_ENABLED_FLAG_EAB,
  RIL_IMS_NW_ENABLED_FLAG_ALL
} RILIMSNWENABLEDFLAGS;
````


## -enum-fields
<dl>

### -field <a id="RIL_IMS_NW_ENABLED_FLAG_PROVISION"></a><a id="ril_ims_nw_enabled_flag_provision"></a><b>RIL_IMS_NW_ENABLED_FLAG_PROVISION</b>

<dd></dd>

### -field <a id="RIL_IMS_NW_ENABLED_FLAG_VOICE"></a><a id="ril_ims_nw_enabled_flag_voice"></a><b>RIL_IMS_NW_ENABLED_FLAG_VOICE</b>

<dd></dd>

### -field <a id="RIL_IMS_NW_ENABLED_FLAG_VIDEO"></a><a id="ril_ims_nw_enabled_flag_video"></a><b>RIL_IMS_NW_ENABLED_FLAG_VIDEO</b>

<dd></dd>

### -field <a id="RIL_IMS_NW_ENABLED_FLAG_EAB"></a><a id="ril_ims_nw_enabled_flag_eab"></a><b>RIL_IMS_NW_ENABLED_FLAG_EAB</b>

<dd></dd>

### -field <a id="RIL_IMS_NW_ENABLED_FLAG_ALL"></a><a id="ril_ims_nw_enabled_flag_all"></a><b>RIL_IMS_NW_ENABLED_FLAG_ALL</b>

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