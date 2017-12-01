---
UID: NS.hbapiwmi._MSFC_FCAdapterHBAAttributes
title: MSFC_FCAdapterHBAAttributes
author: windows-driver-content
description: The MSFC_FCAdapterHBAAttributes structure is used by a WMI provider to expose attribute information associated with a fibre channel adapter.
old-location: storage\msfc_fcadapterhbaattributes.htm
old-project: storage
ms.assetid: 5efe0ede-b55f-499e-9f95-66652cd8a872
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MSFC_FCAdapterHBAAttributes, MSFC_FCAdapterHBAAttributes, *PMSFC_FCAdapterHBAAttributes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MSFC_FCAdapterHBAAttributes
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
req.iface: 
---

# MSFC_FCAdapterHBAAttributes structure



## -description
<p>The MSFC_FCAdapterHBAAttributes structure is used by a WMI provider to expose attribute information associated with a fibre channel adapter. </p>


## -syntax

````
typedef struct _MSFC_FCAdapterHBAAttributes {
  ULONGLONG UniqueAdapterId;
  ULONG     HBAStatus;
  UCHAR     NodeWWN[8];
  ULONG     VendorSpecificID;
  ULONG     NumberOfPorts;
  WCHAR     Manufacturer[64 + 1];
  WCHAR     SerialNumber[64 + 1];
  WCHAR     Model[256 + 1];
  WCHAR     ModelDescription[256 + 1];
  WCHAR     NodeSymbolicName[256 + 1];
  WCHAR     HardwareVersion[256 + 1];
  WCHAR     DriverVersion[256 + 1];
  WCHAR     OptionROMVersion[256 + 1];
  WCHAR     FirmwareVersion[256 + 1];
  WCHAR     DriverName[256 + 1];
  WCHAR     MfgDomain[256 + 1];
} MSFC_FCAdapterHBAAttributes, *PMSFC_FCAdapterHBAAttributes;
````


## -struct-fields
<dl>

### -field <b>UniqueAdapterId</b>

<dd>
<p>Indicates the unique adapter ID. </p>
</dd>

### -field <b>HBAStatus</b>

<dd>
<p>Contains the status of the operation. For a list of allowed values and their descriptions, see <a href="storage.hba_status">HBA_STATUS</a>. </p>
</dd>

### -field <b>NodeWWN</b>

<dd>
<p>Contains the 64 bit world-wide name that indicates the node name of the HBA. For a discussion of worldwide names, see the T11 committee's <i>Fibre Channel HBA API</i> specification.</p>
</dd>

### -field <b>VendorSpecificID</b>

<dd>
<p>Indicates a vendor-specific ID.</p>
</dd>

### -field <b>NumberOfPorts</b>

<dd>
<p>Indicates the number of ports on the HBA. </p>
</dd>

### -field <b>Manufacturer</b>

<dd>
<p>Contains an ASCII string that is 64 bytes or fewer in length and that identifies the name of the manufacturer of the HBA.</p>
</dd>

### -field <b>SerialNumber</b>

<dd>
<p>Contains an ASCII string that is 64 bytes or fewer in length and that identifies the serial number of the HBA.</p>
</dd>

### -field <b>Model</b>

<dd>
<p>Contains an ASCII string that is 256 bytes or fewer in length and that identifies the vendor-specific name of the HBA model.</p>
</dd>

### -field <b>ModelDescription</b>

<dd>
<p>Contains an ASCII string that is 256 bytes or fewer in length and that indicates the model description. </p>
</dd>

### -field <b>NodeSymbolicName</b>

<dd>
<p>Contains an ASCII string that is 256 bytes or fewer in length and that indicates the symbolic name for the fibre channel node. </p>
</dd>

### -field <b>HardwareVersion</b>

<dd>
<p>Contains an ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific hardware revision level of the HBA.</p>
</dd>

### -field <b>DriverVersion</b>

<dd>
<p>Contains an ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific version of the HBA miniport driver. </p>
</dd>

### -field <b>OptionROMVersion</b>

<dd>
<p>Contains an ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific option ROM or BIOS version of the HBA.</p>
</dd>

### -field <b>FirmwareVersion</b>

<dd>
<p>Contains an ASCII string that is 256 bytes or fewer in length and that indicates the vendor-specific firmware version of the HBA.</p>
</dd>

### -field <b>DriverName</b>

<dd>
<p>Contains an ASCII string that is 256 bytes or fewer in length and that indicates the file name for the driver binary file. </p>
</dd>

### -field <b>MfgDomain</b>

<dd>
<p>Contains the name of the HBA manufacturer. </p>
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

## -see-also
<dl>
<dt>
<a href="storage.hba_status">HBA_STATUS</a>
</dt>
<dt>
<a href="storage.msfc_fcadapterhbaattributes_wmi_class">MSFC_FCAdapterHBAAttributes WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MSFC_FCAdapterHBAAttributes structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
