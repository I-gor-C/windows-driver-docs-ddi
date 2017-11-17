---
UID: NE.rilapitypes.RILREQUESTGEOLOCATIONDATAPARAMMASK
title: RILREQUESTGEOLOCATIONDATAPARAMMASK
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilrequestgeolocationdataparammask_2.htm
ms.assetid: b81cbf26-7164-4082-a505-2a849ec3d1ea
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
req.alt-api: RILREQUESTGEOLOCATIONDATAPARAMMASK
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

# RILREQUESTGEOLOCATIONDATAPARAMMASK enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILREQUESTGEOLOCATIONDATAPARAMMASK { 
  RIL_PARAM_REQUESTGEOLOCATIONDATA_SIZE,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_EXECUTOR,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_MASK,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTACCCURACY,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTINFORMATION,
  RIL_PARAM_REQUESTGEOLOCATIONDATA_ALL
} RILREQUESTGEOLOCATIONDATAPARAMMASK;
````


## -enum-fields
<dl>

### -field <a id="RIL_PARAM_REQUESTGEOLOCATIONDATA_SIZE"></a><a id="ril_param_requestgeolocationdata_size"></a><b>RIL_PARAM_REQUESTGEOLOCATIONDATA_SIZE</b>

<dd></dd>

### -field <a id="RIL_PARAM_REQUESTGEOLOCATIONDATA_EXECUTOR"></a><a id="ril_param_requestgeolocationdata_executor"></a><b>RIL_PARAM_REQUESTGEOLOCATIONDATA_EXECUTOR</b>

<dd></dd>

### -field <a id="RIL_PARAM_REQUESTGEOLOCATIONDATA_MASK"></a><a id="ril_param_requestgeolocationdata_mask"></a><b>RIL_PARAM_REQUESTGEOLOCATIONDATA_MASK</b>

<dd></dd>

### -field <a id="RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTACCCURACY"></a><a id="ril_param_requestgeolocationdata_requestacccuracy"></a><b>RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTACCCURACY</b>

<dd></dd>

### -field <a id="RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTINFORMATION"></a><a id="ril_param_requestgeolocationdata_requestinformation"></a><b>RIL_PARAM_REQUESTGEOLOCATIONDATA_REQUESTINFORMATION</b>

<dd></dd>

### -field <a id="RIL_PARAM_REQUESTGEOLOCATIONDATA_ALL"></a><a id="ril_param_requestgeolocationdata_all"></a><b>RIL_PARAM_REQUESTGEOLOCATIONDATA_ALL</b>

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