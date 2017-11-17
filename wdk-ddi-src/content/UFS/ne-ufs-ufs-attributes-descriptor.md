---
UID: NE.ufs.UFS_ATTRIBUTES_DESCRIPTOR
title: UFS_ATTRIBUTES_DESCRIPTOR
author: windows-driver-content
description: UFS_ATTRIBUTES_DESCRIPTOR describes the different types of attributes used by Universal Flash Storage (UFS) descriptors.
old-location: storage\ufs_attributes_descriptor.htm
ms.assetid: 695D8FE9-FADB-488F-A5F7-7715EAD48DD6
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
req.header: ufs.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UFS_ATTRIBUTES_DESCRIPTOR
req.alt-loc: Ufs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Udecxstub.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: UdecxWdfDeviceTryHandleUserIoctl
req.iface: 
req.product: Windows 10 or later.
---

# UFS_ATTRIBUTES_DESCRIPTOR enumeration



## -description
<p><b>UFS_ATTRIBUTES_DESCRIPTOR</b> describes the different types of attributes used by Universal Flash Storage (UFS) descriptors.</p>


## -syntax

````
typedef enum _UFS_ATTRIBUTES_DESCRIPTOR { 
  UFS_bBootLunEn              = 0,
  UFS_Reserved01,
  UFS_bCurrentPowerMode,
  UFS_bActiveICCLevel,
  UFS_bOutOfOrderDataEn,
  UFS_bBackgroundOpStatus,
  UFS_bPurgeStatus,
  UFS_bMaxDataInSize,
  UFS_bMaxDataOutSize,
  UFS_dDynCapNeeded,
  UFS_bRefClkFreq,
  UFS_bConfigDescrLock,
  UFS_bMaxNumOfRTT,
  UFS_wExceptionEventControl,
  UFS_wExceptionEventStatus,
  UFS_dSecondsPassed,
  UFS_wContextConf,
  UFS_Obsolete,
  UFS_Reserved02,
  UFS_Reserved03,
  UFS_bDeviceFFUStatus,
  UFS_bPSAState,
  UFS_dPSADataSize
} UFS_ATTRIBUTES_DESCRIPTOR;
````


## -enum-fields
<dl>

### -field <a id="UFS_bBootLunEn"></a><a id="ufs_bbootlunen"></a><a id="UFS_BBOOTLUNEN"></a><b>UFS_bBootLunEn</b>

<dd>
<p>Indicates if the Boot Logical Unit Number(LUN) is enabled.</p>
</dd>

### -field <a id="UFS_Reserved01"></a><a id="ufs_reserved01"></a><a id="UFS_RESERVED01"></a><b>UFS_Reserved01</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <a id="UFS_bCurrentPowerMode"></a><a id="ufs_bcurrentpowermode"></a><a id="UFS_BCURRENTPOWERMODE"></a><b>UFS_bCurrentPowerMode</b>

<dd>
<p>Indicates the current power mode. Contains one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>0x00</td>
<td>Idle power mode.</td>
</tr>
<tr>
<td>0x10</td>
<td>Pre-Active power mode.</td>
</tr>
<tr>
<td>0x11</td>
<td>Active power mode.</td>
</tr>
<tr>
<td>0x20</td>
<td>Pre-Sleep power mode.</td>
</tr>
<tr>
<td>0x22</td>
<td>Universal Flash Storage (UFS)-Sleep power mode.</td>
</tr>
<tr>
<td>0x30</td>
<td>40% to 50% of the device's estimated life time has been used.</td>
</tr>
<tr>
<td>0x33</td>
<td>50% to 60% of the device's estimated life time has been used.</td>
</tr>
<tr>
<td>All other values</td>
<td>Reserved for future use.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <a id="UFS_bActiveICCLevel"></a><a id="ufs_bactiveicclevel"></a><a id="UFS_BACTIVEICCLEVEL"></a><b>UFS_bActiveICCLevel</b>

