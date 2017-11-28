---
UID: NE.rilapitypes.RILCALLMEDIATYPE
title: RILCALLMEDIATYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallmediatype_2.htm
old-project: netvista
ms.assetid: f4ecaf9a-1d8d-4a56-afa0-b893eb0c4c62
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
req.alt-api: RILCALLMEDIATYPE
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

# RILCALLMEDIATYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILCALLMEDIATYPE { 
  RIL_CALLMEDIATYPE_AUDIO,
  RIL_CALLMEDIATYPE_VIDEO,
  RIL_CALLMEDIATYPE_CUSTOM,
  RIL_CALLMEDIATYPE_MAX
} RILCALLMEDIATYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_CALLMEDIATYPE_AUDIO"></a><a id="ril_callmediatype_audio"></a><b>RIL_CALLMEDIATYPE_AUDIO</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIATYPE_VIDEO"></a><a id="ril_callmediatype_video"></a><b>RIL_CALLMEDIATYPE_VIDEO</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIATYPE_CUSTOM"></a><a id="ril_callmediatype_custom"></a><b>RIL_CALLMEDIATYPE_CUSTOM</b>

<dd></dd>

### -field <a id="RIL_CALLMEDIATYPE_MAX"></a><a id="ril_callmediatype_max"></a><b>RIL_CALLMEDIATYPE_MAX</b>

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