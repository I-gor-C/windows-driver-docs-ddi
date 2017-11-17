---
UID: NS.ntdddisk._IDEREGS
title: IDEREGS
author: windows-driver-content
description: The IDEREGS structure is used to report the contents of the IDE controller registers.
old-location: storage\ideregs.htm
ms.assetid: 20897336-e032-4aa7-be5f-47704c6d1d12
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntdddisk.h
req.include-header: Ntdddisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDEREGS
req.alt-loc: ntdddisk.h
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
ms.keywords: IDEREGS, IDEREGS, *PIDEREGS, *LPIDEREGS
req.iface: 
---

# IDEREGS structure



## -description
<p>The IDEREGS structure is used to report the contents of the IDE controller registers. </p>


## -syntax

````
typedef struct _IDEREGS {
  UCHAR bFeaturesReg;
  UCHAR bSectorCountReg;
  UCHAR bSectorNumberReg;
  UCHAR bCylLowReg;
  UCHAR bCylHighReg;
  UCHAR bDriveHeadReg;
  UCHAR bCommandReg;
  UCHAR bReserved;
} IDEREGS, *PIDEREGS, *LPIDEREGS;
````


## -struct-fields
<dl>

### -field <b>bFeaturesReg</b>

<dd>
<p>Holds the contents of the Features register. This register is used to specify Self-Monitoring Analysis and Reporting Technology (SMART) commands. This member can hold any of the following values:</p>
<table>
<tr>
<th>Feature</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>READ_ATTRIBUTES</p>
</td>
<td>
<p>Retrieve the device attributes</p>
</td>
</tr>
<tr>
<td>
<p>READ_THRESHOLDS.</p>
</td>
<td>
<p>Retrieve threshold values that indicate when a drive is about to fail.</p>
</td>
</tr>
<tr>
<td>
<p>ENABLE_DISABLE_AUTOSAVE.</p>
</td>
<td>
<p>Enables the optional attribute autosave feature of the device when set to 1. Disables this feature when set to 0..</p>
</td>
</tr>
<tr>
<td>
<p>SAVE_ATTRIBUTE_VALUES.</p>
</td>
<td>
<p>Instructs the device to save its attribute values to the device's non-volatile memory.</p>
</td>
</tr>
<tr>
<td>
<p>EXECUTE_OFFLINE_DIAGS</p>
</td>
<td>
<p>Causes the device to begin collecting SMART data in off-line mode or execute a self-diagnostic test routine in either captive or off-line mode.</p>
</td>
</tr>
<tr>
<td>
<p>SMART_READ_LOG</p>
</td>
<td>
<p>Retrieves the indicated log.</p>
</td>
</tr>
<tr>
<td>
<p>SMART_WRITE_LOG</p>
</td>
<td>
<p>Writes the  indicated number of 512-byte data sectors to the indicated log.</p>
</td>
</tr>
<tr>
<td>
<p>ENABLE_SMART</p>
</td>
<td>
<p>Enables SMART functionality on the device.</p>
</td>
</tr>
<tr>
<td>
<p>DISABLE_SMART</p>
</td>
<td>
<p>Disables SMART functionality on the device.</p>
</td>
</tr>
<tr>
<td>
<p>RETURN_SMART_STATUS</p>
</td>
<td>
<p>Retrieves the reliability status of the device.</p>
</td>
</tr>
<tr>
<td>
<p>ENABLE_DISABLE_AUTO_OFFLINE</p>
</td>
<td>
<p>Enables offline mode when set to 1. Disables offline mode when 0.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>bSectorCountReg</b>

<dd>
<p>Holds the contents of the sector count register. IDE sector count register.  </p>
</dd>

### -field <b>bSectorNumberReg</b>

<dd>
<p>Holds the contents of the sector number register. </p>
</dd>

### -field <b>bCylLowReg</b>

<dd>
<p>Holds the contents of the IDE low-order cylinder register. </p>
</dd>

### -field <b>bCylHighReg</b>

<dd>
<p>Holds the contents of the IDE high-order cylinder register. </p>
</dd>

### -field <b>bDriveHeadReg</b>

<dd>
<p>Holds the contents of the IDE drive/head register. </p>
</dd>

### -field <b>bCommandReg</b>

<dd>
<p>Holds the contents of the IDE command register.</p>
</dd>

### -field <b>bReserved</b>

<dd>
<p>Reserved for future use. Should always be zero. </p>
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
<dt>Ntdddisk.h (include Ntdddisk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551323">ATA_PASS_THROUGH_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551322">ATA_PASS_THROUGH_DIRECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20IDEREGS structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
