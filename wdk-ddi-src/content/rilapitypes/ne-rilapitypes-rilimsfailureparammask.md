---
UID: NE.rilapitypes.RILIMSFAILUREPARAMMASK
title: RILIMSFAILUREPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilimsfailureparammask_2.htm
old-project: netvista
ms.assetid: 07d651cd-b890-49cf-a543-2fc2fbf52412
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
req.alt-api: RILIMSFAILUREPARAMMASK
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

# RILIMSFAILUREPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILIMSFAILUREPARAMMASK { 
  RIL_PARAM_IMSFAILURE_MESSAGETYPE,
  RIL_PARAM_IMSFAILURE_MESSAGESUBTYPE,
  RIL_PARAM_IMSFAILURE_ERRORCODE,
  RIL_PARAM_IMSFAILURE_ERRORSTRING,
  RIL_PARAM_IMSFAILURE_ALL
} RILIMSFAILUREPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_IMSFAILURE_MESSAGETYPE"></a><a id="ril_param_imsfailure_messagetype"></a><b>RIL_PARAM_IMSFAILURE_MESSAGETYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_IMSFAILURE_MESSAGESUBTYPE"></a><a id="ril_param_imsfailure_messagesubtype"></a><b>RIL_PARAM_IMSFAILURE_MESSAGESUBTYPE</b>

<dd></dd>

### -field <a id="RIL_PARAM_IMSFAILURE_ERRORCODE"></a><a id="ril_param_imsfailure_errorcode"></a><b>RIL_PARAM_IMSFAILURE_ERRORCODE</b>

<dd></dd>

### -field <a id="RIL_PARAM_IMSFAILURE_ERRORSTRING"></a><a id="ril_param_imsfailure_errorstring"></a><b>RIL_PARAM_IMSFAILURE_ERRORSTRING</b>

<dd></dd>

### -field <a id="RIL_PARAM_IMSFAILURE_ALL"></a><a id="ril_param_imsfailure_all"></a><b>RIL_PARAM_IMSFAILURE_ALL</b>

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