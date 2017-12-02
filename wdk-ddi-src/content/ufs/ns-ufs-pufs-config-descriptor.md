---
UID: NS.ufs.PUFS_CONFIG_DESCRIPTOR
title: PUFS_CONFIG_DESCRIPTOR
author: windows-driver-content
description: The UFS_CONFIG_DESCRIPTOR structure describes the modifiable values of the default device configuration set by the manufacturer.
old-location: storage\ufs_config_descriptor.htm
old-project: storage
ms.assetid: B65A2268-6959-4630-97DA-C0CFD37D9174
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PUFS_CONFIG_DESCRIPTOR, UFS_CONFIG_DESCRIPTOR, *PUFS_CONFIG_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ufs.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UFS_CONFIG_DESCRIPTOR
req.alt-loc: Ufs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PUFS_CONFIG_DESCRIPTOR structure



## -description
<p>The <b>UFS_CONFIG_DESCRIPTOR</b> structure describes the modifiable values of the default device configuration set by the manufacturer. </p>


## -syntax

````
typedef struct _UFS_CONFIG_DESCRIPTOR {
  UCHAR                       bLength;
  UCHAR                       bDescriptorIDN;
  UCHAR                       Reserved1;
  UCHAR                       bBootEnable;
  UCHAR                       bDescrAccessEn;
  UCHAR                       bInitPowerMode;
  UCHAR                       bHighPriorityLUN;
  UCHAR                       bSecureRemovalType;
  UCHAR                        bInitActiveICCLevel;
  UCHAR                       wPeriodicRTCUpdate[2];
  UCHAR                        Reserved2[5];
   UFS_UNIT_CONFIG_DESCRIPTOR UnitConfig[UFS_MAX_NUM_LU];
} UFS_CONFIG_DESCRIPTOR, *PUFS_CONFIG_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field bLength

<dd>
<p>Specifies the size, in bytes, of this descriptor.</p>
</dd>

### -field bDescriptorIDN

<dd>
<p>Specifies the Configuration Descriptor Type Identifier. This descriptor will have a value of <b>UFS_DESC_CONFIGURATION_IDN</b>.</p>
</dd>

### -field Reserved1

<dd>
<p>Reserved for future use.</p>
</dd>

### -field bBootEnable

<dd>
<p>Specifies if a device's boot feature is enabled.</p>
</dd>

### -field bDescrAccessEn

<dd>
<p>Enables access to the Device Descriptor after the
partial initialization phase of the boot sequence.</p>
</dd>

### -field bInitPowerMode

<dd>
<p>Specifies the power mode after device initialization
or hardware reset.</p>
</dd>

### -field bHighPriorityLUN

<dd>
<p><b>bHighPriorityLUN</b> configures the high priority logical unit.</p>
</dd>

### -field bSecureRemovalType

<dd>
<p>Configures the secure removal type.</p>
</dd>

### -field  bInitActiveICCLevel

<dd>
<p>Configures the ICC level in Active mode after device
initialization or hardware reset.</p>
</dd>

### -field wPeriodicRTCUpdate

<dd>
<p>Specifies the frequency and method of real-time clock updates.</p>
</dd>

### -field  Reserved2

<dd>
<p>Reserved for future use.</p>
</dd>

### -field UnitConfig

<dd>
<p>Contains the configurable parameters of the Unit Descriptor. </p>
</dd>
</dl>

## -remarks


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
<a href="storage.ufs_unit_config_descriptor">UFS_UNIT_CONFIG_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20UFS_CONFIG_DESCRIPTOR structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
