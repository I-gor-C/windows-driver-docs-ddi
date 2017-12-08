---
UID: NS.irb._IDE_CONTROLLER_CONFIGURATION
title: IDE_CONTROLLER_CONFIGURATION
author: windows-driver-content
description: The IDE_CONTROLLER_CONFIGURATION structure is used to pass controller configuration information between the port driver and the miniport driver.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ide_controller_configuration.htm
old-project: storage
ms.assetid: 89b7f66e-3a3a-4723-a409-3b3030c1a45b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDE_CONTROLLER_CONFIGURATION, IDE_CONTROLLER_CONFIGURATION, *PIDE_CONTROLLER_CONFIGURATION
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
req.alt-api: IDE_CONTROLLER_CONFIGURATION
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

# IDE_CONTROLLER_CONFIGURATION structure



## -description
<p>The IDE_CONTROLLER_CONFIGURATION structure is used to pass controller configuration information between the port driver and the miniport driver.</p>


## -syntax

````
typedef struct _IDE_CONTROLLER_CONFIGURATION {
  USHORT                  Version;
  UCHAR                   NumberOfChannels;
  IDE_OPERATION_MODE      ControllerMode;
  UCHAR                   NumberOfPhysicalBreaks;
  ULONG                   MaximumTransferLength;
  BOOLEAN                 Reserved;
  BOOLEAN                 NativeModeEnabled;
  BOOLEAN                 Dma64BitAddress;
  BOOLEAN                 BusMaster;
  IDE_BUS_TYPE            AtaBusType;
  PIDE_MINIPORT_RESOURCES ControllerResources;
} IDE_CONTROLLER_CONFIGURATION, *PIDE_CONTROLLER_CONFIGURATION;
````


## -struct-fields
<dl>

### -field Version

<dd>
<p>The port driver sets this field to indicate the version of the port driver. The port driver sets the version to sizeof(IDE_CONTROLLER_CONFIGURATION). The miniport driver should verify that the version is greater than or equal to the one it is using.</p>
</dd>

### -field NumberOfChannels

<dd>
<p>Specifies the number of channels supported by the HBA. Note that this indicates the total number of channels including the ones that are disabled.</p>
</dd>

### -field ControllerMode

<dd>
<p>The port driver sets this field to inform the ATA miniport which mode it is running at. There are two possible modes:
  </p>
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
<p>IdeModeDump</p>
</td>
<td>
<p>This is the limited no memory mode that an ATA miniport operates in during hibernate or crashdump. Call Back Routines and Registry Access Routines cannot be used when in this mode.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field NumberOfPhysicalBreaks

<dd>
<p>Specifies the maximum number of breaks between address ranges that a data buffer can have if the HBA supports scatter/gather. In other words, the number of scatter/gather lists minus one. By default, the value of this member is IDE_UNINITIALIZED_VALUE, which indicates the HBA can support an unlimited number of physical discontiguities. If the port driver sets a value for this member, the miniport driver can adjust the value lower but no higher. If this member is IDE_UNINITIALIZED_VALUE, the miniport driver must reset this member according to the HBA's scatter/gather capacity.</p>
</dd>

### -field MaximumTransferLength

<dd>
<p>Specifies the maximum number of bytes the HBA can transfer in a single transfer operation. By default, the value of this member is IDE_UNINITIALIZED_VALUE, which indicates an unlimited maximum transfer size.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved for future use. The miniport driver must not use this field.</p>
</dd>

### -field NativeModeEnabled

<dd>
<p>The miniport driver could set this member to <b>TRUE</b> to indicate that the controller is to be operated in Native mode.</p>
</dd>

### -field Dma64BitAddress

<dd>
<p>The miniport driver could set this member to <b>TRUE</b> to indicate support for 64 bit DMA operation.</p>
</dd>

### -field BusMaster

<dd>
<p>The miniport driver could set this member to <b>TRUE</b> to indicate bus mastering support.</p>
</dd>

### -field AtaBusType

<dd>
<p>Indicates whether it is a SATA or a PATA controller.</p>
</dd>

### -field ControllerResources

<dd>
<p>Provides the hardware resources for the ATA controller.</p>
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
<dt>Irb.h (include Irb.h)</dt>
</dl>
</td>
</tr>
</table>