<dd>
<p>Specifies the maximum
current consumption allowed during
Active Mode. Value ranges from 0x00 to 0x0F.</p>
</dd>

### -field <a id="UFS_bOutOfOrderDataEn"></a><a id="ufs_boutoforderdataen"></a><a id="UFS_BOUTOFORDERDATAEN"></a><b>UFS_bOutOfOrderDataEn</b>

<dd>
<p>Specifies if out-of-order data transfer is
enabled</p>
</dd>

### -field <a id="UFS_bBackgroundOpStatus"></a><a id="ufs_bbackgroundopstatus"></a><a id="UFS_BBACKGROUNDOPSTATUS"></a><b>UFS_bBackgroundOpStatus</b>

<dd>
<p>Specifies if the device has a need for background operations. Contains one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>0x00</td>
<td>Device requires no background operations.</td>
</tr>
<tr>
<td>0x01</td>
<td>Device has a non-critical need of background operations.</td>
</tr>
<tr>
<td>0x02</td>
<td>Device has a performance impacted-based need of background operations.</td>
</tr>
<tr>
<td>0x03</td>
<td>Device has a critical need of background operations. </td>
</tr>
</table>
<p> </p>
</dd>

### -field <a id="UFS_bPurgeStatus"></a><a id="ufs_bpurgestatus"></a><a id="UFS_BPURGESTATUS"></a><b>UFS_bPurgeStatus</b>

<dd>
<p>Specifies the current purge operation's status.</p>
</dd>

### -field <a id="UFS_bMaxDataInSize"></a><a id="ufs_bmaxdatainsize"></a><a id="UFS_BMAXDATAINSIZE"></a><b>UFS_bMaxDataInSize</b>

<dd>
<p>Specifies the maximum data size in a DATA IN UFS Protocol Information Units (UPIU). This parameter can be written by the
host only when all logical unit task queues are
empty.</p>
</dd>

### -field <a id="UFS_bMaxDataOutSize"></a><a id="ufs_bmaxdataoutsize"></a><a id="UFS_BMAXDATAOUTSIZE"></a><b>UFS_bMaxDataOutSize</b>

<dd>
<p>Specifies the maximum data-out size. This parameter can be written by the
host only when all logical unit task queues are
empty.</p>
</dd>

### -field <a id="UFS_dDynCapNeeded"></a><a id="ufs_ddyncapneeded"></a><a id="UFS_DDYNCAPNEEDED"></a><b>UFS_dDynCapNeeded</b>

<dd>
<p>Specifies the dynamic capacity need.</p>
</dd>

### -field <a id="UFS_bRefClkFreq"></a><a id="ufs_brefclkfreq"></a><a id="UFS_BREFCLKFREQ"></a><b>UFS_bRefClkFreq</b>

<dd>
<p>Specifies the reference clock frequency value.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>0x00</td>
<td>19.2 MHz</td>
</tr>
<tr>
<td>0x01</td>
<td>26 MHz</td>
</tr>
<tr>
<td>0x02</td>
<td>38.4 MHz</td>
</tr>
<tr>
<td>0x03</td>
<td>52 MHz</td>
</tr>
</table>
<p> </p>
</dd>

### -field <a id="UFS_bConfigDescrLock"></a><a id="ufs_bconfigdescrlock"></a><a id="UFS_BCONFIGDESCRLOCK"></a><b>UFS_bConfigDescrLock</b>

<dd>
<p>Specifies if the configuration descriptor is locked.</p>
</dd>

### -field <a id="UFS_bMaxNumOfRTT"></a><a id="ufs_bmaxnumofrtt"></a><a id="UFS_BMAXNUMOFRTT"></a><b>UFS_bMaxNumOfRTT</b>

