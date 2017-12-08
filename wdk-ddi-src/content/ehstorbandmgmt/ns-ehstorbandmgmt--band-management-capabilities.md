---
UID: NS.ehstorbandmgmt._BAND_MANAGEMENT_CAPABILITIES
title: BAND_MANAGEMENT_CAPABILITIES
author: windows-driver-content
description: The BAND_MANAGEMENT_CAPABILITIES structure contains the security capabilities available for a storage device. This structure is returned in the system buffer by the IOCTL_EHSTOR_BANDMGMT_QUERY_CAPABILITIES request.
old-location: storage\band_management_capabilities.htm
old-project: storage
ms.assetid: 102C7CEC-B1DD-49F6-AB7F-0CE0A22EBE54
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: BAND_MANAGEMENT_CAPABILITIES, BAND_MANAGEMENT_CAPABILITIES, *PBAND_MANAGEMENT_CAPABILITIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ehstorbandmgmt.h
req.include-header: EhStorBandMgmt.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BAND_MANAGEMENT_CAPABILITIES
req.alt-loc: EhStorBandMgmt.h
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

# BAND_MANAGEMENT_CAPABILITIES structure



## -description
<p>The <b>BAND_MANAGEMENT_CAPABILITIES</b> structure contains the security capabilities available for a storage device. This structure is returned in the system buffer by the <a href="..\ehstorbandmgmt\ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-query-capabilities.md">IOCTL_EHSTOR_BANDMGMT_QUERY_CAPABILITIES</a> request.</p>


## -syntax

````
typedef struct _BAND_MANAGEMENT_CAPABILITIES {
  ULONG     StructSize;
  ULONG     Capabilities;
  ULONGLONG KeyProtectionMechanism;
  ULONG     MinAuthKeyLength;
  ULONG     MaxAuthKeyLength;
  ULONG     MaxBandCount;
  ULONG     MaxSimultaneousReencryptionCount;
  ULONG     BandMetadataSize;
} BAND_MANAGEMENT_CAPABILITIES, *PBAND_MANAGEMENT_CAPABILITIES;
````


## -struct-fields
<dl>

### -field StructSize

<dd>
<p>The size of this structure in bytes. Set to <b>sizeof</b>(BAND_MANAGEMENT_CAPABILITIES).</p>
</dd>

### -field Capabilities

<dd>
<p>Security capability flags for a storage device. This is a bitwise OR value of the following flags.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="CAPS_ACTIVATED"></a><a id="caps_activated"></a><dl>

### -field CAPS_ACTIVATED

</dl>
</td>
<td width="60%">
<p>If set, the capability members of this structure are available. Otherwise, the remaining members of this structure are not valid.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="CAPS_BANDCROSSING_SUPPORTED"></a><a id="caps_bandcrossing_supported"></a><dl>

### -field CAPS_BANDCROSSING_SUPPORTED

</dl>
</td>
<td width="60%">
<p>The storage device supports reads and writes across multiple bands. If this flag is not set, single reads or writes  spanning multiple bands are divided into multiple IO requests for a device.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="CAPS_SID_SECURED"></a><a id="caps_sid_secured"></a><dl>

### -field CAPS_SID_SECURED

</dl>
</td>
<td width="60%">
<p>SID authority is secured. If set, the default SID pin cannot be used to modify the security configuration of the storage device.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field KeyProtectionMechanism

<dd>
<p>The mechanism used to protect the media keys. This member is set to one of the following.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="0"></a><dl>

### -field 0

</dl>
</td>
<td width="60%">
<p>Keys are not protected.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="MEDIAKEY_PROTECTEDBY_VENDORSCHEME"></a><a id="mediakey_protectedby_vendorscheme"></a><dl>

### -field MEDIAKEY_PROTECTEDBY_VENDORSCHEME

</dl>
</td>
<td width="60%">
<p>Keys are protected by a vendor-supplied method. Do not use. This option is not supported.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="MEDIAKEY_PROTECTEDBY_AUTHKEY"></a><a id="mediakey_protectedby_authkey"></a><dl>

### -field MEDIAKEY_PROTECTEDBY_AUTHKEY

</dl>
</td>
<td width="60%">
<p>Keys are encrypted by keys derived from band authentication keys. Key derivation results in negligible entropy loss from the band authentication data.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field MinAuthKeyLength

<dd>
<p>The minimum length, in bytes, of the  band authentication or erase keys accepted by the storage device.</p>
</dd>

### -field MaxAuthKeyLength

<dd>
<p>The maximum length, in bytes, of the  band authentication or erase keys accepted by the storage device.</p>
</dd>

### -field MaxBandCount

<dd>
<p>The maximum number of simultaneous bands configured in the storage device. This includes the global band.</p>
</dd>

### -field MaxSimultaneousReencryptionCount

<dd>
<p>The number of simultaneous band re-encryptions the hardware on the device supports. If this member is 0, hardware-driven band re-encryptions are not supported.</p>
</dd>

### -field BandMetadataSize

<dd>
<p>The size, in bytes, of the per band metadata store.</p>
</dd>
</dl>

## -remarks
<p>If <b>CAPS_ACTIVATED</b> is not set in <b>Capabilities</b>, security functionality can be activated with the <a href="..\ehstorbandmgmt\ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-activate.md">IOCTL_EHSTOR_BANDMGMT_ACTIVATE</a> request.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ehstorbandmgmt\ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-activate.md">IOCTL_EHSTOR_BANDMGMT_ACTIVATE</a>
</dt>
<dt>
<a href="..\ehstorbandmgmt\ni-ehstorbandmgmt-ioctl-ehstor-bandmgmt-query-capabilities.md">IOCTL_EHSTOR_BANDMGMT_QUERY_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20BAND_MANAGEMENT_CAPABILITIES structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
