---
UID: NE.ntddrilapitypes.RILCALLTYPE
title: RILCALLTYPE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcalltype.htm
old-project: netvista
ms.assetid: bd6b9e57-f50b-4743-9c51-066940aad200
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
req.alt-api: RILCALLTYPE
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

# RILCALLTYPE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILCALLTYPE { 
  RIL_CALLTYPE_VOICE,
  RIL_CALLTYPE_DATA,
  RIL_CALLTYPE_FAX,
  RIL_CALLTYPE_PTT,
  RIL_CALLTYPE_VT,
  RIL_CALLTYPE_USSD,
  RIL_CALLTYPE_SUPSVC,
  RIL_CALLTYPE_IMS,
  RIL_CALLTYPE_MAX
} RILCALLTYPE;
````


## -enum-fields
<dl>

### -field <a id="RIL_CALLTYPE_VOICE"></a><a id="ril_calltype_voice"></a><b>RIL_CALLTYPE_VOICE</b>

<dd></dd>

### -field <a id="RIL_CALLTYPE_DATA"></a><a id="ril_calltype_data"></a><b>RIL_CALLTYPE_DATA</b>

<dd></dd>

### -field <a id="RIL_CALLTYPE_FAX"></a><a id="ril_calltype_fax"></a><b>RIL_CALLTYPE_FAX</b>

<dd></dd>

### -field <a id="RIL_CALLTYPE_PTT"></a><a id="ril_calltype_ptt"></a><b>RIL_CALLTYPE_PTT</b>

<dd></dd>

### -field <a id="RIL_CALLTYPE_VT"></a><a id="ril_calltype_vt"></a><b>RIL_CALLTYPE_VT</b>

<dd></dd>

### -field <a id="RIL_CALLTYPE_USSD"></a><a id="ril_calltype_ussd"></a><b>RIL_CALLTYPE_USSD</b>

<dd></dd>

### -field <a id="RIL_CALLTYPE_SUPSVC"></a><a id="ril_calltype_supsvc"></a><b>RIL_CALLTYPE_SUPSVC</b>

<dd></dd>

### -field <a id="RIL_CALLTYPE_IMS"></a><a id="ril_calltype_ims"></a><b>RIL_CALLTYPE_IMS</b>

<dd></dd>

### -field <a id="RIL_CALLTYPE_MAX"></a><a id="ril_calltype_max"></a><b>RIL_CALLTYPE_MAX</b>

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