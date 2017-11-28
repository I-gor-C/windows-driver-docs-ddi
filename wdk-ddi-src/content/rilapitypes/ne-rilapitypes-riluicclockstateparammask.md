---
UID: NE.rilapitypes.RILUICCLOCKSTATEPARAMMASK
title: RILUICCLOCKSTATEPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluicclockstateparammask_2.htm
old-project: netvista
ms.assetid: 88bdeb85-1ce8-43df-8cf1-4563d90a46ad
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
req.alt-api: RILUICCLOCKSTATEPARAMMASK
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

# RILUICCLOCKSTATEPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILUICCLOCKSTATEPARAMMASK { 
  RIL_PARAM_UICCLOCKSTATE_LOCKSTATE,
  RIL_PARAM_UICCLOCKSTATE_VERIFYATTEMPTSLEFT,
  RIL_PARAM_UICCLOCKSTATE_UNBLOCKATTEMPTSLEFT,
  RIL_PARAM_UICCLOCKSTATE_ALL
} RILUICCLOCKSTATEPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_UICCLOCKSTATE_LOCKSTATE"></a><a id="ril_param_uicclockstate_lockstate"></a><b>RIL_PARAM_UICCLOCKSTATE_LOCKSTATE</b>

<dd></dd>

### -field <a id="RIL_PARAM_UICCLOCKSTATE_VERIFYATTEMPTSLEFT"></a><a id="ril_param_uicclockstate_verifyattemptsleft"></a><b>RIL_PARAM_UICCLOCKSTATE_VERIFYATTEMPTSLEFT</b>

<dd></dd>

### -field <a id="RIL_PARAM_UICCLOCKSTATE_UNBLOCKATTEMPTSLEFT"></a><a id="ril_param_uicclockstate_unblockattemptsleft"></a><b>RIL_PARAM_UICCLOCKSTATE_UNBLOCKATTEMPTSLEFT</b>

<dd></dd>

### -field <a id="RIL_PARAM_UICCLOCKSTATE_ALL"></a><a id="ril_param_uicclockstate_all"></a><b>RIL_PARAM_UICCLOCKSTATE_ALL</b>

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