<dd>
<p>Defines the current maximum number of outstanding READY TO TRANSFER UPIU’s (RTT's) that are
allowed. This value can be set by the host.</p>
</dd>

### -field <a id="UFS_wExceptionEventControl"></a><a id="ufs_wexceptioneventcontrol"></a><a id="UFS_WEXCEPTIONEVENTCONTROL"></a><b>UFS_wExceptionEventControl</b>

<dd>
<p>Specifies the Exception Event Controller. <b>UFS_wExceptionEventControl</b> enables the setting of the
<b>EVENT_ALERT</b> bit in the Device
Information field, which is contained in
the RESPONSE UPIU.</p>
</dd>

### -field <a id="UFS_wExceptionEventStatus"></a><a id="ufs_wexceptioneventstatus"></a><a id="UFS_WEXCEPTIONEVENTSTATUS"></a><b>UFS_wExceptionEventStatus</b>

<dd>
<p>Specifies a bitmap of each exception event status.A bit will be set only if the
relevant event has occurred
(regardless of the
<b>UFS_wExceptionEventControl</b> status). Contains the following bits:</p>
<table>
<tr>
<th>Bit</th>
<th>Value</th>
</tr>
<tr>
<td>0</td>
<td>DYNCAP_NEEDED</td>
</tr>
<tr>
<td>1</td>
<td>SYSPOOL_EXHAUSTED</td>
</tr>
<tr>
<td>2</td>
<td>URGENT_BKOPS</td>
</tr>
<tr>
<td>3 to 15</td>
<td>Reserved.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <a id="UFS_dSecondsPassed"></a><a id="ufs_dsecondspassed"></a><a id="UFS_DSECONDSPASSED"></a><b>UFS_dSecondsPassed</b>

<dd>
<p>Specifies the time passed in seconds.</p>
</dd>

### -field <a id="UFS_wContextConf"></a><a id="ufs_wcontextconf"></a><a id="UFS_WCONTEXTCONF"></a><b>UFS_wContextConf</b>

<dd>
<p>Specifies the context attribute.</p>
</dd>

### -field <a id="UFS_Obsolete"></a><a id="ufs_obsolete"></a><a id="UFS_OBSOLETE"></a><b>UFS_Obsolete</b>

<dd>
<p>Obselete</p>
</dd>

### -field <a id="UFS_Reserved02"></a><a id="ufs_reserved02"></a><a id="UFS_RESERVED02"></a><b>UFS_Reserved02</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <a id="UFS_Reserved03"></a><a id="ufs_reserved03"></a><a id="UFS_RESERVED03"></a><b>UFS_Reserved03</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <a id="UFS_bDeviceFFUStatus"></a><a id="ufs_bdeviceffustatus"></a><a id="UFS_BDEVICEFFUSTATUS"></a><b>UFS_bDeviceFFUStatus</b>

<dd>
<p>Specifies the Device Field Firmware Update (FFU) status.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>0x00</td>
<td>No information on the FFU status.</td>
</tr>
<tr>
<td>0x01</td>
<td>Successful microcode update.</td>
</tr>
<tr>
<td>0x02</td>
<td>Microcode corruption error.</td>
</tr>
<tr>
<td>0x03</td>
<td>Internal error.</td>
</tr>
<tr>
<td>0x04</td>
<td>Microcode version mismatch.</td>
</tr>
<tr>
<td>0x05 to 0xFE </td>
<td>Reserved.</td>
</tr>
<tr>
<td>0xFF</td>
<td>General Error.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <a id="UFS_bPSAState"></a><a id="ufs_bpsastate"></a><a id="UFS_BPSASTATE"></a><b>UFS_bPSAState</b>

<dd>
<p>Specifies the current Product State Awareness (PSA) State.</p>
<table>
<tr>
<th>Value</th>
<th>State</th>
<th>Description</th>
</tr>
<tr>
<td>0x00</td>
<td>Off</td>
<td>PSA feature is off.</td>
</tr>
<tr>
<td>0x01</td>
<td>Pre-solder</td>
<td>PSA feature is on and the device is in a pre-soldering state.</td>
</tr>
<tr>
<td>0x02</td>
<td>Loading Complete</td>
<td>The PSA feature
is on. The host will set to this
value after the host finished
writing data during pre-soldering
state.</td>
</tr>
<tr>
<td>0x03</td>
<td>Soldered</td>
<td>PSA feature is no
longer available. Set by the
Device to indicate it is in a post-soldering state. This attribute
is locked after it is in
‘Soldered’ state.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <a id="UFS_dPSADataSize"></a><a id="ufs_dpsadatasize"></a><a id="UFS_DPSADATASIZE"></a><b>UFS_dPSADataSize</b>

<dd>
<p>Specifies the amount of data that the host plans
to load to all logical units with
<b>bPSASensitive</b> set to 1.</p>
</dd>
</dl>

## -remarks
<p><b>UFS_bCurrentPowerMode</b> is the only attribute the device is required to return in any power mode. If the device
is not in Active power mode or Idle power mode, a <b>QUERY REQUEST UPIU</b> to access descriptors, flags, or attributes other than <b>bCurrentPowerMode</b> may fail.</p>

<p><b>UFS_bDeviceFFUStatu</b>s value is kept after power cycle, hardware reset or any other type of reset. This attribute may change value when a
microcode activation event occurs.</p>

<p><b>UFS_bMaxDataInSize</b> is equal to <b>bMaxInBufferSize</b> when a UFS device is shipped. </p>

<p><b>UFS_bCurrentPowerMode</b> is the only attribute the device is required to return in any power mode. If the device
is not in Active power mode or Idle power mode, a <b>QUERY REQUEST UPIU</b> to access descriptors, flags, or attributes other than <b>bCurrentPowerMode</b> may fail.</p>

<p><b>UFS_bDeviceFFUStatu</b>s value is kept after power cycle, hardware reset or any other type of reset. This attribute may change value when a
microcode activation event occurs.</p>

<p><b>UFS_bMaxDataInSize</b> is equal to <b>bMaxInBufferSize</b> when a UFS device is shipped. </p>

<p><b>UFS_bCurrentPowerMode</b> is the only attribute the device is required to return in any power mode. If the device
is not in Active power mode or Idle power mode, a <b>QUERY REQUEST UPIU</b> to access descriptors, flags, or attributes other than <b>bCurrentPowerMode</b> may fail.</p>

<p><b>UFS_bDeviceFFUStatu</b>s value is kept after power cycle, hardware reset or any other type of reset. This attribute may change value when a
microcode activation event occurs.</p>

<p><b>UFS_bMaxDataInSize</b> is equal to <b>bMaxInBufferSize</b> when a UFS device is shipped. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ufs.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/B65A2268-6959-4630-97DA-C0CFD37D9174">UFS_CONFIG_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6B085DBB-2AAA-4170-A2B1-EA4D2C207A24">UFS_DEVICE_HEALTH_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/CD1F59DA-3D84-422B-A862-8F4C5E1AA515">UFS_DEVICE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/DD3AEB66-E36B-4F18-AFEC-D344132D4B8C">UFS_GEOMETRY_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6C6EAA96-40E9-467F-903B-AE44CE5B77CF">UFS_INTERCONNECT_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/FCF9DCD1-2C04-47E3-97C5-7ACC28B28C6C">UFS_POWER_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/19A066BD-1099-475C-BF81-F1BE7C7778E5">UFS_RPMB_UNIT_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/1F32DA95-6801-4C48-B3C4-A47C3E1C678B">UFS_STRING_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/09CBAD0A-CBDC-464E-908C-BF142D515969">UFS_UNIT_CONFIG_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/5D76C266-875A-40AC-9B26-F17978971783">UFS_UNIT_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20UFS_ATTRIBUTES_DESCRIPTOR enumeration%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
