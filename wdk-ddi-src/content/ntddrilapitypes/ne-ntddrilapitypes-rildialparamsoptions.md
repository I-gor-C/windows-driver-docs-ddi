---
UID: NE.ntddrilapitypes.RILDIALPARAMSOPTIONS
title: RILDIALPARAMSOPTIONS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildialparamsoptions.htm
old-project: netvista
ms.assetid: 78fef8f7-e6cd-4da6-9c2a-2eaf1da6339b
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
req.alt-api: RILDIALPARAMSOPTIONS
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

# RILDIALPARAMSOPTIONS enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>