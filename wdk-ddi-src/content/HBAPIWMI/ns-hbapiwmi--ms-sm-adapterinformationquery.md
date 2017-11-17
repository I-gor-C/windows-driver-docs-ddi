---
UID: NS.hbapiwmi._MS_SM_AdapterInformationQuery
title: MS_SM_AdapterInformationQuery
author: windows-driver-content
description: The MS_SM_AdapterInformationQuery structure is used by a WMI provider to expose attributes that are associated with a SAS adapter.
old-location: storage\ms_sm_adapterinformationquery.htm
ms.assetid: 81c05f47-e75a-4d67-8e77-33ebe1750c67
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MS_SM_AdapterInformationQuery
req.alt-loc: hbapiwmi.h
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
ms.keywords: MS_SM_AdapterInformationQuery, MS_SM_AdapterInformationQuery, *PMS_SM_AdapterInformationQuery
req.iface: 
---

# MS_SM_AdapterInformationQuery structure



## -description
<p>The MS_SM_AdapterInformationQuery structure is used by a WMI provider to expose attributes that are associated with a SAS adapter.</p>


## -syntax

````
typedef struct _MS_SM_AdapterInformationQuery {
  ULONGLONG UniqueAdapterId;
  ULONG     HBAStatus;
  ULONG     NumberOfPorts;
  ULONG     VendorSpecificID;
  WCHAR     Manufacturer[64 + 1];
  WCHAR     SerialNumber[64 + 1];
  WCHAR     Model[256 + 1];
  WCHAR     ModelDescription[256 + 1];
  WCHAR     HardwareVersion[256 + 1];
  WCHAR     DriverVersion[256 + 1];
  WCHAR     OptionROMVersion[256 + 1];
  WCHAR     FirmwareVersion[256 + 1];
  WCHAR     DriverName[256 + 1];
  WCHAR     HBASymbolicName[256 + 1];
  WCHAR     RedundantOptionROMVersion[256 + 1];
  WCHAR     RedundantFirmwareVersion[256 + 1];
  WCHAR     MfgDomain[256 + 1];
} MS_SM_AdapterInformationQuery, *PMS_SM_AdapterInformationQuery;
````


## -struct-fields
<dl>

### -field <b>UniqueAdapterId</b>

<dd>
<p>The unique adapter ID.</p>
</dd>

### -field <b>HBAStatus</b>

<dd>
<p>The status of the operation.</p>
</dd>

### -field <b>NumberOfPorts</b>

<dd>
<p>The number of ports on the HBA.</p>
</dd>

### -field <b>VendorSpecificID</b>

<dd>
<p>A vendor-specific ID.</p>
</dd>

### -field <b>Manufacturer</b>

<dd>
<p>An ASCII string that is 64 bytes or fewer in length and that identifies the name of the manufacturer of the HBA.</p>
</dd>

### -field <b>SerialNumber</b>

<dd>
<p>An ASCII string that is 64 bytes or fewer in length and that identifies the serial number of the HBA.</p>
</dd>

### -field <b>Model</b>

<dd>
<p>An ASCII string that is 256 bytes or fewer in length and that identifies the vendor-specific name of the HBA model.</p>
</dd>

### -field <b>ModelDescription</b>

<dd>
<p>An ASCII string that is 256 bytes or fewer in length and that indicates the model description.</p>
</dd>

### -field <b>HardwareVersion</b>

<dd>
<p>An ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific hardware revision level of the HBA.</p>
</dd>

### -field <b>DriverVersion</b>

<dd>
<p>An ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific version of the HBA miniport driver.</p>
</dd>

### -field <b>OptionROMVersion</b>

<dd>
<p>An ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific option ROM or BIOS version of the HBA.</p>
</dd>

### -field <b>FirmwareVersion</b>

<dd>
<p>An ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific firmware version of the HBA.</p>
</dd>

### -field <b>DriverName</b>

<dd>
<p>An ASCII string that is 256 bytes or fewer in length and that indicates the file name for the driver binary file.</p>
</dd>

### -field <b>HBASymbolicName</b>

<dd>
<p>An ASCII string that is 256 bytes or fewer in length and that indicates the symbolic name for the fibre channel node.</p>
</dd>

### -field <b>RedundantOptionROMVersion</b>

<dd>
<p>An ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific option ROM or BIOS version of the HBA.</p>
</dd>

### -field <b>RedundantFirmwareVersion</b>

<dd>
<p>An ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific firmware version of the HBA.</p>
</dd>

### -field <b>MfgDomain</b>

<dd>
<p>The name of the HBA manufacturer.</p>
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
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>