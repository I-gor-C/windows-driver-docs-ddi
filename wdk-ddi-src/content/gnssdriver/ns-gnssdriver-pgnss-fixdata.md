---
UID: NS.gnssdriver.PGNSS_FIXDATA
title: PGNSS_FIXDATA
author: windows-driver-content
description: This structure defines the specific data elements associated with a GNSS fix returned from the driver.
old-location: sensors\gnss_fixdata.htm
ms.assetid: 2939F01A-2F1C-4434-BAE1-59F1F320BD44
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: sensors
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_FIXDATA
req.alt-loc: gnssdriver.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: PGNSS_FIXDATA, GNSS_FIXDATA, *PGNSS_FIXDATA
req.iface: 
---

# PGNSS_FIXDATA structure



## -description
<p>This structure defines the specific data elements associated with a GNSS fix returned from the driver.</p>


## -syntax

````
typedef struct {
  ULONG                  Size;
  ULONG                  Version;
  ULONG                  FixSessionID;
  FILETIME               FixTimeStamp;
  BOOL                   IsFinalFix;
  NTSTATUS               FixStatus;
  ULONG                  FixLevelOfDetails;
  GNSS_FIXDATA_BASIC     BasicData;
  GNSS_FIXDATA_ACCURACY  AccuracyData;
  GNSS_FIXDATA_SATELLITE SatelliteData;
} GNSS_FIXDATA, *PGNSS_FIXDATA;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Structure size.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Version number.</p>
</dd>

### -field <b>FixSessionID</b>

<dd>
<p>ID of the fix session that generated this fix.</p>
<p>The GNSS driver populates this field so that the GNSS adapter can correlate the fix data with the original start fix request.</p>
</dd>

### -field <b>FixTimeStamp</b>

<dd>
<p>Timestamp when the fix is generated.</p>
<p>This should be the time obtained from the satellites measurements.</p>
</dd>

### -field <b>IsFinalFix</b>

<dd>
<p>Boolean value indicating whether this is a final fix or not.</p>
<p>A value of FALSE implies this is an intermediate fix and a final fix is forthcoming.</p>
</dd>

### -field <b>FixStatus</b>

<dd>
<p>An NTSTATUS value indicating whether this fix contains a valid fix, or if the GNSS engine/driver encountered any error in getting the fix.</p>
<p>Unless this value indicates success, the basic fix data element of this structure should not be relied on. Satellite and mode data elements may still be valid.</p>
</dd>

### -field <b>FixLevelOfDetails</b>

<dd>
<p>A bitmask containing the GNSS_FIXDETAIL_* bits that determine which members of this structure are populated by the GNSS driver. </p>
</dd>

### -field <b>BasicData</b>

<dd>
<p>This element contains the basic fix data fix when FixLevelofDetails field has GNSS_FIXDETAIL_BASIC bit set.</p>
<p>Unless explicitly indicated in the fix session parameter, the GNSS driver is recommended to always populate this element.</p>
</dd>

### -field <b>AccuracyData</b>

<dd>
<p>This element contains the accuracy-related data when FixLevelofDetails field has GNSS_FIXDETAIL_ACCURACY bit set.</p>
</dd>

### -field <b>SatelliteData</b>

<dd>
<p>This element contains the satellite-related data when FixLevelofDetails field has GNSS_FIXDETAIL_SATELLITE bit set.</p>
</dd>
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
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>