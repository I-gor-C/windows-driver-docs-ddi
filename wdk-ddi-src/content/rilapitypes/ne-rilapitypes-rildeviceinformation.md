---
UID: NE.rilapitypes.RILDEVICEINFORMATION
title: RILDEVICEINFORMATION
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildeviceinformation_2.htm
old-project: netvista
ms.assetid: a67a637e-92ac-4a42-bfef-8a42ce26b9b3
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
req.alt-api: RILDEVICEINFORMATION
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

# RILDEVICEINFORMATION enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILDEVICEINFORMATION { 
  RIL_DEVICEINFO_MODEL,
  RIL_DEVICEINFO_REVISION,
  RIL_DEVICEINFO_SERIALNUMBER_GW,
  RIL_DEVICEINFO_SERIALNUMBER_CDMA,
  RIL_DEVICEINFO_ARG_SMALLEST,
  RIL_DEVICEINFO_ARG_LARGEST,
  RIL_DEVICEINFO_MIN,
  RIL_DEVICEINFO_MAX
} RILDEVICEINFORMATION;
````


## -enum-fields
<dl>

### -field <a id="RIL_DEVICEINFO_MODEL"></a><a id="ril_deviceinfo_model"></a><b>RIL_DEVICEINFO_MODEL</b>

<dd></dd>

### -field <a id="RIL_DEVICEINFO_REVISION"></a><a id="ril_deviceinfo_revision"></a><b>RIL_DEVICEINFO_REVISION</b>

<dd></dd>

### -field <a id="RIL_DEVICEINFO_SERIALNUMBER_GW"></a><a id="ril_deviceinfo_serialnumber_gw"></a><b>RIL_DEVICEINFO_SERIALNUMBER_GW</b>

<dd></dd>

### -field <a id="RIL_DEVICEINFO_SERIALNUMBER_CDMA"></a><a id="ril_deviceinfo_serialnumber_cdma"></a><b>RIL_DEVICEINFO_SERIALNUMBER_CDMA</b>

<dd></dd>

### -field <a id="RIL_DEVICEINFO_ARG_SMALLEST"></a><a id="ril_deviceinfo_arg_smallest"></a><b>RIL_DEVICEINFO_ARG_SMALLEST</b>

<dd></dd>

### -field <a id="RIL_DEVICEINFO_ARG_LARGEST"></a><a id="ril_deviceinfo_arg_largest"></a><b>RIL_DEVICEINFO_ARG_LARGEST</b>

<dd></dd>

### -field <a id="RIL_DEVICEINFO_MIN"></a><a id="ril_deviceinfo_min"></a><b>RIL_DEVICEINFO_MIN</b>

<dd></dd>

### -field <a id="RIL_DEVICEINFO_MAX"></a><a id="ril_deviceinfo_max"></a><b>RIL_DEVICEINFO_MAX</b>

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