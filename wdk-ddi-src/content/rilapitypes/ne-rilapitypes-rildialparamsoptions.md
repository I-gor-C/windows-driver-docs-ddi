---
UID: NE.rilapitypes.RILDIALPARAMSOPTIONS
title: RILDIALPARAMSOPTIONS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildialparamsoptions_2.htm
old-project: netvista
ms.assetid: c2635f91-005f-45e7-9d6c-92caca7f4452
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
req.alt-api: RILDIALPARAMSOPTIONS
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

# RILDIALPARAMSOPTIONS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILDIALPARAMSOPTIONS { 
  RIL_DIALOPT_RESTRICTID,
  RIL_DIALOPT_PRESENTID,
  RIL_DIALOPT_ANYEXECUTORFOREMERGENCY,
  RIL_DIALOPT_RTTFULL,
  RIL_DIALOPT_ALL
} RILDIALPARAMSOPTIONS;
````


## -enum-fields
<dl>

### -field <a id="RIL_DIALOPT_RESTRICTID"></a><a id="ril_dialopt_restrictid"></a><b>RIL_DIALOPT_RESTRICTID</b>

<dd></dd>

### -field <a id="RIL_DIALOPT_PRESENTID"></a><a id="ril_dialopt_presentid"></a><b>RIL_DIALOPT_PRESENTID</b>

<dd></dd>

### -field <a id="RIL_DIALOPT_ANYEXECUTORFOREMERGENCY"></a><a id="ril_dialopt_anyexecutorforemergency"></a><b>RIL_DIALOPT_ANYEXECUTORFOREMERGENCY</b>

<dd></dd>

### -field <a id="RIL_DIALOPT_RTTFULL"></a><a id="ril_dialopt_rttfull"></a><b>RIL_DIALOPT_RTTFULL</b>

<dd></dd>

### -field <a id="RIL_DIALOPT_ALL"></a><a id="ril_dialopt_all"></a><b>RIL_DIALOPT_ALL</b>

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