---
UID: NS.irb._IDE_CONTROLLER_INTERFACE
title: IDE_CONTROLLER_INTERFACE
author: windows-driver-content
description: The IDE_CONTROLLER_INTERFACE structure is used to pass controller configuration information between the port driver and the miniport driver.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ide_controller_interface.htm
ms.assetid: cb18f7d9-f9e8-436d-8d61-3641730bd8a2
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: irb.h
req.include-header: Irb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDE_CONTROLLER_INTERFACE
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
ms.keywords: IDE_CONTROLLER_INTERFACE, IDE_CONTROLLER_INTERFACE, *PIDE_CONTROLLER_INTERFACE
req.iface: 
---

# IDE_CONTROLLER_INTERFACE structure



## -description
<p>The IDE_CONTROLLER_INTERFACE structure is used to pass controller configuration information between the port driver and the miniport driver.</p>


## -syntax

````
typedef struct _IDE_CONTROLLER_INTERFACE {
  USHORT                   Version;
  USHORT                   Reserved;
  ULONG                    ControllerExtensionSize;
  ULONG                    ChannelExtensionSize;
  ULONG                    AlignmentMask;
  IDE_CHANNEL_INIT         AtaChannelInitRoutine;
  IDE_CHANNEL_ENABLED      AtaControllerChannelEnabled;
  IDE_TRANSFER_MODE_SELECT AtaControllerTransferModeSelect;
  IDE_ADAPTER_CONTROL      AtaAdapterControl;
} IDE_CONTROLLER_INTERFACE, *PIDE_CONTROLLER_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The port driver sets this field to indicate the version of the port driver. The port driver sets the version to sizeof(IDE_CONTROLLER_INTERFACE). The miniport driver should verify that the version is greater than or equal to the one it is using.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use. The miniport driver shall not use this field.</p>
</dd>

### -field <b>ControllerExtensionSize</b>

<dd>
<p>Specifies the size in bytes required by a miniport driver for its controller device extension.</p>
</dd>

### -field <b>ChannelExtensionSize</b>

<dd>
<p>Specifies the size in bytes required by a miniport driver for its per-channel device extension.</p>
</dd>

### -field <b>AlignmentMask</b>

<dd>
<p>Contains a mask indicating the alignment restrictions for buffers required by the HBA for transfer operations. Valid mask values are also restricted by characteristics of the memory managers on different versions of Windows. Under Windows 2000 and Windows XP, the valid mask values are 0 (byte-aligned), 1 (word-aligned), 3 (DWORD-aligned) and 7 (double DWORD-aligned). The miniport driver should set this mask if the HBA supports scatter/gather.</p>
</dd>

### -field <b>AtaChannelInitRoutine</b>

<dd>
<p>Pointer to the miniport's <b>AtaChannelInitRoutine</b> routine. The miniport needs to set this entry point only if it supports the Channel Interface.</p>
</dd>

### -field <b>AtaControllerChannelEnabled</b>

<dd>
<p>Pointer to the miniport's <b>AtaControllerChannelEnabled</b> routine. This is an optional entry point.</p>
</dd>

### -field <b>AtaControllerTransferModeSelect</b>

<dd>
<p>Pointer to the miniport's <b>AtaControllerTransferModeSelect</b> routine. This is an optional entry point.</p>
</dd>

### -field <b>AtaAdapterControl</b>

<dd>
<p>Pointer to the miniport's <b>AtaControllerAdapterControl</b> routine. This is a required entry point.</p>
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