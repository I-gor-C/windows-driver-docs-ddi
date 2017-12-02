---
UID: NS.rilapitypes.RILOSGEOLOCATIONINFO~r1
title: RILOSGEOLOCATIONINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilosgeolocationinfo_2.htm
old-project: netvista
ms.assetid: 5207e880-67cb-4cd5-9884-a01e6dd20201
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILOSGEOLOCATIONINFO,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILOSGEOLOCATIONINFO
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

# RILOSGEOLOCATIONINFO structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILOSGEOLOCATIONINFO {
  DWORD                              cbSize;
  DWORD                              dwParams;
  DWORD                              dwLatitude;
  DWORD                              dwLongitude;
  DWORD                              dwAltitude;
  DWORD                              dwAccuracy;
  RILGEOLOCATIONTYPEMASK             dwLocationInformationMask;
  RILSYSTEMTIME                      stTimeStamp;
  WCHAR [MAXLENGTH_ADDRESS1]         wszAddressLine1;
  WCHAR [MAXLENGTH_ADDRESS2]         wszAddressLine2;
  WCHAR [MAXLENGTH_CITY]             wszCity;
  WCHAR [MAXLENGTH_STATE]            wszState;
  WCHAR [MAXLENGTH_COUNTRY]          wszCountry;
  WCHAR [MAXLENGTH_ZIP]              wszPostalCode;
  WCHAR [MAXLENGTH_FORMATTEDADDRESS] wszFormattedAddress;
  WCHAR [MAXLENGTH_COUNTRYCODE]      wszCountryCode;
  WCHAR [MAXLENGTH_REGIONCODE]       wszRegionCode;
} RILOSGEOLOCATIONINFO, RILOSGEOLOCATIONINFO;
````


## -struct-fields
<dl>

### -field cbSize

<dd></dd>

### -field dwParams

<dd></dd>

### -field dwLatitude

<dd></dd>

### -field dwLongitude

<dd></dd>

### -field dwAltitude

<dd></dd>

### -field dwAccuracy

<dd></dd>

### -field dwLocationInformationMask

<dd></dd>

### -field stTimeStamp

<dd></dd>

### -field wszAddressLine1

<dd></dd>

### -field wszAddressLine2

<dd></dd>

### -field wszCity

<dd></dd>

### -field wszState

<dd></dd>

### -field wszCountry

<dd></dd>

### -field wszPostalCode

<dd></dd>

### -field wszFormattedAddress

<dd></dd>

### -field wszCountryCode

<dd></dd>

### -field wszRegionCode

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