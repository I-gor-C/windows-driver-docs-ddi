---
UID: NS.ntddrilapitypes.RILOSGEOLOCATIONINFO
title: RILOSGEOLOCATIONINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilosgeolocationinfo.htm
old-project: netvista
ms.assetid: 9a56152e-fb38-4470-8834-a0cbdd7b70ec
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILOSGEOLOCATIONINFO, RILOSGEOLOCATIONINFO, *LPRILOSGEOLOCATIONINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILOSGEOLOCATIONINFO
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

# RILOSGEOLOCATIONINFO structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILOSGEOLOCATIONINFO {
  DWORD                   cbSize;
  DWORD                   dwParams;
  DWORD                   dwLatitude;
  DWORD                   dwLongitude;
  DWORD                   dwAltitude;
  DWORD                   dwAccuracy;
  RILGEOLOCATIONTYPEMASK  dwLocationInformationMask;
  RILSYSTEMTIME           stTimeStamp;
  WCHAR [76]              wszAddressLine1;
  WCHAR [76]              wszAddressLine2;
  WCHAR [76]              wszCity;
  WCHAR [76]              wszState;
  WCHAR [76]              wszCountry;
  WCHAR [15]              wszPostalCode;
  WCHAR [256]             wszFormattedAddress;
  WCHAR [11]              wszCountryCode;
  WCHAR [11]              wszRegionCode;
} RILOSGEOLOCATIONINFO, RILOSGEOLOCATIONINFO;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwLatitude</b>

<dd></dd>

### -field <b>dwLongitude</b>

<dd></dd>

### -field <b>dwAltitude</b>

<dd></dd>

### -field <b>dwAccuracy</b>

<dd></dd>

### -field <b>dwLocationInformationMask</b>

<dd></dd>

### -field <b>stTimeStamp</b>

<dd></dd>

### -field <b>wszAddressLine1</b>

<dd></dd>

### -field <b>wszAddressLine2</b>

<dd></dd>

### -field <b>wszCity</b>

<dd></dd>

### -field <b>wszState</b>

<dd></dd>

### -field <b>wszCountry</b>

<dd></dd>

### -field <b>wszPostalCode</b>

<dd></dd>

### -field <b>wszFormattedAddress</b>

<dd></dd>

### -field <b>wszCountryCode</b>

<dd></dd>

### -field <b>wszRegionCode</b>

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