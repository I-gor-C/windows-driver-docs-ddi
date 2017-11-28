---
UID: NS.irb._IDE_CHANNEL_CONFIGURATION
title: IDE_CHANNEL_CONFIGURATION
author: windows-driver-content
description: The IDE_CHANNEL_CONFIGURATION structure contains configuration information for the indicated channel.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ide_channel_configuration.htm
old-project: storage
ms.assetid: 1ca9a198-ac6b-4837-9503-68eb7ca36527
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDE_CHANNEL_CONFIGURATION, IDE_CHANNEL_CONFIGURATION, *PIDE_CHANNEL_CONFIGURATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: irb.h
req.include-header: Irb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDE_CHANNEL_CONFIGURATION
req.alt-loc: irb.h
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

# IDE_CHANNEL_CONFIGURATION structure



## -description
<p>The IDE_CHANNEL_CONFIGURATION structure contains configuration information for the indicated channel.</p>


## -syntax

````
typedef struct _IDE_CHANNEL_CONFIGURATION {
  USHORT                              Version;
  UCHAR                               ChannelNumber;
  SUPPORTED_ADVANCES                  SupportedAdvances;
  IDE_OPERATION_MODE                  ChannelMode;
  PIDE_MINIPORT_RESOURCES             ChannelResources;
  UCHAR                               NumberOfOverlappedRequests;
  UCHAR                               MaxTargetId;
  BOOLEAN                             SyncWithIsr;
  BOOLEAN                             SupportsWmi;
  PIDE_ADVANCED_CHANNEL_CONFIGURATION AdvancedChannelConfiguration;
} IDE_CHANNEL_CONFIGURATION, *PIDE_CHANNEL_CONFIGURATION;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The port driver sets this member to sizeof(IDE_CHANNEL_CONFIGURATION). The miniport driver should verify that the version is greater than or equal to the one it is using.</p>
</dd>

### -field <b>ChannelNumber</b>

<dd>
<p>The port driver sets this field to the number assigned for this channel. For non-native mode controllers, the primary channel will always be assigned 0 and the secondary channel will always be assigned 1.</p>
</dd>

### -field <b>SupportedAdvances</b>

<dd>
<dl>


</dl>
</dd>

### -field <b>ChannelMode</b>

<dd>
<p>The port driver sets this field to inform the ATA miniport which mode it is running at. There are three possible modes:</p>
<table>
<tr>
<th>Mode</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>IdeModeNormal </p>
</td>
<td>
<p>This is the standard full capabilities mode where the ATA miniport may operate normally.</p>
</td>
</tr>
<tr>
<td>
<p>IdeModeDump,</p>
</td>
<td>
<p>This is the limited no memory mode that an ATA miniport operates in during hibernate or crashdump. Call Back Routines and Registry Access Routines cannot be used when in this mode.</p>
</td>
</tr>
<tr>
<td>
<p>IdeModeRemovableBay</p>
</td>
<td>
<p>Similar to the IdeModeNormal, this indicates the ATA miniport must take extra steps to enable enumeration of devices that may have just been hotplugged onto a Parallel ATA bus.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ChannelResources</b>

<dd>
<p>The port driver uses this pointer to pass miniport hardware resources to be used to access the HBA on a PCI bus.</p>
</dd>

### -field <b>NumberOfOverlappedRequests</b>

<dd>
<p>The miniport driver should set this field to the number of requests the channel can handle at a time. By default, the port driver sets this to 1.</p>
</dd>

### -field <b>MaxTargetId</b>

<dd>
<p>The miniport should set this member to the maximum target ID supported on this channel. Typically, this is 1 less than the maximum number of devices supported on the channel. By default, the port driver sets this is set to 1 to indicate that 2 devices are supported on a channel.</p>
</dd>

### -field <b>SyncWithIsr</b>

<dd>
<p>Indicates support for unsynchronized I/O processing in the miniport driver. The miniport driver must set this member to <b>TRUE</b>.</p>
</dd>

### -field <b>SupportsWmi</b>

<dd>
<p>Indicates support for WMI. The miniport driver must set this member to <b>TRUE</b>.</p>
</dd>

### -field <b>AdvancedChannelConfiguration</b>

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
<dt>Irb.h (include Irb.h)</dt>
</dl>
</td>
</tr>
</table>